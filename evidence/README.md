# 证据摘录

这些文件是从分区中提取的 ELF 的 `strings` / `nm` / `readelf` 结果摘录，
用于支撑 `docs/` 中的结论；不包含 Sony 二进制本身。

| 文件 | 来源 | 用途 |
|---|---|---|
| `init-paths.txt` | `/sbin/init` | 挂载点、设备、insmod、启动进程 |
| `bootin-paths.txt` | `/usr/bin/bootin.elf` | `dmode`、`preload`、`im.elf` 参数、调试库 |
| `im-paths.txt` | `/usr/bin/im.elf` | `libObj`、线程名 |
| `scenario-cli.txt` | `/usr/bin/scenario.elf` | `--ifile/--ibfile/--obfile` 与 `testcmd` |
| `change-mode-table.txt` | `/usr/bin/change_mode.sh` | 0–10 启动阶段表 |
| `libObj-view-symbols.txt` | `libObj.so` | `ViewManager/EventManager/DefRootView` 符号 |
| `key-deps.txt` | `data/deps.tsv` | 关键 ELF 的直接 NEEDED |

重新生成：`bash scripts/collect_evidence.sh`。
