# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 640c56c4bcf8ce8f2aa65d6a633c19d58370527a5213e71aa76546c930c6a6fb
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# secure boot support is for RHEL only
%if 0%{?rhel} >= 8 || 0%{?oreon}
%bcond_without signzipl
%else
%bcond_with signzipl
%endif

%if 0%{?fedora} || 0%{?oreon}
%bcond_without pandoc
%else
%bcond_with pandoc
%endif

# Also controls whether %%cargo_generate_buildrequires generates dev-dependencies
%bcond_without check

Name:           s390utils
Summary:        Utilities and daemons for IBM z Systems
Version:        2.41.0
Release:        2%{?dist}
Epoch:          2
# MIT covers nearly all the files, except init files (LGPL-2.1-or-later)
#
# Statically-linked Rust dependencies contribute additional license terms,
# listed in the output of %%{cargo_license_summary}:
#
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
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
# To create the vendor tarball:
#   tar xf s390-tools-%%{version}.tar.gz ; pushd s390-tools-%%{version}/rust ; \
#   rm -f Cargo.lock && cargo vendor && \
#   tar Jvcf ../../s390-tools-%%{version}-rust-vendor.tar.xz vendor/ ; popd
%if 0%{?rhel} || 0%{?oreon}
Source1:        s390-tools-%{version}-rust-vendor.tar.xz
%endif
Source5:        https://fedorapeople.org/cgit/sharkcz/public_git/utils.git/tree/zfcpconf.sh
Source7:        https://fedorapeople.org/cgit/sharkcz/public_git/utils.git/tree/zfcp.udev
Source12:       https://fedorapeople.org/cgit/sharkcz/public_git/utils.git/tree/dasd.udev
Source13:       https://fedorapeople.org/cgit/sharkcz/public_git/utils.git/tree/dasdconf.sh
Source14:       https://fedorapeople.org/cgit/sharkcz/public_git/utils.git/tree/device_cio_free
Source15:       https://fedorapeople.org/cgit/sharkcz/public_git/utils.git/tree/device_cio_free.service
Source16:       https://fedorapeople.org/cgit/sharkcz/public_git/utils.git/tree/ccw_init
Source17:       https://fedorapeople.org/cgit/sharkcz/public_git/utils.git/tree/ccw.udev
Source21:       https://fedorapeople.org/cgit/sharkcz/public_git/utils.git/tree/normalize_dasd_arg
Source23:       20-zipl-kernel.install
Source24:       52-zipl-rescue.install
Source25:       91-zipl.install

%if %{with signzipl}
%define pesign_name redhatsecureboot302
%endif

# change the defaults to match Fedora environment
Patch0:         s390-tools-zipl-invert-script-options.patch
Patch1:         s390-tools-zipl-blscfg-rpm-nvr-sort.patch

# upstream fixes/updates
#Patch100:       s390utils-%%{version}-fedora.patch

# 
ExcludeArch:    %{ix86}

# Add Provides for upstream name
Provides:       s390-tools = %{epoch}:%{version}-%{release}

%ifarch s390x
#
# s390x/native package structure
#
Requires:       s390utils-core = %{epoch}:%{version}-%{release}
Requires:       s390utils-base = %{epoch}:%{version}-%{release}
Requires:       s390utils-osasnmpd = %{epoch}:%{version}-%{release}
Requires:       s390utils-cpuplugd = %{epoch}:%{version}-%{release}
Requires:       s390utils-mon_statd = %{epoch}:%{version}-%{release}
Requires:       s390utils-iucvterm = %{epoch}:%{version}-%{release}
Requires:       s390utils-ziomon = %{epoch}:%{version}-%{release}
%else
#
# multiarch package structure
#
Requires:       s390utils-se-data = %{epoch}:%{version}-%{release}
%endif

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
%if 0%{?rhel} || 0%{?oreon}
BuildRequires:  libcurl-devel
BuildRequires:  openssl-devel
BuildRequires:  rust-toolset
%else
BuildRequires:  cargo-rpm-macros >= 24
%endif

%description
This is a meta package for installing the default s390-tools sub packages.
If you do not need all default sub packages, it is recommended to install the
required sub packages separately.

The s390utils packages contain a set of user space utilities that should to
be used together with the zSeries (s390) Linux kernel and device drivers.

%prep
%oreon_verify_sources
%autosetup -n s390-tools-%{version} -p1

