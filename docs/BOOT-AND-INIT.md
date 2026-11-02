# 启动链与 init 分析

数据来自 4.03 分区转储与 `/sbin/init`、`/usr/bin/bootin.elf`、
`/usr/bin/launch_shell.elf` 的字符串/符号。

## 0. 三种入口

| 入口 | 路径 | 作用 |
|---|---|---|
| 正常启动 | `/sbin/init` → `bootin.elf` → `im.elf` | 相机应用/菜单 |
| 调试 shell | `/usr/bin/launch_shell.elf` | 在 `/dev/console` 或 `/dev/ttycons` 起 `/bin/ash` |
| 场景/测试命令 | `/usr/bin/scenario.elf`、`testcmd.elf`、`rcvcmd.elf` | 经 `libtestcmd.so` 动态加载 `/usr/scenario/*.so` |

## 1. 存储布局

| 分区 | 大小/格式 | 挂载点 | 内容 |
|---|---|---|---|
| nflashaB0 | 4 MiB EXBL | boot0 | 引导固件 `EXBL V85.00.03` |
| nflasha1 | 8 MiB FAT12 | 不挂载 | `/BOOT` recovery、`KEMCO.TXT`、`LOADADDR.TXT` |
| nflasha2 | 20 MiB FAT12 | `/setting` | `kemco.txt`、`Backup.bin`、`DmmConfig.bin`、`facerec0-7`、`.hasp`、`updater/` |
| nflasha3 | 48 MiB FAT12 | `/system` | `vmlinux.bin`、`initrd.img`、`av-cam.bin`(LIRO)、`dfe_*`、`sabin/`、`lensbin_*` |
| nflasha4 | 12 MiB CMMeX | 不挂载 | 压缩容器（未解） |
| nflasha5 | 60 MiB WBI1 | 不挂载 | WBI 备份容器 |
| nflasha6 | 16 MiB FAT12 | 不挂载 | 空 |
| nflasha7 | 8 MiB ext2 | `/` | BusyBox、`/sbin/init`、glibc、基础 kmod |
| nflasha10 | 12 MiB FAT12 | `/etc`、`/tmp` | `config.spec`、`services`、`toprc`、字体、`jiritsu` 标记 |
| nflasha11 | 500 MiB FAT16 | `/log` | `ACCESS~1.DAT/.BAK` 日志 |
| nflasha12 | 40 MiB FAT12 | `/cert` | 证书挂载点（空） |
| nflasha13 | 4 MiB FAT12 | 不挂载 | `HASH/`、`HISTORY/UPDATE.LOG` |
| nflasha15 | 300 MiB ext2 | `/usr` | 应用/库/场景/kmod/DSP/编解码/资源 |
| nflasha16 | 140 MiB | 不挂载 | 全 0 |
| nflasha17 | 100 MiB FAT16 | 不挂载 | 空 |
| nflasha18 | 20 MiB FAT12 | `/lens` | `VX89xx/VX91xx_lensfile.bin` |
| nflasha19–25 | — | — | 无转储/空 |

## 2. `/sbin/init`：Sony 自写 init

`/sbin/init` 是 28 KB 的 ARM ELF，**不是 BusyBox init**。符号与字符串显示：

```
check_bootmode          check_mode_file        check_oreore1/2
check_qemu              check_nfs              parse_cmdline
parse_and_set_env       mount_partition        insmod_drivers
run_bg_process          set_stack_size         launch_shell
sigchild
```

它读取：

- `/proc/cmdline`、`/proc/mounts`、`/proc/version`、`/proc/snsc_boot_time`；
- `/proc/udm/upm_bootmode`、`/proc/udm/drivers`；
- `/setting/env.txt`、`/setting/mode/dmode`、`/setting/sen/smode`。

### 挂载的设备

```
/dev/nflasha2   -> /setting
/dev/nflasha3   -> /system   (cramfs 优先，失败回退 vfat)
/dev/nflasha7   -> /rootfs   -> / (pivot)
/dev/nflasha10  -> /etc      (同时承担 /tmp)
/dev/nflasha11  -> /log
/dev/nflasha12  -> /cert
/dev/nflasha15  -> /usr      (ext2 -> no-compress -> cramfs -> vfat 多级回退)
/dev/nflasha18  -> /lens
/dev/dnflasha3/7/15           直接设备节点变体
/dev/ms1                      Memory Stick
```

`/system` 与 `/usr` 的挂载都有多级回退逻辑（`mounting ... as ... failed` 字符串）。

### 加载的内核模块

rootfs `/kmod`：

