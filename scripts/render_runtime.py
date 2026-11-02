#!/usr/bin/env python3
"""Render docs/RUNTIME.md from the runtime TSVs."""
import csv
import os

ROOT = "/mnt/f/a7c2-re-main/a7m3/A7M3-System-Analysis"
DATA = os.path.join(ROOT, "data")


def rows(name):
    p = os.path.join(DATA, name)
    if not os.path.exists(p):
        return []
    return list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))


procs = rows("runtime-processes.tsv")
mods = rows("modules.tsv")
mounts = rows("mounts.tsv")
usage = rows("file-usage.tsv")
hints = rows("strings-hints.tsv")

L = []
L.append("# 动态运行分析（QEMU）")
L.append("")
L.append("在 QEMU 中启动同一份 4.03 固件，进入 `/ #` 后通过串口采集：")
L.append("`/proc/mounts`、`/proc/modules`、`/proc/devices`、`/proc/*/status`、")
L.append("`/proc/*/maps`、`/proc/*/fd`，再与静态文件表合并。")
L.append("")
L.append("> 采到的日志会与相机自身的 `[U tNNN]` 跟踪输出交错，部分进程的 maps/fd 可能不完整；")
L.append("> 下表中的 `-` 只表示“本次运行未直接观察到”，不代表文件不会被使用。")
L.append("")
L.append("## 1. 动态关键发现")
L.append("")
L.append("1. **PID 1 是 `launch_shell.elf`**：`/sbin/init` 直接 exec 了它，")
L.append("   它再 exec `/bin/ash --login`；这就是 QEMU 里能直接拿到 `/ #` 的原因。")
L.append("2. **`/etc/ld.so.preload` 在启动时被写入 `/etc/shim_io.so`**：")
L.append("   静态转储的 `/etc` 里没有这两个文件；运行时它们出现在 vfat（nflasha10）上，")
L.append("   并被 launch_shell / bootin / sen / im.elf / ash 全部映射。")
L.append("   `shim_io.so` 是 Sony 的 I/O 兼容/拦截层，调试时优先看它。")
L.append("3. **用户态进程只有 5 个**：`launch_shell.elf`(1)、`bootin.elf`(130)、")
L.append("   `sen.elf`(131)、`ash`(134)、`im.elf`(140)；其余是内核线程。")
L.append("4. **`im.elf` 已经跑起来**，并打开了 Sugilite/媒体/存储相关设备：")
L.append("   `/dev/dmpgles2`、`/dev/mem`、`/dev/stream`、`/dev/stream2`、`/dev/cec`、")
L.append("   `/dev/hdmi`、`/dev/mmcb-char`、`/dev/usb/buspwr`、`/dev/uipc`；")
L.append("   同时写 `/log/AccessLog.dat` 与 `/log/AccessLog.bak`。")
L.append("5. **`sen.elf` 打开 USB 事件/OTG**：`/dev/usb/event`、`/dev/usb/otgcore`，")
L.append("   并加载 `libSTMcmdexecute`、`libInfraUsbCmn`、`libsencore`、`libpro00`、")
L.append("   `libcrypto/libssl`。")
L.append("6. **`bootin.elf` 读 `/proc/snsc_boot_time`**，打开 `/dev/uipc`、`/dev/console`；")
L.append("   它是启动阶段管理器，运行期仍驻留。")
L.append("")
L.append("## 2. 挂载表（`/proc/mounts`）")
L.append("")
L.append("| 设备 | 挂载点 | 类型 | 选项 |")
L.append("|---|---|---|---|")
for m in mounts:
    L.append("| `%s` | `%s` | %s | %s |" % (
        m["device"], m["mountpoint"], m["fstype"], m["options"].replace("|", "\\|")))
L.append("")
L.append("要点：`/`（nflasha7）和 `/usr`（nflasha15）是 **只读 ext2**；")
L.append("`/tmp` 与 `/etc` 都来自 **nflasha10 vfat rw**；`/system`、`/setting`、")
L.append("`/log`、`/lens`、`/cert` 是 vfat rw。")
L.append("")
L.append("## 3. 已加载内核模块（`/proc/modules`）")
L.append("")
L.append("| 模块 | 大小 | 引用 | 依赖 | 状态 |")
L.append("|---|---:|---:|---|---|")
for m in mods:
    L.append("| `%s` | %s | %s | %s | %s |" % (
        m["module"], m["size"], m["refcount"], m["deps"], m["state"]))
