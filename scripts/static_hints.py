#!/usr/bin/env python3
"""Extract CLI/usage hints from ELF strings for /usr/bin, /usr/sbin, /usr/scenario."""
import os
import re
import subprocess

ROOT = "/mnt/f/a7c2-re-main/a7m3/A7M3-System-Analysis"
OUT = os.path.join(ROOT, "data", "strings-hints.tsv")
ROOTS = [
    "/home/derek/a7m3-usr/bin",
    "/home/derek/a7m3-usr/sbin",
    "/home/derek/a7m3-usr/scenario",
    "/home/derek/a7m3-rootfs/sbin",
    "/home/derek/a7m3-rootfs/bin",
]
PREF = "usage|options:|\bcommand|--[a-z]|-\w\s| : |\bstart\b|\bstop\b|\btest\b"


def is_elf(p):
    try:
        return open(p, "rb").read(4) == b"\x7fELF"
    except OSError:
        return False


def strings(p):
    try:
        out = subprocess.run(["strings", "-n", "5", p], capture_output=True,
                             text=True, timeout=20).stdout
    except Exception:
        return []
    return out.splitlines()


def main():
    rows = []
    for root in ROOTS:
        for dirpath, _, names in os.walk(root):
            for n in names:
                p = os.path.join(dirpath, n)
                if not is_elf(p) or os.path.islink(p):
                    continue
                rel = p.replace("/home/derek/a7m3-usr", "/usr")
                rel = rel.replace("/home/derek/a7m3-rootfs", "")
                hints = []
                for s in strings(p):
                    s = s.strip()
                    if len(s) < 4 or len(s) > 160:
                        continue
                    low = s.lower()
                    if ("usage" in low or "options" in low or
                            re.search(r"(^|\s)--[a-z]", s) or
                            re.match(r"^-\w\s", s)):
                        hints.append(s)
                    if len(hints) >= 6:
                        break
                rows.append((rel, " | ".join(hints) if hints else "-"))
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("path\thints\n")
        for r in rows:
            f.write("%s\t%s\n" % r)
    print("wrote", OUT, len(rows))


if __name__ == "__main__":
    main()