```
devno.ko dmac.ko emmc.ko ldec.ko lld.ko nand.ko
```

`/usr/kmod`（由 init 的 `insmod_drivers` 加载）：

```
accel backup codec_drv compass dma330 dmm grm_gles grm_ma i2c indctr
input kikilog mag mcmn_drv mmc_drv ms_drv msen_drv nfc osal_uipc
osal_ulogio osal_utm sata_drv sircs stream stream2 udate upm
usb_extcmd usb_portMonitor usbg_sen utimer
```

`/usr/kmod` 里还带网络/USB/声卡/Wi-Fi 依赖模块（`bcmdhd`、`mac80211`、
`usb-storage`、`snd-*`、`ppp_*` 等），由脚本或模块依赖按需加载。

### 启动的后台进程

字符串中直接出现：

```
/usr/bin/bootin.elf
/usr/bin/launch_shell.elf
/usr/bin/net_cmdd.elf   (4.03 转储中没有该文件，可能仅 updater/其他机型)
/usr/bin/sen.elf
```

`launch_shell` 符号表明它负责在 `/dev/console` 或 `/dev/ttycons` 上 `execv("/bin/ash")`。

## 3. 启动阶段与 `bootin.elf`

`/usr/bin/change_mode.sh` 明确写出启动阶段：

| dmode | 阶段 |
|---|---|
| 0 | kernel boot |
| 1 | kernel boot → global infra |
| 2 | kernel boot → global infra → LIRO boot |
| 3 | kernel boot → global infra → LIRO boot → **appFw boot（默认）** |
| 4 | 同 1，但不启用 unified driver |
| 5 | 同 2，但不启用 unified driver |
| 6 | 同 3，但不启用 unified driver |
| 7 | appFw + LeakTracer |
| 8 | appFw + sslibc Wfree Check |
| 9 | appFw + KMC ICE |
| a | appFw + target gdb |
| b | appFw + gdbserver |
| d | appFw + DUMA |
| e | appFw + Electric Fence |
| f | appFw + jemalloc |
| 10 | appFw + mcheckb |

`bootin.elf` 的行为（strings）：

```
bootin.elf { file=<mode_file> } { dmode=<debug_mode> }
<im_target> : im.elf target=<tim_target>
/usr/bin/im.elf a &   /usr/bin/im.elf g &   /usr/bin/im.elf i &
/usr/bin/im.elf l &   /usr/bin/im.elf r &   /usr/bin/im.elf s &
/usr/bin/im.elf u &
/usr/bin/qsi.elf &   /usr/bin/qsi.elf noevent0 &
```

- 读 `/setting/mode/dmode` 与 `/setting/mode/preload`；
- 按目标（a/g/i/l/r/s/u）启动 `im.elf`；`qsi.elf` 在当前 4.03 转储中不存在；
- 可设置 `LD_PRELOAD` 为 `/usr/tool/LeakTracer.so`、`libefence.so`、
  `libjemalloc_tsh.so`、`libmcheckb.so`。

## 4. `im.elf`：薄启动器

`im.elf` 只有 23 KB，依赖：

```
libjemalloc_ds.so.1 libIMDB.so libosal_uipc.so libosal_utm.so libbackup.so
libdl.so.2 libpthread.so.0 libSTMcmdexecute.so libssl.so.3 libstdc++.so.6 ...
```

字符串显示：

```
/usr/lib/libObj.so
THREAD_APP / THREAD_INFRA0 / THREAD_INFRA1 / THREAD_INFRA2
a_thread / i0_thread / i1_thread / i2_thread
main()
```

推断：`im.elf` 解析参数后 `dlopen("/usr/lib/libObj.so")`，由 libObj 拉起应用框架，
并创建 App 线程与 3 个 Infra 线程。

## 5. 调试 shell

正常启动时 `launch_shell.elf` 会尝试：

```
/dev/ttycons -> /dev/console -> /bin/ash
/dev/ram0、/initrd（fallback）
```

这也是 QEMU 中能拿到 `/ #` 的原因之一；另一条路径是异常监视器的 `exit`。

## 6. QEMU 相关性

- QEMU 的 `cxd90045` 机器只模拟到“内核 + 用户态 + 部分驱动”；
- `grm_gles.ko` 未真正初始化 GPU，`im.elf` 打开菜单后会在 GPU 命令提交处失败；
- 这不会影响 `/sbin/init` 的挂载/启动逻辑，因此 shell 仍可用；
- 分区布局、`/setting/mode`、`bootin` 的参数是复现启动顺序的关键。
