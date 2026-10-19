%global source0_hash 05455baba4bcd3f2e6243aacf2d26f742c22944a29e412d50b89cc73e3028114
%if 0%{?rhel} >= 8 || (0%{?oreon} >= 11)
%bcond_without signzipl
%else
%bcond_with signzipl
%endif
%if 0%{?fedora} || (0%{?oreon} >= 11)
%bcond_without pandoc
%else
%bcond_with pandoc
%endif
%bcond_without check
Name:           s390utils
Summary:        Utilities and daemons for IBM z Systems
Version:        2.44.0
Release:        1%{?dist}
Epoch:          2
%global extra_licenses_from_rust_deps %{shrink:
Apache-2.0 AND
(Apache-2.0 OR BSL-1.0) AND
(Apache-2.0 OR MIT) AND
(Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
(BSD-2-Clause OR Apache-2.0 OR MIT) AND
Unicode-DFS-2016 AND
(Unlicense OR MIT)
}
License:        MIT AND LGPL-2.1-or-later AND %{extra_licenses_from_rust_deps}
URL:            https://github.com/ibm-s390-linux/s390-tools
Source0:        https://github.com/ibm-s390-linux/s390-tools/archive/v%{version}.tar.gz#/s390-tools-%{version}.tar.gz
Source5:        zfcpconf.sh
Source7:        zfcp.udev
Source12:        dasd.udev
Source13:        dasdconf.sh
Source14:        device_cio_free
Source15:        device_cio_free.service
Source16:        ccw_init
Source17:        ccw.udev
Source21:        normalize_dasd_arg
Source23:        20-zipl-kernel.install
Source24:        52-zipl-rescue.install
Source25:        91-zipl.install
%if %{with signzipl}
%define pesign_name redhatsecureboot302
%endif
Patch0:        s390-tools-zipl-invert-script-options.patch
Patch1:        s390-tools-zipl-blscfg-rpm-nvr-sort.patch
ExcludeArch:    %{ix86}
Provides:       s390-tools = %{epoch}:%{version}-%{release}
%ifarch s390x
Requires:       s390utils-core = %{epoch}:%{version}-%{release}
Requires:       s390utils-base = %{epoch}:%{version}-%{release}
Requires:       s390utils-osasnmpd = %{epoch}:%{version}-%{release}
Requires:       s390utils-cpuplugd = %{epoch}:%{version}-%{release}
Requires:       s390utils-mon_statd = %{epoch}:%{version}-%{release}
Requires:       s390utils-iucvterm = %{epoch}:%{version}-%{release}
Requires:       s390utils-ziomon = %{epoch}:%{version}-%{release}
%else
Requires:       s390utils-se-data = %{epoch}:%{version}-%{release}
%endif
%if 0%{?rhel} || (0%{?oreon} >= 11)
%else
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  make
BuildRequires:  rustc
# /oreon:deps
%description
This is a meta package for installing the default s390-tools sub packages.
If you do not need all default sub packages, it is recommended to install the
required sub packages separately.

The s390utils packages contain a set of user space utilities that should to
be used together with the zSeries (s390) Linux kernel and device drivers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n s390-tools-%{version} -p1
%if 0%{?rhel} || (0%{?oreon} >= 11)
_vendor="s390-tools-%{version}-rust-vendor.tar.xz"
if test ! -f "$_vendor"; then
pushd rust
rm -rf vendor
cargo vendor vendor
tar cJf "../$_vendor" vendor
popd
fi
pushd rust
tar xf "../$_vendor"
popd
%else
%endif
rm ./rust/Cargo.lock
echo 'g zkeyadm' > s390utils-base.conf.usr
echo 'g ts-shell' > s390utils-iucvterm.conf.usr
echo 'g cpacfstats' > s390utils-cpacfstatsd.conf.usr
echo 'd /var/log/ts-shell 2770 root ts-shell' > s390utils-iucvterm.conf.tmp
%if !0%{?rhel} || (0%{?oreon} >= 11)
%oreon_vendor_cargo
%build

make \
        CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}" LDFLAGS="%{build_ldflags}" \
        HAVE_DRACUT=1 \
%if %{with pandoc}
        ENABLE_DOC=1 \
%endif
        NO_PIE_LDFLAGS="" \
