#!/usr/bin/env python3
"""Build a file inventory + ELF dependency graph for the A7M3 firmware.

Reads the partitions extracted under /home/derek/a7m3-* and writes:
  data/files.tsv   partition path size kind type role summary
  data/deps.tsv    elf_path -> needed_library
  data/elf.tsv     elf_path type machine soname needed_count
"""
import os
import struct
import subprocess
import sys

ROOT = "/mnt/f/a7c2-re-main/a7m3/A7M3-System-Analysis"
DATA = os.path.join(ROOT, "data")

TREES = [
    ("/", "/home/derek/a7m3-rootfs"),
    ("/usr", "/home/derek/a7m3-usr"),
    ("/etc", "/home/derek/a7m3-fat10"),
    ("/system", "/home/derek/a7m3-fat3"),
    ("/setting", "/home/derek/a7m3-fat2"),
    ("/lens", "/home/derek/a7m3-fat18"),
]

KEY_FILES = {
    "bin/busybox": ("核心工具", "BusyBox 多合一二进制，提供 sh/ls/mount/insmod 等"),
    "bin/cat": ("基础命令", "cat：查看/拼接文件"),
    "bin/chattr": ("文件属性", "chattr：修改 ext2 文件属性"),
    "bin/lsattr": ("文件属性", "lsattr：查看 ext2 文件属性"),
    "bin/compile_et": ("开发工具", "Kerberos error-table 编译脚本"),
    "bin/mk_cmds": ("开发工具", "生成命令表脚本"),
    "bin/ps": ("进程工具", "procps：进程列表"),
    "bin/top": ("进程工具", "procps：实时进程/负载"),
    "bin/vmstat": ("进程工具", "procps：虚拟内存统计"),
    "bin/hostname": ("主机名工具", "设置/显示主机名"),
    "bin/dnsdomainname": ("主机名工具", "显示 DNS 域名"),
    "sbin/init": ("初始化", "PID 1：解析 cmdline/环境、挂载 nflasha、insmod、启动后台服务"),
    "sbin/dosfsck": ("文件系统工具", "FAT 文件系统检查/修复"),
    "sbin/mkdosfs": ("文件系统工具", "创建 FAT 文件系统"),
    "sbin/sysctl": ("内核参数工具", "读写 /proc/sys"),
    "root/common.src": ("升级脚本库", "FIRMUP/updater 的通用变量与函数（mount、错误码、LED）"),
    "usr/bin/im.elf": ("应用框架启动器", "Appframework 入口：libIMDB/libosal/backup，dlopen 场景与视图"),
    "usr/bin/scenario.elf": ("场景命令入口", "解析 name:size:data，dlopen /usr/scenario/*.so 并调用 scenario_run"),
    "usr/bin/sen.elf": ("传感器服务", "Senser/传感器相关用户态服务"),
    "usr/bin/adjstctl.elf": ("调整控制", "镜头/传感器调整控制"),
    "usr/bin/testcmd.elf": ("测试命令", "工厂/测试命令分发"),
    "usr/bin/rcvcmd.elf": ("命令接收", "接收并分发命令"),
    "usr/bin/sndcmd.elf": ("命令发送", "发送命令到服务"),
    "usr/bin/ulogio.elf": ("日志 IO", "用户态日志读写"),
    "usr/bin/ujlog.elf": ("日志", "ujlog 日志工具"),
    "usr/bin/mpr_monio.elf": ("监控", "MPR 消息/状态监控"),
    "usr/bin/mwf_monio.elf": ("监控", "MWF 消息/状态监控"),
    "usr/bin/mpr_viewLog.elf": ("日志查看", "查看 MPR 日志"),
    "usr/bin/netblog.elf": ("网络日志", "网络日志服务"),
    "usr/bin/btblog.elf": ("蓝牙日志", "蓝牙日志服务"),
    "usr/bin/crypter.elf": ("加解密", "固件/数据加解密工具"),
    "usr/bin/bootin.elf": ("启动信息", "启动参数/启动信息处理"),
    "usr/bin/bk.elf": ("备份", "备份/恢复相关"),
    "usr/bin/launch_shell.elf": ("调试 shell", "启动调试 shell（launch_shell）"),
    "usr/bin/gpioctrl.elf": ("GPIO", "GPIO 控制"),
    "usr/bin/SetPort.elf": ("端口", "端口/GPIO 设置"),
    "usr/bin/GPIO2SDIO.elf": ("GPIO/SDIO", "GPIO 切到 SDIO 模式"),
    "usr/bin/SDIO2GPIO.elf": ("GPIO/SDIO", "SDIO 切回 GPIO"),
    "usr/bin/NsBkSet.elf": ("备份设置", "备份相关设置"),
    "usr/bin/bsa_server": ("蓝牙", "Broadcom BSA 蓝牙协议栈服务"),
    "usr/bin/orb-server": ("BT/网络服务", "ORB 服务（蓝牙/网络相关）"),
    "usr/bin/dhd": ("Wi-Fi", "Broadcom dhd Wi-Fi 驱动用户态"),
    "usr/bin/wl": ("Wi-Fi", "Broadcom wl 工具"),
    "usr/bin/wpa_supplicant": ("Wi-Fi", "WPA  supplicant"),
    "usr/bin/dhcpd": ("网络", "DHCP 服务"),
    "usr/bin/pump": ("网络", "DHCP 客户端"),
    "usr/bin/iptables-multi": ("网络", "iptables 多合一"),
    "usr/bin/tcpdump": ("网络", "抓包工具"),
    "usr/bin/openssl": ("密码学", "OpenSSL 命令行"),
    "usr/bin/iperf": ("网络测试", "iperf 带宽测试"),
    "usr/bin/soundstretch": ("音频", "音频变速/变调"),
    "usr/bin/uuidgen": ("系统工具", "生成 UUID"),
    "usr/bin/Wltestcmd": ("Wi-Fi 测试", "无线测试命令"),
    "usr/bin/btRFTest.elf": ("蓝牙测试", "蓝牙 RF 测试"),
    "usr/bin/up.sh": ("升级脚本", "切换 updater 模式（UFP/version skip/MS crypt）"),
    "usr/bin/change_mode.sh": ("模式脚本", "切换启动/升级模式"),
    "usr/bin/appdbglv.sh": ("调试脚本", "设置应用调试等级"),
    "usr/bin/startBTCore.sh": ("蓝牙脚本", "启动蓝牙 core"),
    "usr/bin/WebApiLauncher.sh": ("Web API", "启动 Web API 服务"),
    "usr/bin/compat_firmware.sh": ("兼容脚本", "固件兼容处理"),
    "usr/bin/swap_prepare.sh": ("内存脚本", "准备 swap"),
    "usr/bin/usb_insmod.sh": ("USB 脚本", "加载 USB 相关模块"),
    "usr/lib/libObj.so": ("应用对象框架", "libObj：Appframework 对象/视图/场景核心（最大库）"),
    "usr/lib/libmpr.so": ("MPR 中间件", "MPR（Camera Middleware）核心"),
    "usr/lib/libmprctrl.so": ("MPR 控制", "MPR 控制/命令接口"),
    "usr/lib/libJiritsu.so": ("JIRITSU", "JIRITSU 服务协议（文件/升级/调试/工厂）"),
    "usr/lib/libSysDef.so": ("系统定义", "系统常量/型号/区域定义"),
    "usr/lib/libInfraMakeScenario.so": ("场景框架", "Infra 场景注册/加载框架"),
    "usr/lib/libNetService.so": ("网络服务", "网络服务框架"),
    "usr/lib/libMWF.so": ("MWF", "MWF 中间件"),
    "usr/lib/libcrypto.so.3": ("密码学", "OpenSSL libcrypto"),
    "usr/lib/libssl.so.3": ("TLS", "OpenSSL libssl"),
    "usr/lib/libcurl.so.4.8.0": ("HTTP", "libcurl"),
    "usr/lib/libpcap.so.1.0.0": ("抓包", "libpcap"),
    "usr/lib/libblkid.so.1.1.0": ("块设备", "块设备识别"),
    "system/av-cam.bin": ("LIRO 固件", "LIRO 相机固件，QEMU 可预加载到 0x035c6000"),
    "system/initrd.img": ("initrd", "启动 initrd（ext2），含模块加载/备份逻辑"),
    "system/vmlinux.bin": ("内核镜像", "Linux 3.0.27 zImage"),
    "system/bonobo.bin": ("启动数据", "Bonobo 启动/传感器数据"),
    "system/dfe_app.bin": ("DFE 应用", "DFE 图像处理应用固件"),
    "system/dfe_dat.bin": ("DFE 数据", "DFE 配置/数据"),
    "system/ldr_drv.bin": ("LIRO loader", "LIRO 驱动加载器"),
    "system/lif_app.bin": ("LIF 应用", "LIF 应用固件"),
    "system/lensbin_lensproperty/LensAberrationData.bin": ("镜头像差", "镜头像差/校正数据"),
    "setting/kemco.txt": ("内存地图", "主内核 memrsv/内存保留区参数"),
    "setting/Backup.bin": ("备份", "设置备份"),
    "setting/Backup.bak": ("备份", "设置备份（旧）"),
    "setting/DmmConfig.bin": ("DMM 配置", "显示内存管理配置"),
    "setting/.hasp": ("Senser 许可", "Senser/HASP 认证数据"),
    "setting/.etools": ("工厂工具标记", "工厂/调试工具标记"),
    "setting/psd.bin": ("PSD 数据", "画质/传感器校准数据"),
    "setting/ulogio.bin": ("日志缓冲", "用户态日志缓冲"),
    "etc/config.spec": ("系统配置", "型号/区域/规格配置"),
    "etc/dhcpd.conf": ("DHCP", "DHCP 服务配置"),
    "etc/services": ("服务表", "TCP/UDP 服务名表"),
    "etc/protocols": ("协议表", "IP 协议名表"),
    "etc/resolv.conf": ("DNS", "DNS 配置"),
    "etc/nsswitch.conf": ("NSS", "名称解析顺序"),
    "etc/toprc": ("top", "top 配置"),
    "etc/uipc_stat_kernel.txt": ("UIPC", "UIPC 内核统计/配置"),
    "etc/kikilog.dat": ("日志", "kikilog 日志数据"),
    "usr/kmod/grm_gles.ko": ("GPU 驱动", "Sugilite GLES 驱动"),
    "usr/kmod/grm_ma.ko": ("媒体加速", "Sugilite 媒体加速"),
    "usr/kmod/dmm.ko": ("显示内存", "显示内存管理"),
    "usr/kmod/dma330.ko": ("DMA", "DMA330 引擎"),
    "usr/kmod/accel.ko": ("加速器", "图像/媒体加速器"),
    "usr/kmod/upm.ko": ("统一电源/内存", "UPM 驱动"),
    "usr/kmod/udate.ko": ("升级", "固件升级辅助"),
    "usr/kmod/backup.ko": ("备份", "备份/恢复驱动"),
    "usr/kmod/codec_drv.ko": ("编解码", "编解码器驱动"),
    "usr/kmod/stream.ko": ("视频流", "视频流驱动"),
    "usr/kmod/stream2.ko": ("视频流", "第二视频流驱动"),
    "usr/lib/libtestcmd.so": ("测试命令框架", "testcmd_* / scenario 插件加载"),
    "usr/lib/libIMDB.so": ("消息数据库", "IMDB 内部消息数据库"),
    "usr/lib/libosal_uipc.so": ("用户态 IPC", "消息队列/同步/线程"),
    "usr/lib/libosal_utm.so": ("用户态定时器", "定时器/线程管理"),
    "usr/lib/libSTMcmdexecute.so": ("STM 命令", "系统控制命令执行"),
    "usr/lib/libsencore.so": ("Senser 核心", "传感器核心库"),
    "usr/lib/libclema.so": ("Clema", "媒体/图像处理库"),
}