L.append("")
L.append("## 4. 用户态进程")
L.append("")
L.append("| PID | PPid | comm | exe | cmdline | 映射 | fds |")
L.append("|---:|---:|---|---|---|---:|---:|")
for p in procs:
    if not p["comm"] and not p["exe"]:
        continue
    if not (p["exe"] or p["cmdline"].strip() or p["libs"] or p["fds"]):
        continue
    nl = len([x for x in p["libs"].split(";") if x])
    nf = len([x for x in p["fds"].split(";") if x])
    L.append("| %s | %s | %s | `%s` | `%s` | %d | %d |" % (
        p["pid"], p["ppid"], p["comm"], p["exe"], p["cmdline"][:80], nl, nf))
L.append("")
L.append("## 5. 关键进程的库/设备映射与打开文件")
L.append("")
for pid in ("1", "130", "131", "140"):
    p = next((x for x in procs if x["pid"] == pid), None)
    if not p:
        continue
    L.append("### PID %s：`%s`（%s）" % (pid, p["exe"] or p["comm"], p["comm"]))
    L.append("")
    L.append("- cmdline：`%s`" % (p["cmdline"] or "(空)"))
    L.append("- 映射（库/设备）：")
    for lib in p["libs"].split(";"):
        if lib:
            L.append("  - `%s`" % lib)
    L.append("- fds：")
    for fd in p["fds"].split(";"):
        if fd:
            L.append("  - `%s`" % fd)
    L.append("")
L.append("## 6. 文件 → 使用进程（动态观察）")
L.append("")
L.append("| 文件/设备 | 使用进程（PID:comm） |")
L.append("|---|---|")
for u in usage:
    L.append("| `%s` | %s |" % (u["path"], u["processes"].replace("|", "\\|")))
L.append("")
L.append("## 7. `/usr/bin` 等可执行文件的 CLI 提示（静态 strings）")
L.append("")
L.append("| 文件 | 用法/选项提示 |")
L.append("|---|---|")
for h in hints:
    L.append("| `%s` | %s |" % (h["path"], h["hints"].replace("|", "\\|")))
L.append("")
L.append("## 8. 调试建议")
L.append("")
L.append("| 子系统 | 先看这些进程/文件 |")
L.append("|---|---|")
L.append("| UI / 菜单 / GPU | `im.elf`、`libObj.so`、`viewUnified*.so`、`/dev/dmpgles2`、`/dev/mem`、`grm_gles.ko` |")
L.append("| 媒体/流 | `libmpr.so`、`/dev/stream`、`/dev/stream2`、`dma330.ko`、`codec_drv.ko`、`/usr/sabin` |")
L.append("| 存储/日志 | `im.elf` → `/log/AccessLog.*`、`emmc.ko`、`mmc_drv.ko`、`/dev/mmcb-char` |")
L.append("| USB / Senser | `sen.elf`、`/dev/usb/event`、`/dev/usb/otgcore`、`usbg_sen.ko`、`usb_extcmd.ko` |")
L.append("| 显示/HDMI | `/dev/cec`、`/dev/hdmi`、`hdmi.ko`、`cec.ko`、`dmm.ko` |")
L.append("| IPC / 启动阶段 | `/dev/uipc`、`osal_uipc.ko`、`libosal_uipc.so`、`bootin.elf`、`/proc/snsc_boot_time` |")
L.append("| 测试/工厂 | `scenario.elf`、`testcmd.elf`、`rcvcmd.elf`、`libtestcmd.so`、`/usr/scenario/*.so` |")
L.append("")
L.append("## 9. 复现")
L.append("")
L.append("```bash")
L.append("# 启动 QEMU（A7M3-QEMU-shell 的镜像 + 预编译 QEMU）")
L.append("python3 scripts/collect_runtime.py   # 采集 serial.log")
L.append("python3 scripts/collect_runtime2.py  # 采集 serial2.log（关键进程）")
L.append("python3 scripts/parse_runtime.py    # 生成 data/runtime-*.tsv")
L.append("python3 scripts/render_runtime.py   # 生成本文档")
L.append("```")
L.append("")
L.append("原始串口日志在 `/home/derek/a7m3-dyn/serial*.log`（未随仓库分发）。")

open(os.path.join(ROOT, "docs", "RUNTIME.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
print("wrote docs/RUNTIME.md", len(L), "lines")
