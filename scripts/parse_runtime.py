#!/usr/bin/env python3
"""Parse QEMU serial probe logs into runtime tables.

Input:  /home/derek/a7m3-dyn/serial.log   (broad /proc probe)
        /home/derek/a7m3-dyn/serial2.log  (targeted process probe)
Output: data/runtime-processes.tsv
        data/file-usage.tsv
        data/modules.tsv
        data/mounts.tsv
"""
import os
import re

ROOT = "/mnt/f/a7c2-re-main/a7m3/A7M3-System-Analysis"
DYN = "/home/derek/a7m3-dyn"
OUT = os.path.join(ROOT, "data")
os.makedirs(OUT, exist_ok=True)

PREFIX_CAT = re.compile(r"^\[U t\d+\] EXEC /bin/cat \[cat\] \[/proc/[^\]]+\]")
PREFIX_LS = re.compile(r"^\[U t\d+\] EXEC /bin/ls \[ls\] \[[^\]]*\]")
P_PID = re.compile(r"^@@PID\s+(\d+)\s*$")
P_CAT = re.compile(r"^\[U t\d+\] EXEC /bin/cat \[cat\] \[/proc/(\d+)/(comm|cmdline|maps)\]")
P_LS = re.compile(r"^\[U t\d+\] EXEC /bin/ls \[ls\] \[-l\] \[/proc/(\d+)/fd\]")
P_MAP = re.compile(r"^([0-9a-f]{8})-([0-9a-f]{8})\s+\S+\s+\S+\s+\S+\s+\S+\s+(\S+)$")
P_EXE = re.compile(r"/proc/(\d+)/exe\s+->\s+(\S+)")


def strip_prefix(line):
    s = PREFIX_CAT.sub("", line)
    s = PREFIX_LS.sub("", s)
    return s


def parse_procs(path):
    procs = {}
    exe_by_pid = {}
    if not os.path.exists(path):
        return procs, exe_by_pid
    raw = open(path, "rb").read().replace(b"\x00", b" ")
    lines = raw.decode("utf-8", "replace").splitlines()
    cur = None
    for line in lines:
        m = P_PID.match(line)
        if m:
            cur = {"pid": m.group(1), "comm": "", "cmdline": "",
                   "libs": set(), "fds": set(), "exe": "", "ppid": ""}
            procs[cur["pid"]] = cur
            continue
        m = re.match(r"^@@P\s+(\d+)\s+(\S+)", line)
        if m:
            cur = {"pid": m.group(1), "comm": m.group(2), "cmdline": "",
                   "libs": set(), "fds": set(), "exe": "", "ppid": ""}
            procs[cur["pid"]] = cur
            continue
        if cur is None:
            continue
        m = P_CAT.match(line)
        if m:
            pid, what = m.group(1), m.group(2)
            if pid != cur["pid"]:
                cur = procs.get(pid) or {"pid": pid, "comm": "", "cmdline": "",
                                         "libs": set(), "fds": set(), "exe": "", "ppid": ""}
                procs[pid] = cur
            rest = line[m.end():]
            if what == "comm":
                mm = re.match(r"([A-Za-z0-9_.\-]+)", rest)
                if mm:
                    cur["comm"] = mm.group(1)
            elif what == "cmdline":
                cur["cmdline"] = re.split(r"\[U t\d+\]", rest)[0].strip()
            else:
                mm = P_MAP.match(rest)
                if mm and mm.group(3).startswith("/"):
                    cur["libs"].add(mm.group(3))
            continue
        m = P_LS.match(line)
        if m:
            for target in re.findall(r"->\s*(\S+)", line[m.end():]):
                cur["fds"].add(target)
            continue
        if "->" in line and "/proc/" in line:
            for pid, exe in P_EXE.findall(line):
                exe_by_pid[pid] = exe
        s = strip_prefix(line)
        m = re.match(r"^PPid:\s+(\d+)", s)
        if m:
            cur["ppid"] = m.group(1)
        m = P_MAP.match(s)
        if m and m.group(3).startswith("/"):
            cur["libs"].add(m.group(3))
        for target in re.findall(r"->\s*(\S+)", s):
            if target.startswith("/"):
                cur["fds"].add(target)
    for pid, exe in exe_by_pid.items():
        if pid in procs:
            procs[pid]["exe"] = exe
    for pid, rec in procs.items():
        if not rec["exe"] and rec["comm"]:
            cand = "/usr/bin/%s" % rec["comm"]
            if cand in rec["libs"]:
                rec["exe"] = cand
            else:
                for lib in rec["libs"]:
                    base = os.path.basename(lib)
                    if base.startswith(rec["comm"]) or rec["comm"].startswith(base):
                        rec["exe"] = lib
                        break
        if not rec["exe"] and rec["comm"] == "ash" and "/bin/busybox" in rec["libs"]:
            rec["exe"] = "/bin/busybox"
    return procs, exe_by_pid