DIR_ROLES = [
    ("/usr/share/app/", ("UI 资源", "应用/视图资源")),
    ("/usr/share/aveffect/", ("图像资源", "效果/滤镜参数")),
    ("/usr/share/avsystemsound/", ("声音资源", "系统提示音")),
    ("/usr/share/data/", ("数据资源", "通用数据")),
    ("/usr/share/network/", ("网络资源", "证书/DLNA/MTP/NVRAM/遥控")),
    ("/usr/share/pmbp/", ("PMBP", "PMBP 资源")),
    ("/usr/share/startbinary/", ("启动资源", "开机启动二进制/数据")),
    ("/usr/share/terminfo/", ("终端", "terminfo 数据库")),
    ("/usr/sabin/", ("DSP 固件", "图像/音频/JPEG 等加速器固件数据")),
    ("/usr/codec/", ("编解码固件", "BNI/BNL/VCD 编解码器固件")),
    ("/usr/wlan/", ("Wi-Fi 固件", "Broadcom Wi-Fi 固件/NVRAM")),
    ("/usr/wifi-scripts/", ("Wi-Fi 脚本", "Wi-Fi 加载/连接脚本")),
    ("/usr/tool/", ("调试工具", "泄漏检查/jemalloc")),
    ("/usr/scenario/", ("场景模块", "scenario.elf 动态加载的命令模块")),
    ("/usr/kmod/", ("内核模块", "相机/存储/显示相关 ko")),
    ("/usr/lib/", ("共享库", "用户态共享库")),
    ("/usr/share/", ("资源", "只读资源")),
    ("/usr/bin/", ("用户态程序", "服务/工具/脚本")),
    ("/usr/sbin/", ("系统管理", "网络/管理工具")),
]


