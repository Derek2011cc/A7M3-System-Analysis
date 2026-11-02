# 文件清单与作用

由 `scripts/analyze.py` 从服务模式分区转储中提取并生成；
角色为按路径/文件类型/ELF 依赖做的**大致分类**，关键文件有单独说明。
“动态使用”来自 QEMU 运行时 `/proc/*/maps`、`/proc/*/fd` 采集，`-` 表示本次运行中未直接观察到（不代表不会使用）。

总文件数 **1177**（其中 ELF 457、脚本 24、符号链接 139、数据 557）。

## nflasha7（rootfs，挂载到 /）

### `/`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `version.txt` | 19 B | data | 数据/其他：version.txt | - |

### `/bin`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `ash` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `busybox` | 423 KB | elf | 核心工具：BusyBox 多合一二进制，提供 sh/ls/mount/insmod 等 | ash |
| `cat` | 25 KB | elf | 基础命令：cat：查看/拼接文件 | - |
| `chattr` | 12 KB | elf | 文件属性：chattr：修改 ext2 文件属性 | - |
| `chgrp` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `chmod` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `chown` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `compile_et` | 1 KB | script | 开发工具：Kerberos error-table 编译脚本 | - |
| `cp` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `cpio` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `date` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `dd` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `dmesg` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `dnsdomainname` | 16 KB | elf | 主机名工具：显示 DNS 域名 | - |
| `echo` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `egrep` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `false` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `fgrep` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `grep` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `gunzip` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `gzip` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `hostname` | 16 KB | elf | 主机名工具：设置/显示主机名 | - |
| `kill` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `ln` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `login` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `ls` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `lsattr` | 11 KB | elf | 文件属性：lsattr：查看 ext2 文件属性 | - |
| `mk_cmds` | 1 KB | script | 开发工具：生成命令表脚本 | - |
| `mkdir` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `mknod` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `mktemp` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `mount` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `mv` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `pidof` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `ping` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `ping6` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `ps` | 72 KB | elf | 进程工具：procps：进程列表 | - |
| `pwd` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `rm` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `rmdir` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `sed` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `sh` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `sleep` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `sync` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `tar` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `top` | 89 KB | elf | 进程工具：procps：实时进程/负载 | - |
| `touch` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `true` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `umount` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `uname` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `usleep` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `vmstat` | 22 KB | elf | 进程工具：procps：虚拟内存统计 | - |
| `zcat` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |

### `/dev`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `core` | 134217712.0 MB | symlink | 符号链接：指向 /proc/kcore | - |
| `stderr` | 0 B | symlink | 符号链接：指向 fd/2 | - |
| `stdin` | 0 B | symlink | 符号链接：指向 fd/0 | - |
| `stdout` | 0 B | symlink | 符号链接：指向 fd/1 | - |

### `/kmod`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `devno.ko` | 4 KB | elf | 内核模块：devno.ko：内核驱动 | - |
| `dmac.ko` | 16 KB | elf | 内核模块：dmac.ko：内核驱动 | - |
| `emmc.ko` | 207 KB | elf | 内核模块：emmc.ko：内核驱动 | - |
| `ldec.ko` | 15 KB | elf | 内核模块：ldec.ko：内核驱动 | - |
| `lld.ko` | 77 KB | elf | 内核模块：lld.ko：内核驱动 | - |
| `nand.ko` | 149 KB | elf | 内核模块：nand.ko：内核驱动 | - |

### `/lib`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `ld-2.11.2.so` | 99 KB | elf | 运行时库：glibc/系统库 | ash, bootin.elf, im.elf, launch_shell.el, sen.elf |
| `ld-linux.so.3` | 99 KB | symlink | 符号链接：指向 ld-2.11.2.so | - |
| `libSTMcmdexecute.so` | 4 KB | elf | 运行时库：glibc/系统库 | im.elf, sen.elf |
| `libanl-2.11.2.so` | 14 KB | elf | 运行时库：glibc/系统库 | - |
| `libanl.so.1` | 14 KB | symlink | 符号链接：指向 libanl-2.11.2.so | - |
| `libblkid.so.1` | 137 KB | symlink | 符号链接：指向 libblkid.so.1.1.0 | - |
| `libblkid.so.1.1.0` | 137 KB | elf | 运行时库：glibc/系统库 | - |
| `libc-2.11.2.so` | 961 KB | elf | 运行时库：glibc/系统库 | ash, bootin.elf, im.elf, launch_shell.el, sen.elf |
| `libc.so.6` | 961 KB | symlink | 符号链接：指向 libc-2.11.2.so | - |
| `libcrypt-2.11.2.so` | 38 KB | elf | 运行时库：glibc/系统库 | ash |
| `libcrypt.so.1` | 38 KB | symlink | 符号链接：指向 libcrypt-2.11.2.so | - |
| `libdl-2.11.2.so` | 14 KB | elf | 运行时库：glibc/系统库 | bootin.elf, im.elf, launch_shell.el, sen.elf |
| `libdl.so.2` | 14 KB | symlink | 符号链接：指向 libdl-2.11.2.so | - |
| `libgcc_s.so.1` | 247 KB | elf | 运行时库：glibc/系统库 | bootin.elf, im.elf, launch_shell.el, sen.elf |
| `libm-2.11.2.so` | 418 KB | elf | 运行时库：glibc/系统库 | bootin.elf, im.elf, launch_shell.el, sen.elf |
| `libm.so.6` | 418 KB | symlink | 符号链接：指向 libm-2.11.2.so | - |
| `libnsl-2.11.2.so` | 66 KB | elf | 运行时库：glibc/系统库 | - |
| `libnsl.so.1` | 66 KB | symlink | 符号链接：指向 libnsl-2.11.2.so | - |
| `libnss_dns-2.11.2.so` | 22 KB | elf | 运行时库：glibc/系统库 | - |
| `libnss_dns.so.2` | 22 KB | symlink | 符号链接：指向 libnss_dns-2.11.2.so | - |
| `libnss_files-2.11.2.so` | 34 KB | elf | 运行时库：glibc/系统库 | ash |
| `libnss_files.so.2` | 34 KB | symlink | 符号链接：指向 libnss_files-2.11.2.so | - |
| `libnss_nis-2.11.2.so` | 34 KB | elf | 运行时库：glibc/系统库 | - |
| `libnss_nis.so.2` | 34 KB | symlink | 符号链接：指向 libnss_nis-2.11.2.so | - |
| `libpthread-2.11.2.so` | 66 KB | elf | 运行时库：glibc/系统库 | ash, bootin.elf, im.elf, launch_shell.el, sen.elf |
| `libpthread.so.0` | 66 KB | symlink | 符号链接：指向 libpthread-2.11.2.so | - |
| `libresolv-2.11.2.so` | 66 KB | elf | 运行时库：glibc/系统库 | - |
| `libresolv.so.2` | 66 KB | symlink | 符号链接：指向 libresolv-2.11.2.so | - |
| `librt-2.11.2.so` | 22 KB | elf | 运行时库：glibc/系统库 | ash, bootin.elf, im.elf, launch_shell.el, sen.elf |
| `librt.so.1` | 22 KB | symlink | 符号链接：指向 librt-2.11.2.so | - |
| `libutil-2.11.2.so` | 14 KB | elf | 运行时库：glibc/系统库 | - |
| `libutil.so.1` | 14 KB | symlink | 符号链接：指向 libutil-2.11.2.so | - |
| `libuuid.so.1` | 35 KB | symlink | 符号链接：指向 libuuid.so.1.3.0 | - |
| `libuuid.so.1.3.0` | 35 KB | elf | 运行时库：glibc/系统库 | - |

### `/lib/xtables`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `libip6t_HL.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libip6t_LOG.so` | 10 KB | elf | 运行时库：glibc/系统库 | - |
| `libip6t_REJECT.so` | 8 KB | elf | 运行时库：glibc/系统库 | - |
| `libip6t_ah.so` | 8 KB | elf | 运行时库：glibc/系统库 | - |
| `libip6t_dst.so` | 9 KB | elf | 运行时库：glibc/系统库 | - |
| `libip6t_eui64.so` | 5 KB | elf | 运行时库：glibc/系统库 | - |
| `libip6t_frag.so` | 9 KB | elf | 运行时库：glibc/系统库 | - |
| `libip6t_hbh.so` | 9 KB | elf | 运行时库：glibc/系统库 | - |
| `libip6t_hl.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libip6t_icmp6.so` | 9 KB | elf | 运行时库：glibc/系统库 | - |
| `libip6t_ipv6header.so` | 9 KB | elf | 运行时库：glibc/系统库 | - |
| `libip6t_mh.so` | 10 KB | elf | 运行时库：glibc/系统库 | - |
| `libip6t_rt.so` | 10 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_CLUSTERIP.so` | 9 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_DNAT.so` | 9 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_ECN.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_LOG.so` | 10 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_MASQUERADE.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_MIRROR.so` | 5 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_NETMAP.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_REDIRECT.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_REJECT.so` | 9 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_SAME.so` | 8 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_SNAT.so` | 9 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_TTL.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_ULOG.so` | 9 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_addrtype.so` | 10 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_ah.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_ecn.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_icmp.so` | 9 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_realm.so` | 8 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_ttl.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libipt_unclean.so` | 5 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_CHECKSUM.so` | 6 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_CLASSIFY.so` | 6 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_CONNMARK.so` | 11 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_CONNSECMARK.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_CT.so` | 9 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_DSCP.so` | 8 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_IDLETIMER.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_LED.so` | 8 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_MARK.so` | 9 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_NFLOG.so` | 8 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_NFQUEUE.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_NOTRACK.so` | 5 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_RATEEST.so` | 9 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_SECMARK.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_SET.so` | 11 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_TCPMSS.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_TCPOPTSTRIP.so` | 8 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_TEE.so` | 8 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_TOS.so` | 10 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_TPROXY.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_TRACE.so` | 5 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_cluster.so` | 8 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_comment.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_connbytes.so` | 8 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_connlimit.so` | 8 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_connmark.so` | 8 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_conntrack.so` | 20 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_cpu.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_dccp.so` | 10 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_dscp.so` | 8 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_esp.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_hashlimit.so` | 18 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_helper.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_iprange.so` | 10 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_ipvs.so` | 11 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_length.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_limit.so` | 10 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_mac.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_mark.so` | 8 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_multiport.so` | 12 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_osf.so` | 8 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_owner.so` | 12 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_physdev.so` | 9 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_pkttype.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_policy.so` | 13 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_quota.so` | 6 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_rateest.so` | 12 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_recent.so` | 10 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_sctp.so` | 12 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_set.so` | 10 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_socket.so` | 5 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_standard.so` | 5 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_state.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_statistic.so` | 9 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_string.so` | 10 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_tcp.so` | 11 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_tcpmss.so` | 7 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_time.so` | 12 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_tos.so` | 9 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_u32.so` | 8 KB | elf | 运行时库：glibc/系统库 | - |
| `libxt_udp.so` | 8 KB | elf | 运行时库：glibc/系统库 | - |

### `/root`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `chassis` | 9 B | data | 数据/其他：chassis | - |
| `common.src` | 3 KB | data | 升级脚本库：FIRMUP/updater 的通用变量与函数（mount、错误码、LED） | - |

### `/sbin`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `dosfsck` | 63 KB | elf | 文件系统工具：FAT 文件系统检查/修复 | - |
| `freeramdisk` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `getty` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `halt` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `ifconfig` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `init` | 28 KB | elf | 初始化：PID 1：解析 cmdline/环境、挂载 nflasha、insmod、启动后台服务 | - |
| `insmod` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `lsmod` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `mkdosfs` | 46 KB | elf | 文件系统工具：创建 FAT 文件系统 | - |
| `pivot_root` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `poweroff` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `reboot` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `rmmod` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `route` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `swapoff` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `swapon` | 423 KB | symlink | BusyBox 链接：指向 busybox 的命令别名 | - |
| `sysctl` | 14 KB | elf | 内核参数工具：读写 /proc/sys | - |

## nflasha3（/system：内核、initrd、LIRO、镜头/传感器数据）

### `/system`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `av-cam.bin` | 17.6 MB | data | LIRO 固件：LIRO 相机固件，QEMU 可预加载到 0x035c6000 | - |
| `bonobo.bin` | 168 KB | data | 启动数据：Bonobo 启动/传感器数据 | - |
| `dfe_app.bin` | 2 KB | data | DFE 应用：DFE 图像处理应用固件 | - |
| `dfe_dat.bin` | 64 KB | data | DFE 数据：DFE 配置/数据 | - |
| `initrd.img` | 2.1 MB | data | initrd：启动 initrd（ext2），含模块加载/备份逻辑 | - |
| `ldr_drv.bin` | 7 KB | data | LIRO loader：LIRO 驱动加载器 | - |
| `lif_app.bin` | 7 KB | data | LIF 应用：LIF 应用固件 | - |
| `vmlinux.bin` | 3.9 MB | data | 内核镜像：Linux 3.0.27 zImage | - |

### `/system/lensbin_lensproperty`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `LensAberrationData.bin` | 158 KB | data | 镜头像差：镜头像差/校正数据 | - |

### `/system/sabin`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `idt_cam.bin` | 172 KB | data | 启动/传感器数据：idt_cam.bin：启动镜像或传感器数据 | - |
| `sa_dfdet.bin` | 153 KB | data | 启动/传感器数据：sa_dfdet.bin：启动镜像或传感器数据 | - |
| `ssboot.bin` | 11 KB | data | 启动/传感器数据：ssboot.bin：启动镜像或传感器数据 | - |
| `ssboot_any.bin` | 9 KB | data | 启动/传感器数据：ssboot_any.bin：启动镜像或传感器数据 | - |

## nflasha2（/setting：私有设置、备份、内存地图）

### `/setting`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `.etools` | 4 KB | data | 工厂工具标记：工厂/调试工具标记 | - |
| `.hasp` | 88 B | data | Senser 许可：Senser/HASP 认证数据 | - |
| `Backup.bak` | 1.1 MB | data | 备份：设置备份（旧） | - |
| `Backup.bin` | 1.1 MB | data | 备份：设置备份 | - |
| `DmmConfig.bin` | 75 KB | data | DMM 配置：显示内存管理配置 | - |
| `facedmy.bin` | 50 KB | data | 私有设置：facedmy.bin：设置/备份数据 | - |
| `facerec0.bin` | 57 KB | data | 私有设置：facerec0.bin：设置/备份数据 | - |
| `facerec1.bin` | 57 KB | data | 私有设置：facerec1.bin：设置/备份数据 | - |
| `facerec2.bin` | 57 KB | data | 私有设置：facerec2.bin：设置/备份数据 | - |
| `facerec3.bin` | 57 KB | data | 私有设置：facerec3.bin：设置/备份数据 | - |
| `facerec4.bin` | 57 KB | data | 私有设置：facerec4.bin：设置/备份数据 | - |
| `facerec5.bin` | 57 KB | data | 私有设置：facerec5.bin：设置/备份数据 | - |
| `facerec6.bin` | 57 KB | data | 私有设置：facerec6.bin：设置/备份数据 | - |
| `facerec7.bin` | 57 KB | data | 私有设置：facerec7.bin：设置/备份数据 | - |
| `kemco.txt` | 2 KB | data | 内存地图：主内核 memrsv/内存保留区参数 | - |
| `psd.bin` | 4.2 MB | data | PSD 数据：画质/传感器校准数据 | - |
| `ulogio.bin` | 4 KB | data | 日志缓冲：用户态日志缓冲 | - |

### `/setting/updater`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `comp` | 0 B | data | 私有设置：comp：设置/备份数据 | - |
| `dat4` | 2 B | data | 私有设置：dat4：设置/备份数据 | - |

## nflasha10（/etc 与 /tmp：运行时配置、字体、JIRITSU 标记）

### `/etc`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `config.spec` | 0 B | data | 系统配置：型号/区域/规格配置 | - |
| `dhcpd.conf` | 3 KB | data | DHCP：DHCP 服务配置 | - |
| `kikilog.dat` | 608 KB | data | 日志：kikilog 日志数据 | - |
| `mtab` | 14 B | data | 运行时配置：mtab：配置/数据 | - |
| `nsswitch.conf` | 261 B | data | NSS：名称解析顺序 | - |
| `protocols` | 3 KB | data | 协议表：IP 协议名表 | - |
| `resolv.conf` | 24 B | data | DNS：DNS 配置 | - |
| `services` | 19 KB | data | 服务表：TCP/UDP 服务名表 | - |
| `toprc` | 617 B | data | top：top 配置 | - |
| `uipc_stat_kernel.txt` | 39 KB | data | UIPC：UIPC 内核统计/配置 | - |

