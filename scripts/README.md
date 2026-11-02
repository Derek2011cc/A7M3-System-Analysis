# 复现脚本

这些脚本只读取本机已提取的分区目录，不接触相机、不修改分区。

## 前置提取

```bash
D=/path/to/service-dump
debugfs -R "rdump / /home/derek/a7m3-rootfs" "$D/nflasha7.bin"
debugfs -R "rdump / /home/derek/a7m3-usr"    "$D/nflasha15.bin"
7z x "$D/nflasha10.bin" -o/home/derek/a7m3-fat10
7z x "$D/nflasha3.bin"  -o/home/derek/a7m3-fat3
7z x "$D/nflasha2.bin"  -o/home/derek/a7m3-fat2
7z x "$D/nflasha18.bin" -o/home/derek/a7m3-fat18
```

## 生成数据

```bash
python3 scripts/analyze.py      # -> data/files.tsv, data/deps.tsv, data/elf.tsv
python3 scripts/render_files.py # -> docs/FILES.md
python3 scripts/summary.py      # 打印统计/关键依赖
```

## 依赖

- `python3`（标准库）
- `file`、`readelf`（binutils）
- `debugfs`（e2fsprogs）
- `7z`（p7zip）

## 路径

脚本里的提取目录固定为 `/home/derek/a7m3-*`；换机器时改
`scripts/analyze.py` 顶部的 `TREES` 即可。