def is_elf(path):
    try:
        with open(path, "rb") as f:
            return f.read(4) == b"\x7fELF"
    except OSError:
        return False


def elf_info(path):
    info = {"type": "", "machine": "", "soname": "", "needed": []}
    try:
        h = subprocess.run(["readelf", "-h", path], capture_output=True,
                           text=True, timeout=10).stdout
        for line in h.splitlines():
            line = line.strip()
            if line.startswith("Type:"):
                info["type"] = line.split(":", 1)[1].strip()
            elif line.startswith("Machine:"):
                info["machine"] = line.split(":", 1)[1].strip()
        d = subprocess.run(["readelf", "-d", path], capture_output=True,
                           text=True, timeout=10).stdout
        for line in d.splitlines():
            s = line.strip()
            if "(NEEDED)" in s and "[" in s:
                info["needed"].append(s.split("[", 1)[1].split("]", 1)[0])
            elif "(SONAME)" in s and "[" in s:
                info["soname"] = s.split("[", 1)[1].split("]", 1)[0]
    except Exception:
        pass
    return info


def file_type(path):
    try:
        return subprocess.run(["file", "-b", path], capture_output=True,
                              text=True, timeout=10).stdout.strip()
    except Exception:
        return ""


def classify(rel, ftype, elf):
    base = os.path.basename(rel)
    key = rel.lstrip("/")
    if key in KEY_FILES:
        return KEY_FILES[key]
    for prefix, role in DIR_ROLES:
        if rel.startswith(prefix):
            if prefix == "/usr/lib/" and base.startswith("viewUnified"):
                return ("UI 视图库", "viewUnified：Sugilite 菜单视图/绘制")
            if prefix == "/usr/scenario/":
                return ("场景模块", "%s：scenario 命令实现" % base)
            if prefix == "/usr/kmod/":
                return ("内核模块", "%s：内核驱动" % base)
            if prefix == "/usr/sabin/":
                return ("DSP 固件", "%s：加速器/编码固件数据" % base)
            if prefix == "/usr/share/app/":
                return ("UI 资源", "%s：视图/资源文件" % base)
            return role
    if rel.startswith("/bin/") or rel.startswith("/sbin/"):
        return ("核心工具", "BusyBox 命令/系统工具")
    if rel.startswith("/lib/"):
        return ("运行时库", "glibc/系统库")
    if rel.startswith("/kmod/"):
        return ("内核模块", "%s：内核驱动" % base)
    if rel.startswith("/etc/"):
        return ("运行时配置", "%s：配置/数据" % base)
    if rel.startswith("/system/"):
        return ("启动/传感器数据", "%s：启动镜像或传感器数据" % base)
    if rel.startswith("/setting/"):
        return ("私有设置", "%s：设置/备份数据" % base)
    if rel.startswith("/lens/"):
        return ("镜头数据", "%s：镜头/像差数据" % base)
    if ftype.startswith("ELF"):
        return ("ELF 文件", base)
    if ftype.startswith("POSIX shell") or ftype.startswith("Bourne"):
        return ("脚本", base)
    return ("数据/其他", base)


