import csv
import collections

D = "/mnt/f/a7c2-re-main/a7m3/A7M3-System-Analysis/data/files.tsv"
files = list(csv.DictReader(open(D, encoding="utf-8"), delimiter="\t"))
print("total", len(files))
print("partitions", collections.Counter(f["partition"] for f in files))
print("kinds", collections.Counter(f["kind"] for f in files))
print("roles top 25")
for r, n in collections.Counter(f["role"] for f in files).most_common(25):
    print("%5d  %s" % (n, r))

deps = list(csv.DictReader(open("/mnt/f/a7c2-re-main/a7m3/A7M3-System-Analysis/data/deps.tsv", encoding="utf-8"), delimiter="\t"))
by = collections.defaultdict(list)
for d in deps:
    by[d["elf"]].append(d["needed"])
for k in ["/usr/bin/im.elf", "/usr/bin/scenario.elf", "/usr/bin/sen.elf",
          "/usr/bin/testcmd.elf", "/usr/lib/libObj.so", "/usr/lib/libmpr.so",
          "/usr/lib/libJiritsu.so", "/usr/bin/bsa_server", "/usr/bin/orb-server"]:
    print(k, "->", ", ".join(by.get(k, [])[:20]))
