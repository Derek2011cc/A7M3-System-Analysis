import csv
import os
from collections import defaultdict

ROOT = "/mnt/f/a7c2-re-main/a7m3/A7M3-System-Analysis"
DATA = os.path.join(ROOT, "data", "files.tsv")
OUT = os.path.join(ROOT, "docs", "FILES.md")

rows = list(csv.DictReader(open(DATA, encoding="utf-8"), delimiter="\t"))

usage = {}
u_path = os.path.join(os.path.dirname(DATA), "file-usage.tsv")
if os.path.exists(u_path):
    for r in csv.DictReader(open(u_path, encoding="utf-8"), delimiter="\t"):
        names = []
        for item in r["processes"].split(";"):
            if ":" in item:
                names.append(item.split(":", 1)[1])
        usage[r["path"]] = sorted(set(names))

parts = defaultdict(list)
for r in rows:
    parts[r["partition"]].append(r)

order = ["/", "/system", "/setting", "/etc", "/usr", "/lens"]
titles = {
    "/": "nflasha7（rootfs，挂载到 /）",
    "/system": "nflasha3（/system：内核、initrd、LIRO、镜头/传感器数据）",
    "/setting": "nflasha2（/setting：私有设置、备份、内存地图）",
    "/etc": "nflasha10（/etc 与 /tmp：运行时配置、字体、JIRITSU 标记）",
    "/usr": "nflasha15（/usr：应用、库、场景、DSP/编解码固件、资源）",
    "/lens": "nflasha18（/lens：镜头/像差数据）",
}

lines = []
lines.append("# 文件清单与作用")
lines.append("")
lines.append("由 `scripts/analyze.py` 从服务模式分区转储中提取并生成；")
lines.append("角色为按路径/文件类型/ELF 依赖做的**大致分类**，关键文件有单独说明。")
lines.append("“动态使用”来自 QEMU 运行时 `/proc/*/maps`、`/proc/*/fd` 采集，"
             "`-` 表示本次运行中未直接观察到（不代表不会使用）。")
lines.append("")
lines.append("总文件数 **%d**（其中 ELF %d、脚本 %d、符号链接 %d、数据 %d）。" % (
    len(rows),
    sum(1 for r in rows if r["kind"] == "elf"),
    sum(1 for r in rows if r["kind"] == "script"),
    sum(1 for r in rows if r["kind"] == "symlink"),
    sum(1 for r in rows if r["kind"] == "data"),
))
lines.append("")

for p in order:
    if p not in parts:
        continue
    lines.append("## %s" % titles.get(p, p))
    lines.append("")
    groups = defaultdict(list)
    for r in parts[p]:
        d = os.path.dirname(r["path"]) or "/"
        groups[d].append(r)
    for d in sorted(groups):
        lines.append("### `%s`" % d)
        lines.append("")
        lines.append("| 文件 | 大小 | 类型 | 作用 | 动态使用 |")
        lines.append("|---|---:|---|---|---|")
        for r in sorted(groups[d], key=lambda x: x["path"]):
            name = os.path.basename(r["path"])
            size = int(r["size"])
            if size >= 1024 * 1024:
                sz = "%.1f MB" % (size / 1048576.0)
            elif size >= 1024:
                sz = "%.0f KB" % (size / 1024.0)
            else:
                sz = "%d B" % size
            role = r["role"]
            summary = r["summary"]
            desc = role if summary == role else "%s：%s" % (role, summary)
            desc = desc.replace("|", "\\|")
            name = name.replace("|", "\\|")
            dyn = ", ".join(usage.get(r["path"], [])) or "-"
            lines.append("| `%s` | %s | %s | %s | %s |" % (name, sz, r["kind"], desc, dyn))
        lines.append("")

lines.append("## 运行时生成/修改的文件（静态转储中不存在）")
lines.append("")
lines.append("| 文件 | 大小 | 作用 | 动态使用 |")
lines.append("|---|---:|---|---|")
for path, desc, size in [
    ("/etc/ld.so.preload", "启动时写入，内容为 `/etc/shim_io.so`", "16 B"),
    ("/etc/shim_io.so", "Sony I/O shim/兼容层，被所有用户态进程预加载", "39 KB"),
]:
    dyn = ", ".join(usage.get(path, [])) or "-"
    lines.append("| `%s` | %s | %s | %s |" % (path, size, desc, dyn))
lines.append("")

open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("wrote", OUT, "lines", len(lines))