def main():
    os.makedirs(DATA, exist_ok=True)
    files = []
    deps = []
    elfs = []
    for label, root in TREES:
        for dirpath, _, names in os.walk(root):
            for n in names:
                p = os.path.join(dirpath, n)
                if os.path.islink(p) and not os.path.exists(p):
                    continue
                rel = os.path.relpath(p, root)
                if rel == ".":
                    continue
                rel = "/" + rel if label == "/" else label + "/" + rel
                rel = rel.replace("//", "/")
                try:
                    size = os.path.getsize(p)
                except OSError:
                    continue
                ftype = ""
                kind = "data"
                if os.path.islink(p):
                    kind = "symlink"
                    target = os.readlink(p)
                    ftype = "symlink -> %s" % target
                    if "busybox" in target:
                        role, summary = ("BusyBox 链接", "指向 busybox 的命令别名")
                    else:
                        role, summary = ("符号链接", "指向 %s" % target)
                    files.append((label, rel, size, kind, ftype, role, summary))
                    continue
                if is_elf(p):
                    kind = "elf"
                    info = elf_info(p)
                    ftype = "ELF %s %s" % (info["type"], info["machine"])
                    elfs.append((rel, info["type"], info["machine"],
                                 info["soname"], len(info["needed"])))
                    for lib in info["needed"]:
                        deps.append((rel, lib))
                else:
                    ftype = file_type(p)
                    if "shell script" in ftype or "ASCII text" in ftype and p.endswith(".sh"):
                        kind = "script"
                    elif ftype.startswith("ELF"):
                        kind = "elf"
                role, summary = classify(rel, ftype, kind == "elf")
                files.append((label, rel, size, kind, ftype, role, summary))
    with open(os.path.join(DATA, "files.tsv"), "w", encoding="utf-8") as f:
        f.write("partition\tpath\tsize\tkind\ttype\trole\tsummary\n")
        for row in files:
            f.write("\t".join(str(x) for x in row) + "\n")
    with open(os.path.join(DATA, "deps.tsv"), "w", encoding="utf-8") as f:
        f.write("elf\tneeded\n")
        for row in deps:
            f.write("%s\t%s\n" % row)
    with open(os.path.join(DATA, "elf.tsv"), "w", encoding="utf-8") as f:
        f.write("elf\ttype\tmachine\tsoname\tneeded_count\n")
        for row in elfs:
            f.write("\t".join(str(x) for x in row) + "\n")
    print("files", len(files), "deps", len(deps), "elfs", len(elfs))


if __name__ == "__main__":
    main()
