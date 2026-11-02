# 动态运行分析（QEMU）

在 QEMU 中启动同一份 4.03 固件，进入 `/ #` 后通过串口采集：
`/proc/mounts`、`/proc/modules`、`/proc/devices`、`/proc/*/status`、
`/proc/*/maps`、`/proc/*/fd`，再与静态文件表合并。

> 采到的日志会与相机自身的 `[U tNNN]` 跟踪输出交错，部分进程的 maps/fd 可能不完整；
> 下表中的 `-` 只表示“本次运行未直接观察到”，不代表文件不会被使用。

## 1. 动态关键发现

1. **PID 1 是 `launch_shell.elf`**：`/sbin/init` 直接 exec 了它，
   它再 exec `/bin/ash --login`；这就是 QEMU 里能直接拿到 `/ #` 的原因。
2. **`/etc/ld.so.preload` 在启动时被写入 `/etc/shim_io.so`**：
   静态转储的 `/etc` 里没有这两个文件；运行时它们出现在 vfat（nflasha10）上，
   并被 launch_shell / bootin / sen / im.elf / ash 全部映射。
   `shim_io.so` 是 Sony 的 I/O 兼容/拦截层，调试时优先看它。
3. **用户态进程只有 5 个**：`launch_shell.elf`(1)、`bootin.elf`(130)、
   `sen.elf`(131)、`ash`(134)、`im.elf`(140)；其余是内核线程。
4. **`im.elf` 已经跑起来**，并打开了 Sugilite/媒体/存储相关设备：
   `/dev/dmpgles2`、`/dev/mem`、`/dev/stream`、`/dev/stream2`、`/dev/cec`、
   `/dev/hdmi`、`/dev/mmcb-char`、`/dev/usb/buspwr`、`/dev/uipc`；
   同时写 `/log/AccessLog.dat` 与 `/log/AccessLog.bak`。
5. **`sen.elf` 打开 USB 事件/OTG**：`/dev/usb/event`、`/dev/usb/otgcore`，
   并加载 `libSTMcmdexecute`、`libInfraUsbCmn`、`libsencore`、`libpro00`、
   `libcrypto/libssl`。
6. **`bootin.elf` 读 `/proc/snsc_boot_time`**，打开 `/dev/uipc`、`/dev/console`；
   它是启动阶段管理器，运行期仍驻留。

## 2. 挂载表（`/proc/mounts`）

| 设备 | 挂载点 | 类型 | 选项 |
|---|---|---|---|
| `rootfs` | `/` | rootfs | rw |
| `/dev/nflasha7` | `/` | ext2 | ro,relatime,errors=continue |
| `/dev/nflasha15` | `/usr` | ext2 | ro,relatime,errors=continue |
| `/dev/nflasha10` | `/tmp` | vfat | rw,sync,dirsync,noatime,fmask=0022,dmask=0022,codepage=cp437,iocharset=ascii,shortname=mixed,posix_attr,avoid_dlink,errors=remount-ro |
| `/dev/nflasha10` | `/etc` | vfat | rw,sync,dirsync,noatime,fmask=0022,dmask=0022,codepage=cp437,iocharset=ascii,shortname=mixed,posix_attr,avoid_dlink,errors=remount-ro |
| `/dev/nflasha3` | `/system` | vfat | rw,sync,dirsync,noatime,fmask=0022,dmask=0022,codepage=cp437,iocharset=ascii,shortname=mixed,posix_attr,avoid_dlink,errors=remount-ro |
| `/dev/nflasha2` | `/setting` | vfat | rw,sync,dirsync,noatime,fmask=0022,dmask=0022,codepage=cp437,iocharset=ascii,shortname=mixed,posix_attr,avoid_dlink,errors=remount-ro |
| `/dev/nflasha11` | `/log` | vfat | rw,dirsync,noatime,fmask=0022,dmask=0022,codepage=cp437,iocharset=ascii,shortname=mixed,batch_sync,posix_attr,avoid_dlink,errors=remount-ro |
| `/dev/nflasha18` | `/lens` | vfat | rw,sync,dirsync,noatime,fmask=0022,dmask=0022,codepage=cp437,iocharset=ascii,shortname=mixed,posix_attr,avoid_dlink,errors=remount-ro |
| `/dev/nflasha12` | `/cert` | vfat | rw,dirsync,noatime,fmask=0022,dmask=0022,codepage=cp437,iocharset=ascii,shortname=mixed,batch_sync,posix_attr,avoid_dlink,errors=remount-ro |

要点：`/`（nflasha7）和 `/usr`（nflasha15）是 **只读 ext2**；
`/tmp` 与 `/etc` 都来自 **nflasha10 vfat rw**；`/system`、`/setting`、
`/log`、`/lens`、`/cert` 是 vfat rw。