def parse_modules(path):
    mods = []
    if not os.path.exists(path):
        return mods
    raw = open(path, "rb").read().replace(b"\x00", b" ")
    lines = raw.decode("utf-8", "replace").splitlines()
    on = False
    for line in lines:
        if "__BEGIN3__" in line:
            on = True
            continue
        if not on:
            continue
        if re.search(r"__END_\d+", line):
            break
        s = re.sub(r"^\[U t\d+\] EXEC /bin/cat \[cat\] \[/proc/modules\]", "", line)
        parts = s.split()
        if len(parts) >= 5 and parts[1].isdigit():
            name, size, refs = parts[0], parts[1], parts[2]
            deps = parts[3] if len(parts) > 3 else "-"
            state = parts[4] if len(parts) > 4 else ""
            mods.append((name, size, refs, deps, state))
    return mods


def parse_mounts(path):
    rows = []
    if not os.path.exists(path):
        return rows
    raw = open(path, "rb").read().replace(b"\x00", b" ")
    lines = raw.decode("utf-8", "replace").splitlines()
    on = False
    for line in lines:
        if "__BEGIN2__" in line:
            on = True
            continue
        if not on:
            continue
        if re.search(r"__END_\d+", line):
            break
        s = re.sub(r"^\[U t\d+\] EXEC /bin/cat \[cat\] \[/proc/mounts\]", "", line)
        parts = s.split()
        if len(parts) >= 4 and parts[0].startswith("/") or (len(parts) >= 4 and parts[0] == "rootfs"):
            rows.append((parts[0], parts[1], parts[2], parts[3]))
    return rows


def main():
    procs = {}
    for log in (os.path.join(DYN, "serial.log"), os.path.join(DYN, "serial2.log")):
        p, _ = parse_procs(log)
        for pid, rec in p.items():
            if pid in procs:
                old = procs[pid]
                for k in ("comm", "cmdline", "exe", "ppid"):
                    if not old[k] and rec[k]:
                        old[k] = rec[k]
                old["libs"] |= rec["libs"]
                old["fds"] |= rec["fds"]
            else:
                procs[pid] = rec

    usage = {}
    for p in procs.values():
        if p["exe"]:
            usage.setdefault(p["exe"], set()).add((p["pid"], p["comm"]))
        for lib in p["libs"]:
            usage.setdefault(lib, set()).add((p["pid"], p["comm"]))
        for fd in p["fds"]:
            if fd.startswith("/"):
                usage.setdefault(fd, set()).add((p["pid"], p["comm"]))

    with open(os.path.join(OUT, "runtime-processes.tsv"), "w", encoding="utf-8") as f:
        f.write("pid\tppid\tcomm\texe\tcmdline\tlibs\tfds\n")
        for pid in sorted(procs, key=int):
            p = procs[pid]
            f.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (
                p["pid"], p["ppid"], p["comm"], p["exe"], p["cmdline"],
                ";".join(sorted(p["libs"])), ";".join(sorted(p["fds"]))))

    with open(os.path.join(OUT, "file-usage.tsv"), "w", encoding="utf-8") as f:
        f.write("path\tprocesses\n")
        for path in sorted(usage):
            who = sorted(usage[path])
            f.write("%s\t%s\n" % (path, ";".join("%s:%s" % (p, c) for p, c in who)))

    mods = parse_modules(os.path.join(DYN, "serial.log"))
    with open(os.path.join(OUT, "modules.tsv"), "w", encoding="utf-8") as f:
        f.write("module\tsize\trefcount\tdeps\tstate\n")
        for m in mods:
            f.write("\t".join(m) + "\n")

    mounts = parse_mounts(os.path.join(DYN, "serial.log"))
    with open(os.path.join(OUT, "mounts.tsv"), "w", encoding="utf-8") as f:
        f.write("device\tmountpoint\tfstype\toptions\n")
        for m in mounts:
            f.write("\t".join(m) + "\n")

    print("processes", len(procs), "usage", len(usage),
          "modules", len(mods), "mounts", len(mounts))


if __name__ == "__main__":
    main()
