# data 字段说明

## files.tsv

| 字段 | 含义 |
|---|---|
| `partition` | 分区挂载点标签：`/`、`/usr`、`/etc`、`/system`、`/setting`、`/lens` |
| `path` | 相机内的绝对路径 |
| `size` | 字节数（符号链接为链接本身大小） |
| `kind` | `elf` / `script` / `symlink` / `data` |
| `type` | `file`/`readelf` 得到的类型描述 |
| `role` | 大致分类（核心工具、共享库、场景模块……） |
| `summary` | 具体说明（关键文件有人工描述，其余按命名/目录推断） |

## deps.tsv

`elf` → `needed`：由 `readelf -d` 的 `(NEEDED)` 提取，共 1928 条。

## elf.tsv

| 字段 | 含义 |
|---|---|
| `elf` | ELF 路径 |
| `type` | `DYN`（PIE/共享库）或 `EXEC` |
| `machine` | 目标架构（ARM） |
| `soname` | 共享库 SONAME |
| `needed_count` | 直接依赖库数量 |

## 文件规模

| 分区 | 挂载点 | 文件数 | 说明 |
|---|---|---:|---|
| nflasha7 | `/` | 211 | rootfs：BusyBox、init、glibc、基础 kmod |
| nflasha15 | `/usr` | 864 | 应用、库、场景、DSP/编解码、资源 |
| nflasha10 | `/etc`（及 `/tmp`） | 13 | 网络/日志/字体/JIRITSU 配置 |
| nflasha3 | `/system` | 13 | 内核、initrd、LIRO、DFE、sabin 启动 |
| nflasha2 | `/setting` | 19 | 私有设置、备份、face rec、`kemco.txt` |
| nflasha18 | `/lens` | 57 | 镜头/像差数据 |
| **合计** | | **1177** | ELF 457、脚本 24、符号链接 139、数据 557 |

## runtime-processes.tsv

| 字段 | 含义 |
|---|---|
| `pid` / `ppid` | 进程号 / 父进程号（部分 PPid 未采到） |
| `comm` | 内核 comm（最长 15 字符） |
| `exe` | `/proc/*/exe` 或从 maps 推断的可执行文件 |
| `cmdline` | `/proc/*/cmdline` |
| `libs` | maps 中的库/设备映射路径 |
| `fds` | 打开的文件/设备（`/proc/*/fd`） |

## file-usage.tsv

`path` → `processes`（`PID:comm` 列表）：静态文件在运行时被哪些进程映射/打开。

## modules.tsv / mounts.tsv

`/proc/modules` 与 `/proc/mounts` 的解析结果。

## strings-hints.tsv

`path` → 从 ELF 字符串中提取的 `usage`/选项提示。

## 注意

- `files.tsv` 中同一文件可能同时出现在 `files.tsv` 与 `deps.tsv`；
- `summary` 为静态推断，未做动态验证；
- 没有 Sony 二进制本身，只有元数据。