## 3. 已加载内核模块（`/proc/modules`）

| 模块 | 大小 | 引用 | 依赖 | 状态 |
|---|---:|---:|---|---|
| `devno` | 1941 | 15 | dma330,mmc_drv,ms_drv,mcmn_drv,grm_gles,usb_extcmd,usbg_sen,usb_portMonitor,stream2,stream,backup,osal_uipc,emmc,ldec,dmac, | Live |
| `dmac` | 12284 | 2 | emmc,ldec, | Live |
| `ldec` | 10106 | 1 | emmc, | Live |
| `emmc` | 169443 | 9 | - | Live |
| `osal_utm` | 2139 | 12 | codec_drv,ms_drv,mcmn_drv,accel,nfc,upm,dmm,usb_portMonitor,i2c,osal_ulogio,utimer,osal_uipc, | Live |
| `osal_uipc` | 35801 | 25 | codec_drv,dma330,mmc_drv,ms_drv,mcmn_drv,compass,mag,accel,grm_gles,grm_ma,nfc,upm,dmm,usbg_sen,usb_portMonitor,sircs,i2c,indctr,input,osal_ulogio,backup,utimer, | Live |
| `utimer` | 21490 | 0 | - | Live |
| `backup` | 61073 | 12 | mcmn_drv,mag,accel,nfc,upm,dmm,usbg_sen,usb_portMonitor,i2c,indctr,input,osal_ulogio, | Live |
| `osal_ulogio` | 29859 | 0 | - | Live |
| `input` | 22826 | 0 | - | Live |
| `indctr` | 7911 | 0 | - | Live |
| `i2c` | 10261 | 0 | - | Live |
| `sircs` | 15346 | 0 | - | Live |
| `stream` | 1077 | 0 | - | Live |
| `stream2` | 1629 | 0 | - | Live |
| `usb_portMonitor` | 11648 | 0 | - | Live |
| `usbg_sen` | 30337 | 0 | - | Live |
| `usb_extcmd` | 9499 | 0 | - | Live |
| `dmm` | 3133020 | 1 | upm, | Live |
| `upm` | 108467 | 0 | - | Live |
| `nfc` | 10006 | 0 | - | Live |
| `grm_ma` | 19628 | 0 | - | Live |
| `grm_gles` | 9304 | 0 | - | Live |
| `accel` | 9064 | 0 | - | Live |
| `mag` | 6821 | 0 | - | Live |
| `compass` | 2734 | 0 | - | Live |
| `mcmn_drv` | 91316 | 2 | mmc_drv,ms_drv, | Live |
| `ms_drv` | 162852 | 0 | - | Live |
| `mmc_drv` | 185234 | 0 | - | Live |
| `dma330` | 247683 | 0 | - | Live |
| `codec_drv` | 12620 | 0 | - | Live |

## 4. 用户态进程

| PID | PPid | comm | exe | cmdline | 映射 | fds |
|---:|---:|---|---|---|---:|---:|
| 1 |  | launch_shell.el | `/usr/bin/launch_shell.elf` | `/usr/bin/launch_shell.elf 1 1` | 10 | 1 |
| 130 |  | bootin.elf | `/usr/bin/bootin.elf` | `/usr/bin/bootin.elf` | 14 | 3 |
| 131 |  | sen.elf | `/usr/bin/sen.elf` | `/usr/bin/sen.elf` | 20 | 5 |
| 134 |  | ash | `/bin/busybox` | `/bin/ash --login` | 8 | 2 |
| 140 |  | im.elf | `/usr/bin/im.elf` | `` | 74 | 12 |

## 5. 关键进程的库/设备映射与打开文件

### PID 1：`/usr/bin/launch_shell.elf`（launch_shell.el）

- cmdline：`/usr/bin/launch_shell.elf 1 1`
- 映射（库/设备）：
  - `/etc/shim_io.so`
  - `/lib/ld-2.11.2.so`
  - `/lib/libc-2.11.2.so`
  - `/lib/libdl-2.11.2.so`
  - `/lib/libgcc_s.so.1`
  - `/lib/libm-2.11.2.so`
  - `/lib/libpthread-2.11.2.so`
  - `/lib/librt-2.11.2.so`
  - `/usr/bin/launch_shell.elf`
  - `/usr/lib/libstdc++.so.6.0.14`
- fds：
  - `/dev/ttyAM0`

### PID 130：`/usr/bin/bootin.elf`（bootin.elf）