%if 0%{?rhel} || 0%{?oreon}
pushd rust
tar xf %{SOURCE1}
%cargo_prep -v vendor
popd
%else
%cargo_prep
%endif
rm ./rust/Cargo.lock

# Create sysusers config files
echo 'g zkeyadm' > s390utils-base.conf.usr
echo 'g ts-shell' > s390utils-iucvterm.conf.usr
echo 'g cpacfstats' > s390utils-cpacfstatsd.conf.usr

# Create tmpfiles config files
echo 'd /var/log/ts-shell 2770 root ts-shell' > s390utils-iucvterm.conf.tmp

%if !0%{?rhel} || 0%{?oreon}
%generate_buildrequires
pushd rust >/dev/null
%cargo_generate_buildrequires
popd >/dev/null
%endif

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
%if 0%{?rhel} || 0%{?oreon}
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
#
# s390x/native specific %%install section
#
# sign the stage3 bootloader
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

# move tools to searchable dir
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

# upstream udev rules
install -Dp -m 644 etc/udev/rules.d/*.rules %{buildroot}%{_udevrulesdir}

# upstream modules config
install -Dp -m 644 etc/modules-load.d/*.conf %{buildroot}%{_prefix}/lib/modules-load.d

# Install kernel-install scripts
install -d -m 0755 %{buildroot}%{_prefix}/lib/kernel/install.d/
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ zfcpdump/10-zfcpdump.install
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE23}
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE24}
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE25}
install -d -m 0755 %{buildroot}%{_sysconfdir}/kernel/install.d/
install -m 0644 /dev/null %{buildroot}%{_sysconfdir}/kernel/install.d/20-grubby.install

# install usefull headers for devel subpackage
mkdir -p %{buildroot}%{_includedir}/%{name}
install -p -m 644 include/lib/vtoc.h %{buildroot}%{_includedir}/%{name}

# device_cio_free
install -p -m 755 %{SOURCE14} %{buildroot}%{_sbindir}
pushd %{buildroot}%{_sbindir}
for lnk in dasd zfcp znet; do
    ln -sf device_cio_free ${lnk}_cio_free
done
popd
install -p -m 644 %{SOURCE15} %{buildroot}%{_unitdir}

# ccw
install -p -m 755 %{SOURCE16} %{buildroot}/usr/lib/udev/ccw_init
install -p -m 644 %{SOURCE17} %{buildroot}%{_udevrulesdir}/81-ccw.rules

# zipl.conf to be ghosted
touch %{buildroot}%{_sysconfdir}/zipl.conf

# install systemd sysusers and tmpfiles
mkdir -p %{buildroot}{%{_sysusersdir},%{_tmpfilesdir}}/
for f in s390utils-*.conf.usr; do
    install -p -m 644 $f %{buildroot}%{_sysusersdir}/$(basename -s .usr $f)
done
for f in s390utils-*.conf.tmp; do
    install -p -m 644 $f %{buildroot}%{_tmpfilesdir}/$(basename -s .tmp $f)
done

%endif

%ifarch s390x
#
# s390x/native main %%files section
#
%files
%doc README.md

%else
#
# multiarch %%files section
#

%files
%doc README.md
%license LICENSE
%license rust/LICENSE.dependencies
%if 0%{?rhel} || 0%{?oreon}
%license rust/cargo-vendor.txt
%endif
%{_bindir}/genprotimg
%{_bindir}/pvattest
%{_bindir}/pvextract-hdr
%{_bindir}/pvimg
%{_bindir}/pvsecret
%{_bindir}/pvverify
%{_mandir}/man1/genprotimg.1*
%{_mandir}/man1/pvattest.1*
%{_mandir}/man1/pvattest-check.1*
%{_mandir}/man1/pvattest-create.1*
%{_mandir}/man1/pvattest-perform.1*
%{_mandir}/man1/pvattest-verify.1*
%{_mandir}/man1/pvimg.1*
%{_mandir}/man1/pvimg-create.1*
%{_mandir}/man1/pvimg-info.1*
%{_mandir}/man1/pvimg-test.1*
%{_mandir}/man1/pvsecret-add.1*
%{_mandir}/man1/pvsecret-create-association.1*
%{_mandir}/man1/pvsecret-create-meta.1*
%{_mandir}/man1/pvsecret-create-retrievable.1*
%{_mandir}/man1/pvsecret-create-update-cck.1*
%{_mandir}/man1/pvsecret-create.1*
%{_mandir}/man1/pvsecret-list.1*
%{_mandir}/man1/pvsecret-lock.1*
%{_mandir}/man1/pvsecret-retrieve.1*
%{_mandir}/man1/pvsecret-verify.1*
%{_mandir}/man1/pvsecret.1*
%{_mandir}/man1/pvverify.1*
%dir %{_datadir}/s390-tools
%{_datadir}/s390-tools/netboot/
%{_datadir}/s390-tools/pvimg/
%{bash_completions_dir}/*.bash
%{zsh_completions_dir}/_*

#
# enf of multi-arch section
#
%endif

%ifarch s390x
#
# s390x specific sub-packages
#
#
# ************************* s390-tools core package  *************************
#
%package core
License:        MIT
Summary:        S390 core tools
Provides:       s390-tools-core = %{epoch}:%{version}-%{release}
Requires:       coreutils
Requires:       makedumpfile
%{?systemd_requires}
# BRs are covered via the base package


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

%files core
%doc README.md zdev/src/chzdev_usage.txt
%license LICENSE
%{_sbindir}/chreipl
%{_sbindir}/chzdev
%{_sbindir}/cio_ignore
%{_sbindir}/dasdfmt
%{_sbindir}/dasdinfo
%{_sbindir}/fdasd
%{_sbindir}/lszdev
%{_sbindir}/vmcp
%{_sbindir}/zipl
%{_sbindir}/zipl-editenv
%dir /lib/s390-tools
/lib/s390-tools/{zipl,chreipl}_helper.*
/lib/s390-tools/cpictl
/lib/s390-tools/stage3.bin
/lib/s390-tools/zdev_id
/lib/s390-tools/zdev-from-dasd_mod.dasd
/lib/s390-tools/zdev-root-update
/lib/s390-tools/zdev-to-dasd_mod.dasd
/lib/s390-tools/zdev-to-rd.znet
/lib/s390-tools/zipl.conf
%ghost %config(noreplace) %{_sysconfdir}/zipl.conf
%config(noreplace) %{_sysconfdir}/ziplenv
%{_unitdir}/cpi.service
%config(noreplace) %{_sysconfdir}/sysconfig/cpi
/usr/lib/dracut/modules.d/95zdev/
/usr/lib/dracut/modules.d/95zdev-kdump/
%{_mandir}/man5/zipl.conf.5*
%{_mandir}/man8/chreipl.8*
%{_mandir}/man8/chzdev.8*
%{_mandir}/man8/cio_ignore.8*
%{_mandir}/man8/dasdfmt.8*
%{_mandir}/man8/dasdinfo.8*
%{_mandir}/man8/fdasd.8*
%{_mandir}/man8/lszdev.8*
%{_mandir}/man8/vmcp.8*
%{_mandir}/man8/zipl.8*
%{_mandir}/man8/zipl-editenv.8*

# Additional Fedora/RHEL specific stuff
%ghost %config(noreplace) %{_sysconfdir}/dasd.conf
%ghost %config(noreplace) %{_sysconfdir}/zfcp.conf
%{_sbindir}/dasdconf.sh
%{_sbindir}/normalize_dasd_arg
%{_sbindir}/zfcpconf.sh
%{_sbindir}/device_cio_free
%{_sbindir}/dasd_cio_free
%{_sbindir}/zfcp_cio_free
%{_sbindir}/znet_cio_free
%{_unitdir}/device_cio_free.service
/usr/lib/udev/ccw_init
%{_udevrulesdir}/40-z90crypt.rules
%{_udevrulesdir}/56-dasd.rules
%{_udevrulesdir}/56-zfcp.rules
%{_udevrulesdir}/59-dasd.rules
%{_udevrulesdir}/59-virtio-blk.rules
%{_udevrulesdir}/60-readahead.rules
%{_udevrulesdir}/81-ccw.rules
%{_udevrulesdir}/81-dpm.rules
%{_udevrulesdir}/90-cpi.rules
%{_udevrulesdir}/80-hotplug-cpu.rules
%{_sysconfdir}/kernel/install.d/20-grubby.install
%{_prefix}/lib/kernel/install.d/10-zfcpdump.install
%{_prefix}/lib/kernel/install.d/20-zipl-kernel.install
%{_prefix}/lib/kernel/install.d/52-zipl-rescue.install
%{_prefix}/lib/kernel/install.d/91-zipl.install
%{_prefix}/lib/modules-load.d/s390-pkey.conf

#
# *********************** s390-tools base package  ***********************
#

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

%files base
%doc README.md zdev/src/lszdev_usage.txt
%license rust/LICENSE.dependencies
%if 0%{?rhel} || 0%{?oreon}
%license rust/cargo-vendor.txt
%endif
%{_sbindir}/chccwdev
%{_sbindir}/chchp
%{_sbindir}/chcpumf
%{_sbindir}/chpstat
%{_sbindir}/chshut
%{_sbindir}/chzcrypt
%{_sbindir}/dasdstat
%{_sbindir}/dasdview
%{_sbindir}/dbginfo.sh
%{_sbindir}/hsavmcore
%{_sbindir}/hsci
%{_sbindir}/hyptop
%{_sbindir}/ip_watcher.pl
%{_sbindir}/lschp
%{_sbindir}/lscpumf
%{_sbindir}/lscss
%{_sbindir}/lsdasd
%{_sbindir}/lshwc
%{_sbindir}/lsluns
%{_sbindir}/lsqeth
%{_sbindir}/lspai
%{_sbindir}/lsreipl
%{_sbindir}/lsscm
%{_sbindir}/lsshut
%{_sbindir}/lsstp
%{_sbindir}/lstape
%{_sbindir}/lszcrypt
%{_sbindir}/lszfcp
%{_sbindir}/opticsmon
%{_sbindir}/pai
%{_sbindir}/qetharp
%{_sbindir}/qethconf
%{_sbindir}/qethqoat
%{_sbindir}/sclpdbf
%{_sbindir}/start_hsnc.sh
%{_sbindir}/tape390_crypt
%{_sbindir}/tape390_display
%{_sbindir}/ttyrun
%{_sbindir}/tunedasd
%{_sbindir}/vmur
%{_sbindir}/xcec-bridge
%{_sbindir}/zcryptctl
%{_sbindir}/zcryptstats
%{_sbindir}/zfcpdbf
%{_sbindir}/zgetdump
%{_sbindir}/zipl-switch-to-blscfg
%{_sbindir}/zmemtopo
%{_sbindir}/znetconf
%{_sbindir}/zpcictl
%{_bindir}/cpacfinfo
%{_bindir}/dump2tar
%{_bindir}/genprotimg
%{_bindir}/mk-s390image
%{_bindir}/pvapconfig
%{_bindir}/pvimg
%{_bindir}/pvinfo
%{_bindir}/pvattest
%{_bindir}/pvextract-hdr
%{_bindir}/pvsecret
%{_bindir}/pvverify
%{_bindir}/zkey
%{_bindir}/zkey-cryptsetup
%{_bindir}/zpwr
%{_unitdir}/dumpconf.service
%{_unitdir}/opticsmon.service
%ghost %config(noreplace) %{_sysconfdir}/zipl.conf
%config(noreplace) %{_sysconfdir}/sysconfig/dumpconf
%{_sysconfdir}/mdevctl.d/*
%{_sysusersdir}/s390utils-base.conf
/usr/lib/dracut/modules.d/99ngdump/
/usr/lib/dracut/dracut.conf.d/99-pkey.conf
# own the mdevctl dirs until new release is available
%dir /usr/lib/mdevctl
%dir /usr/lib/mdevctl/scripts.d
%dir /usr/lib/mdevctl/scripts.d/callouts
/usr/lib/mdevctl/scripts.d/callouts/ap-check
/lib/s390-tools/dumpconf
/lib/s390-tools/lsznet.raw
%dir /lib/s390-tools/zfcpdump
/lib/s390-tools/zfcpdump/zfcpdump-initrd
/lib/s390-tools/znetcontrolunits
%{_libdir}/libekmfweb.so.*
%{_libdir}/libkmipclient.so.*
%dir %{_libdir}/zkey
%{_libdir}/zkey/zkey-ekmfweb.so
%{_libdir}/zkey/zkey-kmip.so
%{_mandir}/man1/cpacfinfo.1*
%{_mandir}/man1/dump2tar.1*
%{_mandir}/man1/genprotimg.1*
%{_mandir}/man1/mk-s390image.1*
%{_mandir}/man1/pvapconfig.1*
%{_mandir}/man1/pvattest.1*
%{_mandir}/man1/pvattest-check.1*
%{_mandir}/man1/pvattest-create.1*
%{_mandir}/man1/pvattest-perform.1*
%{_mandir}/man1/pvattest-verify.1*
%{_mandir}/man1/pvimg.1*
%{_mandir}/man1/pvimg-create.1*
%{_mandir}/man1/pvimg-info.1*
%{_mandir}/man1/pvimg-test.1*
%{_mandir}/man1/pvsecret-add.1*
%{_mandir}/man1/pvsecret-create-association.1*
%{_mandir}/man1/pvsecret-create-meta.1*
%{_mandir}/man1/pvsecret-create-retrievable.1*
%{_mandir}/man1/pvsecret-create-update-cck.1*
%{_mandir}/man1/pvsecret-create.1*
%{_mandir}/man1/pvsecret-list.1*
%{_mandir}/man1/pvsecret-lock.1*
%{_mandir}/man1/pvsecret-retrieve.1*
%{_mandir}/man1/pvsecret-verify.1*
%{_mandir}/man1/pvsecret.1*
%{_mandir}/man1/pvverify.1*
%{_mandir}/man1/zkey.1*
%{_mandir}/man1/zkey-cryptsetup.1*
%{_mandir}/man1/zkey-ekmfweb.1*
%{_mandir}/man1/zkey-kmip.1*
%{_mandir}/man1/zpwr.1*
%{_mandir}/man4/prandom.4*
%{_mandir}/man5/hsavmcore.conf.5*
%{_mandir}/man8/chccwdev.8*
%{_mandir}/man8/chchp.8*
%{_mandir}/man8/chcpumf.8*
%{_mandir}/man8/chpstat.8*
%{_mandir}/man8/chshut.8*
%{_mandir}/man8/chzcrypt.8*
%{_mandir}/man8/dasdstat.8*
%{_mandir}/man8/dasdview.8*
%{_mandir}/man8/dbginfo.sh.8*
%{_mandir}/man8/dumpconf.8*
%{_mandir}/man8/hsavmcore.8*
%{_mandir}/man8/hsci.8*
%{_mandir}/man8/hyptop.8*
%{_mandir}/man8/lschp.8*
%{_mandir}/man8/lscpumf.8*
%{_mandir}/man8/lscss.8*
%{_mandir}/man8/lsdasd.8*
%{_mandir}/man8/lshwc.8*
%{_mandir}/man8/lsluns.8*
%{_mandir}/man8/lspai.8*
%{_mandir}/man8/lsqeth.8*
%{_mandir}/man8/lsreipl.8*
%{_mandir}/man8/lsscm.8*
%{_mandir}/man8/lsshut.8*
%{_mandir}/man8/lsstp.8*
%{_mandir}/man8/lstape.8*
%{_mandir}/man8/lszcrypt.8*
%{_mandir}/man8/lszfcp.8*
%{_mandir}/man8/opticsmon.8*
%{_mandir}/man8/pai.8*
%{_mandir}/man8/qetharp.8*
%{_mandir}/man8/qethconf.8*
%{_mandir}/man8/qethqoat.8*
%{_mandir}/man8/tape390_crypt.8*
%{_mandir}/man8/tape390_display.8*
%{_mandir}/man8/ttyrun.8*
%{_mandir}/man8/tunedasd.8*
%{_mandir}/man8/vmur.8*
%{_mandir}/man8/zcryptctl.8*
%{_mandir}/man8/zcryptstats.8*
%{_mandir}/man8/zfcpdbf.8*
%{_mandir}/man8/zgetdump.8*
%{_mandir}/man8/zipl-switch-to-blscfg.8*
%{_mandir}/man8/zmemtopo.8*
%{_mandir}/man8/znetconf.8*
%{_mandir}/man8/zpcictl.8*
%dir %{_datadir}/s390-tools
%{_datadir}/s390-tools/netboot/
%{bash_completions_dir}/*.bash
%{zsh_completions_dir}/_*
%dir %attr(0770,root,zkeyadm) %{_sysconfdir}/zkey
%dir %attr(0770,root,zkeyadm) %{_sysconfdir}/zkey/kmip
%dir %attr(0770,root,zkeyadm) %{_sysconfdir}/zkey/kmip/profiles
%config(noreplace) %attr(0660,root,zkeyadm)%{_sysconfdir}/zkey/kmip/profiles/*.profile
%dir %attr(0770,root,zkeyadm) %{_sysconfdir}/zkey/repository
%config(noreplace) %attr(0660,root,zkeyadm)%{_sysconfdir}/zkey/kms-plugins.conf

# Additional Fedora/RHEL specific stuff
/boot/tape0

%package se-data
License:        MIT
Summary:        Data for Secure Execution
Provides:       s390-tools-se-data = %{epoch}:%{version}-%{release}
BuildArch:      noarch

%description se-data
%{summary}.

%files se-data
%dir %{_datadir}/s390-tools
%{_datadir}/s390-tools/pvimg/

#
# *********************** s390-tools osasnmpd package  ***********************
#
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

%files osasnmpd
%{_sbindir}/osasnmpd
%{_udevrulesdir}/57-osasnmpd.rules
%{_mandir}/man8/osasnmpd.8*

#
# *********************** s390-tools mon_statd package  **********************
#
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

%files mon_statd
%{_sbindir}/mon_fsstatd
%{_sbindir}/mon_procd
%config(noreplace) %{_sysconfdir}/sysconfig/mon_fsstatd
%config(noreplace) %{_sysconfdir}/sysconfig/mon_procd
%{_unitdir}/mon_fsstatd.service
%{_unitdir}/mon_procd.service
%{_mandir}/man8/mon_fsstatd.8*
%{_mandir}/man8/mon_procd.8*

#
# *********************** s390-tools cpuplugd package  ***********************
#
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

%files cpuplugd
%config(noreplace) %{_sysconfdir}/cpuplugd.conf
%{_sbindir}/cpuplugd
%{_mandir}/man5/cpuplugd.conf.5*
%{_mandir}/man8/cpuplugd.8*
%{_unitdir}/cpuplugd.service

#
# *********************** s390-tools ziomon package  *************************
#
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

%files ziomon
%{_sbindir}/ziomon
%{_sbindir}/ziomon_fcpconf
%{_sbindir}/ziomon_mgr
%{_sbindir}/ziomon_util
%{_sbindir}/ziomon_zfcpdd
%{_sbindir}/ziorep_config
%{_sbindir}/ziorep_traffic
%{_sbindir}/ziorep_utilization
%{_mandir}/man8/ziomon.8*
%{_mandir}/man8/ziomon_fcpconf.8*
%{_mandir}/man8/ziomon_mgr.8*
%{_mandir}/man8/ziomon_util.8*
%{_mandir}/man8/ziomon_zfcpdd.8*
%{_mandir}/man8/ziorep_config.8*
%{_mandir}/man8/ziorep_traffic.8*
%{_mandir}/man8/ziorep_utilization.8*

#
# *********************** s390-tools iucvterm package  *************************
#
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
# /etc/shells is provided by "setup"
grep -q '^/usr/bin/ts-shell$' /etc/shells \
    || echo "/usr/bin/ts-shell" >> /etc/shells

%postun iucvterm
if [ $1 = 0 ]
then
    # remove ts-shell from /etc/shells on uninstall
    grep -v '^/usr/bin/ts-shell$' /etc/shells > /etc/shells.ts-new
    mv /etc/shells.ts-new /etc/shells
    chmod 0644 /etc/shells
fi

%files iucvterm
%dir %{_sysconfdir}/iucvterm
%config(noreplace) %attr(0640,root,ts-shell) %{_sysconfdir}/iucvterm/ts-audit-systems.conf
%config(noreplace) %attr(0640,root,ts-shell) %{_sysconfdir}/iucvterm/ts-authorization.conf
%config(noreplace) %attr(0640,root,ts-shell) %{_sysconfdir}/iucvterm/ts-shell.conf
%config(noreplace) %attr(0640,root,ts-shell) %{_sysconfdir}/iucvterm/unrestricted.conf
%{_bindir}/iucvconn
%{_bindir}/iucvtty
%{_bindir}/ts-shell
%{_sbindir}/chiucvallow
%{_sbindir}/lsiucvallow
%{_sysusersdir}/s390utils-iucvterm.conf
%{_tmpfilesdir}/s390utils-iucvterm.conf
%ghost %dir %attr(2770,root,ts-shell) /var/log/ts-shell
%doc iucvterm/doc/ts-shell
%{_mandir}/man1/iucvconn.1*
%{_mandir}/man1/iucvtty.1*
%{_mandir}/man1/ts-shell.1*
%{_mandir}/man7/af_iucv.7*
%{_mandir}/man8/chiucvallow.8*
%{_mandir}/man8/lsiucvallow.8*
%{_mandir}/man9/hvc_iucv.9*
%{_unitdir}/iucvtty-login@.service
%{_unitdir}/ttyrun-getty@.service


#
# *********************** cmsfs-fuse package  ***********************
#
%package cmsfs-fuse
Summary:        CMS file system based on FUSE
BuildRequires:  fuse3-devel
Requires:       fuse3
Provides:       s390-tools-cmsfs-fuse = %{epoch}:%{version}-%{release}
Requires:       glibc-gconv-extra
Obsoletes:      %{name}-cmsfs < 2:2.7.0-3

%description cmsfs-fuse
This package contains the CMS file system based on FUSE.

%files cmsfs-fuse
%dir %{_sysconfdir}/cmsfs-fuse
%config(noreplace) %{_sysconfdir}/cmsfs-fuse/filetypes.conf
%{_bindir}/cmsfs-fuse
%{_mandir}/man1/cmsfs-fuse.1*

#
# *********************** zdsfs package  ***********************
#
%package zdsfs
Summary:        z/OS data set access based on FUSE
BuildRequires:  fuse3-devel
BuildRequires:  libcurl-devel
Requires:       fuse3
Provides:       s390-tools-zdsfs = %{epoch}:%{version}-%{release}

%description zdsfs
This package contains the z/OS data set access based on FUSE.

%files zdsfs
%{_bindir}/zdsfs
%{_mandir}/man1/zdsfs.1*

#
# *********************** hmcdrvfs package  ***********************
#
%package hmcdrvfs
Summary:       HMC drive file system based on FUSE
BuildRequires: fuse3-devel
Requires:      fuse3
Provides:      s390-tools-hmcdrvfs = %{epoch}:%{version}-%{release}

%description hmcdrvfs
This package contains a HMC drive file system based on FUSE and a tool
to list files and directories.

%files hmcdrvfs
%{_bindir}/hmcdrvfs
%{_sbindir}/lshmc
%{_mandir}/man1/hmcdrvfs.1*
%{_mandir}/man8/lshmc.8*

#
# *********************** cpacfstatsd package  ***********************
#
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

%files cpacfstatsd
%{_bindir}/cpacfstats
%{_sbindir}/cpacfstatsd
%{_mandir}/man1/cpacfstats.1*
%{_mandir}/man8/cpacfstatsd.8*
%{_unitdir}/cpacfstatsd.service
%{_sysusersdir}/s390utils-cpacfstatsd.conf

#
# *********************** chreipl-fcp-mpath package  ***********************
#
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

%files chreipl-fcp-mpath
%doc chreipl-fcp-mpath/README.md
%if %{with pandoc}
%doc chreipl-fcp-mpath/README.html
%endif
%dir %{_prefix}/lib/chreipl-fcp-mpath/
%{_prefix}/lib/chreipl-fcp-mpath/*
%{_prefix}/lib/dracut/dracut.conf.d/70-chreipl-fcp-mpath.conf
%{_prefix}/lib/udev/chreipl-fcp-mpath-is-ipl-tgt
%{_prefix}/lib/udev/chreipl-fcp-mpath-is-ipl-vol
%{_prefix}/lib/udev/chreipl-fcp-mpath-is-reipl-zfcp
%{_prefix}/lib/udev/chreipl-fcp-mpath-record-volume-identifier
%{_prefix}/lib/udev/chreipl-fcp-mpath-try-change-ipl-path
%{_udevrulesdir}/70-chreipl-fcp-mpath.rules
%{_mandir}/man7/chreipl-fcp-mpath.7*

#
# *********************** devel package  ***********************
#
%package devel
Summary:        Development files
Provides: s390-tools-devel = %{epoch}:%{version}-%{release}
Requires: %{name}-base%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
User-space development files for the s390/s390x architecture.

%files devel
%{_includedir}/%{name}/
%{_includedir}/ekmfweb/
%{_includedir}/kmipclient/
%{_libdir}/libekmfweb.so
%{_libdir}/libkmipclient.so

#
# end of s390x specific sub-packages
#
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2:2.41.0-2
- Import
