# A7M3 系统结构逆向分析

> 项目有借助大量AI工具，请注意辨别
>
> qq交流群:736434809

对 Sony ILCE-7M3（A7M3）4.03 固件文件系统的静态逆向：每个文件的大致作用、
分层架构与调用关系。数据来自本机服务模式只读分区转储（nflasha2/3/7/10/15/18）。

**本文件只介绍仓库结构；具体分析、结论和证据都在 [`docs/`](docs/) 与
[`data/`](data/) 中。**

## 分仓库说明

本仓库是
[A7M3-Firmware-QEMU-Boot-Experiment](https://github.com/Derek2011cc/A7M3-Firmware-QEMU-Boot-Experiment)
的**分仓库**，专门存放 A7M3 4.03 系统结构的静态逆向结果（逐文件作用、分层架构、调用关系）。
主仓库负责启动链、QEMU 机器模型、服务模式、隐藏功能与菜单渲染实验；本仓库只做文件系统结构分析。

相关仓库：

- [A7M3-Firmware-QEMU-Boot-Experiment](https://github.com/Derek2011cc/A7M3-Firmware-QEMU-Boot-Experiment) — 研究主仓库
- [a7m3-QEMU-shell](https://github.com/Derek2011cc/a7m3-QEMU-shell) — 下载即用的 A7M3 虚拟机 shell
- [a7m3-connect-shell](https://github.com/Derek2011cc/a7m3-connect-shell) — 服务模式 shell / 分区转储工具

## 仓库结构

```
A7M3-System-Analysis/
├── README.md                     本文件：仓库导览
├── docs/                         分析文档
│   ├── BOOT-AND-INIT.md          分区挂载、init、启动阶段、bootin/im.elf
│   ├── ARCHITECTURE.md           6 层架构、子系统、进程/服务、数据流
│   ├── CALL-GRAPH.md             启动/依赖/插件调用关系（Mermaid）
│   └── FILES.md                  全部 1177 个文件的逐项作用表
├── data/                         机器可读结果
│   ├── files.tsv                 文件清单（分区/路径/大小/类型/角色/说明）
│   ├── deps.tsv                  ELF → NEEDED（1928 条）
│   ├── elf.tsv                   457 个 ELF 的类型/架构/SONAME/依赖数
│   └── README.md                 字段说明 + 文件规模
├── evidence/                     关键 strings/nm 摘录（可复核）
│   ├── init-paths.txt
│   ├── bootin-paths.txt
│   ├── im-paths.txt
│   ├── scenario-cli.txt
│   ├── change-mode-table.txt
│   ├── libObj-view-symbols.txt
│   ├── key-deps.txt
│   └── README.md
└── scripts/                      复现脚本
    ├── analyze.py                生成 files/deps/elf TSV
    ├── render_files.py           生成 docs/FILES.md
    ├── collect_evidence.sh       生成 evidence/ 摘录
    ├── summary.py                打印统计与关键依赖
    └── README.md                 提取与生成步骤
```

### 各路径作用

| 路径 | 作用 |
|---|---|
| `docs/BOOT-AND-INIT.md` | 从 EXBL/内核到 `/sbin/init` 的启动链、分区表、挂载与 insmod、`dmode` 阶段、`bootin.elf` / `im.elf` / `launch_shell.elf` |
| `docs/ARCHITECTURE.md` | 结论速览、6 层图、init/IPC/Appframework/媒体/Infra/网络/存储/传感器/测试等子系统、进程表、数据流 |
| `docs/CALL-GRAPH.md` | 启动与进程图、关键 ELF 依赖图、被依赖最多的库、scenario/UI 调用链、脚本调用 |
| `docs/FILES.md` | 按分区/目录列出每个文件的大小、类型、作用（1177 条） |
| `data/files.tsv` | 上述文件表的原始数据，便于脚本处理 |
| `data/deps.tsv` | `readelf -d` 的 NEEDED 原始边，用于画依赖图 |
| `data/elf.tsv` | ELF 元数据（DYN/EXEC、ARM、SONAME、依赖数） |
| `data/README.md` | 字段含义与各分区文件数 |
| `evidence/` | `strings`/`nm` 摘录，支撑启动、场景、UI 的结论 |
| `scripts/` | 从分区提取目录重新生成全部结果的脚本 |

## 该看哪一篇

| 想了解 | 看 |
|---|---|
| 相机怎么启动、分区怎么挂载 | [docs/BOOT-AND-INIT.md](docs/BOOT-AND-INIT.md) |
| 系统分几层、各子系统怎么分工 | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) |
| 谁调用谁、依赖哪些库 | [docs/CALL-GRAPH.md](docs/CALL-GRAPH.md) |
| 某个文件是干什么的 | [docs/FILES.md](docs/FILES.md) |
| 数据字段/文件规模 | [data/README.md](data/README.md) |
| 怎么重新生成结果 | [scripts/README.md](scripts/README.md) |

## 数据概况

- 文件条目 **1177**：ELF 457、脚本 24、符号链接 139、数据 557；
- 依赖边 **1928**；
- 分区：`/`（nflasha7）、`/usr`（nflasha15）、`/etc`（nflasha10）、
  `/system`（nflasha3）、`/setting`（nflasha2）、`/lens`（nflasha18）。

## 复现

```bash
# 1) 用 debugfs/7z 提取分区（命令见 scripts/README.md）
# 2) 生成数据、文件表和证据
python3 scripts/analyze.py
python3 scripts/render_files.py
bash scripts/collect_evidence.sh
```

## 边界

- 静态分析 + 符号/字符串推断，不是逐指令反编译；未做动态验证的条目已在文档中标注。
- 不包含 Sony 二进制，只有元数据、文档和脚本。
- 固件版本 4.03（`version.txt: 37114_12.2025061901`），4.04 布局可能不同。
- 项目借助 AI 工具，结论请自行辨别。