- cmdline：`/usr/bin/bootin.elf`
- 映射（库/设备）：
  - `/dev/uipc`
  - `/etc/shim_io.so`
  - `/lib/ld-2.11.2.so`
  - `/lib/libc-2.11.2.so`
  - `/lib/libdl-2.11.2.so`
  - `/lib/libgcc_s.so.1`
  - `/lib/libm-2.11.2.so`
  - `/lib/libpthread-2.11.2.so`
  - `/lib/librt-2.11.2.so`
  - `/usr/bin/bootin.elf`
  - `/usr/lib/libbackup.so`
  - `/usr/lib/libosal_uipc.so`
  - `/usr/lib/libosal_utm.so`
  - `/usr/lib/libstdc++.so.6.0.14`
- fds：
  - `/dev/console`
  - `/dev/uipc`
  - `/proc/snsc_boot_time`

### PID 131：`/usr/bin/sen.elf`（sen.elf）

- cmdline：`/usr/bin/sen.elf`
- 映射（库/设备）：
  - `/dev/uipc`
  - `/etc/shim_io.so`
  - `/lib/ld-2.11.2.so`
  - `/lib/libSTMcmdexecute.so`
  - `/lib/libc-2.11.2.so`
  - `/lib/libdl-2.11.2.so`
  - `/lib/libgcc_s.so.1`
  - `/lib/libm-2.11.2.so`
  - `/lib/libpthread-2.11.2.so`
  - `/lib/librt-2.11.2.so`
  - `/usr/bin/sen.elf`
  - `/usr/lib/libInfraUsbCmn.so`
  - `/usr/lib/libbackup.so`
  - `/usr/lib/libcrypto.so.3`
  - `/usr/lib/libosal_uipc.so`
  - `/usr/lib/libpro00.so`
  - `/usr/lib/libsencore.so`
  - `/usr/lib/libssl.so.3`
  - `/usr/lib/libstdc++.so.6.0.14`
  - `/usr/lib/libtestcmd.so`
- fds：
  - `/dev/console`
  - `/dev/uipc`
  - `/dev/usb/event`
  - `/dev/usb/otgcore`
  - `/proc/snsc_boot_time`

### PID 140：`/usr/bin/im.elf`（im.elf）

- cmdline：`(空)`
- 映射（库/设备）：
  - `/dev/dmpgles2`
  - `/dev/mem`
  - `/dev/stream`
  - `/dev/uipc`
  - `/etc/shim_io.so`
  - `/lib/ld-2.11.2.so`
  - `/lib/libSTMcmdexecute.so`
  - `/lib/libc-2.11.2.so`
  - `/lib/libdl-2.11.2.so`
  - `/lib/libgcc_s.so.1`
  - `/lib/libm-2.11.2.so`
  - `/lib/libpthread-2.11.2.so`
  - `/lib/librt-2.11.2.so`
  - `/usr/bin/im.elf`
  - `/usr/lib/CautionConfig.so`
  - `/usr/lib/dataflowInfraFramework.so`
  - `/usr/lib/libAK8975.so`
  - `/usr/lib/libBTAdjust.so`
  - `/usr/lib/libBTUtils.so`
  - `/usr/lib/libBackupManager.so`
  - `/usr/lib/libBizFw.so`
  - `/usr/lib/libBizFw2.so`
  - `/usr/lib/libBusPower.so`
  - `/usr/lib/libGOConnectionManager.so`
  - `/usr/lib/libIMDB.so`
  - `/usr/lib/libInfraAccessLog.so`
  - `/usr/lib/libInfraAirplaneMode.so`
  - `/usr/lib/libInfraBluetooth.so`
  - `/usr/lib/libInfraBluetoothCore.so`
  - `/usr/lib/libInfraFsys.so`
  - `/usr/lib/libInfraHdmi.so`
  - `/usr/lib/libInfraKikiLogGenerator.so`
  - `/usr/lib/libInfraMediaCommon.so`
  - `/usr/lib/libInfraMediaDetect.so`
  - `/usr/lib/libInfraMediaMount.so`
  - `/usr/lib/libInfraNetInitializer.so`
  - `/usr/lib/libInfraNfc.so`
  - `/usr/lib/libInfraSKD.so`
  - `/usr/lib/libInfraUsbCmn.so`
  - `/usr/lib/libJiritsu.so`
  - `/usr/lib/libMWF.so`
  - `/usr/lib/libNetCommon.so`
  - `/usr/lib/libNetContUtil.so`
  - `/usr/lib/libNetRemote.so`
  - `/usr/lib/libObj.so`
  - `/usr/lib/libOnDemandLoader.so`
  - `/usr/lib/libResourceBluetooth.so`
  - `/usr/lib/libRsrcHotshoe.so`
  - `/usr/lib/libSKDWrapperManager.so`
  - `/usr/lib/libSysDef.so`
  - `/usr/lib/libUsbBusPower.so`
  - `/usr/lib/libUsbControl.so`
  - `/usr/lib/libbackup.so`
  - `/usr/lib/libclema.so`
  - `/usr/lib/libcompassutil.so`
  - `/usr/lib/libcrypto.so.3`
  - `/usr/lib/libexpat.so.1.6.11`
  - `/usr/lib/libjemalloc_ds.so.1`
  - `/usr/lib/libjsoncpp.so.23`
  - `/usr/lib/libmintx.so`
  - `/usr/lib/libmpr.so`
  - `/usr/lib/libmprctrl.so`
  - `/usr/lib/libmprdummy.so`
  - `/usr/lib/libosal_uipc.so`
  - `/usr/lib/libosal_ulogio.so`
  - `/usr/lib/libosal_utm.so`
  - `/usr/lib/libpro00.so`
  - `/usr/lib/libsencore.so`
  - `/usr/lib/libssl.so.3`
  - `/usr/lib/libstdc++.so.6.0.14`
  - `/usr/lib/libtestcmd.so`
  - `/usr/lib/libutil_date.so`
  - `/usr/lib/libz.so.1.2.11`
  - `/usr/lib/viewUnified2.so`