### `/etc/images`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `MYingHeiC-Big5-SJ_wIcon.ltt` | 1.1 MB | data | 运行时配置：MYingHeiC-Big5-SJ_wIcon.ltt：配置/数据 | - |
| `MYingHeiC-GB18030-SJ_wIcon.ltt` | 2.0 MB | data | 运行时配置：MYingHeiC-GB18030-SJ_wIcon.ltt：配置/数据 | - |
| `Sony_DI_Icons.ttf` | 605 KB | data | 运行时配置：Sony_DI_Icons.ttf：配置/数据 | - |

## nflasha15（/usr：应用、库、场景、DSP/编解码固件、资源）

### `/usr/bin`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `GPIO2SDIO.elf` | 4 KB | elf | GPIO/SDIO：GPIO 切到 SDIO 模式 | - |
| `NsBkSet.elf` | 4 KB | elf | 备份设置：备份相关设置 | - |
| `SDIO2GPIO.elf` | 4 KB | elf | GPIO/SDIO：SDIO 切回 GPIO | - |
| `SetPort.elf` | 4 KB | elf | 端口：端口/GPIO 设置 | - |
| `WebApiLauncher.sh` | 211 B | script | Web API：启动 Web API 服务 | - |
| `Wltestcmd` | 24 KB | elf | Wi-Fi 测试：无线测试命令 | - |
| `adjstctl.elf` | 111 KB | elf | 调整控制：镜头/传感器调整控制 | - |
| `appdbglv.sh` | 10 KB | script | 调试脚本：设置应用调试等级 | - |
| `bk.elf` | 10 KB | elf | 备份：备份/恢复相关 | - |
| `bootin.elf` | 15 KB | elf | 启动信息：启动参数/启动信息处理 | bootin.elf |
| `bsa_server` | 4.6 MB | elf | 蓝牙：Broadcom BSA 蓝牙协议栈服务 | - |
| `btRFTest.elf` | 35 KB | elf | 蓝牙测试：蓝牙 RF 测试 | - |
| `bt_firm.hcd` | 57 KB | data | 用户态程序：服务/工具/脚本 | - |
| `bt_firm_sar.hcd` | 53 KB | data | 用户态程序：服务/工具/脚本 | - |
| `btblog.elf` | 7 KB | elf | 蓝牙日志：蓝牙日志服务 | - |
| `change_mode.sh` | 4 KB | script | 模式脚本：切换启动/升级模式 | - |
| `common.src` | 3 KB | data | 用户态程序：服务/工具/脚本 | - |
| `compat_firmware.sh` | 1 KB | script | 兼容脚本：固件兼容处理 | - |
| `crypter.elf` | 38 KB | elf | 加解密：固件/数据加解密工具 | - |
| `dhd` | 231 KB | elf | Wi-Fi：Broadcom dhd Wi-Fi 驱动用户态 | - |
| `doemparse.sh` | 387 B | script | 用户态程序：服务/工具/脚本 | - |
| `gpioctrl.elf` | 85 KB | elf | GPIO：GPIO 控制 | - |
| `im.elf` | 23 KB | elf | 应用框架启动器：Appframework 入口：libIMDB/libosal/backup，dlopen 场景与视图 | im.elf |
| `iperf` | 61 KB | elf | 网络测试：iperf 带宽测试 | - |
| `launch_shell.elf` | 5 KB | elf | 调试 shell：启动调试 shell（launch_shell） | launch_shell.el |
| `mpr_monio.elf` | 7 KB | elf | 监控：MPR 消息/状态监控 | - |
| `mpr_viewLog.elf` | 8 KB | elf | 日志查看：查看 MPR 日志 | - |
| `mwf_monio.elf` | 22 KB | elf | 监控：MWF 消息/状态监控 | - |
| `netblog.elf` | 7 KB | elf | 网络日志：网络日志服务 | - |
| `openssl` | 721 KB | elf | 密码学：OpenSSL 命令行 | - |
| `orb-server` | 5.4 MB | elf | BT/网络服务：ORB 服务（蓝牙/网络相关） | - |
| `rcvcmd.elf` | 5 KB | elf | 命令接收：接收并分发命令 | - |
| `scenario.elf` | 5 KB | elf | 场景命令入口：解析 name:size:data，dlopen /usr/scenario/*.so 并调用 scenario_run | - |
| `sen.elf` | 19 KB | elf | 传感器服务：Senser/传感器相关用户态服务 | sen.elf |
| `sndcmd.elf` | 5 KB | elf | 命令发送：发送命令到服务 | - |
| `soundstretch` | 39 KB | elf | 音频：音频变速/变调 | - |
| `startBTCore.sh` | 1 KB | script | 蓝牙脚本：启动蓝牙 core | - |
| `swap_prepare.sh` | 496 B | script | 内存脚本：准备 swap | - |
| `testcmd.elf` | 5 KB | elf | 测试命令：工厂/测试命令分发 | - |
| `ud_datcnv.elf` | 6 KB | elf | 用户态程序：服务/工具/脚本 | - |
| `ud_send_lsi.elf` | 4 KB | elf | 用户态程序：服务/工具/脚本 | - |
| `udtrbody.bin` | 140 KB | data | 用户态程序：服务/工具/脚本 | - |
| `ujlog.elf` | 7 KB | elf | 日志：ujlog 日志工具 | - |
| `ulogio` | 19 KB | symlink | 符号链接：指向 ulogio.elf | - |
| `ulogio.elf` | 19 KB | elf | 日志 IO：用户态日志读写 | - |
| `up.sh` | 5 KB | script | 升级脚本：切换 updater 模式（UFP/version skip/MS crypt） | - |
| `usb_insmod.sh` | 225 B | script | USB 脚本：加载 USB 相关模块 | - |
| `uuidgen` | 9 KB | elf | 系统工具：生成 UUID | - |
| `wl` | 1.1 MB | elf | Wi-Fi：Broadcom wl 工具 | - |
| `wpa_supplicant` | 740 KB | elf | Wi-Fi：WPA  supplicant | - |

### `/usr/codec`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `bni_firmware.bin` | 653 KB | data | 编解码固件：BNI/BNL/VCD 编解码器固件 | - |
| `bni_ipl.bin` | 19 KB | data | 编解码固件：BNI/BNL/VCD 编解码器固件 | - |
| `bnl_firmware.bin` | 1.4 MB | data | 编解码固件：BNI/BNL/VCD 编解码器固件 | - |
| `bnl_ipl.bin` | 20 KB | data | 编解码固件：BNI/BNL/VCD 编解码器固件 | - |
| `vcd_firmware.bin` | 5.2 MB | data | 编解码固件：BNI/BNL/VCD 编解码器固件 | - |
| `vcd_firmware_testing.bin` | 5.2 MB | data | 编解码固件：BNI/BNL/VCD 编解码器固件 | - |

### `/usr/kmod`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `accel.ko` | 13 KB | elf | 加速器：图像/媒体加速器 | - |
| `asix.ko` | 25 KB | elf | 内核模块：asix.ko：内核驱动 | - |
| `backup.ko` | 72 KB | elf | 备份：备份/恢复驱动 | - |
| `bcmdhd.ko` | 510 KB | elf | 内核模块：bcmdhd.ko：内核驱动 | - |
| `cdc-acm.ko` | 26 KB | elf | 内核模块：cdc-acm.ko：内核驱动 | - |
| `cdc_ether.ko` | 8 KB | elf | 内核模块：cdc_ether.ko：内核驱动 | - |
| `cdc_ncm.ko` | 11 KB | elf | 内核模块：cdc_ncm.ko：内核驱动 | - |
| `cdrom.ko` | 36 KB | elf | 内核模块：cdrom.ko：内核驱动 | - |
| `cec.ko` | 77 KB | elf | 内核模块：cec.ko：内核驱动 | - |
| `cfg80211.ko` | 188 KB | elf | 内核模块：cfg80211.ko：内核驱动 | - |
| `codec_drv.ko` | 18 KB | elf | 编解码：编解码器驱动 | - |
| `compass.ko` | 5 KB | elf | 内核模块：compass.ko：内核驱动 | - |
| `compat.ko` | 8 KB | elf | 内核模块：compat.ko：内核驱动 | - |
| `configfs.ko` | 29 KB | elf | 内核模块：configfs.ko：内核驱动 | - |
| `crc-ccitt.ko` | 2 KB | elf | 内核模块：crc-ccitt.ko：内核驱动 | - |
| `dma330.ko` | 251 KB | elf | DMA：DMA330 引擎 | - |
| `dmm.ko` | 81 KB | elf | 显示内存：显示内存管理 | - |
| `g_mass_storage.ko` | 7 KB | elf | 内核模块：g_mass_storage.ko：内核驱动 | - |
| `grm_gles.ko` | 15 KB | elf | GPU 驱动：Sugilite GLES 驱动 | - |
| `grm_ma.ko` | 24 KB | elf | 媒体加速：Sugilite 媒体加速 | - |
| `hdmi.ko` | 233 KB | elf | 内核模块：hdmi.ko：内核驱动 | - |
| `htmd.ko` | 4 KB | elf | 内核模块：htmd.ko：内核驱动 | - |
| `i2c.ko` | 14 KB | elf | 内核模块：i2c.ko：内核驱动 | - |
| `indctr.ko` | 13 KB | elf | 内核模块：indctr.ko：内核驱动 | - |
| `input.ko` | 33 KB | elf | 内核模块：input.ko：内核驱动 | - |
| `kikilog.ko` | 31 KB | elf | 内核模块：kikilog.ko：内核驱动 | - |
| `lg-vl600.ko` | 5 KB | elf | 内核模块：lg-vl600.ko：内核驱动 | - |
| `lib80211_crypt_ccmp.ko` | 6 KB | elf | 内核模块：lib80211_crypt_ccmp.ko：内核驱动 | - |
| `lib80211_crypt_tkip.ko` | 9 KB | elf | 内核模块：lib80211_crypt_tkip.ko：内核驱动 | - |
| `lib80211_crypt_wep.ko` | 5 KB | elf | 内核模块：lib80211_crypt_wep.ko：内核驱动 | - |
| `libcomposite.ko` | 33 KB | elf | 内核模块：libcomposite.ko：内核驱动 | - |
| `liro.ko` | 64 KB | elf | 内核模块：liro.ko：内核驱动 | - |
| `mac80211.ko` | 274 KB | elf | 内核模块：mac80211.ko：内核驱动 | - |
| `mag.ko` | 10 KB | elf | 内核模块：mag.ko：内核驱动 | - |
| `mcmn_drv.ko` | 111 KB | elf | 内核模块：mcmn_drv.ko：内核驱动 | - |
| `mii.ko` | 5 KB | elf | 内核模块：mii.ko：内核驱动 | - |
| `mmc_core.ko` | 72 KB | elf | 内核模块：mmc_core.ko：内核驱动 | - |
| `mmc_drv.ko` | 219 KB | elf | 内核模块：mmc_drv.ko：内核驱动 | - |
| `mmcioWrapper.ko` | 7 KB | elf | 内核模块：mmcioWrapper.ko：内核驱动 | - |
| `ms_drv.ko` | 203 KB | elf | 内核模块：ms_drv.ko：内核驱动 | - |
| `nfc.ko` | 16 KB | elf | 内核模块：nfc.ko：内核驱动 | - |
| `nls_utf8.ko` | 2 KB | elf | 内核模块：nls_utf8.ko：内核驱动 | - |
| `option.ko` | 76 KB | elf | 内核模块：option.ko：内核驱动 | - |
| `osal_uipc.ko` | 38 KB | elf | 内核模块：osal_uipc.ko：内核驱动 | - |
| `osal_ulogio.ko` | 38 KB | elf | 内核模块：osal_ulogio.ko：内核驱动 | - |
| `osal_utm.ko` | 5 KB | elf | 内核模块：osal_utm.ko：内核驱动 | - |
| `ppp_async.ko` | 11 KB | elf | 内核模块：ppp_async.ko：内核驱动 | - |
| `ppp_generic.ko` | 26 KB | elf | 内核模块：ppp_generic.ko：内核驱动 | - |
| `r8168.ko` | 414 KB | elf | 内核模块：r8168.ko：内核驱动 | - |
| `rndis_host.ko` | 9 KB | elf | 内核模块：rndis_host.ko：内核驱动 | - |
| `scsi_mod.ko` | 108 KB | elf | 内核模块：scsi_mod.ko：内核驱动 | - |
| `scsi_wait_scan.ko` | 2 KB | elf | 内核模块：scsi_wait_scan.ko：内核驱动 | - |
| `sd_mod.ko` | 33 KB | elf | 内核模块：sd_mod.ko：内核驱动 | - |
| `sircs.ko` | 21 KB | elf | 内核模块：sircs.ko：内核驱动 | - |
| `slhc.ko` | 6 KB | elf | 内核模块：slhc.ko：内核驱动 | - |
| `snd-aloop.ko` | 18 KB | elf | 内核模块：snd-aloop.ko：内核驱动 | - |
| `snd-dummy.ko` | 14 KB | elf | 内核模块：snd-dummy.ko：内核驱动 | - |
| `snd-hwdep.ko` | 9 KB | elf | 内核模块：snd-hwdep.ko：内核驱动 | - |
| `snd-mixer-oss.ko` | 18 KB | elf | 内核模块：snd-mixer-oss.ko：内核驱动 | - |
| `snd-page-alloc.ko` | 8 KB | elf | 内核模块：snd-page-alloc.ko：内核驱动 | - |
| `snd-pcm-oss.ko` | 41 KB | elf | 内核模块：snd-pcm-oss.ko：内核驱动 | - |
| `snd-pcm.ko` | 78 KB | elf | 内核模块：snd-pcm.ko：内核驱动 | - |
| `snd-rawmidi.ko` | 22 KB | elf | 内核模块：snd-rawmidi.ko：内核驱动 | - |
| `snd-seq-device.ko` | 7 KB | elf | 内核模块：snd-seq-device.ko：内核驱动 | - |
| `snd-seq-dummy.ko` | 4 KB | elf | 内核模块：snd-seq-dummy.ko：内核驱动 | - |
| `snd-seq-midi-event.ko` | 7 KB | elf | 内核模块：snd-seq-midi-event.ko：内核驱动 | - |
| `snd-seq-midi.ko` | 8 KB | elf | 内核模块：snd-seq-midi.ko：内核驱动 | - |
| `snd-seq-oss.ko` | 34 KB | elf | 内核模块：snd-seq-oss.ko：内核驱动 | - |
| `snd-seq-virmidi.ko` | 8 KB | elf | 内核模块：snd-seq-virmidi.ko：内核驱动 | - |
| `snd-seq.ko` | 57 KB | elf | 内核模块：snd-seq.ko：内核驱动 | - |
| `snd-timer.ko` | 23 KB | elf | 内核模块：snd-timer.ko：内核驱动 | - |
| `snd-usb-audio.ko` | 101 KB | elf | 内核模块：snd-usb-audio.ko：内核驱动 | - |
| `snd-usbmidi-lib.ko` | 20 KB | elf | 内核模块：snd-usbmidi-lib.ko：内核驱动 | - |
| `snd-virmidi.ko` | 5 KB | elf | 内核模块：snd-virmidi.ko：内核驱动 | - |
| `snd.ko` | 49 KB | elf | 内核模块：snd.ko：内核驱动 | - |
| `soundcore.ko` | 8 KB | elf | 内核模块：soundcore.ko：内核驱动 | - |
| `sr_mod.ko` | 17 KB | elf | 内核模块：sr_mod.ko：内核驱动 | - |
| `stream.ko` | 3 KB | elf | 视频流：视频流驱动 | - |
| `stream2.ko` | 4 KB | elf | 视频流：第二视频流驱动 | - |
| `udate.ko` | 14 KB | elf | 升级：固件升级辅助 | - |
| `upm.ko` | 132 KB | elf | 统一电源/内存：UPM 驱动 | - |
| `usb-storage.ko` | 28 KB | elf | 内核模块：usb-storage.ko：内核驱动 | - |
| `usb_buspwr.ko` | 13 KB | elf | 内核模块：usb_buspwr.ko：内核驱动 | - |
| `usb_current.ko` | 5 KB | elf | 内核模块：usb_current.ko：内核驱动 | - |
| `usb_darwin.ko` | 28 KB | elf | 内核模块：usb_darwin.ko：内核驱动 | - |
| `usb_extcmd.ko` | 14 KB | elf | 内核模块：usb_extcmd.ko：内核驱动 | - |
| `usb_f_mass_storage.ko` | 35 KB | elf | 内核模块：usb_f_mass_storage.ko：内核驱动 | - |
| `usb_portMonitor.ko` | 17 KB | elf | 内核模块：usb_portMonitor.ko：内核驱动 | - |
| `usb_wwan.ko` | 9 KB | elf | 内核模块：usb_wwan.ko：内核驱动 | - |
| `usbcore.ko` | 154 KB | elf | 内核模块：usbcore.ko：内核驱动 | - |
| `usbg_buspower.ko` | 14 KB | elf | 内核模块：usbg_buspower.ko：内核驱动 | - |
| `usbg_cmn.ko` | 4 KB | elf | 内核模块：usbg_cmn.ko：内核驱动 | - |
| `usbg_sen.ko` | 30 KB | elf | 内核模块：usbg_sen.ko：内核驱动 | - |
| `usbg_stillimage.ko` | 27 KB | elf | 内核模块：usbg_stillimage.ko：内核驱动 | - |
| `usbg_storage.ko` | 65 KB | elf | 内核模块：usbg_storage.ko：内核驱动 | - |
| `usbhid.ko` | 23 KB | elf | 内核模块：usbhid.ko：内核驱动 | - |
| `usbnet.ko` | 22 KB | elf | 内核模块：usbnet.ko：内核驱动 | - |
| `usbserial.ko` | 27 KB | elf | 内核模块：usbserial.ko：内核驱动 | - |
| `utimer.ko` | 20 KB | elf | 内核模块：utimer.ko：内核驱动 | - |
| `wlanIrq.ko` | 4 KB | elf | 内核模块：wlanIrq.ko：内核驱动 | - |
| `wlanMemoryAllocator.ko` | 8 KB | elf | 内核模块：wlanMemoryAllocator.ko：内核驱动 | - |
| `xhci-hcd.ko` | 102 KB | elf | 内核模块：xhci-hcd.ko：内核驱动 | - |

### `/usr/lib`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `CameraOnDemandSaver.so` | 12 KB | elf | 共享库：用户态共享库 | - |
| `CautionConfig.so` | 9.7 MB | elf | 共享库：用户态共享库 | im.elf |
| `CautionRsrcConfig.so` | 120 KB | elf | 共享库：用户态共享库 | - |
| `ModelCautionConfig.so` | 7 KB | elf | 共享库：用户态共享库 | - |
| `dataflowInfraFramework.so` | 164 KB | elf | 共享库：用户态共享库 | im.elf |
| `githash` | 67 B | data | 共享库：用户态共享库 | - |
| `libAK8975.so` | 44 KB | elf | 共享库：用户态共享库 | im.elf |
| `libBTAdjust.so` | 11 KB | elf | 共享库：用户态共享库 | im.elf |
| `libBTUtils.so` | 16 KB | elf | 共享库：用户态共享库 | im.elf |
| `libBackupManager.so` | 6 KB | elf | 共享库：用户态共享库 | im.elf |
| `libBizFw.so` | 310 KB | elf | 共享库：用户态共享库 | im.elf |
| `libBizFw2.so` | 220 KB | elf | 共享库：用户态共享库 | im.elf |
| `libBusPower.so` | 31 KB | elf | 共享库：用户态共享库 | im.elf |
| `libExternalCommand.so` | 5 KB | elf | 共享库：用户态共享库 | - |
| `libGOConnectionManager.so` | 65 KB | elf | 共享库：用户态共享库 | im.elf |
| `libIMDB.so` | 31 KB | elf | 消息数据库：IMDB 内部消息数据库 | im.elf |
| `libInfraAccessLog.so` | 11 KB | elf | 共享库：用户态共享库 | im.elf |
| `libInfraAccessLogWrapper.so` | 3 KB | elf | 共享库：用户态共享库 | - |
| `libInfraAirplaneMode.so` | 8 KB | elf | 共享库：用户态共享库 | im.elf |
| `libInfraBGMMeta.so` | 149 KB | elf | 共享库：用户态共享库 | - |
| `libInfraBluetooth.so` | 84 KB | elf | 共享库：用户态共享库 | im.elf |
| `libInfraBluetoothCore.so` | 141 KB | elf | 共享库：用户态共享库 | im.elf |
| `libInfraBluetoothLowEnergy.so` | 255 KB | elf | 共享库：用户态共享库 | - |
| `libInfraCacheMgr.so` | 164 KB | elf | 共享库：用户态共享库 | - |
| `libInfraCameraProfile.so` | 51 KB | elf | 共享库：用户态共享库 | - |
| `libInfraCertificate.so` | 12 KB | elf | 共享库：用户态共享库 | - |
| `libInfraDevInfoSender.so` | 13 KB | elf | 共享库：用户态共享库 | - |
| `libInfraDlnaControl.so` | 374 KB | elf | 共享库：用户态共享库 | - |
| `libInfraExtBackupCommunicator.so` | 14 KB | elf | 共享库：用户态共享库 | - |
| `libInfraExtCmdSvc.so` | 16 KB | elf | 共享库：用户态共享库 | - |
| `libInfraFsys.so` | 402 KB | elf | 共享库：用户态共享库 | im.elf |
| `libInfraFtpClient.so` | 129 KB | elf | 共享库：用户态共享库 | - |
| `libInfraHdmi.so` | 392 KB | elf | 共享库：用户态共享库 | im.elf |
| `libInfraHighlight.so` | 188 KB | elf | 共享库：用户态共享库 | - |
| `libInfraHttpClient.so` | 34 KB | elf | 共享库：用户态共享库 | - |
| `libInfraHttpClientUtil.so` | 16 KB | elf | 共享库：用户态共享库 | - |
| `libInfraKikiLogGenerator.so` | 10 KB | elf | 共享库：用户态共享库 | im.elf |
| `libInfraKikiLogSender.so` | 7 KB | elf | 共享库：用户态共享库 | - |
| `libInfraLensCommunicator.so` | 8 KB | elf | 共享库：用户态共享库 | - |
| `libInfraMDnsControl.so` | 129 KB | elf | 共享库：用户态共享库 | - |
| `libInfraMakeScenario.so` | 397 KB | elf | 场景框架：Infra 场景注册/加载框架 | - |
| `libInfraMediaCommon.so` | 304 KB | elf | 共享库：用户态共享库 | im.elf |
| `libInfraMediaDetect.so` | 76 KB | elf | 共享库：用户态共享库 | im.elf |
| `libInfraMediaMount.so` | 36 KB | elf | 共享库：用户态共享库 | im.elf |
| `libInfraMetaSupplier.so` | 13 KB | elf | 共享库：用户态共享库 | - |
| `libInfraMscServer.so` | 44 KB | elf | 共享库：用户态共享库 | - |
| `libInfraMtpServer.so` | 155 KB | elf | 共享库：用户态共享库 | - |
| `libInfraNetConnectionManager.so` | 24 KB | elf | 共享库：用户态共享库 | - |
| `libInfraNetDeviceInfo.so` | 8 KB | elf | 共享库：用户态共享库 | - |
| `libInfraNetFunctionManager.so` | 36 KB | elf | 共享库：用户态共享库 | - |
| `libInfraNetInitializer.so` | 17 KB | elf | 共享库：用户态共享库 | im.elf |
| `libInfraNetworkServiceInfo.so` | 33 KB | elf | 共享库：用户态共享库 | - |
| `libInfraNfc.so` | 27 KB | elf | 共享库：用户态共享库 | im.elf |
| `libInfraPtpControl.so` | 30 KB | elf | 共享库：用户态共享库 | - |
| `libInfraPtpExtCmd.so` | 33 KB | elf | 共享库：用户态共享库 | - |
| `libInfraRemote.so` | 98 KB | elf | 共享库：用户态共享库 | - |
| `libInfraRemoteControlNet.so` | 184 KB | elf | 共享库：用户态共享库 | - |
| `libInfraSKD.so` | 10 KB | elf | 共享库：用户态共享库 | im.elf |
| `libInfraStreamingServer.so` | 111 KB | elf | 共享库：用户态共享库 | - |
| `libInfraUsbCmn.so` | 84 KB | elf | 共享库：用户态共享库 | im.elf, sen.elf |
| `libInfraUsbHostStorage.so` | 19 KB | elf | 共享库：用户态共享库 | - |
| `libInfraWebApi.so` | 260 KB | elf | 共享库：用户态共享库 | - |
| `libJiritsu.so` | 151 KB | elf | JIRITSU：JIRITSU 服务协议（文件/升级/调试/工厂） | im.elf |
| `libMWF.so` | 232 KB | elf | MWF：MWF 中间件 | im.elf |
| `libNetCommon.so` | 120 KB | elf | 共享库：用户态共享库 | im.elf |
| `libNetContUtil.so` | 73 KB | elf | 共享库：用户态共享库 | im.elf |
| `libNetRemote.so` | 21 KB | elf | 共享库：用户态共享库 | im.elf |
| `libNetService.so` | 643 KB | elf | 网络服务：网络服务框架 | - |
| `libObj.so` | 18.9 MB | elf | 应用对象框架：libObj：Appframework 对象/视图/场景核心（最大库） | im.elf |
| `libOnDemandLoader.so` | 39 KB | elf | 共享库：用户态共享库 | im.elf |
| `libResourceBluetooth.so` | 8 KB | elf | 共享库：用户态共享库 | im.elf |
| `libRsrcHotshoe.so` | 14 KB | elf | 共享库：用户态共享库 | im.elf |
| `libSKDWrapperManager.so` | 6 KB | elf | 共享库：用户态共享库 | im.elf |
| `libSoundTouch.so` | 59 KB | symlink | 符号链接：指向 libSoundTouch.so.1.0.0 | - |
| `libSoundTouch.so.1` | 59 KB | symlink | 符号链接：指向 libSoundTouch.so.1.0.0 | - |
| `libSoundTouch.so.1.0.0` | 59 KB | elf | 共享库：用户态共享库 | - |
| `libSysDef.so` | 2.5 MB | elf | 系统定义：系统常量/型号/区域定义 | im.elf |
| `libUsbBusPower.so` | 21 KB | elf | 共享库：用户态共享库 | im.elf |
| `libUsbChargingApp.so` | 36 KB | elf | 共享库：用户态共享库 | - |
| `libUsbControl.so` | 92 KB | elf | 共享库：用户态共享库 | im.elf |
| `libWlanAdjust.so` | 55 KB | elf | 共享库：用户态共享库 | - |
| `libWlanControlCommon.so` | 14 KB | elf | 共享库：用户态共享库 | - |
| `libWlanResource.so` | 34 KB | elf | 共享库：用户态共享库 | - |
| `libbackup.so` | 9 KB | elf | 共享库：用户态共享库 | bootin.elf, im.elf, sen.elf |
| `libbsa.so` | 106 KB | elf | 共享库：用户态共享库 | - |
| `libclema.so` | 76 KB | elf | Clema：媒体/图像处理库 | im.elf |
| `libcom_err.so` | 8 KB | symlink | 符号链接：指向 libcom_err.so.2 | - |
| `libcom_err.so.2` | 8 KB | symlink | 符号链接：指向 libcom_err.so.2.1 | - |
| `libcom_err.so.2.1` | 8 KB | elf | 共享库：用户态共享库 | - |
| `libcompassutil.so` | 6 KB | elf | 共享库：用户态共享库 | im.elf |
| `libcrypto.so` | 2.5 MB | symlink | 符号链接：指向 libcrypto.so.3 | - |
| `libcrypto.so.3` | 2.5 MB | elf | 密码学：OpenSSL libcrypto | im.elf, sen.elf |
| `libcrypto.so.3.0` | 2.5 MB | symlink | 符号链接：指向 libcrypto.so.3 | - |
| `libcurl.so` | 400 KB | symlink | 符号链接：指向 libcurl.so.4.8.0 | - |
| `libcurl.so.4` | 400 KB | symlink | 符号链接：指向 libcurl.so.4.8.0 | - |
| `libcurl.so.4.8.0` | 400 KB | elf | HTTP：libcurl | - |
| `libdig_level.so` | 26 KB | elf | 共享库：用户态共享库 | - |
| `libe2p.so` | 20 KB | symlink | 符号链接：指向 libe2p.so.2 | - |
| `libe2p.so.2` | 20 KB | symlink | 符号链接：指向 libe2p.so.2.3 | - |
| `libe2p.so.2.3` | 20 KB | elf | 共享库：用户态共享库 | - |
| `libevent-2.1.so.6` | 225 KB | symlink | 符号链接：指向 libevent-2.1.so.6.0.2 | - |
| `libevent-2.1.so.6.0.2` | 225 KB | elf | 共享库：用户态共享库 | - |
| `libevent.so` | 225 KB | symlink | 符号链接：指向 libevent-2.1.so.6.0.2 | - |
| `libevent_core-2.1.so.6` | 147 KB | symlink | 符号链接：指向 libevent_core-2.1.so.6.0.2 | - |
| `libevent_core-2.1.so.6.0.2` | 147 KB | elf | 共享库：用户态共享库 | - |
| `libevent_core.so` | 147 KB | symlink | 符号链接：指向 libevent_core-2.1.so.6.0.2 | - |
| `libevent_openssl-2.1.so.6` | 15 KB | symlink | 符号链接：指向 libevent_openssl-2.1.so.6.0.2 | - |
| `libevent_openssl-2.1.so.6.0.2` | 15 KB | elf | 共享库：用户态共享库 | - |
| `libevent_openssl.so` | 15 KB | symlink | 符号链接：指向 libevent_openssl-2.1.so.6.0.2 | - |
| `libevent_pthreads-2.1.so.6` | 5 KB | symlink | 符号链接：指向 libevent_pthreads-2.1.so.6.0.2 | - |
| `libevent_pthreads-2.1.so.6.0.2` | 5 KB | elf | 共享库：用户态共享库 | - |
| `libevent_pthreads.so` | 5 KB | symlink | 符号链接：指向 libevent_pthreads-2.1.so.6.0.2 | - |
| `libexpat.so` | 105 KB | symlink | 符号链接：指向 libexpat.so.1.6.11 | - |
| `libexpat.so.1` | 105 KB | symlink | 符号链接：指向 libexpat.so.1.6.11 | - |
| `libexpat.so.1.6.11` | 105 KB | elf | 共享库：用户态共享库 | im.elf |
| `libgenuinetime.so` | 4 KB | elf | 共享库：用户态共享库 | - |
| `libgps_rsrc.so` | 16 KB | elf | 共享库：用户态共享库 | - |
| `libip4tc.so` | 17 KB | symlink | 符号链接：指向 libip4tc.so.0.0.0 | - |
| `libip4tc.so.0` | 17 KB | symlink | 符号链接：指向 libip4tc.so.0.0.0 | - |
| `libip4tc.so.0.0.0` | 17 KB | elf | 共享库：用户态共享库 | - |
| `libjemalloc_ds.so` | 3 KB | symlink | 符号链接：指向 libjemalloc_ds.so.1 | - |
| `libjemalloc_ds.so.1` | 3 KB | elf | 共享库：用户态共享库 | im.elf |
| `libjsoncpp.so` | 196 KB | elf | 共享库：用户态共享库 | - |
| `libjsoncpp.so.00.11.0` | 196 KB | elf | 共享库：用户态共享库 | - |
| `libjsoncpp.so.23` | 196 KB | elf | 共享库：用户态共享库 | im.elf |
| `libmintx.so` | 1.5 MB | elf | 共享库：用户态共享库 | im.elf |
| `libmpr.so` | 11.9 MB | elf | MPR 中间件：MPR（Camera Middleware）核心 | im.elf |
| `libmprctrl.so` | 248 KB | elf | MPR 控制：MPR 控制/命令接口 | im.elf |
| `libmprdummy.so` | 6 KB | elf | 共享库：用户态共享库 | im.elf |
| `libncurses.so` | 254 KB | symlink | 符号链接：指向 libncurses.so.6 | - |
| `libncurses.so.6` | 254 KB | symlink | 符号链接：指向 libncurses.so.6.2 | - |
| `libncurses.so.6.2` | 254 KB | elf | 共享库：用户态共享库 | - |
| `libnl-3.so` | 77 KB | symlink | 符号链接：指向 libnl-3.so.200.17.0 | - |
| `libnl-3.so.200` | 77 KB | symlink | 符号链接：指向 libnl-3.so.200.17.0 | - |
| `libnl-3.so.200.17.0` | 77 KB | elf | 共享库：用户态共享库 | - |
| `libnl-cli-3.so` | 28 KB | symlink | 符号链接：指向 libnl-cli-3.so.200.17.0 | - |
| `libnl-cli-3.so.200` | 28 KB | symlink | 符号链接：指向 libnl-cli-3.so.200.17.0 | - |
| `libnl-cli-3.so.200.17.0` | 28 KB | elf | 共享库：用户态共享库 | - |
| `libnl-genl-3.so` | 13 KB | symlink | 符号链接：指向 libnl-genl-3.so.200.17.0 | - |
| `libnl-genl-3.so.200` | 13 KB | symlink | 符号链接：指向 libnl-genl-3.so.200.17.0 | - |
| `libnl-genl-3.so.200.17.0` | 13 KB | elf | 共享库：用户态共享库 | - |
| `libnl-nf-3.so` | 54 KB | symlink | 符号链接：指向 libnl-nf-3.so.200.17.0 | - |
| `libnl-nf-3.so.200` | 54 KB | symlink | 符号链接：指向 libnl-nf-3.so.200.17.0 | - |
| `libnl-nf-3.so.200.17.0` | 54 KB | elf | 共享库：用户态共享库 | - |
| `libnl-route-3.so` | 195 KB | symlink | 符号链接：指向 libnl-route-3.so.200.17.0 | - |
| `libnl-route-3.so.200` | 195 KB | symlink | 符号链接：指向 libnl-route-3.so.200.17.0 | - |
| `libnl-route-3.so.200.17.0` | 195 KB | elf | 共享库：用户态共享库 | - |
| `libopus.so` | 345 KB | symlink | 符号链接：指向 libopus.so.0.8.0 | - |
| `libopus.so.0` | 345 KB | symlink | 符号链接：指向 libopus.so.0.8.0 | - |
| `libopus.so.0.8.0` | 345 KB | elf | 共享库：用户态共享库 | - |
| `libosal_uipc.so` | 26 KB | elf | 用户态 IPC：消息队列/同步/线程 | bootin.elf, im.elf, sen.elf |
| `libosal_ulogio.so` | 30 KB | elf | 共享库：用户态共享库 | im.elf |
| `libosal_utm.so` | 5 KB | elf | 用户态定时器：定时器/线程管理 | bootin.elf, im.elf |
| `libpcap.so` | 150 KB | symlink | 符号链接：指向 libpcap.so.1.0.0 | - |
| `libpcap.so.1` | 150 KB | symlink | 符号链接：指向 libpcap.so.1.0.0 | - |
| `libpcap.so.1.0` | 150 KB | symlink | 符号链接：指向 libpcap.so.1.0.0 | - |
| `libpcap.so.1.0.0` | 150 KB | elf | 抓包：libpcap | - |
| `libpcre.so` | 233 KB | symlink | 符号链接：指向 libpcre.so.1.2.12 | - |
| `libpcre.so.1` | 233 KB | symlink | 符号链接：指向 libpcre.so.1.2.12 | - |
| `libpcre.so.1.2.12` | 233 KB | elf | 共享库：用户态共享库 | - |
| `libpopt.so` | 21 KB | symlink | 符号链接：指向 libpopt.so.0.0.0 | - |
| `libpopt.so.0` | 21 KB | symlink | 符号链接：指向 libpopt.so.0.0.0 | - |
| `libpopt.so.0.0.0` | 21 KB | elf | 共享库：用户态共享库 | - |
| `libpro00.so` | 4 KB | elf | 共享库：用户态共享库 | im.elf, sen.elf |
| `libprocps.so` | 47 KB | symlink | 符号链接：指向 libprocps.so.6.0.0 | - |
| `libprocps.so.6` | 47 KB | symlink | 符号链接：指向 libprocps.so.6.0.0 | - |
| `libprocps.so.6.0.0` | 47 KB | elf | 共享库：用户态共享库 | - |
| `libptp.so` | 52 KB | elf | 共享库：用户态共享库 | - |
| `libqrencode.so` | 27 KB | elf | 共享库：用户态共享库 | - |
| `libsencore.so` | 330 KB | elf | Senser 核心：传感器核心库 | im.elf, sen.elf |
| `libssh2.so` | 156 KB | symlink | 符号链接：指向 libssh2.so.1.0.1 | - |
| `libssh2.so.1` | 156 KB | symlink | 符号链接：指向 libssh2.so.1.0.1 | - |
| `libssh2.so.1.0.1` | 156 KB | elf | 共享库：用户态共享库 | - |
| `libssl.so` | 403 KB | symlink | 符号链接：指向 libssl.so.3 | - |
| `libssl.so.3` | 403 KB | elf | TLS：OpenSSL libssl | im.elf, sen.elf |
| `libssl.so.3.0` | 403 KB | symlink | 符号链接：指向 libssl.so.3 | - |
| `libssp.so` | 6 KB | symlink | 符号链接：指向 libssp.so.0.0.0 | - |
| `libssp.so.0` | 6 KB | symlink | 符号链接：指向 libssp.so.0.0.0 | - |
| `libssp.so.0.0.0` | 6 KB | elf | 共享库：用户态共享库 | - |
| `libstdc++.so` | 654 KB | symlink | 符号链接：指向 libstdc++.so.6.0.14 | - |
| `libstdc++.so.6` | 654 KB | symlink | 符号链接：指向 libstdc++.so.6.0.14 | - |
| `libstdc++.so.6.0.14` | 654 KB | elf | 共享库：用户态共享库 | bootin.elf, im.elf, launch_shell.el, sen.elf |
| `libtestcmd.so` | 10 KB | elf | 测试命令框架：testcmd_* / scenario 插件加载 | im.elf, sen.elf |
| `libtestcmd_scn.so` | 5 KB | elf | 共享库：用户态共享库 | - |
| `libul_GpioCtrl.so` | 4 KB | elf | 共享库：用户态共享库 | - |
| `libul_xml.so` | 55 KB | elf | 共享库：用户态共享库 | - |
| `libupdatercommon.so` | 36 KB | elf | 共享库：用户态共享库 | - |
| `libupdatertalk.so` | 3 KB | elf | 共享库：用户态共享库 | - |
| `libupdaterufp.so` | 10 KB | elf | 共享库：用户态共享库 | - |
| `libupdaterufunc.so` | 4 KB | elf | 共享库：用户态共享库 | - |
| `libusbcmd.so` | 16 KB | elf | 共享库：用户态共享库 | - |
| `libutil_date.so` | 5 KB | elf | 共享库：用户态共享库 | im.elf |
| `libxtables.so` | 19 KB | symlink | 符号链接：指向 libxtables.so.5.0.0 | - |
| `libxtables.so.5` | 19 KB | symlink | 符号链接：指向 libxtables.so.5.0.0 | - |
| `libxtables.so.5.0.0` | 19 KB | elf | 共享库：用户态共享库 | - |
| `libz.so` | 76 KB | symlink | 符号链接：指向 libz.so.1 | - |
| `libz.so.1` | 76 KB | symlink | 符号链接：指向 libz.so.1.2.11 | - |
| `libz.so.1.2.11` | 76 KB | elf | 共享库：用户态共享库 | im.elf |
| `viewUnified2.so` | 10.4 MB | elf | UI 视图库：viewUnified：Sugilite 菜单视图/绘制 | im.elf |
| `viewUnified3.so` | 806 KB | elf | UI 视图库：viewUnified：Sugilite 菜单视图/绘制 | - |
| `viewUnified4.so` | 2.6 MB | elf | UI 视图库：viewUnified：Sugilite 菜单视图/绘制 | - |
| `viewUnified5.so` | 716 KB | elf | UI 视图库：viewUnified：Sugilite 菜单视图/绘制 | - |
| `viewUnified6.so` | 532 KB | elf | UI 视图库：viewUnified：Sugilite 菜单视图/绘制 | - |
| `viewUnified7.so` | 584 KB | elf | UI 视图库：viewUnified：Sugilite 菜单视图/绘制 | - |
| `viewUnified8.so` | 267 KB | elf | UI 视图库：viewUnified：Sugilite 菜单视图/绘制 | - |

### `/usr/lib/dhcpd`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `dhcpd.leases` | 0 B | data | 共享库：用户态共享库 | - |

### `/usr/lib/netconf`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `bss.conf` | 449 B | data | 共享库：用户态共享库 | - |
| `dhcpd.conf` | 373 B | data | 共享库：用户态共享库 | - |
| `p2p.conf` | 599 B | data | 共享库：用户态共享库 | - |
| `p2p_multi_go.conf` | 599 B | data | 共享库：用户态共享库 | - |
| `pump.conf` | 134 B | data | 共享库：用户态共享库 | - |
| `pump_dns.conf` | 59 B | data | 共享库：用户态共享库 | - |

### `/usr/lib/ossl-modules`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `legacy.so` | 65 KB | elf | 共享库：用户态共享库 | - |

### `/usr/sabin`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `dcv_psf_table_movie.bin` | 10 KB | data | DSP 固件：dcv_psf_table_movie.bin：加速器/编码固件数据 | - |
| `dcv_psf_table_movie_4k.bin` | 10 KB | data | DSP 固件：dcv_psf_table_movie_4k.bin：加速器/编码固件数据 | - |
| `dcv_psf_table_movie_bayer.bin` | 18 KB | data | DSP 固件：dcv_psf_table_movie_bayer.bin：加速器/编码固件数据 | - |
| `dcv_psf_table_still.bin` | 56 KB | data | DSP 固件：dcv_psf_table_still.bin：加速器/编码固件数据 | - |
| `drt_dic.bin` | 52 KB | data | DSP 固件：drt_dic.bin：加速器/编码固件数据 | - |
| `sa_aaclcdec.bin` | 280 KB | data | DSP 固件：sa_aaclcdec.bin：加速器/编码固件数据 | - |
| `sa_aaclcenc.bin` | 216 KB | data | DSP 固件：sa_aaclcenc.bin：加速器/编码固件数据 | - |
| `sa_aaclcenc_aaclcdec.bin` | 489 KB | data | DSP 固件：sa_aaclcenc_aaclcdec.bin：加速器/编码固件数据 | - |
| `sa_ac3dec.bin` | 372 KB | data | DSP 固件：sa_ac3dec.bin：加速器/编码固件数据 | - |
| `sa_ac3enc_ac3dec.bin` | 464 KB | data | DSP 固件：sa_ac3enc_ac3dec.bin：加速器/编码固件数据 | - |
| `sa_aed.bin` | 1.0 MB | data | DSP 固件：sa_aed.bin：加速器/编码固件数据 | - |
| `sa_aes_sha2.bin` | 53 KB | data | DSP 固件：sa_aes_sha2.bin：加速器/编码固件数据 | - |
| `sa_apollo.bin` | 236 KB | data | DSP 固件：sa_apollo.bin：加速器/编码固件数据 | - |
| `sa_avcd_compatible_zma.bin` | 85 KB | data | DSP 固件：sa_avcd_compatible_zma.bin：加速器/编码固件数据 | - |
| `sa_avcd_performance_zma.bin` | 67 KB | data | DSP 固件：sa_avcd_performance_zma.bin：加速器/编码固件数据 | - |
| `sa_avce_performance_plus_zma.bin` | 223 KB | data | DSP 固件：sa_avce_performance_plus_zma.bin：加速器/编码固件数据 | - |
| `sa_avce_performance_zma.bin` | 222 KB | data | DSP 固件：sa_avce_performance_zma.bin：加速器/编码固件数据 | - |
| `sa_avce_quality_zma.bin` | 226 KB | data | DSP 固件：sa_avce_quality_zma.bin：加速器/编码固件数据 | - |
| `sa_bayes_tracker.bin` | 69 KB | data | DSP 固件：sa_bayes_tracker.bin：加速器/编码固件数据 | - |
| `sa_bayes_tracker_edge.bin` | 96 KB | data | DSP 固件：sa_bayes_tracker_edge.bin：加速器/编码固件数据 | - |
| `sa_bd_lpcmenc.bin` | 64 KB | data | DSP 固件：sa_bd_lpcmenc.bin：加速器/编码固件数据 | - |
| `sa_bdro2_bdex.bin` | 52 KB | data | DSP 固件：sa_bdro2_bdex.bin：加速器/编码固件数据 | - |
| `sa_cecil.bin` | 35 KB | data | DSP 固件：sa_cecil.bin：加速器/编码固件数据 | - |
| `sa_dcv.bin` | 18 KB | data | DSP 固件：sa_dcv.bin：加速器/编码固件数据 | - |
| `sa_dd51enc.bin` | 296 KB | data | DSP 固件：sa_dd51enc.bin：加速器/编码固件数据 | - |
| `sa_defect.bin` | 36 KB | data | DSP 固件：sa_defect.bin：加速器/编码固件数据 | - |
| `sa_dfdet.bin` | 153 KB | data | DSP 固件：sa_dfdet.bin：加速器/编码固件数据 | - |
| `sa_drt.bin` | 111 KB | data | DSP 固件：sa_drt.bin：加速器/编码固件数据 | - |
| `sa_dtcf.bin` | 66 KB | data | DSP 固件：sa_dtcf.bin：加速器/编码固件数据 | - |
| `sa_fec_enc32.bin` | 16 KB | data | DSP 固件：sa_fec_enc32.bin：加速器/编码固件数据 | - |
| `sa_frc2.bin` | 61 KB | data | DSP 固件：sa_frc2.bin：加速器/编码固件数据 | - |
| `sa_integdec.bin` | 343 KB | data | DSP 固件：sa_integdec.bin：加速器/编码固件数据 | - |
| `sa_integenc.bin` | 372 KB | data | DSP 固件：sa_integenc.bin：加速器/编码固件数据 | - |
| `sa_jpeg_dec_1core.bin` | 11 KB | data | DSP 固件：sa_jpeg_dec_1core.bin：加速器/编码固件数据 | - |
| `sa_jpeg_dec_1unit.bin` | 11 KB | data | DSP 固件：sa_jpeg_dec_1unit.bin：加速器/编码固件数据 | - |
| `sa_jpeg_enc_1core.bin` | 14 KB | data | DSP 固件：sa_jpeg_enc_1core.bin：加速器/编码固件数据 | - |
| `sa_jpeg_enc_1unit.bin` | 22 KB | data | DSP 固件：sa_jpeg_enc_1unit.bin：加速器/编码固件数据 | - |
| `sa_kknr.bin` | 65 KB | data | DSP 固件：sa_kknr.bin：加速器/编码固件数据 | - |
| `sa_lfnr_minna0.bin` | 22 KB | data | DSP 固件：sa_lfnr_minna0.bin：加速器/编码固件数据 | - |
| `sa_lfnr_minna1.bin` | 22 KB | data | DSP 固件：sa_lfnr_minna1.bin：加速器/编码固件数据 | - |
| `sa_lfnr_zma0.bin` | 22 KB | data | DSP 固件：sa_lfnr_zma0.bin：加速器/编码固件数据 | - |
| `sa_motionshot.bin` | 83 KB | data | DSP 固件：sa_motionshot.bin：加速器/编码固件数据 | - |
| `sa_nlap.bin` | 22 KB | data | DSP 固件：sa_nlap.bin：加速器/编码固件数据 | - |
| `sa_pcmcc.bin` | 17 KB | data | DSP 固件：sa_pcmcc.bin：加速器/编码固件数据 | - |
| `sa_replacer.bin` | 28 KB | data | DSP 固件：sa_replacer.bin：加速器/编码固件数据 | - |
| `sa_rotate90.bin` | 4 KB | data | DSP 固件：sa_rotate90.bin：加速器/编码固件数据 | - |
| `sa_seg.bin` | 52 KB | data | DSP 固件：sa_seg.bin：加速器/编码固件数据 | - |
| `sa_sftfcs.bin` | 43 KB | data | DSP 固件：sa_sftfcs.bin：加速器/编码固件数据 | - |
| `sa_shapep.bin` | 3 KB | data | DSP 固件：sa_shapep.bin：加速器/编码固件数据 | - |
| `sa_smod.bin` | 79 KB | data | DSP 固件：sa_smod.bin：加速器/编码固件数据 | - |
| `sa_spica.bin` | 23 KB | data | DSP 固件：sa_spica.bin：加速器/编码固件数据 | - |
| `sa_staple.bin` | 85 KB | data | DSP 固件：sa_staple.bin：加速器/编码固件数据 | - |
| `sa_star.bin` | 461 KB | data | DSP 固件：sa_star.bin：加速器/编码固件数据 | - |
| `sa_sweep_panorama.bin` | 19 KB | data | DSP 固件：sa_sweep_panorama.bin：加速器/编码固件数据 | - |
| `sa_tbox.bin` | 76 KB | data | DSP 固件：sa_tbox.bin：加速器/编码固件数据 | - |
| `sa_udrt.bin` | 112 KB | data | DSP 固件：sa_udrt.bin：加速器/编码固件数据 | - |
| `sa_zima_startup_minna.bin` | 3 KB | data | DSP 固件：sa_zima_startup_minna.bin：加速器/编码固件数据 | - |
| `sa_zima_startup_minna1.bin` | 3 KB | data | DSP 固件：sa_zima_startup_minna1.bin：加速器/编码固件数据 | - |
| `sa_zima_startup_zma0.bin` | 3 KB | data | DSP 固件：sa_zima_startup_zma0.bin：加速器/编码固件数据 | - |
| `sa_zima_startup_zma1.bin` | 3 KB | data | DSP 固件：sa_zima_startup_zma1.bin：加速器/编码固件数据 | - |
| `sa_zma_lpcmdec.bin` | 150 KB | data | DSP 固件：sa_zma_lpcmdec.bin：加速器/编码固件数据 | - |
| `sa_zoom_nr.bin` | 92 KB | data | DSP 固件：sa_zoom_nr.bin：加速器/编码固件数据 | - |
| `sa_zphdefdet.bin` | 18 KB | data | DSP 固件：sa_zphdefdet.bin：加速器/编码固件数据 | - |
| `spica_musashi_dualrec_4k_c_tap_step1.bin` | 39 KB | data | DSP 固件：spica_musashi_dualrec_4k_c_tap_step1.bin：加速器/编码固件数据 | - |
| `spica_musashi_dualrec_4k_c_tap_step2.bin` | 39 KB | data | DSP 固件：spica_musashi_dualrec_4k_c_tap_step2.bin：加速器/编码固件数据 | - |
| `spica_musashi_dualrec_4k_y_tap_step1.bin` | 47 KB | data | DSP 固件：spica_musashi_dualrec_4k_y_tap_step1.bin：加速器/编码固件数据 | - |
| `spica_musashi_dualrec_4k_y_tap_step2.bin` | 47 KB | data | DSP 固件：spica_musashi_dualrec_4k_y_tap_step2.bin：加速器/编码固件数据 | - |
| `spica_musashi_dualrec_c_tap_step1.bin` | 39 KB | data | DSP 固件：spica_musashi_dualrec_c_tap_step1.bin：加速器/编码固件数据 | - |
| `spica_musashi_dualrec_c_tap_step2.bin` | 39 KB | data | DSP 固件：spica_musashi_dualrec_c_tap_step2.bin：加速器/编码固件数据 | - |
| `spica_musashi_dualrec_y_tap_step1.bin` | 47 KB | data | DSP 固件：spica_musashi_dualrec_y_tap_step1.bin：加速器/编码固件数据 | - |
| `spica_musashi_dualrec_y_tap_step2.bin` | 47 KB | data | DSP 固件：spica_musashi_dualrec_y_tap_step2.bin：加速器/编码固件数据 | - |
| `spica_musashi_mov_4k_c_tap_step1.bin` | 39 KB | data | DSP 固件：spica_musashi_mov_4k_c_tap_step1.bin：加速器/编码固件数据 | - |
| `spica_musashi_mov_4k_c_tap_step2.bin` | 39 KB | data | DSP 固件：spica_musashi_mov_4k_c_tap_step2.bin：加速器/编码固件数据 | - |
| `spica_musashi_mov_4k_y_tap_step1.bin` | 47 KB | data | DSP 固件：spica_musashi_mov_4k_y_tap_step1.bin：加速器/编码固件数据 | - |
| `spica_musashi_mov_4k_y_tap_step2.bin` | 47 KB | data | DSP 固件：spica_musashi_mov_4k_y_tap_step2.bin：加速器/编码固件数据 | - |
| `spica_musashi_mov_c_tap_step1.bin` | 39 KB | data | DSP 固件：spica_musashi_mov_c_tap_step1.bin：加速器/编码固件数据 | - |
| `spica_musashi_mov_c_tap_step2.bin` | 39 KB | data | DSP 固件：spica_musashi_mov_c_tap_step2.bin：加速器/编码固件数据 | - |
| `spica_musashi_mov_interlace_c_tap_step1.bin` | 39 KB | data | DSP 固件：spica_musashi_mov_interlace_c_tap_step1.bin：加速器/编码固件数据 | - |
| `spica_musashi_mov_interlace_y_tap_step1.bin` | 47 KB | data | DSP 固件：spica_musashi_mov_interlace_y_tap_step1.bin：加速器/编码固件数据 | - |
| `spica_musashi_mov_y_tap_step1.bin` | 47 KB | data | DSP 固件：spica_musashi_mov_y_tap_step1.bin：加速器/编码固件数据 | - |
| `spica_musashi_mov_y_tap_step2.bin` | 47 KB | data | DSP 固件：spica_musashi_mov_y_tap_step2.bin：加速器/编码固件数据 | - |
| `spica_musashi_still_c_tap_step1.bin` | 39 KB | data | DSP 固件：spica_musashi_still_c_tap_step1.bin：加速器/编码固件数据 | - |
| `spica_musashi_still_c_tap_step2.bin` | 39 KB | data | DSP 固件：spica_musashi_still_c_tap_step2.bin：加速器/编码固件数据 | - |
| `spica_musashi_still_y_tap_step1.bin` | 47 KB | data | DSP 固件：spica_musashi_still_y_tap_step1.bin：加速器/编码固件数据 | - |
| `spica_musashi_still_y_tap_step2.bin` | 47 KB | data | DSP 固件：spica_musashi_still_y_tap_step2.bin：加速器/编码固件数据 | - |
| `star_kernel_param.bin` | 19 KB | data | DSP 固件：star_kernel_param.bin：加速器/编码固件数据 | - |

### `/usr/sbin`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `dhcpd` | 1.5 MB | elf | 系统管理：网络/管理工具 | - |
| `iptables` | 70 KB | symlink | 符号链接：指向 iptables-multi | - |
| `iptables-multi` | 70 KB | elf | 系统管理：网络/管理工具 | - |
| `iptables-restore` | 70 KB | symlink | 符号链接：指向 iptables-multi | - |
| `iptables-save` | 70 KB | symlink | 符号链接：指向 iptables-multi | - |
| `pump` | 65 KB | elf | 系统管理：网络/管理工具 | - |
| `tcpdump` | 1.8 MB | elf | 系统管理：网络/管理工具 | - |

### `/usr/scenario`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `AVBB_SCN_L_R_SETTING.so` | 5 KB | elf | 场景模块：AVBB_SCN_L_R_SETTING.so：scenario 命令实现 | - |
| `AVBB_SCN_L_R_SETTING_PANELEVF.so` | 5 KB | elf | 场景模块：AVBB_SCN_L_R_SETTING_PANELEVF.so：scenario 命令实现 | - |
| `AVBB_SCN_OPTAXIS_PANELEVF.so` | 5 KB | elf | 场景模块：AVBB_SCN_OPTAXIS_PANELEVF.so：scenario 命令实现 | - |
| `AVBB_SCN_START_AUDIO.so` | 10 KB | elf | 场景模块：AVBB_SCN_START_AUDIO.so：scenario 命令实现 | - |
| `AVBB_SCN_START_HDMI.so` | 20 KB | elf | 场景模块：AVBB_SCN_START_HDMI.so：scenario 命令实现 | - |
| `AVBB_SCN_START_HDMI_INPUT.so` | 17 KB | elf | 场景模块：AVBB_SCN_START_HDMI_INPUT.so：scenario 命令实现 | - |
| `AVBB_SCN_START_HDMI_INPUT_SUB.so` | 17 KB | elf | 场景模块：AVBB_SCN_START_HDMI_INPUT_SUB.so：scenario 命令实现 | - |
| `AVBB_SCN_START_HDMI_SUB.so` | 14 KB | elf | 场景模块：AVBB_SCN_START_HDMI_SUB.so：scenario 命令实现 | - |
| `AVBB_SCN_START_MIC.so` | 12 KB | elf | 场景模块：AVBB_SCN_START_MIC.so：scenario 命令实现 | - |
| `AVBB_SCN_START_MICSENSE.so` | 10 KB | elf | 场景模块：AVBB_SCN_START_MICSENSE.so：scenario 命令实现 | - |
| `AVBB_SCN_START_PANELEVF.so` | 13 KB | elf | 场景模块：AVBB_SCN_START_PANELEVF.so：scenario 命令实现 | - |
| `AVBB_SCN_START_VIDEO.so` | 10 KB | elf | 场景模块：AVBB_SCN_START_VIDEO.so：scenario 命令实现 | - |
| `AVBB_SCN_STOP_AUDIO.so` | 12 KB | elf | 场景模块：AVBB_SCN_STOP_AUDIO.so：scenario 命令实现 | - |
| `AVBB_SCN_STOP_HDMI.so` | 14 KB | elf | 场景模块：AVBB_SCN_STOP_HDMI.so：scenario 命令实现 | - |
| `AVBB_SCN_STOP_HDMI_INPUT.so` | 18 KB | elf | 场景模块：AVBB_SCN_STOP_HDMI_INPUT.so：scenario 命令实现 | - |
| `AVBB_SCN_STOP_MIC.so` | 12 KB | elf | 场景模块：AVBB_SCN_STOP_MIC.so：scenario 命令实现 | - |
| `AVBB_SCN_STOP_MICSENSE.so` | 10 KB | elf | 场景模块：AVBB_SCN_STOP_MICSENSE.so：scenario 命令实现 | - |
| `AVBB_SCN_STOP_PANELEVF.so` | 11 KB | elf | 场景模块：AVBB_SCN_STOP_PANELEVF.so：scenario 命令实现 | - |
| `AVBB_SCN_STOP_VIDEO.so` | 10 KB | elf | 场景模块：AVBB_SCN_STOP_VIDEO.so：scenario 命令实现 | - |
| `CAMERA_SCN_EE_SETUP_START_STOP.so` | 17 KB | elf | 场景模块：CAMERA_SCN_EE_SETUP_START_STOP.so：scenario 命令实现 | - |
| `CAMERA_SCN_EE_SET_PRM.so` | 9 KB | elf | 场景模块：CAMERA_SCN_EE_SET_PRM.so：scenario 命令实现 | - |
| `CAMERA_SCN_EE_START_STOP.so` | 18 KB | elf | 场景模块：CAMERA_SCN_EE_START_STOP.so：scenario 命令实现 | - |
| `CAMERA_SCN_EXTERNAL_RAW_RECORD.so` | 8 KB | elf | 场景模块：CAMERA_SCN_EXTERNAL_RAW_RECORD.so：scenario 命令实现 | - |
| `CAMERA_SCN_FACE_REC_DATA.so` | 7 KB | elf | 场景模块：CAMERA_SCN_FACE_REC_DATA.so：scenario 命令实现 | - |
| `CAMERA_SCN_MOVIE_REC_START.so` | 7 KB | elf | 场景模块：CAMERA_SCN_MOVIE_REC_START.so：scenario 命令实现 | - |
| `CAMERA_SCN_SET_ZOOM_DRV.so` | 6 KB | elf | 场景模块：CAMERA_SCN_SET_ZOOM_DRV.so：scenario 命令实现 | - |
| `CAMERA_SCN_VIDEOLIGHT_SW.so` | 6 KB | elf | 场景模块：CAMERA_SCN_VIDEOLIGHT_SW.so：scenario 命令实现 | - |
| `MPR_SCN_EXEC_FACTORY_MODE.so` | 6 KB | elf | 场景模块：MPR_SCN_EXEC_FACTORY_MODE.so：scenario 命令实现 | - |
| `MPR_SCN_EXEC_WIFI_TEST.so` | 6 KB | elf | 场景模块：MPR_SCN_EXEC_WIFI_TEST.so：scenario 命令实现 | - |
| `MPR_SCN_FLASH_BACKUP_INIT.so` | 6 KB | elf | 场景模块：MPR_SCN_FLASH_BACKUP_INIT.so：scenario 命令实现 | - |
| `MPR_SCN_FORMAT.so` | 19 KB | elf | 场景模块：MPR_SCN_FORMAT.so：scenario 命令实现 | - |
| `MPR_SCN_GET_CONTENT_COUNT.so` | 16 KB | elf | 场景模块：MPR_SCN_GET_CONTENT_COUNT.so：scenario 命令实现 | - |
| `MPR_SCN_GET_TOTAL_LOG.so` | 34 KB | elf | 场景模块：MPR_SCN_GET_TOTAL_LOG.so：scenario 命令实现 | - |
| `MPR_SCN_INSTALL_MAP_DEMOMOVIE.so` | 145 KB | elf | 场景模块：MPR_SCN_INSTALL_MAP_DEMOMOVIE.so：scenario 命令实现 | - |
| `MPR_SCN_SET_FACTORY_MODE.so` | 6 KB | elf | 场景模块：MPR_SCN_SET_FACTORY_MODE.so：scenario 命令实现 | - |

### `/usr/share/app`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `HeiseiKakuGothW5-SJ_wIcon.ltt` | 832 KB | data | UI 资源：HeiseiKakuGothW5-SJ_wIcon.ltt：视图/资源文件 | - |
| `IRShooting.uxc` | 7 KB | data | UI 资源：IRShooting.uxc：视图/资源文件 | - |
| `LayoutMaster_Menu.uxc` | 3 KB | data | UI 资源：LayoutMaster_Menu.uxc：视图/资源文件 | - |
| `MYingHeiC-KSX1001-SJ_wIcon.ltt` | 902 KB | data | UI 资源：MYingHeiC-KSX1001-SJ_wIcon.ltt：视图/资源文件 | - |
| `Sony_DI_Icons.ttf` | 605 KB | data | UI 资源：Sony_DI_Icons.ttf：视图/资源文件 | - |
| `UniversOTS-SJ_wIcon.ltt` | 597 KB | data | UI 资源：UniversOTS-SJ_wIcon.ltt：视图/资源文件 | - |
| `area_check_data.dat` | 683 KB | data | UI 资源：area_check_data.dat：视图/资源文件 | - |
| `color_cmn.uxc` | 312 B | data | UI 资源：color_cmn.uxc：视图/资源文件 | - |
| `fontlist.dat` | 360 B | data | UI 资源：fontlist.dat：视图/资源文件 | - |
| `global.xdb` | 10 KB | data | UI 资源：global.xdb：视图/资源文件 | - |
| `image_DSC_Entry_Only_43.uxc` | 526 KB | data | UI 资源：image_DSC_Entry_Only_43.uxc：视图/资源文件 | - |
| `image_DSC_Only_43.uxc` | 10.2 MB | data | UI 资源：image_DSC_Only_43.uxc：视图/资源文件 | - |
| `image_DSLR_Only_43.uxc` | 2.3 MB | data | UI 资源：image_DSLR_Only_43.uxc：视图/资源文件 | - |
| `image_EVF.uxc` | 2.7 MB | data | UI 资源：image_EVF.uxc：视图/资源文件 | - |
| `image_Fn_Menu_43.uxc` | 145 KB | data | UI 资源：image_Fn_Menu_43.uxc：视图/资源文件 | - |
| `image_Rich_Help_Guide_43.uxc` | 4.9 MB | data | UI 资源：image_Rich_Help_Guide_43.uxc：视图/资源文件 | - |
| `image_cmn_43.uxc` | 25.3 MB | data | UI 资源：image_cmn_43.uxc：视图/资源文件 | - |
| `image_cmn_o_direct_43.uxc` | 1.2 MB | data | UI 资源：image_cmn_o_direct_43.uxc：视图/资源文件 | - |
| `lang.uxb` | 3 KB | data | UI 资源：lang.uxb：视图/资源文件 | - |
| `lang_cmn.uxc` | 1 KB | data | UI 资源：lang_cmn.uxc：视图/资源文件 | - |
| `master_browser.uxc` | 27 KB | data | UI 资源：master_browser.uxc：视图/资源文件 | - |
| `master_camera.uxc` | 99 KB | data | UI 资源：master_camera.uxc：视图/资源文件 | - |
| `master_network.uxc` | 35 KB | data | UI 资源：master_network.uxc：视图/资源文件 | - |
| `master_other.uxc` | 14 KB | data | UI 资源：master_other.uxc：视图/资源文件 | - |
| `string_arabic.uxc` | 568 KB | data | UI 资源：string_arabic.uxc：视图/资源文件 | - |
| `string_brazilianportuguese.uxc` | 399 KB | data | UI 资源：string_brazilianportuguese.uxc：视图/资源文件 | - |
| `string_bulgarian.uxc` | 614 KB | data | UI 资源：string_bulgarian.uxc：视图/资源文件 | - |
| `string_canadianfrench.uxc` | 261 KB | data | UI 资源：string_canadianfrench.uxc：视图/资源文件 | - |
| `string_croatian.uxc` | 384 KB | data | UI 资源：string_croatian.uxc：视图/资源文件 | - |
| `string_czech.uxc` | 422 KB | data | UI 资源：string_czech.uxc：视图/资源文件 | - |
| `string_danish.uxc` | 402 KB | data | UI 资源：string_danish.uxc：视图/资源文件 | - |
| `string_dutch.uxc` | 421 KB | data | UI 资源：string_dutch.uxc：视图/资源文件 | - |
| `string_english.uxc` | 383 KB | data | UI 资源：string_english.uxc：视图/资源文件 | - |
| `string_finnish.uxc` | 398 KB | data | UI 资源：string_finnish.uxc：视图/资源文件 | - |
| `string_french.uxc` | 453 KB | data | UI 资源：string_french.uxc：视图/资源文件 | - |
| `string_german.uxc` | 430 KB | data | UI 资源：string_german.uxc：视图/资源文件 | - |
| `string_greek.uxc` | 702 KB | data | UI 资源：string_greek.uxc：视图/资源文件 | - |
| `string_hindi.uxc` | 871 KB | data | UI 资源：string_hindi.uxc：视图/资源文件 | - |
| `string_hungarian.uxc` | 441 KB | data | UI 资源：string_hungarian.uxc：视图/资源文件 | - |
| `string_indonesia.uxc` | 377 KB | data | UI 资源：string_indonesia.uxc：视图/资源文件 | - |
| `string_italian.uxc` | 445 KB | data | UI 资源：string_italian.uxc：视图/资源文件 | - |
| `string_japanese.uxc` | 476 KB | data | UI 资源：string_japanese.uxc：视图/资源文件 | - |
| `string_korean.uxc` | 447 KB | data | UI 资源：string_korean.uxc：视图/资源文件 | - |
| `string_malay.uxc` | 396 KB | data | UI 资源：string_malay.uxc：视图/资源文件 | - |
| `string_norwegian.uxc` | 392 KB | data | UI 资源：string_norwegian.uxc：视图/资源文件 | - |
| `string_persian.uxc` | 616 KB | data | UI 资源：string_persian.uxc：视图/资源文件 | - |
| `string_polish.uxc` | 425 KB | data | UI 资源：string_polish.uxc：视图/资源文件 | - |
| `string_portuguese.uxc` | 419 KB | data | UI 资源：string_portuguese.uxc：视图/资源文件 | - |
| `string_romanian.uxc` | 415 KB | data | UI 资源：string_romanian.uxc：视图/资源文件 | - |
| `string_russian.uxc` | 670 KB | data | UI 资源：string_russian.uxc：视图/资源文件 | - |
| `string_simplifiedchinese.uxc` | 342 KB | data | UI 资源：string_simplifiedchinese.uxc：视图/资源文件 | - |
| `string_spanish.uxc` | 432 KB | data | UI 资源：string_spanish.uxc：视图/资源文件 | - |
| `string_swedish.uxc` | 396 KB | data | UI 资源：string_swedish.uxc：视图/资源文件 | - |
| `string_thai.uxc` | 830 KB | data | UI 资源：string_thai.uxc：视图/资源文件 | - |
| `string_traditionalchinese.uxc` | 344 KB | data | UI 资源：string_traditionalchinese.uxc：视图/资源文件 | - |
| `string_turkish.uxc` | 414 KB | data | UI 资源：string_turkish.uxc：视图/资源文件 | - |
| `string_ukrainian.uxc` | 628 KB | data | UI 资源：string_ukrainian.uxc：视图/资源文件 | - |
| `string_vietnamese.uxc` | 457 KB | data | UI 资源：string_vietnamese.uxc：视图/资源文件 | - |
| `style_cmn.uxc` | 2 KB | data | UI 资源：style_cmn.uxc：视图/资源文件 | - |
| `view24pMode.uxc` | 748 B | data | UI 资源：view24pMode.uxc：视图/资源文件 | - |
| `view3DPb.uxc` | 748 B | data | UI 资源：view3DPb.uxc：视图/资源文件 | - |
| `viewAccessPoint.uxc` | 27 KB | data | UI 资源：viewAccessPoint.uxc：视图/资源文件 | - |
| `viewAfAdjustment.uxc` | 1 KB | data | UI 资源：viewAfAdjustment.uxc：视图/资源文件 | - |
| `viewAfTrackingSpeed.uxc` | 1 KB | data | UI 资源：viewAfTrackingSpeed.uxc：视图/资源文件 | - |
| `viewAnimation360.uxc` | 588 B | data | UI 资源：viewAnimation360.uxc：视图/资源文件 | - |
| `viewAreaSet.uxc` | 1 KB | data | UI 资源：viewAreaSet.uxc：视图/资源文件 | - |
| `viewArtFilter.uxc` | 1 KB | data | UI 资源：viewArtFilter.uxc：视图/资源文件 | - |
| `viewAspectRatio.uxc` | 1 KB | data | UI 资源：viewAspectRatio.uxc：视图/资源文件 | - |
| `viewAudioRecLevel_D.uxc` | 868 B | data | UI 资源：viewAudioRecLevel_D.uxc：视图/资源文件 | - |
| `viewAutoDualRec.uxc` | 944 B | data | UI 资源：viewAutoDualRec.uxc：视图/资源文件 | - |
| `viewAutoPlay.uxc` | 1 KB | data | UI 资源：viewAutoPlay.uxc：视图/资源文件 | - |
| `viewAutoPlaySetting.uxc` | 1 KB | data | UI 资源：viewAutoPlaySetting.uxc：视图/资源文件 | - |
| `viewAutoPowerOff.uxc` | 132 B | data | UI 资源：viewAutoPowerOff.uxc：视图/资源文件 | - |
| `viewAutoRepair.uxc` | 2 KB | data | UI 资源：viewAutoRepair.uxc：视图/资源文件 | - |
| `viewAutoSelection.uxc` | 868 B | data | UI 资源：viewAutoSelection.uxc：视图/资源文件 | - |
| `viewBaseMenu.uxc` | 84 B | data | UI 资源：viewBaseMenu.uxc：视图/资源文件 | - |
| `viewBatteryAuthentication.uxc` | 320 B | data | UI 资源：viewBatteryAuthentication.uxc：视图/资源文件 | - |
| `viewBeautyEffect.uxc` | 7 KB | data | UI 资源：viewBeautyEffect.uxc：视图/资源文件 | - |
| `viewBluetoothPairing.uxc` | 7 KB | data | UI 资源：viewBluetoothPairing.uxc：视图/资源文件 | - |
| `viewCalibration.uxc` | 2 KB | data | UI 资源：viewCalibration.uxc：视图/资源文件 | - |
| `viewCaution.uxc` | 7 KB | data | UI 资源：viewCaution.uxc：视图/资源文件 | - |
| `viewCertificationLogo.uxc` | 428 B | data | UI 资源：viewCertificationLogo.uxc：视图/资源文件 | - |
| `viewCleaningMode.uxc` | 556 B | data | UI 资源：viewCleaningMode.uxc：视图/资源文件 | - |
| `viewCommonDedicatedScreenBase.uxc` | 132 B | data | UI 资源：viewCommonDedicatedScreenBase.uxc：视图/资源文件 | - |
| `viewCommonDedicatedScreenFunc.uxc` | 1 KB | data | UI 资源：viewCommonDedicatedScreenFunc.uxc：视图/资源文件 | - |
| `viewCommonShootingSetting.uxc` | 5 KB | data | UI 资源：viewCommonShootingSetting.uxc：视图/资源文件 | - |
| `viewContPbGroup.uxc` | 7 KB | data | UI 资源：viewContPbGroup.uxc：视图/资源文件 | - |
| `viewContPriorityExpMode.uxc` | 636 B | data | UI 资源：viewContPriorityExpMode.uxc：视图/资源文件 | - |
| `viewCopyrightInformation.uxc` | 992 B | data | UI 资源：viewCopyrightInformation.uxc：视图/资源文件 | - |
| `viewCreateFolder.uxc` | 412 B | data | UI 资源：viewCreateFolder.uxc：视图/资源文件 | - |
| `viewCreativeStyle.uxc` | 1 KB | data | UI 资源：viewCreativeStyle.uxc：视图/资源文件 | - |
| `viewCustomWB.uxc` | 3 KB | data | UI 资源：viewCustomWB.uxc：视图/资源文件 | - |
| `viewCustomZebra.uxc` | 1 KB | data | UI 资源：viewCustomZebra.uxc：视图/资源文件 | - |
| `viewDateSet.uxc` | 1 KB | data | UI 资源：viewDateSet.uxc：视图/资源文件 | - |
| `viewDeleteAllIn4Single.uxc` | 1 KB | data | UI 资源：viewDeleteAllIn4Single.uxc：视图/资源文件 | - |
| `viewDeleteSelected4Index.uxc` | 3 KB | data | UI 资源：viewDeleteSelected4Index.uxc：视图/资源文件 | - |
| `viewDeleteSelected4Single.uxc` | 4 KB | data | UI 资源：viewDeleteSelected4Single.uxc：视图/资源文件 | - |
| `viewDeleteThis4Index.uxc` | 216 B | data | UI 资源：viewDeleteThis4Index.uxc：视图/资源文件 | - |
| `viewDeleteThis4Single.uxc` | 372 B | data | UI 资源：viewDeleteThis4Single.uxc：视图/资源文件 | - |
| `viewDeleteThisConfirm4Index.uxc` | 268 B | data | UI 资源：viewDeleteThisConfirm4Index.uxc：视图/资源文件 | - |
| `viewDemoMoviePb.uxc` | 552 B | data | UI 资源：viewDemoMoviePb.uxc：视图/资源文件 | - |
| `viewDgtlZoomSetting.uxc` | 2 KB | data | UI 资源：viewDgtlZoomSetting.uxc：视图/资源文件 | - |
| `viewDpofCancelAll.uxc` | 1 KB | data | UI 资源：viewDpofCancelAll.uxc：视图/资源文件 | - |
| `viewDpofPhotoBookDatePrint.uxc` | 500 B | data | UI 资源：viewDpofPhotoBookDatePrint.uxc：视图/资源文件 | - |
| `viewDpofPhotoBookSelected4Index.uxc` | 3 KB | data | UI 资源：viewDpofPhotoBookSelected4Index.uxc：视图/资源文件 | - |
| `viewDpofPhotoBookSelected4Single.uxc` | 4 KB | data | UI 资源：viewDpofPhotoBookSelected4Single.uxc：视图/资源文件 | - |
| `viewDpofSetting.uxc` | 1 KB | data | UI 资源：viewDpofSetting.uxc：视图/资源文件 | - |
| `viewDro.uxc` | 1 KB | data | UI 资源：viewDro.uxc：视图/资源文件 | - |
| `viewDummyBaseView.uxc` | 132 B | data | UI 资源：viewDummyBaseView.uxc：视图/资源文件 | - |
| `viewDummyBlack.uxc` | 148 B | data | UI 资源：viewDummyBlack.uxc：视图/资源文件 | - |
| `viewEditPrefixFileName.uxc` | 1 KB | data | UI 资源：viewEditPrefixFileName.uxc：视图/资源文件 | - |
| `viewEpo.uxc` | 3 KB | data | UI 资源：viewEpo.uxc：视图/资源文件 | - |
| `viewEvfAdjustment_D.uxc` | 944 B | data | UI 资源：viewEvfAdjustment_D.uxc：视图/资源文件 | - |
| `viewEvfBrightness.uxc` | 1 KB | data | UI 资源：viewEvfBrightness.uxc：视图/资源文件 | - |
| `viewExecuteConfirmDlg.uxc` | 700 B | data | UI 资源：viewExecuteConfirmDlg.uxc：视图/资源文件 | - |
| `viewExposureCompensation.uxc` | 1 KB | data | UI 资源：viewExposureCompensation.uxc：视图/资源文件 | - |
| `viewExtFlashComp.uxc` | 2 KB | data | UI 资源：viewExtFlashComp.uxc：视图/资源文件 | - |
| `viewExtFlashFnSetting.uxc` | 32 KB | data | UI 资源：viewExtFlashFnSetting.uxc：视图/资源文件 | - |
| `viewExtFlashLevel.uxc` | 1 KB | data | UI 资源：viewExtFlashLevel.uxc：视图/资源文件 | - |
| `viewExtFlashMenuSetting.uxc` | 16 KB | data | UI 资源：viewExtFlashMenuSetting.uxc：视图/资源文件 | - |
| `viewExtFlashPopUpSettings.uxc` | 936 B | data | UI 资源：viewExtFlashPopUpSettings.uxc：视图/资源文件 | - |
| `viewFaceDetection.uxc` | 1 KB | data | UI 资源：viewFaceDetection.uxc：视图/资源文件 | - |
| `viewFinderFrameRate.uxc` | 808 B | data | UI 资源：viewFinderFrameRate.uxc：视图/资源文件 | - |
| `viewFlash.uxc` | 1 KB | data | UI 资源：viewFlash.uxc：视图/资源文件 | - |
| `viewFlashLevel.uxc` | 1 KB | data | UI 资源：viewFlashLevel.uxc：视图/资源文件 | - |
| `viewFnMenu.uxc` | 7 KB | data | UI 资源：viewFnMenu.uxc：视图/资源文件 | - |
| `viewFocusArea.uxc` | 2 KB | data | UI 资源：viewFocusArea.uxc：视图/资源文件 | - |
| `viewFocusArea_C.uxc` | 2 KB | data | UI 资源：viewFocusArea_C.uxc：视图/资源文件 | - |
| `viewFocusControl.uxc` | 1 KB | data | UI 资源：viewFocusControl.uxc：视图/资源文件 | - |
| `viewFocusMagnification.uxc` | 8 KB | data | UI 资源：viewFocusMagnification.uxc：视图/资源文件 | - |
| `viewFocusMagnificationMovie.uxc` | 8 KB | data | UI 资源：viewFocusMagnificationMovie.uxc：视图/资源文件 | - |
| `viewFocusMode.uxc` | 1 KB | data | UI 资源：viewFocusMode.uxc：视图/资源文件 | - |
| `viewFocusRangeLimiter.uxc` | 708 B | data | UI 资源：viewFocusRangeLimiter.uxc：视图/资源文件 | - |
| `viewFocusSet.uxc` | 5 KB | data | UI 资源：viewFocusSet.uxc：视图/资源文件 | - |
| `viewFormat.uxc` | 1 KB | data | UI 资源：viewFormat.uxc：视图/资源文件 | - |
| `viewFtpExecution.uxc` | 3 KB | data | UI 资源：viewFtpExecution.uxc：视图/资源文件 | - |
| `viewFtpFunction.uxc` | 2 KB | data | UI 资源：viewFtpFunction.uxc：视图/资源文件 | - |
| `viewFtpImgTypeSelection.uxc` | 3 KB | data | UI 资源：viewFtpImgTypeSelection.uxc：视图/资源文件 | - |
| `viewFtpResult.uxc` | 5 KB | data | UI 资源：viewFtpResult.uxc：视图/资源文件 | - |
| `viewFtpServer.uxc` | 7 KB | data | UI 资源：viewFtpServer.uxc：视图/资源文件 | - |
| `viewFtpServerSettings.uxc` | 1 KB | data | UI 资源：viewFtpServerSettings.uxc：视图/资源文件 | - |
| `viewFtpSettingTransfer.uxc` | 440 B | data | UI 资源：viewFtpSettingTransfer.uxc：视图/资源文件 | - |
| `viewFtpTransfer.uxc` | 4 KB | data | UI 资源：viewFtpTransfer.uxc：视图/资源文件 | - |
| `viewFtpTransferring.uxc` | 2 KB | data | UI 资源：viewFtpTransferring.uxc：视图/资源文件 | - |
| `viewGenKeyboard.uxc` | 12 KB | data | UI 资源：viewGenKeyboard.uxc：视图/资源文件 | - |
| `viewGlobalMenu.uxc` | 3 KB | data | UI 资源：viewGlobalMenu.uxc：视图/资源文件 | - |
| `viewGpsInfo.uxc` | 5 KB | data | UI 资源：viewGpsInfo.uxc：视图/资源文件 | - |
| `viewGpsTest.uxc` | 440 B | data | UI 资源：viewGpsTest.uxc：视图/资源文件 | - |
| `viewGpsTracker.uxc` | 4 KB | data | UI 资源：viewGpsTracker.uxc：视图/资源文件 | - |
| `viewGroupSelectionCalendar.uxc` | 4 KB | data | UI 资源：viewGroupSelectionCalendar.uxc：视图/资源文件 | - |
| `viewGroupSelectionFolder.uxc` | 3 KB | data | UI 资源：viewGroupSelectionFolder.uxc：视图/资源文件 | - |
| `viewIREditOne.uxc` | 14 KB | data | UI 资源：viewIREditOne.uxc：视图/资源文件 | - |
| `viewImageRotate.uxc` | 1 KB | data | UI 资源：viewImageRotate.uxc：视图/资源文件 | - |
| `viewIndexPb.uxc` | 3 KB | data | UI 资源：viewIndexPb.uxc：视图/资源文件 | - |
| `viewIndividualRecognition.uxc` | 2 KB | data | UI 资源：viewIndividualRecognition.uxc：视图/资源文件 | - |
| `viewInitialSetting.uxc` | 8 KB | data | UI 资源：viewInitialSetting.uxc：视图/资源文件 | - |
| `viewIntervalSetting.uxc` | 3 KB | data | UI 资源：viewIntervalSetting.uxc：视图/资源文件 | - |
| `viewIroiroCon.uxc` | 22 KB | data | UI 资源：viewIroiroCon.uxc：视图/资源文件 | - |
| `viewIsoAutoMinSS.uxc` | 684 B | data | UI 资源：viewIsoAutoMinSS.uxc：视图/资源文件 | - |
| `viewIsoSensitivity.uxc` | 2 KB | data | UI 资源：viewIsoSensitivity.uxc：视图/资源文件 | - |
| `viewKeyboard.uxc` | 13 KB | data | UI 资源：viewKeyboard.uxc：视图/资源文件 | - |
| `viewLcdBrightness.uxc` | 1 KB | data | UI 资源：viewLcdBrightness.uxc：视图/资源文件 | - |
| `viewLensRing.uxc` | 2 KB | data | UI 资源：viewLensRing.uxc：视图/资源文件 | - |
| `viewManualControlDial_D.uxc` | 10 KB | data | UI 资源：viewManualControlDial_D.uxc：视图/资源文件 | - |
| `viewManualRepair.uxc` | 3 KB | data | UI 资源：viewManualRepair.uxc：视图/资源文件 | - |
| `viewManualRepairForPlay.uxc` | 3 KB | data | UI 资源：viewManualRepairForPlay.uxc：视图/资源文件 | - |
| `viewMediaCopy.uxc` | 3 KB | data | UI 资源：viewMediaCopy.uxc：视图/资源文件 | - |
| `viewMediaFileMgmt.uxc` | 2 KB | data | UI 资源：viewMediaFileMgmt.uxc：视图/资源文件 | - |
| `viewMeteringmode.uxc` | 1 KB | data | UI 资源：viewMeteringmode.uxc：视图/资源文件 | - |
| `viewModeDialGuide.uxc` | 1 KB | data | UI 资源：viewModeDialGuide.uxc：视图/资源文件 | - |
| `viewMonitorBrightness.uxc` | 1 KB | data | UI 资源：viewMonitorBrightness.uxc：视图/资源文件 | - |
| `viewMotionAdjustment.uxc` | 1 KB | data | UI 资源：viewMotionAdjustment.uxc：视图/资源文件 | - |
| `viewMotionVideo.uxc` | 4 KB | data | UI 资源：viewMotionVideo.uxc：视图/资源文件 | - |
| `viewMovieExpMode.uxc` | 2 KB | data | UI 资源：viewMovieExpMode.uxc：视图/资源文件 | - |
| `viewMoviePb.uxc` | 13 KB | data | UI 资源：viewMoviePb.uxc：视图/资源文件 | - |
| `viewMoviePreview.uxc` | 3 KB | data | UI 资源：viewMoviePreview.uxc：视图/资源文件 | - |
| `viewNoImage.uxc` | 2 KB | data | UI 资源：viewNoImage.uxc：视图/资源文件 | - |
| `viewNtscPalSEL_D.uxc` | 700 B | data | UI 资源：viewNtscPalSEL_D.uxc：视图/资源文件 | - |
| `viewObjectTracking.uxc` | 1 KB | data | UI 资源：viewObjectTracking.uxc：视图/资源文件 | - |
| `viewObjecttrackingBase.uxc` | 1 KB | data | UI 资源：viewObjecttrackingBase.uxc：视图/资源文件 | - |
| `viewPanoramaMode.uxc` | 912 B | data | UI 资源：viewPanoramaMode.uxc：视图/资源文件 | - |
| `viewPanoramaPb.uxc` | 3 KB | data | UI 资源：viewPanoramaPb.uxc：视图/资源文件 | - |
| `viewPanoramaStl.uxc` | 44 KB | data | UI 资源：viewPanoramaStl.uxc：视图/资源文件 | - |
| `viewPhotoCapture.uxc` | 440 B | data | UI 资源：viewPhotoCapture.uxc：视图/资源文件 | - |
| `viewPictureEffectPb_C.uxc` | 2 KB | data | UI 资源：viewPictureEffectPb_C.uxc：视图/资源文件 | - |
| `viewPictureProfile.uxc` | 1 KB | data | UI 资源：viewPictureProfile.uxc：视图/资源文件 | - |
| `viewPlayingMedia_D.uxc` | 1 KB | data | UI 资源：viewPlayingMedia_D.uxc：视图/资源文件 | - |
| `viewPortraitFraming.uxc` | 1 KB | data | UI 资源：viewPortraitFraming.uxc：视图/资源文件 | - |
| `viewPriorAWB.uxc` | 1 KB | data | UI 资源：viewPriorAWB.uxc：视图/资源文件 | - |
| `viewPrivacyNotice.uxc` | 760 B | data | UI 资源：viewPrivacyNotice.uxc：视图/资源文件 | - |
| `viewProtectAll.uxc` | 1 KB | data | UI 资源：viewProtectAll.uxc：视图/资源文件 | - |
| `viewProtectSelected4Index.uxc` | 3 KB | data | UI 资源：viewProtectSelected4Index.uxc：视图/资源文件 | - |
| `viewProtectSelected4Single.uxc` | 4 KB | data | UI 资源：viewProtectSelected4Single.uxc：视图/资源文件 | - |
| `viewQuickNavi.uxc` | 9 KB | data | UI 资源：viewQuickNavi.uxc：视图/资源文件 | - |
| `viewRating.uxc` | 6 KB | data | UI 资源：viewRating.uxc：视图/资源文件 | - |
| `viewRatingLimitSetting.uxc` | 2 KB | data | UI 资源：viewRatingLimitSetting.uxc：视图/资源文件 | - |
| `viewRecCustomReset.uxc` | 192 B | data | UI 资源：viewRecCustomReset.uxc：视图/资源文件 | - |
| `viewRecDriveMode.uxc` | 1 KB | data | UI 资源：viewRecDriveMode.uxc：视图/资源文件 | - |
| `viewRecRecordingMedia.uxc` | 2 KB | data | UI 资源：viewRecRecordingMedia.uxc：视图/资源文件 | - |
| `viewRecSteadyShot.uxc` | 2 KB | data | UI 资源：viewRecSteadyShot.uxc：视图/资源文件 | - |
| `viewRecallShootSet.uxc` | 3 KB | data | UI 资源：viewRecallShootSet.uxc：视图/资源文件 | - |
| `viewRecovery.uxc` | 172 B | data | UI 资源：viewRecovery.uxc：视图/资源文件 | - |
| `viewRegisteredAfFrame.uxc` | 676 B | data | UI 资源：viewRegisteredAfFrame.uxc：视图/资源文件 | - |
| `viewRemoteCameraControl.uxc` | 8 KB | data | UI 资源：viewRemoteCameraControl.uxc：视图/资源文件 | - |
| `viewRichHelpGuide.uxc` | 2 KB | data | UI 资源：viewRichHelpGuide.uxc：视图/资源文件 | - |
| `viewRootPowerSw.uxc` | 2 KB | data | UI 资源：viewRootPowerSw.uxc：视图/资源文件 | - |
| `viewSLogDispAssist.uxc` | 848 B | data | UI 资源：viewSLogDispAssist.uxc：视图/资源文件 | - |
| `viewSalvageRestore.uxc` | 1 KB | data | UI 资源：viewSalvageRestore.uxc：视图/资源文件 | - |
| `viewScnSelection.uxc` | 572 B | data | UI 资源：viewScnSelection.uxc：视图/资源文件 | - |
| `viewSelectContentType.uxc` | 1 KB | data | UI 资源：viewSelectContentType.uxc：视图/资源文件 | - |
| `viewSelectFolder.uxc` | 636 B | data | UI 资源：viewSelectFolder.uxc：视图/资源文件 | - |
| `viewSelectTransferType.uxc` | 1 KB | data | UI 资源：viewSelectTransferType.uxc：视图/资源文件 | - |
| `viewSelfTimerOnBracket.uxc` | 940 B | data | UI 资源：viewSelfTimerOnBracket.uxc：视图/资源文件 | - |
| `viewSendSelected4Index.uxc` | 3 KB | data | UI 资源：viewSendSelected4Index.uxc：视图/资源文件 | - |
| `viewSendSelected4IndexFtp.uxc` | 10 KB | data | UI 资源：viewSendSelected4IndexFtp.uxc：视图/资源文件 | - |
| `viewSendSelected4Single.uxc` | 5 KB | data | UI 资源：viewSendSelected4Single.uxc：视图/资源文件 | - |
| `viewSendSelected4SingleFtp.uxc` | 15 KB | data | UI 资源：viewSendSelected4SingleFtp.uxc：视图/资源文件 | - |
| `viewSendToComputer.uxc` | 6 KB | data | UI 资源：viewSendToComputer.uxc：视图/资源文件 | - |
| `viewSendToSmartphone.uxc` | 11 KB | data | UI 资源：viewSendToSmartphone.uxc：视图/资源文件 | - |
| `viewSettingMenu.uxc` | 8 KB | data | UI 资源：viewSettingMenu.uxc：视图/资源文件 | - |
| `viewSettingReset.uxc` | 2 KB | data | UI 资源：viewSettingReset.uxc：视图/资源文件 | - |
| `viewSettingSave.uxc` | 8 KB | data | UI 资源：viewSettingSave.uxc：视图/资源文件 | - |
| `viewSetupCustomFunction.uxc` | 1 KB | data | UI 资源：viewSetupCustomFunction.uxc：视图/资源文件 | - |
| `viewShootingInfoDisp.uxc` | 2 KB | data | UI 资源：viewShootingInfoDisp.uxc：视图/资源文件 | - |
| `viewShutterSpeed.uxc` | 772 B | data | UI 资源：viewShutterSpeed.uxc：视图/资源文件 | - |
| `viewSinglePb.uxc` | 8 KB | data | UI 资源：viewSinglePb.uxc：视图/资源文件 | - |
| `viewSinglePb4K.uxc` | 2 KB | data | UI 资源：viewSinglePb4K.uxc：视图/资源文件 | - |
| `viewSlowquickFrameRate.uxc` | 1 KB | data | UI 资源：viewSlowquickFrameRate.uxc：视图/资源文件 | - |
| `viewSmileShutter.uxc` | 1 KB | data | UI 资源：viewSmileShutter.uxc：视图/资源文件 | - |
| `viewSnapShotBoot.uxc` | 132 B | data | UI 资源：viewSnapShotBoot.uxc：视图/资源文件 | - |
| `viewSoftSkin.uxc` | 2 KB | data | UI 资源：viewSoftSkin.uxc：视图/资源文件 | - |
| `viewStillImageQuality.uxc` | 1004 B | data | UI 资源：viewStillImageQuality.uxc：视图/资源文件 | - |
| `viewStillImageSize.uxc` | 2 KB | data | UI 资源：viewStillImageSize.uxc：视图/资源文件 | - |
| `viewStlrec.uxc` | 30 KB | data | UI 资源：viewStlrec.uxc：视图/资源文件 | - |
| `viewTcPreset.uxc` | 936 B | data | UI 资源：viewTcPreset.uxc：视图/资源文件 | - |
| `viewTcUbReset.uxc` | 196 B | data | UI 资源：viewTcUbReset.uxc：视图/资源文件 | - |
| `viewTriDial.uxc` | 3 KB | data | UI 资源：viewTriDial.uxc：视图/资源文件 | - |
| `viewUbPreset.uxc` | 644 B | data | UI 资源：viewUbPreset.uxc：视图/资源文件 | - |
| `viewUpdateRootCertificate.uxc` | 1 KB | data | UI 资源：viewUpdateRootCertificate.uxc：视图/资源文件 | - |
| `viewUsbAuto.uxc` | 5 KB | data | UI 资源：viewUsbAuto.uxc：视图/资源文件 | - |
| `viewUsbMTP.uxc` | 5 KB | data | UI 资源：viewUsbMTP.uxc：视图/资源文件 | - |
| `viewUsbMassStorage.uxc` | 5 KB | data | UI 资源：viewUsbMassStorage.uxc：视图/资源文件 | - |
| `viewUsbRemotePc.uxc` | 772 B | data | UI 资源：viewUsbRemotePc.uxc：视图/资源文件 | - |
| `viewUserUpdate.uxc` | 720 B | data | UI 资源：viewUserUpdate.uxc：视图/资源文件 | - |
| `viewVersionNumber.uxc` | 2 KB | data | UI 资源：viewVersionNumber.uxc：视图/资源文件 | - |
| `viewViewOnTVForConnect.uxc` | 2 KB | data | UI 资源：viewViewOnTVForConnect.uxc：视图/资源文件 | - |
| `viewViewOnTVForSinglePb.uxc` | 2 KB | data | UI 资源：viewViewOnTVForSinglePb.uxc：视图/资源文件 | - |
| `viewViewOnTVForSlideShow.uxc` | 2 KB | data | UI 资源：viewViewOnTVForSlideShow.uxc：视图/资源文件 | - |
| `viewViewOnTVForSlideShowSetting.uxc` | 2 KB | data | UI 资源：viewViewOnTVForSlideShowSetting.uxc：视图/资源文件 | - |
| `viewVolume.uxc` | 556 B | data | UI 资源：viewVolume.uxc：视图/资源文件 | - |
| `viewWaterProof.uxc` | 1 KB | data | UI 资源：viewWaterProof.uxc：视图/资源文件 | - |
| `viewWhiteBalance.uxc` | 7 KB | data | UI 资源：viewWhiteBalance.uxc：视图/资源文件 | - |
| `viewWidgetTest.uxc` | 120 B | data | UI 资源：viewWidgetTest.uxc：视图/资源文件 | - |
| `viewWiredLanSetting.uxc` | 5 KB | data | UI 资源：viewWiredLanSetting.uxc：视图/资源文件 | - |
| `viewWlanTest.uxc` | 2 KB | data | UI 资源：viewWlanTest.uxc：视图/资源文件 | - |
| `viewZoomAssist.uxc` | 3 KB | data | UI 资源：viewZoomAssist.uxc：视图/资源文件 | - |
| `viewZoomPb.uxc` | 3 KB | data | UI 资源：viewZoomPb.uxc：视图/资源文件 | - |
| `viewmovierecpatch.uxc` | 41 KB | data | UI 资源：viewmovierecpatch.uxc：视图/资源文件 | - |
| `viewresetRegisteredAfFrame.uxc` | 1 KB | data | UI 资源：viewresetRegisteredAfFrame.uxc：视图/资源文件 | - |

### `/usr/share/aveffect`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `filmSingle_mv.jpg` | 26 KB | data | 图像资源：效果/滤镜参数 | - |
| `film_bg2.jpg` | 35 KB | data | 图像资源：效果/滤镜参数 | - |
| `rotate_back_ground_movie.jpg` | 33 KB | data | 图像资源：效果/滤镜参数 | - |
| `rotate_back_ground_mv.jpg` | 34 KB | data | 图像资源：效果/滤镜参数 | - |

### `/usr/share/avsystemsound`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `Dslr_Emnt_High_10FPS_Kasha.bin` | 3 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_Back_Cancel.bin` | 2 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_Caution.bin` | 8 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_FocusLock.bin` | 4 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_Menu_Close_Option_Off.bin` | 2 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_Menu_Open_Option_On.bin` | 2 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_Move_Down_Wheel_Down.bin` | 1 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_Move_Up_Wheel_Up.bin` | 896 B | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_Rec_Start.bin` | 3 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_Rec_Stop.bin` | 9 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_Select_SwitchMode.bin` | 2 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_SelfTimer_2sec.bin` | 3 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_SelfTimer_RemoteRelease.bin` | 3 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_Shutter_Burst.bin` | 3 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_Shutter_Ka.bin` | 256 B | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_Shutter_Sha.bin` | 3 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_T_Back_Cancel.bin` | 2 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_T_Menu_Close.bin` | 2 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_T_Menu_Open.bin` | 2 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_T_Move_Down.bin` | 1 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_T_Move_Up.bin` | 896 B | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_T_Off.bin` | 2 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_T_On.bin` | 1 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_T_Select.bin` | 2 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_T_Touch.bin` | 1 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_WPS_Connect.bin` | 24 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_WPS_PBC.bin` | 29 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_WPS_Push.bin` | 18 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_Wifi_Toggle.bin` | 7 KB | data | 声音资源：系统提示音 | - |
| `Dslr_Emnt_High_Wifi_Toggle_Off.bin` | 10 KB | data | 声音资源：系统提示音 | - |
| `beeplist.txt` | 5 KB | data | 声音资源：系统提示音 | - |

### `/usr/share/data`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `kikilog_pub.pem` | 625 B | data | 数据资源：通用数据 | - |

### `/usr/share/network/cert`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `certification.pem` | 256 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |

### `/usr/share/network/dlna`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `CdsDesc.xml` | 5 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `CmsDesc.xml` | 4 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `DLNA_camera_120.jpg` | 7 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `DLNA_camera_120.png` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `DLNA_camera_48.jpg` | 5 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `DLNA_camera_48.png` | 2 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `DmsDesc.xml` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `DmsDescInternal.xml` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `DmsDescPush.xml` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `DmsDescPushInternal.xml` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `DmsDescVideoRoot.xml` | 2 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `DmsRmtDesc.xml` | 5 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `ScalarWebApiDesc.xml` | 353 B | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `XPlsDesc.xml` | 2 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |

### `/usr/share/network/mtp`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `ServiceDescription.xml` | 340 B | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |

### `/usr/share/network/nvram/high`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `bcm4339_H_01.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_H_02.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_H_03.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_H_04.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_H_05.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_H_06.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_H_07.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_H_08.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_H_09.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_H_10.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_H_11.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_H_12.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_H_13.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_H_14.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_H_15.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |

### `/usr/share/network/nvram/low`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `bcm4339_L_01.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_L_02.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_L_03.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_L_04.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_L_05.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_L_06.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_L_07.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_L_08.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_L_09.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_L_10.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_L_11.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_L_12.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_L_13.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_L_14.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |
| `bcm4339_L_15.txt` | 3 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |

### `/usr/share/network/remotecontrol`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `index.html` | 966 B | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |

### `/usr/share/network/remotecontrol/orbjs/dist`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `orb-client.min.js` | 10 KB | data | 网络资源：证书/DLNA/MTP/NVRAM/遥控 | - |

### `/usr/share/pmbp`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `DeviceInfo.xml` | 517 B | data | PMBP：PMBP 资源 | - |

### `/usr/share/startbinary`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `logo.bin` | 8 KB | data | 启动资源：开机启动二进制/数据 | - |

### `/usr/share/terminfo/l`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `linux` | 2 KB | data | 终端：terminfo 数据库 | - |

### `/usr/tool`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `LeakCheck` | 689 B | script | 调试工具：泄漏检查/jemalloc | - |
| `LeakTracer.so` | 30 KB | elf | 调试工具：泄漏检查/jemalloc | - |
| `libjemalloc.so` | 113 KB | symlink | 符号链接：指向 libjemalloc_tsh.so.1 | - |
| `libjemalloc_tsh.so` | 113 KB | symlink | 符号链接：指向 libjemalloc_tsh.so.1 | - |
| `libjemalloc_tsh.so.1` | 113 KB | elf | 调试工具：泄漏检查/jemalloc | - |

### `/usr/wifi-scripts`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `cli.sh` | 92 B | script | Wi-Fi 脚本：Wi-Fi 加载/连接脚本 | - |
| `cli_p2p0.sh` | 125 B | script | Wi-Fi 脚本：Wi-Fi 加载/连接脚本 | - |
| `cli_wlan0.sh` | 126 B | script | Wi-Fi 脚本：Wi-Fi 加载/连接脚本 | - |
| `load_firm.sh` | 588 B | script | Wi-Fi 脚本：Wi-Fi 加载/连接脚本 | - |
| `run_single_p2p.sh` | 940 B | script | Wi-Fi 脚本：Wi-Fi 加载/连接脚本 | - |
| `run_supplicant.sh` | 925 B | script | Wi-Fi 脚本：Wi-Fi 加载/连接脚本 | - |
| `set_gpio.sh` | 2 KB | script | Wi-Fi 脚本：Wi-Fi 加载/连接脚本 | - |
| `setwifi.sh` | 1 KB | script | Wi-Fi 脚本：Wi-Fi 加载/连接脚本 | - |
| `start_dhd.sh` | 2 KB | script | Wi-Fi 脚本：Wi-Fi 加载/连接脚本 | - |
| `stop_dhd.sh` | 2 KB | script | Wi-Fi 脚本：Wi-Fi 加载/连接脚本 | - |
| `ulset.sh` | 2 KB | script | Wi-Fi 脚本：Wi-Fi 加载/连接脚本 | - |
| `wifi-test.sh` | 4 KB | script | Wi-Fi 脚本：Wi-Fi 加载/连接脚本 | - |

### `/usr/wlan/bcm`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `bcm4339.bin` | 551 KB | data | Wi-Fi 固件：Broadcom Wi-Fi 固件/NVRAM | - |
| `bcm4339_mfg.bin` | 540 KB | data | Wi-Fi 固件：Broadcom Wi-Fi 固件/NVRAM | - |

## nflasha18（/lens：镜头/像差数据）

### `/lens`

| 文件 | 大小 | 类型 | 作用 | 动态使用 |
|---|---:|---|---|---|
| `VX8900_lensfile.bin` | 3 KB | data | 镜头数据：VX8900_lensfile.bin：镜头/像差数据 | - |
| `VX8901_lensfile.bin` | 3 KB | data | 镜头数据：VX8901_lensfile.bin：镜头/像差数据 | - |
| `VX8902_lensfile.bin` | 3 KB | data | 镜头数据：VX8902_lensfile.bin：镜头/像差数据 | - |
| `VX8903_lensfile.bin` | 6 KB | data | 镜头数据：VX8903_lensfile.bin：镜头/像差数据 | - |
| `VX8904_lensfile.bin` | 4 KB | data | 镜头数据：VX8904_lensfile.bin：镜头/像差数据 | - |
| `VX89058924_lensfile.bin` | 3 KB | data | 镜头数据：VX89058924_lensfile.bin：镜头/像差数据 | - |
| `VX8905_lensfile.bin` | 5 KB | data | 镜头数据：VX8905_lensfile.bin：镜头/像差数据 | - |
| `VX8906_lensfile.bin` | 6 KB | data | 镜头数据：VX8906_lensfile.bin：镜头/像差数据 | - |
| `VX89138924_lensfile.bin` | 4 KB | data | 镜头数据：VX89138924_lensfile.bin：镜头/像差数据 | - |
| `VX89138925_lensfile.bin` | 4 KB | data | 镜头数据：VX89138925_lensfile.bin：镜头/像差数据 | - |
| `VX8913_lensfile.bin` | 7 KB | data | 镜头数据：VX8913_lensfile.bin：镜头/像差数据 | - |
| `VX8915_lensfile.bin` | 3 KB | data | 镜头数据：VX8915_lensfile.bin：镜头/像差数据 | - |
| `VX89168924_lensfile.bin` | 2 KB | data | 镜头数据：VX89168924_lensfile.bin：镜头/像差数据 | - |
| `VX89168925_lensfile.bin` | 2 KB | data | 镜头数据：VX89168925_lensfile.bin：镜头/像差数据 | - |
| `VX8916_lensfile.bin` | 2 KB | data | 镜头数据：VX8916_lensfile.bin：镜头/像差数据 | - |
| `VX8922_lensfile.bin` | 5 KB | data | 镜头数据：VX8922_lensfile.bin：镜头/像差数据 | - |
| `VX8923_lensfile.bin` | 4 KB | data | 镜头数据：VX8923_lensfile.bin：镜头/像差数据 | - |
| `VX8928_lensfile.bin` | 5 KB | data | 镜头数据：VX8928_lensfile.bin：镜头/像差数据 | - |
| `VX8932_lensfile.bin` | 2 KB | data | 镜头数据：VX8932_lensfile.bin：镜头/像差数据 | - |
| `VX8935_lensfile.bin` | 2 KB | data | 镜头数据：VX8935_lensfile.bin：镜头/像差数据 | - |
| `VX8936_lensfile.bin` | 8 KB | data | 镜头数据：VX8936_lensfile.bin：镜头/像差数据 | - |
| `VX8937_lensfile.bin` | 3 KB | data | 镜头数据：VX8937_lensfile.bin：镜头/像差数据 | - |
| `VX8938_lensfile.bin` | 3 KB | data | 镜头数据：VX8938_lensfile.bin：镜头/像差数据 | - |
| `VX8942_lensfile.bin` | 6 KB | data | 镜头数据：VX8942_lensfile.bin：镜头/像差数据 | - |
| `VX89438924_lensfile.bin` | 1 KB | data | 镜头数据：VX89438924_lensfile.bin：镜头/像差数据 | - |
| `VX89438925_lensfile.bin` | 1 KB | data | 镜头数据：VX89438925_lensfile.bin：镜头/像差数据 | - |
| `VX8943_lensfile.bin` | 2 KB | data | 镜头数据：VX8943_lensfile.bin：镜头/像差数据 | - |
| `VX8944_lensfile.bin` | 3 KB | data | 镜头数据：VX8944_lensfile.bin：镜头/像差数据 | - |
| `VX8945_lensfile.bin` | 2 KB | data | 镜头数据：VX8945_lensfile.bin：镜头/像差数据 | - |
| `VX8946_lensfile.bin` | 6 KB | data | 镜头数据：VX8946_lensfile.bin：镜头/像差数据 | - |
| `VX8948_lensfile.bin` | 6 KB | data | 镜头数据：VX8948_lensfile.bin：镜头/像差数据 | - |
| `VX8949_lensfile.bin` | 3 KB | data | 镜头数据：VX8949_lensfile.bin：镜头/像差数据 | - |
| `VX9101_lensfile.bin` | 6 KB | data | 镜头数据：VX9101_lensfile.bin：镜头/像差数据 | - |
| `VX9102_lensfile.bin` | 5 KB | data | 镜头数据：VX9102_lensfile.bin：镜头/像差数据 | - |
| `VX9103_lensfile.bin` | 13 KB | data | 镜头数据：VX9103_lensfile.bin：镜头/像差数据 | - |
| `VX9104_lensfile.bin` | 2 KB | data | 镜头数据：VX9104_lensfile.bin：镜头/像差数据 | - |
| `VX9105_lensfile.bin` | 3 KB | data | 镜头数据：VX9105_lensfile.bin：镜头/像差数据 | - |
| `VX9106_lensfile.bin` | 3 KB | data | 镜头数据：VX9106_lensfile.bin：镜头/像差数据 | - |
| `VX9107_lensfile.bin` | 5 KB | data | 镜头数据：VX9107_lensfile.bin：镜头/像差数据 | - |
| `VX9108_lensfile.bin` | 2 KB | data | 镜头数据：VX9108_lensfile.bin：镜头/像差数据 | - |
| `VX9109_lensfile.bin` | 7 KB | data | 镜头数据：VX9109_lensfile.bin：镜头/像差数据 | - |
| `VX9110_lensfile.bin` | 2 KB | data | 镜头数据：VX9110_lensfile.bin：镜头/像差数据 | - |
| `VX9111_lensfile.bin` | 6 KB | data | 镜头数据：VX9111_lensfile.bin：镜头/像差数据 | - |
| `VX9113_lensfile.bin` | 9 KB | data | 镜头数据：VX9113_lensfile.bin：镜头/像差数据 | - |
| `VX9114_lensfile.bin` | 2 KB | data | 镜头数据：VX9114_lensfile.bin：镜头/像差数据 | - |
| `VX9115_lensfile.bin` | 3 KB | data | 镜头数据：VX9115_lensfile.bin：镜头/像差数据 | - |
| `VX9116_lensfile.bin` | 12 KB | data | 镜头数据：VX9116_lensfile.bin：镜头/像差数据 | - |
| `VX9123_lensfile.bin` | 13 KB | data | 镜头数据：VX9123_lensfile.bin：镜头/像差数据 | - |
| `VX9124_lensfile.bin` | 3 KB | data | 镜头数据：VX9124_lensfile.bin：镜头/像差数据 | - |
| `VX9129_lensfile.bin` | 12 KB | data | 镜头数据：VX9129_lensfile.bin：镜头/像差数据 | - |
| `VX9200_lensfile.bin` | 9 KB | data | 镜头数据：VX9200_lensfile.bin：镜头/像差数据 | - |
| `VX92018924_lensfile.bin` | 5 KB | data | 镜头数据：VX92018924_lensfile.bin：镜头/像差数据 | - |
| `VX92018925_lensfile.bin` | 4 KB | data | 镜头数据：VX92018925_lensfile.bin：镜头/像差数据 | - |
| `VX9201_lensfile.bin` | 7 KB | data | 镜头数据：VX9201_lensfile.bin：镜头/像差数据 | - |
| `VX92028924_lensfile.bin` | 2 KB | data | 镜头数据：VX92028924_lensfile.bin：镜头/像差数据 | - |
| `VX92028925_lensfile.bin` | 2 KB | data | 镜头数据：VX92028925_lensfile.bin：镜头/像差数据 | - |
| `VX9202_lensfile.bin` | 2 KB | data | 镜头数据：VX9202_lensfile.bin：镜头/像差数据 | - |

## 运行时生成/修改的文件（静态转储中不存在）

| 文件 | 大小 | 作用 | 动态使用 |
|---|---:|---|---|
| `/etc/ld.so.preload` | 16 B | 启动时写入，内容为 `/etc/shim_io.so` | - |
| `/etc/shim_io.so` | 39 KB | Sony I/O shim/兼容层，被所有用户态进程预加载 | ash, bootin.elf, im.elf, launch_shell.el, sen.elf |

