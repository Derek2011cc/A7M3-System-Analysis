#!/bin/bash
# Collect small text evidence used by the docs. Runs on the extracted trees.
set -e
ROOT=/mnt/f/a7c2-re-main/a7m3/A7M3-System-Analysis
R=/home/derek/a7m3-rootfs
U=/home/derek/a7m3-usr
E="$ROOT/evidence"
mkdir -p "$E"

strings -n 4 "$R/sbin/init" | grep -E '^/|\.elf|\.sh|nflasha|mount|insmod|/proc|/setting' | sort -u > "$E/init-paths.txt"
strings -n 4 "$U/bin/bootin.elf" | grep -E '^/|\.elf|im\.elf|dmode|preload|Leak|efence|jemalloc|mcheck' | sort -u > "$E/bootin-paths.txt"
strings -n 4 "$U/bin/im.elf" | grep -E '^/|libObj|THREAD_|thread|main' | sort -u > "$E/im-paths.txt"
strings -n 4 "$U/bin/scenario.elf" | grep -E 'cmdline|testcmd|scenario|--' | sort -u > "$E/scenario-cli.txt"
sed -n '1,60p' "$U/bin/change_mode.sh" > "$E/change-mode-table.txt"
nm -D -C "$U/lib/libObj.so" 2>/dev/null | grep -E 'ViewManager|EventManager|DefRootView|ScalarView' | head -30 > "$E/libObj-view-symbols.txt"
head -1 "$ROOT/data/deps.tsv" > "$E/key-deps.txt"
for elf in /usr/bin/im.elf /usr/bin/scenario.elf /usr/lib/libObj.so /usr/lib/libmpr.so /usr/lib/libtestcmd.so; do
  echo "== $elf ==" >> "$E/key-deps.txt"
  grep -P "^${elf}\t" "$ROOT/data/deps.tsv" | cut -f2 | tr '\n' ' ' >> "$E/key-deps.txt"
  echo >> "$E/key-deps.txt"
done
echo "evidence written to $E"
ls -l "$E"