%if "%{_sbindir}" == "%{_bindir}"
        BINDIR=/usr/bin \
        USRSBINDIR=/usr/bin \
%else
        BINDIR=/usr/sbin \
%endif
        DISTRELEASE=%{release} \
        V=1
pushd rust
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%if 0%{?rhel} || (0%{?oreon} >= 11)
%cargo_vendor_manifest
%endif
popd
%install
%make_install \
        HAVE_DRACUT=1 \
%if %{with pandoc}
        ENABLE_DOC=1 \
%endif
%if "%{_sbindir}" == "%{_bindir}"
        BINDIR=/usr/bin \
        USRSBINDIR=/usr/bin \
%else
        BINDIR=/usr/sbin \
%endif
        SYSTEMDSYSTEMUNITDIR=%{_unitdir} \
        DISTRELEASE=%{release} \
        V=1
%ifarch s390x
%if %{with signzipl}
if [ -x /usr/bin/rpm-sign ]; then
    pushd %{buildroot}/lib/s390-tools/
        rpm-sign --key "%{pesign_name}" --lkmsign stage3.bin --output stage3.signed
        mv stage3.signed stage3.bin
    popd
else
    echo "rpm-sign not available, stage3 won't be signed"
fi
%endif
mv %{buildroot}%{_datadir}/s390-tools/netboot/mk-s390image %{buildroot}%{_bindir}
mv %{buildroot}%{_datadir}/s390-tools/netboot/mk-s390image.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}{/boot,%{_udevrulesdir},%{_sysconfdir}/{profile.d,sysconfig},%{_prefix}/lib/modules-load.d}
install -p -m 644 zipl/boot/tape0.bin %{buildroot}/boot/tape0
install -p -m 755 %{SOURCE5} %{buildroot}%{_sbindir}
install -p -m 755 %{SOURCE13} %{buildroot}%{_sbindir}
install -p -m 755 %{SOURCE21} %{buildroot}%{_sbindir}
install -p -m 644 %{SOURCE7} %{buildroot}%{_udevrulesdir}/56-zfcp.rules
install -p -m 644 %{SOURCE12} %{buildroot}%{_udevrulesdir}/56-dasd.rules
touch %{buildroot}%{_sysconfdir}/{zfcp.conf,dasd.conf}
install -Dp -m 644 etc/udev/rules.d/*.rules %{buildroot}%{_udevrulesdir}
install -Dp -m 644 etc/modules-load.d/*.conf %{buildroot}%{_prefix}/lib/modules-load.d
install -d -m 0755 %{buildroot}%{_prefix}/lib/kernel/install.d/
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ zfcpdump/10-zfcpdump.install
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE23}
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE24}
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE25}
install -d -m 0755 %{buildroot}%{_sysconfdir}/kernel/install.d/
install -m 0644 /dev/null %{buildroot}%{_sysconfdir}/kernel/install.d/20-grubby.install
mkdir -p %{buildroot}%{_includedir}/%{name}
install -p -m 644 include/lib/vtoc.h %{buildroot}%{_includedir}/%{name}
install -p -m 755 %{SOURCE14} %{buildroot}%{_sbindir}
pushd %{buildroot}%{_sbindir}
for lnk in dasd zfcp znet; do
    ln -sf device_cio_free ${lnk}_cio_free
done
popd
install -p -m 644 %{SOURCE15} %{buildroot}%{_unitdir}
install -p -m 755 %{SOURCE16} %{buildroot}/usr/lib/udev/ccw_init
install -p -m 644 %{SOURCE17} %{buildroot}%{_udevrulesdir}/81-ccw.rules
touch %{buildroot}%{_sysconfdir}/zipl.conf
mkdir -p %{buildroot}{%{_sysusersdir},%{_tmpfilesdir}}/
for f in s390utils-*.conf.usr; do
    install -p -m 644 $f %{buildroot}%{_sysusersdir}/$(basename -s .usr $f)
done
for f in s390utils-*.conf.tmp; do
    install -p -m 644 $f %{buildroot}%{_tmpfilesdir}/$(basename -s .tmp $f)
done
%endif
%ifarch s390x
%oreon_autofiles main

%package core
License:        MIT
Summary:        S390 core tools
Provides:       s390-tools-core = %{epoch}:%{version}-%{release}
Requires:       coreutils
Requires:       makedumpfile
%{?systemd_requires}
%description core
This package provides minimal set of tools needed to system to boot.

%post core

%systemd_post device_cio_free.service
%systemd_post cpi.service
%preun core

%systemd_preun device_cio_free.service
%systemd_preun cpi.service
%postun core

%systemd_postun_with_restart cpi.service
%package base
License:        MIT AND LGPL-2.1-or-later AND %{extra_licenses_from_rust_deps}
Summary:        S390 base tools
Provides:       s390-tools-base = %{epoch}:%{version}-%{release}
Requires:       coreutils
Requires:       ethtool
Requires:       file
Requires:       gawk
Requires:       sed
Requires:       sg3_utils
Requires:       tar
Requires:       s390utils-core = %{epoch}:%{version}-%{release}
Requires:       s390utils-se-data = %{epoch}:%{version}-%{release}
%{?systemd_requires}
BuildRequires:  perl-generators
BuildRequires:  ncurses-devel
BuildRequires:  glibc-static
BuildRequires:  cryptsetup-devel >= 2.8.2
BuildRequires:  json-c-devel
BuildRequires:  rpm-devel
BuildRequires:  libxml2-devel
BuildRequires:  libnl3-devel
%description base
s390 base tools. This collection provides the following utilities:
   * dasdfmt:
     Low-level format ECKD DASDs with the classical linux disk layout or the
     new z/OS compatible disk layout.

   * fdasd:
     Create or modify partitions on ECKD DASDs formatted with the z/OS
     compatible disk layout.

   * dasdview:
     Display DASD and VTOC information or dump the contents of a DASD to the
     console.

   * dasdinfo:
     Display unique DASD ID, either UID or volser.

   * udev rules:
     - 59-dasd.rules: rules for unique DASD device nodes created in /dev/disk/.

   * zipl:
     Make DASDs or tapes bootable for system IPL or system dump.

   * zgetdump:
     Retrieve system dumps from either tapes or DASDs.

   * qetharp:
     Read and flush the ARP cache on OSA Express network cards.

   * tape390_display:
     Display information on the message display facility of a zSeries tape
     device.

   * tape390_crypt:
     Control and query crypto settings for 3592 zSeries tape devices.

   * qethconf:
     bash shell script simplifying the usage of qeth IPA (IP address
     takeover), VIPA (Virtual IP address) and Proxy ARP.

   * dbginfo.sh:
     Shell script collecting useful information about the current system for
     debugging purposes.

   * zfcpdump:
     Dump tool to create system dumps on fibre channel attached SCSI disks.
     It is installed using the zipl command.

   * zfcpdump_v2:
     Version 2 of the zfcpdump tool. Now based on the upstream 2.6.26 Linux
     kernel.

   * ip_watcher:
     Provides HiperSockets Network Concentrator functionality.
     It looks for addresses in the HiperSockets and sets them as Proxy ARP
     on the OSA cards. It also adds routing entries for all IP addresses
     configured on active HiperSockets devices.
     Use start_hsnc.sh to start HiperSockets Network Concentrator.

   * tunedasd:
     Adjust tunable parameters on DASD devices.

   * vmcp:
     Allows Linux users to send commands to the z/VM control program (CP).
     The normal usage is to invoke vmcp with the command you want to
     execute. The response of z/VM is written to the standard output.

   * vmur:
     Allows to work with z/VM spool file queues (reader, punch, printer).

   * zfcpdbf:
     Display debug data of zfcp. zfcp provides traces via the s390 debug
     feature. Those traces are filtered with the zfcpdbf script, i.e. merge
     several traces, make it more readable etc.

   * zconf:
     Set of scripts to configure and list status information of Linux for
     zSeries IO devices.
     - chccwdev:   Modify generic attributes of channel attached devices.
     - lscss:      List channel subsystem devices.
     - lsdasd:     List channel attached direct access storage devices (DASD).
     - lsqeth:     List all qeth-based network devices with their corresponding
                   settings.
     - lstape:     List tape devices, both channel and FCP attached.
     - lszfcp:     Shows information contained in sysfs about zfcp adapters,
                   ports and units that are online.
     - lschp:      List information about available channel-paths.
     - chchp:      Modify channel-path state.
     - lsluns:     List available SCSI LUNs depending on adapter or port.
     - lszcrypt:   Show Information about zcrypt devices and configuration.
     - chzcrypt:   Modify zcrypt configuration.
     - znetconf:   List and configure network devices for System z network
                   adapters.
     - cio_ignore: Query and modify the contents of the CIO device driver
                   blacklist.

   * dumpconf:
     Allows to configure the dump device used for system dump in case a kernel
     panic occurs. This tool can also be used as an init script for etc/init.d.
     Prerequisite for dumpconf is a Linux kernel with the "dump on panic"
     feature.

   * ipl_tools:
     Tools set to configure and list reipl and shutdown actions.
     - lsreipl: List information of reipl device.
     - chreipl: Change reipl device settings.
     - lsshut:  List actions which will be done in case of halt, poff, reboot
                or panic.
     - chshut:  Change actions which should be done in case of halt, poff,
                reboot or panic.

   * cpi:
    Allows to set the system and sysplex names from the Linux guest to
    the HMC/SE using the Control Program Identification feature.

   * genprotimg:
    Tool for the creation of PV images. The image consists of a concatenation of
    a plain text boot loader, the encrypted components for kernel, initrd, and
    cmdline, and the integrity-protected PV header, containing metadata necessary for
    running the guest in PV mode. Protected VMs (PVM) are KVM VMs, where KVM can't
    access the VM's state like guest memory and guest registers anymore.

For more information refer to the following publications:
   * "Device Drivers, Features, and Commands" chapter "Useful Linux commands"
   * "Using the dump tools"

%post base

%systemd_post dumpconf.service
%preun base

%systemd_preun dumpconf.service
%postun base

%systemd_postun_with_restart dumpconf.service
%package se-data
License:        MIT
Summary:        Data for Secure Execution
Provides:       s390-tools-se-data = %{epoch}:%{version}-%{release}
BuildArch:      noarch
%description se-data
%{summary}.

%package osasnmpd
Summary:        SNMP sub-agent for OSA-Express cards
Provides:       s390-tools-osasnmpd = %{epoch}:%{version}-%{release}
Requires:       net-snmp
Requires:       psmisc
BuildRequires:  net-snmp-devel
%description osasnmpd
UCD-SNMP/NET-SNMP sub-agent implementing MIBs provided by OSA-Express
features Fast Ethernet, Gigabit Ethernet, High Speed Token Ring and
ATM Ethernet LAN Emulation in QDIO mode.

%package mon_statd
Summary:         Monitoring daemons for Linux in z/VM
Provides:        s390-tools-mon_statd = %{epoch}:%{version}-%{release}
Requires:        coreutils
%{?systemd_requires}
%description mon_statd
Monitoring daemons for Linux in z/VM:

  - mon_fsstatd: Daemon that writes file system utilization data to the
                 z/VM monitor stream.

  - mon_procd:   Daemon that writes process information data to the z/VM
                 monitor stream.

%post mon_statd

%systemd_post mon_fsstatd.service
%systemd_post mon_procd.service
%preun mon_statd

%systemd_preun mon_fsstatd.service
%systemd_preun mon_procd.service
%postun mon_statd

%systemd_postun_with_restart mon_fsstatd.service
%systemd_postun_with_restart mon_procd.service
%package cpuplugd
Summary:         Daemon that manages CPU and memory resources
Provides:        s390-tools-cpuplugd = %{epoch}:%{version}-%{release}
%{?systemd_requires}
BuildRequires: systemd
%description cpuplugd
Daemon that manages CPU and memory resources based on a set of rules.
Depending on the workload CPUs can be enabled or disabled. The amount of
memory can be increased or decreased exploiting the CMM1 feature.

%post cpuplugd

%systemd_post cpuplugd.service
%preun cpuplugd

%systemd_preun cpuplugd.service
%postun cpuplugd

%systemd_postun_with_restart cpuplugd.service
%package ziomon
Summary:        S390 ziomon tools
Provides:       s390-tools-ziomon = %{epoch}:%{version}-%{release}
Requires:       blktrace
Requires:       coreutils
Requires:       device-mapper-multipath
Requires:       gawk
Requires:       grep
Requires:       lsscsi
Requires:       procps-ng
Requires:       rsync
Requires:       sed
Requires:       tar
Requires:       util-linux
%description ziomon
Tool set to collect data for zfcp performance analysis and report.

%package iucvterm
Summary:        z/VM IUCV terminal applications
Provides:       s390-tools-iucvterm = %{epoch}:%{version}-%{release}
Requires(pre):  shadow-utils
Requires(post): grep
Requires(postun): grep
BuildRequires:  gettext
BuildRequires: systemd
%description iucvterm
A set of applications to provide terminal access via the z/VM Inter-User
Communication Vehicle (IUCV). The terminal access does not require an
active TCP/IP connection between two Linux guest operating systems.

- iucvconn:  Application to establish a terminal connection via z/VM IUCV.
- iucvtty:   Application to provide terminal access via z/VM IUCV.
- ts-shell:  Terminal server shell to authorize and control IUCV terminal
             connections for individual Linux users.

%post iucvterm

grep -q '^/usr/bin/ts-shell$' /etc/shells \
    || echo "/usr/bin/ts-shell" >> /etc/shells
%postun iucvterm

if [ $1 = 0 ]
then
    grep -v '^/usr/bin/ts-shell$' /etc/shells > /etc/shells.ts-new
    mv /etc/shells.ts-new /etc/shells
    chmod 0644 /etc/shells
fi
%package cmsfs-fuse
Summary:        CMS file system based on FUSE
BuildRequires:  fuse3-devel
Requires:       fuse3
Provides:       s390-tools-cmsfs-fuse = %{epoch}:%{version}-%{release}
Requires:       glibc-gconv-extra
Obsoletes:      %{name}-cmsfs < 2:2.7.0-3
%description cmsfs-fuse
This package contains the CMS file system based on FUSE.

%package zdsfs
Summary:        z/OS data set access based on FUSE
BuildRequires:  fuse3-devel
BuildRequires:  libcurl-devel
Requires:       fuse3
Provides:       s390-tools-zdsfs = %{epoch}:%{version}-%{release}
%description zdsfs
This package contains the z/OS data set access based on FUSE.

%package hmcdrvfs
Summary:       HMC drive file system based on FUSE
BuildRequires: fuse3-devel
Requires:      fuse3
Provides:      s390-tools-hmcdrvfs = %{epoch}:%{version}-%{release}
%description hmcdrvfs
This package contains a HMC drive file system based on FUSE and a tool
to list files and directories.

%package cpacfstatsd
Summary:       Monitor and maintain CPACF activity counters
Provides:      s390-tools-cpacfstatsd = %{epoch}:%{version}-%{release}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires(pre): shadow-utils
BuildRequires: systemd
BuildRequires: systemd-devel
%description cpacfstatsd
The cpacfstats tools provide a client/server application set to monitor
and maintain CPACF activity counters.

%post cpacfstatsd

%systemd_post cpacfstatsd.service
%preun cpacfstatsd

%systemd_preun cpacfstatsd.service
%postun cpacfstatsd

%systemd_postun_with_restart cpacfstatsd.service
%package chreipl-fcp-mpath
Summary:          Use multipath information for re-IPL path failover
BuildRequires:    make
BuildRequires:    bash
BuildRequires:    coreutils
%if %{with pandoc}
BuildRequires:    pandoc
%endif
BuildRequires:    gawk
BuildRequires:    gzip
BuildRequires:    sed
Provides:         s390-tools-chreipl-fcp-mpath = %{epoch}:%{version}-%{release}
Requires:         bash
Requires:         coreutils
Requires:         util-linux
Requires:         systemd-udev
Requires:         device-mapper-multipath
Requires:         dracut
%description chreipl-fcp-mpath
The chreipl-fcp-mpath toolset monitors udev events about paths to the re-IPL
volume. If the currently configured FCP re-IPL path becomes unavailable, the
toolset checks for operational paths to the same volume. If available, it
reconfigures the FCP re-IPL settings to use an operational path.

%package devel
Summary:        Development files
Provides: s390-tools-devel = %{epoch}:%{version}-%{release}
Requires: %{name}-base%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
User-space development files for the s390/s390x architecture.

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2:2.41.0-2
- Import
%endif
%endif