- fds：
  - `/dev/cec`
  - `/dev/console`
  - `/dev/dmpgles2`
  - `/dev/hdmi`
  - `/dev/mem`
  - `/dev/mmcb-char`
  - `/dev/stream`
  - `/dev/stream2`
  - `/dev/uipc`
  - `/dev/usb/buspwr`
  - `/log/AccessLog.bak`
  - `/log/AccessLog.dat`

## 6. 文件 → 使用进程（动态观察）

| 文件/设备 | 使用进程（PID:comm） |
|---|---|
| `/bin/busybox` | 134:ash |
| `/dev/cec` | 140:im.elf |
| `/dev/console` | 130:bootin.elf;131:sen.elf;140:im.elf |
| `/dev/dmpgles2` | 140:im.elf |
| `/dev/hdmi` | 140:im.elf |
| `/dev/mem` | 140:im.elf |
| `/dev/mmcb-char` | 140:im.elf |
| `/dev/stream` | 140:im.elf |
| `/dev/stream2` | 140:im.elf |
| `/dev/tty` | 134:ash |
| `/dev/ttyAM0` | 1:launch_shell.el;134:ash |
| `/dev/uipc` | 130:bootin.elf;131:sen.elf;140:im.elf |
| `/dev/usb/buspwr` | 140:im.elf |
| `/dev/usb/event` | 131:sen.elf |
| `/dev/usb/otgcore` | 131:sen.elf |
| `/etc/shim_io.so` | 1:launch_shell.el;130:bootin.elf;131:sen.elf;134:ash;140:im.elf |
| `/lib/ld-2.11.2.so` | 1:launch_shell.el;130:bootin.elf;131:sen.elf;134:ash;140:im.elf |
| `/lib/libSTMcmdexecute.so` | 131:sen.elf;140:im.elf |
| `/lib/libc-2.11.2.so` | 1:launch_shell.el;130:bootin.elf;131:sen.elf;134:ash;140:im.elf |
| `/lib/libcrypt-2.11.2.so` | 134:ash |
| `/lib/libdl-2.11.2.so` | 1:launch_shell.el;130:bootin.elf;131:sen.elf;140:im.elf |
| `/lib/libgcc_s.so.1` | 1:launch_shell.el;130:bootin.elf;131:sen.elf;140:im.elf |
| `/lib/libm-2.11.2.so` | 1:launch_shell.el;130:bootin.elf;131:sen.elf;140:im.elf |
| `/lib/libnss_files-2.11.2.so` | 134:ash |
| `/lib/libpthread-2.11.2.so` | 1:launch_shell.el;130:bootin.elf;131:sen.elf;134:ash;140:im.elf |
| `/lib/librt-2.11.2.so` | 1:launch_shell.el;130:bootin.elf;131:sen.elf;134:ash;140:im.elf |
| `/log/AccessLog.bak` | 140:im.elf |
| `/log/AccessLog.dat` | 140:im.elf |
| `/proc/snsc_boot_time` | 130:bootin.elf;131:sen.elf |
| `/usr/bin/bootin.elf` | 130:bootin.elf |
| `/usr/bin/im.elf` | 140:im.elf |
| `/usr/bin/launch_shell.elf` | 1:launch_shell.el |
| `/usr/bin/sen.elf` | 131:sen.elf |
| `/usr/lib/CautionConfig.so` | 140:im.elf |
| `/usr/lib/dataflowInfraFramework.so` | 140:im.elf |
| `/usr/lib/libAK8975.so` | 140:im.elf |
| `/usr/lib/libBTAdjust.so` | 140:im.elf |
| `/usr/lib/libBTUtils.so` | 140:im.elf |
| `/usr/lib/libBackupManager.so` | 140:im.elf |
| `/usr/lib/libBizFw.so` | 140:im.elf |
| `/usr/lib/libBizFw2.so` | 140:im.elf |
| `/usr/lib/libBusPower.so` | 140:im.elf |
| `/usr/lib/libGOConnectionManager.so` | 140:im.elf |
| `/usr/lib/libIMDB.so` | 140:im.elf |
| `/usr/lib/libInfraAccessLog.so` | 140:im.elf |
| `/usr/lib/libInfraAirplaneMode.so` | 140:im.elf |
| `/usr/lib/libInfraBluetooth.so` | 140:im.elf |
| `/usr/lib/libInfraBluetoothCore.so` | 140:im.elf |
| `/usr/lib/libInfraFsys.so` | 140:im.elf |
| `/usr/lib/libInfraHdmi.so` | 140:im.elf |
| `/usr/lib/libInfraKikiLogGenerator.so` | 140:im.elf |
| `/usr/lib/libInfraMediaCommon.so` | 140:im.elf |
| `/usr/lib/libInfraMediaDetect.so` | 140:im.elf |
| `/usr/lib/libInfraMediaMount.so` | 140:im.elf |
| `/usr/lib/libInfraNetInitializer.so` | 140:im.elf |
| `/usr/lib/libInfraNfc.so` | 140:im.elf |
| `/usr/lib/libInfraSKD.so` | 140:im.elf |
| `/usr/lib/libInfraUsbCmn.so` | 131:sen.elf;140:im.elf |
| `/usr/lib/libJiritsu.so` | 140:im.elf |
| `/usr/lib/libMWF.so` | 140:im.elf |
| `/usr/lib/libNetCommon.so` | 140:im.elf |
| `/usr/lib/libNetContUtil.so` | 140:im.elf |
| `/usr/lib/libNetRemote.so` | 140:im.elf |
| `/usr/lib/libObj.so` | 140:im.elf |
| `/usr/lib/libOnDemandLoader.so` | 140:im.elf |
| `/usr/lib/libResourceBluetooth.so` | 140:im.elf |
| `/usr/lib/libRsrcHotshoe.so` | 140:im.elf |
| `/usr/lib/libSKDWrapperManager.so` | 140:im.elf |
| `/usr/lib/libSysDef.so` | 140:im.elf |
| `/usr/lib/libUsbBusPower.so` | 140:im.elf |
| `/usr/lib/libUsbControl.so` | 140:im.elf |
| `/usr/lib/libbackup.so` | 130:bootin.elf;131:sen.elf;140:im.elf |
| `/usr/lib/libclema.so` | 140:im.elf |
| `/usr/lib/libcompassutil.so` | 140:im.elf |
| `/usr/lib/libcrypto.so.3` | 131:sen.elf;140:im.elf |
| `/usr/lib/libexpat.so.1.6.11` | 140:im.elf |
| `/usr/lib/libjemalloc_ds.so.1` | 140:im.elf |
| `/usr/lib/libjsoncpp.so.23` | 140:im.elf |
| `/usr/lib/libmintx.so` | 140:im.elf |
| `/usr/lib/libmpr.so` | 140:im.elf |
| `/usr/lib/libmprctrl.so` | 140:im.elf |
| `/usr/lib/libmprdummy.so` | 140:im.elf |
| `/usr/lib/libosal_uipc.so` | 130:bootin.elf;131:sen.elf;140:im.elf |
| `/usr/lib/libosal_ulogio.so` | 140:im.elf |
| `/usr/lib/libosal_utm.so` | 130:bootin.elf;140:im.elf |
| `/usr/lib/libpro00.so` | 131:sen.elf;140:im.elf |
| `/usr/lib/libsencore.so` | 131:sen.elf;140:im.elf |
| `/usr/lib/libssl.so.3` | 131:sen.elf;140:im.elf |
| `/usr/lib/libstdc++.so.6.0.14` | 1:launch_shell.el;130:bootin.elf;131:sen.elf;140:im.elf |
| `/usr/lib/libtestcmd.so` | 131:sen.elf;140:im.elf |
| `/usr/lib/libutil_date.so` | 140:im.elf |
| `/usr/lib/libz.so.1.2.11` | 140:im.elf |
| `/usr/lib/viewUnified2.so` | 140:im.elf |

