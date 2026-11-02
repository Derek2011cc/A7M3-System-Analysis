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
python3 scripts/analyze.py       # -> data/files.tsv, deps.tsv, elf.tsv
python3 scripts/static_hints.py  # -> data/strings-hints.tsv
python3 scripts/render_files.py  # -> docs/FILES.md（含动态使用列）
python3 scripts/summary.py       # 打印统计/关键依赖
```

## 动态采集（QEMU）

依赖 [A7M3-QEMU-shell](https://github.com/Derek2011cc/a7m3-QEMU-shell)
的镜像与 QEMU（脚本里默认路径为 `F:\a7c2-re-main\a7m3\a7m3-QEMU-shell`）：

```bash
python3 scripts/collect_runtime.py   # 宽范围 /proc -> /home/derek/a7m3-dyn/serial.log
python3 scripts/collect_runtime2.py  # 关键进程/shim -> serial2.log
python3 scripts/parse_runtime.py     # -> runtime-processes.tsv 等
python3 scripts/render_runtime.py    # -> docs/RUNTIME.md
```

QEMU 以 `snapshot=on` 启动，不修改镜像；采集会与相机自身的 `[U tNNN]`
日志交错，部分进程的 maps/fd 可能缺失。

## 依赖

- `python3`（标准库）
- `file`、`readelf`、`strings`（binutils）
- `debugfs`（e2fsprogs）
- `7z`（p7zip）
- 动态部分：QEMU 镜像 + `qemu-system-arm`（见 A7M3-QEMU-shell）

## 路径

脚本里的提取目录固定为 `/home/derek/a7m3-*`；换机器时改
`scripts/analyze.py` 顶部的 `TREES` 即可。
