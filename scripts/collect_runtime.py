#!/usr/bin/env python3
"""Boot the A7M3 QEMU image, run a fixed probe script in the guest shell,
and save the raw serial log for offline parsing."""
import os
import re
import socket
import subprocess
import sys
import time

QEMU = "/mnt/f/a7c2-re-main/a7m3/a7m3-QEMU-shell/qemu-prebuilt/qemu-system-arm"
FW = "/mnt/f/a7c2-re-main/a7m3/a7m3-QEMU-shell/firmware"
IMG = FW + "/qemu-emmc-2g.img"
KERNEL = FW + "/vmlinux-console.bin"
INITRD = FW + "/initrd-qemu.img"
OUT = "/home/derek/a7m3-dyn/serial.log"
ERR = "/home/derek/a7m3-dyn/qemu.err"

CMDS = [
    "uname -a",
    "cat /proc/version",
    "cat /proc/mounts",
    "cat /proc/modules",
    "cat /proc/partitions",
    "cat /proc/devices",
    "ps",
    "ls -l /proc/[0-9]*/exe",
    "for p in /proc/[0-9]*; do echo \"@@PID ${p##*/}\"; cat $p/comm; cat $p/cmdline; echo; echo @@MAPS; cat $p/maps; echo @@FD; ls -l $p/fd; echo @@END; done",
]


def send(sock, text):
    sock.sendall(text.encode())


def wait_regex(sock, buf, pattern, timeout, start=0):
    rx = re.compile(pattern)
    end = time.time() + timeout
    while time.time() < end:
        try:
            data = sock.recv(65536)
        except socket.timeout:
            continue
        if not data:
            break
        buf.extend(data)
        if rx.search(buf[start:].decode("utf-8", "replace")):
            return True
    return False


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    env = dict(os.environ)
    env["A7M3_LIRO_AUTOREADY"] = "1"
    env["A7M3_NO_GFX_CONSOLE"] = "1"
    qemu = subprocess.Popen([
        QEMU, "-M", "cxd90045",
        "-kernel", KERNEL, "-initrd", INITRD,
        "-drive", "if=mtd,file=%s,format=raw,snapshot=on" % IMG,
        "-display", "none", "-monitor", "none",
        "-no-reboot", "-no-shutdown",
        "-serial", "tcp:127.0.0.1:4444,server=on,wait=off",
    ], stdout=subprocess.DEVNULL, stderr=open(ERR, "wb"), env=env)

    try:
        sock = None
        for _ in range(30):
            try:
                sock = socket.create_connection(("127.0.0.1", 4444), timeout=2)
                break
            except OSError:
                time.sleep(1)
        if sock is None:
            raise SystemExit("cannot connect to QEMU serial")
        sock.settimeout(1)
        buf = bytearray()

        if not wait_regex(sock, buf, r"/ #|Exception>", 180):
            print("no prompt; log bytes", len(buf))
            return 1
        text = buf.decode("utf-8", "replace")
        if "Exception>" in text and "/ #" not in text:
            send(sock, "exit\n")
            wait_regex(sock, buf, r"/ #", 90)

        send(sock, "export PS1='A7M3> '\necho __PS1_OK__\n")
        wait_regex(sock, buf, r"__PS1_OK__", 15)

        for i, cmd in enumerate(CMDS):
            start = len(buf)
            send(sock, "echo __BEGIN%d__\n" % i)
            send(sock, cmd + "\necho __END_$$\n")
            ok = wait_regex(sock, buf, r"__END_\d+", 120, start=start)
            print("cmd %d done=%s" % (i, ok), flush=True)
            if not ok:
                tail = buf[start:].decode("utf-8", "replace")[-400:]
                print("TAIL:", repr(tail), flush=True)
            time.sleep(0.5)

        send(sock, "echo __ALL_DONE__\n")
        wait_regex(sock, buf, r"__ALL_DONE__", 10)
        open(OUT, "wb").write(buf)
        print("wrote", OUT, len(buf))
        return 0
    finally:
        qemu.terminate()
        try:
            qemu.wait(timeout=5)
        except Exception:
            qemu.kill()


if __name__ == "__main__":
    sys.exit(main())
