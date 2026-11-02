#!/usr/bin/env python3
"""Second targeted probe: shim preload + per-process status/maps/fds."""
import os
import re
import socket
import subprocess
import sys
import time

QEMU = "/mnt/f/a7c2-re-main/a7m3/a7m3-QEMU-shell/qemu-prebuilt/qemu-system-arm"
FW = "/mnt/f/a7c2-re-main/a7m3/a7m3-QEMU-shell/firmware"
OUT = "/home/derek/a7m3-dyn/serial2.log"
ERR = "/home/derek/a7m3-dyn/qemu2.err"

CMDS = [
    "ls -l /etc/shim_io.so /etc/ld.so.preload",
    "cat /etc/ld.so.preload",
    "for p in /proc/[0-9]*; do c=$(cat $p/comm 2>/dev/null); case \"$c\" in bootin.elf|sen.elf|im.elf|launch_shell.elf) echo \"@@P ${p##*/} $c\"; cat $p/status; echo @@MAPS; cat $p/maps; echo @@FD; ls -l $p/fd; echo @@PEND;; esac; done",
]


def send(s, t):
    s.sendall(t.encode())


def wait(sock, buf, pattern, timeout, start=0):
    rx = re.compile(pattern)
    end = time.time() + timeout
    while time.time() < end:
        try:
            d = sock.recv(65536)
        except socket.timeout:
            continue
        if not d:
            break
        buf.extend(d)
        if rx.search(buf[start:].decode("utf-8", "replace")):
            return True
    return False


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    env = dict(os.environ)
    env["A7M3_LIRO_AUTOREADY"] = "1"
    env["A7M3_NO_GFX_CONSOLE"] = "1"
    q = subprocess.Popen([
        QEMU, "-M", "cxd90045",
        "-kernel", FW + "/vmlinux-console.bin",
        "-initrd", FW + "/initrd-qemu.img",
        "-drive", "if=mtd,file=%s,format=raw,snapshot=on" % (FW + "/qemu-emmc-2g.img"),
        "-display", "none", "-monitor", "none", "-no-reboot", "-no-shutdown",
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
            raise SystemExit("no serial")
        sock.settimeout(1)
        buf = bytearray()
        if not wait(sock, buf, r"/ #|Exception>", 180):
            print("no prompt", len(buf))
            return 1
        if "Exception>" in buf.decode("utf-8", "replace") and "/ #" not in buf.decode("utf-8", "replace"):
            send(sock, "exit\n")
            wait(sock, buf, r"/ #", 90)
        send(sock, "export PS1='A7M3> '\necho __PS1_OK__\n")
        wait(sock, buf, r"__PS1_OK__", 15)
        for i, cmd in enumerate(CMDS):
            start = len(buf)
            send(sock, "echo __BEGIN%d__\n" % i)
            send(sock, cmd + "\necho __END_$$\n")
            ok = wait(sock, buf, r"__END_\d+", 90, start=start)
            print("cmd", i, ok, flush=True)
            time.sleep(0.5)
        open(OUT, "wb").write(buf)
        print("wrote", OUT, len(buf))
        return 0
    finally:
        q.terminate()
        try:
            q.wait(timeout=5)
        except Exception:
            q.kill()


if __name__ == "__main__":
    sys.exit(main())