## 7. `/usr/bin` 等可执行文件的 CLI 提示（静态 strings）

| 文件 | 用法/选项提示 |
|---|---|
| `/usr/bin/bk.elf` | usage: bk command [command-option-and-arguments] \| usage: bk r BackupID \| usage: bk w BackupID Data \| usage: bk y num BackupID \| usage: bk z num BackupID Data |
| `/usr/bin/ujlog.elf` | USAGE:type ujlog.elf usb or ujlog.elf jet |
| `/usr/bin/wpa_supplicant` | SSL_CTX_set_options \| SSL_set_options \| TLS: using phase2 config options \| TLS: using phase1 config options \| usage: \| options: |
| `/usr/bin/iperf` | Usage: %s [-s\|-c host] [options] \| Try `%s --help' for more information. \| Usage: iperf [-s\|-c host] [options] \| -f, --format    [kmKM]   format to report: Kbits, Mbits, KBytes, MBytes \| -i, --interval  #        seconds between periodic bandwidth reports \| -l, --len       #[KM]    length of buffer to read or write (default 8 KB) |
| `/usr/bin/btRFTest.elf` | Usage: %s [OPTION]... <API> [param]... \| Options : \| -d      Enable debug print. \| -h      Show this usage. \| --help  Show how to use in detail. \| Please execute `%s --help' |
| `/usr/bin/Wltestcmd` | -help/-h                            :  usage \| /usr/bin/sndcmd.elf --sync 0xA503FB d:0x1011 d:0x0000 d:0x00%.2x \| print_usage \| usage |
| `/usr/bin/scenario.elf` | cmdline_show_usage \| --ver \| --ifile ifile \| --ibfile ibfile \| --obfile obfile \| <options> [scenario_name] [size]:[data] ... |
| `/usr/bin/bootin.elf` | MALLOC_OPTIONS=2W \| gdb --args \| MALLOC_OPTIONS |
| `/usr/bin/wl` | Give suboption "list" to list various suboptions \| Usage: ol_cons [<cmd>] \| Usage: srclear <len> \| --preview option allows you to review the update without committing it \| -b <file> -- also write raw bytes to <file> \| -1 (default) means automatically determine the best rate |
| `/usr/bin/mwf_monio.elf` | - |
| `/usr/bin/sen.elf` | [ built options ] \| b |
| `/usr/bin/adjstctl.elf` | cmdline_show_usage \| UNINSTALL_ALL_OPTIONS \| --ver \| --ifile ifile \| --ibfile ibfile \| --obfile obfile |
| `/usr/bin/netblog.elf` | USAGE:netblog.elf [object\|dlna\|other\|error] |
| `/usr/bin/btblog.elf` | - |
| `/usr/bin/dhd` | -h   <data> is a sequence of hex digits rather than a char string \| -r   output binary to stdout rather hex \| --noreset    do not reset SOCRAM core before download \| --norun      do not start dongle CPU after download \| --verify     do readback verify \| -c means write regardless of crc |
| `/usr/bin/testcmd.elf` | cmdline_show_usage \| --ver \| --sync \| <options> [osal_id] [data] ... |
| `/usr/bin/SetPort.elf` | - |
| `/usr/bin/ud_send_lsi.elf` | - |
| `/usr/bin/soundstretch` | Usage : \| _ZL5usage |
| `/usr/bin/sndcmd.elf` | cmdline_show_usage \| --ver \| --ifile ifile \| --ibfile ibfile \| --obfile obfile \| --ulogio |
| `/usr/bin/ulogio.elf` | - |
| `/usr/bin/launch_shell.elf` | --login |
| `/usr/bin/orb-server` | (%04d)[INF:OrbServerMain: %04d]input options ... \| ["getSettingsTree",["{\"usage\":\"string\"}"], ["{\"settings\":\"SettingsTreeList[]\"}"],"1.1"] \| usage \| {"usage":"string"} \| OPTIONS \| OPTIONS |
| `/usr/bin/NsBkSet.elf` | - |
| `/usr/bin/gpioctrl.elf` | Usage: gpioctrl [--help] [--verbose] <command> [<args>] \| write     \| w  [PIN_NAME \| port bit] <options> <0\|1>   write data to specified gpio registers \| intwrite  \| iw [PIN_NAME \| bit] <options>              write data to gpio-interrput registers \| -f, --func                      set pin mode 'Function' \| -g, --gpio                      set pin mode 'GPIO' \| -d, --dir direction             set gpio direction |
| `/usr/bin/rcvcmd.elf` | cmdline_show_usage \| --ver \| --ifile ifile \| --ulogio \| --sync \| --tmo timeout |
| `/usr/bin/crypter.elf` | - |
| `/usr/bin/bsa_server` | uipc_thread_get_usage: task missed \| l2c_fcr_adj_our_req_options - preferred_mode (%d), does not match mode (%d) \| l2c_fcr_adj_our_req_options (mode %d): ERROR: No FCR options set using BASIC mode \| bsa_sv_tm_get_mem_usage_hdlr \| bsa_sv_tm_get_mem_usage_hdlr Get GKI Tasks info \| bsa_sv_tm_get_mem_usage_hdlr task:%d missed |
| `/usr/bin/uuidgen` | Usage: %s [-r] [-t] |
| `/usr/bin/GPIO2SDIO.elf` | - |
| `/usr/bin/mpr_viewLog.elf` | - |
| `/usr/bin/im.elf` | - |
| `/usr/bin/SDIO2GPIO.elf` | - |
| `/usr/bin/ud_datcnv.elf` | - |
| `/usr/bin/mpr_monio.elf` | - |
| `/usr/bin/openssl` | SSL_CTX_set_options \| SSL_set_options \| SSL_get_options \| BN_options \| General options: \| I/O options: |
| `/usr/sbin/pump` | poptHelpOptions \| Help options: \| Usage: \| usage \| Display brief usage message \| showShortOptions |
| `/usr/sbin/dhcpd` | Usage: %s [-p <UDP port #>] [-f] [-d] [-q] [-t\|-T] \| --no-pid \| --version \| stash-agent-options \| options.c \| can't look up options in %s space. |
| `/usr/sbin/iptables-multi` | xtables_merge_options \| Usage: %s [-b] [-c] [-v] [-t] [-h] \| [ --binary ] \| [ --counters ] \| [ --verbose ] \| [ --test ] |
| `/usr/sbin/tcpdump` | Options \| , options ( \| Options: [%s] \| Options [%s] \| Router LSA Options: [%s] \| Options: 0x%08x [%s] |
| `/usr/scenario/CAMERA_SCN_MOVIE_REC_START.so` | - |
| `/usr/scenario/AVBB_SCN_L_R_SETTING.so` | - |
| `/usr/scenario/AVBB_SCN_START_AUDIO.so` | - |
| `/usr/scenario/MPR_SCN_SET_FACTORY_MODE.so` | - |
| `/usr/scenario/AVBB_SCN_START_HDMI.so` | - |
| `/usr/scenario/AVBB_SCN_START_PANELEVF.so` | - |
| `/usr/scenario/CAMERA_SCN_SET_ZOOM_DRV.so` | - |
| `/usr/scenario/CAMERA_SCN_FACE_REC_DATA.so` | - |
| `/usr/scenario/AVBB_SCN_START_VIDEO.so` | - |
| `/usr/scenario/MPR_SCN_FLASH_BACKUP_INIT.so` | - |
| `/usr/scenario/AVBB_SCN_STOP_VIDEO.so` | - |
| `/usr/scenario/AVBB_SCN_STOP_MICSENSE.so` | - |
| `/usr/scenario/AVBB_SCN_START_MIC.so` | - |
| `/usr/scenario/AVBB_SCN_START_HDMI_INPUT.so` | - |
| `/usr/scenario/CAMERA_SCN_VIDEOLIGHT_SW.so` | - |
| `/usr/scenario/AVBB_SCN_STOP_PANELEVF.so` | - |
| `/usr/scenario/CAMERA_SCN_EXTERNAL_RAW_RECORD.so` | - |
| `/usr/scenario/AVBB_SCN_STOP_HDMI_INPUT.so` | - |
| `/usr/scenario/AVBB_SCN_START_HDMI_SUB.so` | - |
| `/usr/scenario/MPR_SCN_INSTALL_MAP_DEMOMOVIE.so` | UNINSTALL_ALL_OPTIONS |
| `/usr/scenario/AVBB_SCN_L_R_SETTING_PANELEVF.so` | - |
| `/usr/scenario/AVBB_SCN_STOP_MIC.so` | - |
| `/usr/scenario/MPR_SCN_EXEC_FACTORY_MODE.so` | - |
| `/usr/scenario/AVBB_SCN_START_HDMI_INPUT_SUB.so` | - |
| `/usr/scenario/AVBB_SCN_STOP_HDMI.so` | - |
| `/usr/scenario/MPR_SCN_FORMAT.so` | - |
| `/usr/scenario/MPR_SCN_EXEC_WIFI_TEST.so` | - |
| `/usr/scenario/CAMERA_SCN_EE_SETUP_START_STOP.so` | - |
| `/usr/scenario/MPR_SCN_GET_TOTAL_LOG.so` | - |
| `/usr/scenario/AVBB_SCN_OPTAXIS_PANELEVF.so` | - |
| `/usr/scenario/AVBB_SCN_START_MICSENSE.so` | - |
| `/usr/scenario/CAMERA_SCN_EE_START_STOP.so` | - |
| `/usr/scenario/AVBB_SCN_STOP_AUDIO.so` | - |
| `/usr/scenario/CAMERA_SCN_EE_SET_PRM.so` | - |
| `/usr/scenario/MPR_SCN_GET_CONTENT_COUNT.so` | - |
| `/sbin/init` | MALLOC_OPTIONS=gfffffffff \| /bin/ash --login |
| `/sbin/mkdosfs` | Usage: mkdosfs [-A] [-c] [-C] [-v] [-I] [-l bad-block-file] [-b backup-boot-sector] \| usage |
| `/sbin/sysctl` | Usage: \| %s [options] [variable[=value] ...] \| Options: \| -a, --all            display all variables \| -A                   alias of -a \| -X                   alias of -a |
| `/sbin/dosfsck` | usage: %s [-aAflrtvVwy] [-d path -d ...] [-u path -u ...] \| -a       automatically repair the file system \| -A       toggle Atari file system format \| -d path  drop that file \| -f       salvage unused chains to files \| -l       list path names |
| `/bin/vmstat` | Usage: \| %s [options] [delay [count]] \| Options: \| -a, --active           active/inactive memory \| -f, --forks            number of forks since boot \| -m, --slabs            slabinfo |
| `/bin/top` | CPU Usage \| Memory Usage (RES) \| Usage: \| Usage: \| Usage: \| -d disallowed in "secure" mode |
| `/bin/ps` | q/-q/--quick-pid cannot be combined with other selection options. \| q/-q,--quick-pid cannot be used together with sort options. \| Usage: \| %s [options] \| Basic options: \| -a                   all with tty, except session leaders |
| `/bin/dnsdomainname` | Usage: hostname [-v] [-b] {hostname\|-F file}         set host name (from file) \| Program options: \| -s, --short            short host name \| -a, --alias            alias names \| -i, --ip-address       addresses for the host name \| -I, --all-ip-addresses all addresses for the host |
| `/bin/hostname` | Usage: hostname [-v] [-b] {hostname\|-F file}         set host name (from file) \| Program options: \| -s, --short            short host name \| -a, --alias            alias names \| -i, --ip-address       addresses for the host name \| -I, --all-ip-addresses all addresses for the host |
| `/bin/cat` | Try `%s --help' for more information. \| Usage: %s [OPTION] [FILE]... \| -A, --show-all           equivalent to -vET \| -b, --number-nonblank    number nonblank output lines \| -e                       equivalent to -vE \| -E, --show-ends          display $ at end of each line |
| `/bin/lsattr` | Usage: %s [-RVadlv] [files...] \| pf_options |
| `/bin/chattr` | Usage: %s [-RVf] [-+=AacDdeijsSu] [-v version] files... \| usage |
| `/bin/busybox` | -0 bS \| -d |

## 8. 调试建议

| 子系统 | 先看这些进程/文件 |
|---|---|
| UI / 菜单 / GPU | `im.elf`、`libObj.so`、`viewUnified*.so`、`/dev/dmpgles2`、`/dev/mem`、`grm_gles.ko` |
| 媒体/流 | `libmpr.so`、`/dev/stream`、`/dev/stream2`、`dma330.ko`、`codec_drv.ko`、`/usr/sabin` |
| 存储/日志 | `im.elf` → `/log/AccessLog.*`、`emmc.ko`、`mmc_drv.ko`、`/dev/mmcb-char` |
| USB / Senser | `sen.elf`、`/dev/usb/event`、`/dev/usb/otgcore`、`usbg_sen.ko`、`usb_extcmd.ko` |
| 显示/HDMI | `/dev/cec`、`/dev/hdmi`、`hdmi.ko`、`cec.ko`、`dmm.ko` |
| IPC / 启动阶段 | `/dev/uipc`、`osal_uipc.ko`、`libosal_uipc.so`、`bootin.elf`、`/proc/snsc_boot_time` |
| 测试/工厂 | `scenario.elf`、`testcmd.elf`、`rcvcmd.elf`、`libtestcmd.so`、`/usr/scenario/*.so` |

## 9. 复现

```bash
# 启动 QEMU（A7M3-QEMU-shell 的镜像 + 预编译 QEMU）
python3 scripts/collect_runtime.py   # 采集 serial.log
python3 scripts/collect_runtime2.py  # 采集 serial2.log（关键进程）
python3 scripts/parse_runtime.py    # 生成 data/runtime-*.tsv
python3 scripts/render_runtime.py   # 生成本文档
```

原始串口日志在 `/home/derek/a7m3-dyn/serial*.log`（未随仓库分发）。
