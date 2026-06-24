%global source0_hash none

# Build ocaml bits unless rpmbuild was run with --without ocaml 
# or ocamlopt is missing (the xen makefile doesn't build ocaml bits if it isn't there)
%define with_ocaml  %{?_without_ocaml: 0} %{?!_without_ocaml: 1}
%define build_ocaml %(test -x %{_bindir}/ocamlopt && echo %{with_ocaml} || echo 0)
# Build with docs unless rpmbuild was run with --without docs
%define build_docs %{?_without_docs: 0} %{?!_without_docs: 1}
# Build with stubdom unless rpmbuild was run with --without stubdom
%define build_stubdom %{?_without_stubdom: 0} %{?!_without_stubdom: 1}
# build with ovmf from edk2-ovmf unless rpmbuild was run with --without ovmf
%define build_ovmf %{?_without_ovmf: 0} %{?!_without_ovmf: 1}
# set to 0 for archs that don't use ovmf (reduces build dependencies)
%ifnarch x86_64
%define build_ovmf 0
%endif
# Build with xen hypervisor unless rpmbuild was run with --without hyp
%define build_hyp %{?_without_hyp: 0} %{?!_without_hyp: 1}
# build xsm support unless rpmbuild was run with --without xsm
# or required packages are missing
%define with_xsm  %{?_without_xsm: 0} %{?!_without_xsm: 1}
%define build_xsm %(test -x %{_bindir}/checkpolicy && test -x %{_bindir}/m4 && echo %{with_xsm} || echo 0)
# cross compile 64-bit hypervisor on ix86 unless rpmbuild was run
#	with --without crosshyp
%define build_crosshyp %{?_without_crosshyp: 0} %{?!_without_crosshyp: 1}
%ifnarch %{ix86}
%define build_crosshyp 0
%else
%if ! %build_crosshyp
%define build_hyp 0
%endif
%endif
# no point in trying to build xsm on ix86 without a hypervisor
%if ! %build_hyp
%define build_xsm 0
%endif
# build an efi boot image (where supported) unless rpmbuild was run with
# --without efi
%define build_efi %{?_without_efi: 0} %{?!_without_efi: 1}
# xen only supports efi boot images on x86_64 or aarch64
%ifnarch x86_64 aarch64
%define build_efi 0
%endif
%if "%dist" >= ".fc20"
%define with_systemd_presets 1
%else
%define with_systemd_presets 0
%endif

# Hypervisor ABI
%define hv_abi  4.21

Summary: Xen is a virtual machine monitor
Name:    xen
Version: 4.21.1
Release: 7%{?dist}
# Automatically converted from old format: GPLv2+ and LGPLv2+ and BSD - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD
URL:     http://xen.org/
Source0: https://downloads.xenproject.org/release/xen/%{version}/xen-%{version}.tar.xz
Source2: %{name}.logrotate
# used by stubdoms
Source10: lwip-1.3.0.tar.gz
Source11: newlib-1.16.0.tar.gz
Source12: zlib-1.2.3.tar.gz
Source13: pciutils-2.2.9.tar.bz2
Source14: grub-0.97.tar.gz
Source15: polarssl-1.1.4-gpl.tgz
# .config file for xen hypervisor
Source21: xen.hypervisor.config
# mini-os xen-RELEASE-4.21.0 with .git and .gitignore stripped
Source22: mini-os-4.21.0.tar.xz

Patch1: xen.fedora.systemd.patch
Patch2: xen.ocaml.selinux.fix.patch
Patch3: xen.canonicalize.patch
Patch4: droplibvirtconflict.patch
Patch5: xen.gcc9.fixes.patch
Patch6: xen.gcc11.fixes.patch
Patch7: xen.gcc12.fixes.patch
Patch8: xen.efi.build.patch
Patch9: xen.python3.12.patch
Patch11: xen.json.nocpuid.patch
Patch12: xsa483.patch
Patch13: xsa484.patch
Patch14: xsa486.patch
Patch15: xen.git-90b20547b756a5cf9b0fec9fb0de5b361e8bf4c3.patch
Patch16: xsa490-4.21.patch
Patch17: xsa491-4.21.patch
Patch18: xsa492-4.21-01.patch
Patch19: xsa492-4.21-02.patch
Patch20: xsa492-4.21-03.patch
Patch21: xsa492-4.21-04.patch
Patch22: xsa492-4.21-05.patch
Patch23: xsa492-4.21-06.patch
Patch24: xsa492-4.21-07.patch
Patch25: xsa492-4.21-08.patch
Patch26: xsa492-4.21-09.patch
Patch27: xsa492-4.21-10.patch
Patch28: xsa492-4.21-11.patch
Patch29: xsa492-4.21-12.patch
Patch30: xsa492-4.21-13.patch
Patch31: xsa492-4.21-14.patch
Patch32: xsa492-4.21-15.patch
Patch33: xsa492-4.21-16.patch
Patch34: xsa492-4.21-17.patch
Patch35: xsa492-4.21-18.patch
Patch36: xsa492-4.21-19.patch
Patch37: xsa492-4.21-20.patch
Patch38: xsa493-4.21-01.patch
Patch39: xsa493-4.21-02.patch
Patch40: xsa493-4.21-03.patch
Patch41: xsa493-4.21-04.patch
Patch42: xsa494-4.21.patch


# build using Fedora seabios and ipxe packages for roms
BuildRequires: seabios-bin ipxe-roms-qemu
%ifarch %{ix86} x86_64
# for the VMX "bios"
BuildRequires: dev86
%endif
BuildRequires: python3-devel ncurses-devel python3-setuptools
BuildRequires: perl-interpreter perl-generators
BuildRequires: gettext
BuildRequires: gnutls-devel
BuildRequires: openssl-devel
# For ioemu PCI passthrough
BuildRequires: pciutils-devel
# Several tools now use uuid
BuildRequires: libuuid-devel
# iasl needed to build hvmloader
BuildRequires: acpica-tools
# modern compressed kernels
BuildRequires: bzip2-devel xz-devel libzstd-devel
# libfsimage
BuildRequires: e2fsprogs-devel
# tools now require wget
BuildRequires: wget
# use json-c instead of yajl
BuildRequires: json-c-devel
# remus support now needs libnl3
BuildRequires: libnl3-devel
%if %with_xsm
# xsm policy file needs needs checkpolicy and m4
BuildRequires: checkpolicy m4
%endif
%if %build_crosshyp
# cross compiler for building 64-bit hypervisor on ix86
BuildRequires: gcc-x86_64-linux-gnu
%endif
BuildRequires: gcc make
Requires: iproute
Requires: python3-lxml
Requires: xen-runtime = %{version}-%{release}
# Not strictly a dependency, but kpartx is by far the most useful tool right
# now for accessing domU data from within a dom0 so bring it in when the user
# installs xen.
Requires: kpartx
ExclusiveArch: x86_64 aarch64
%if %with_ocaml
BuildRequires: ocaml, ocaml-findlib
BuildRequires: perl(Data::Dumper)
%endif
%if %with_systemd_presets
Requires(post): systemd
Requires(preun): systemd
BuildRequires: systemd
%endif
BuildRequires: systemd-devel
%ifarch aarch64
BuildRequires: libfdt-devel
%endif
%if %build_hyp
BuildRequires: bison flex
%endif
BuildRequires: hostname

%description
This package contains the XenD daemon and xm command line
tools, needed to manage virtual machines running under the
Xen hypervisor

%package libs
Summary: Libraries for Xen tools
Requires: xen-licenses

%description libs
This package contains the libraries needed to run applications
which manage Xen virtual machines.


%package runtime
Summary: Core Xen runtime environment
Requires: xen-libs = %{version}-%{release}
#Requires: /usr/bin/qemu-img /usr/bin/qemu-nbd
Requires: /usr/bin/qemu-img
# Ensure we at least have a suitable kernel installed, though we can't
# force user to actually boot it.
Requires: xen-hypervisor-abi = %{hv_abi}
# perl is used in /etc/xen/scripts/locking.sh
Recommends: perl
%ifnarch aarch64
# use /usr/bin/qemu-system-i386 in Fedora instead of qemu-xen
Recommends: qemu-system-x86-core
%endif
%if %build_ovmf
Recommends: edk2-ovmf-xen
%endif

%description runtime
This package contains the runtime programs and daemons which
form the core Xen userspace environment.


%package hypervisor
Summary: Libraries for Xen tools
Provides: xen-hypervisor-abi = %{hv_abi}
Requires: xen-licenses
%if %build_hyp
%ifarch %{ix86}
Recommends: grub2-pc-modules
%endif
%ifarch x86_64
Recommends: grub2-pc-modules grub2-efi-x64-modules
%endif
%endif

%description hypervisor
This package contains the Xen hypervisor


%if %build_docs
%package doc
Summary: Xen documentation
BuildArch: noarch
Requires: xen-licenses
# for the docs
BuildRequires: perl(Pod::Man) perl(Pod::Text) perl(File::Find)
BuildRequires: transfig pandoc perl(Pod::Html)

%description doc
This package contains the Xen documentation.
%endif


%package devel
Summary: Development libraries for Xen tools
Requires: xen-libs = %{version}-%{release}
Requires: libuuid-devel

%description devel
This package contains what's needed to develop applications
which manage Xen virtual machines.


%package licenses
Summary: License files from Xen source

%description licenses
This package contains the license files from the source used
to build the xen packages.


%if %build_ocaml
%package ocaml
Summary: Ocaml libraries for Xen tools
Requires: ocaml-runtime, xen-libs = %{version}-%{release}

%description ocaml
This package contains libraries for ocaml tools to manage Xen
virtual machines.


%package ocaml-devel
Summary: Ocaml development libraries for Xen tools
Requires: xen-ocaml = %{version}-%{release}

%description ocaml-devel
This package contains libraries for developing ocaml tools to
manage Xen virtual machines.
%endif

%package test
Summary: internal xen tests
%description test
This package contains files used in testing the xen builds

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1
%patch 4 -p1
%patch 5 -p1
%patch 6 -p1
%patch 7 -p1
%patch 8 -p1
%patch 9 -p1
%patch 11 -p1
%patch 12 -p1
%patch 13 -p1
%patch 14 -p1
%patch 15 -p1
%patch 16 -p1
%patch 17 -p1
%patch 18 -p1
%patch 19 -p1
%patch 20 -p1
%patch 21 -p1
%patch 22 -p1
%patch 23 -p1
%patch 24 -p1
%patch 25 -p1
%patch 26 -p1
%patch 27 -p1
%patch 28 -p1
%patch 29 -p1
%patch 30 -p1
%patch 31 -p1
%patch 32 -p1
%patch 33 -p1
%patch 34 -p1
%patch 35 -p1
%patch 36 -p1
%patch 37 -p1
%patch 38 -p1
%patch 39 -p1
%patch 40 -p1
%patch 41 -p1
%patch 42 -p1

# stubdom sources
cp -v %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE15} stubdom
# copy xen hypervisor .config file to change settings
cp -v %{SOURCE21} xen/.config
# mini-os is now separate file
mkdir extras
tar -C extras -xf %{SOURCE22}

%build
# This package calls binutils components directly and would need to pass
# in flags to enable the LTO plugins
# Disable LTO
%define _lto_cflags %{nil}

%if !%build_ocaml
%define ocaml_flags OCAML_TOOLS=n
%endif
%if %build_efi
mkdir -p dist/install/boot/efi/efi/fedora
%endif
%if %build_ocaml
mkdir -p dist/install%{_libdir}/ocaml/stublibs
%endif
export EXTRA_CFLAGS_XEN_TOOLS="$RPM_OPT_FLAGS -Wno-error=use-after-free $LDFLAGS"
export PYTHON="/usr/bin/python3"
export LDFLAGS_SAVE=`echo $LDFLAGS | sed -e 's/-Wl,//g' -e 's/,/ /g' -e 's? -specs=[-a-z/0-9]*??g'`
export CFLAGS_SAVE="$CFLAGS"
CONFIG_EXTRA=""
%if %build_ovmf
CONFIG_EXTRA="$CONFIG_EXTRA --with-system-ovmf=/usr/share/edk2/xen/OVMF.fd"
%endif
%ifarch aarch64
CONFIG_EXTRA="$CONFIG_EXTRA --with-system-ipxe=/usr/share/ipxe/10ec8139.rom"
%endif
%if %(test -f /usr/share/seabios/bios-256k.bin && echo 1|| echo 0)
CONFIG_EXTRA="$CONFIG_EXTRA --with-system-seabios=/usr/share/seabios/bios-256k.bin"
%else
CONFIG_EXTRA="$CONFIG_EXTRA --disable-seabios"
%endif
%if %with_systemd_presets
CONFIG_EXTRA="$CONFIG_EXTRA --enable-systemd"
%endif
./configure --prefix=%{_prefix} --libdir=%{_libdir} --libexecdir=%{_libexecdir} --with-system-qemu=/usr/bin/qemu-system-i386 --with-linux-backend-modules="xen-evtchn xen-gntdev xen-gntalloc xen-blkback xen-netback xen-pciback xen-scsiback xen-acpi-processor" $CONFIG_EXTRA
unset CFLAGS CXXFLAGS FFLAGS LDFLAGS
export LDFLAGS="$LDFLAGS_SAVE"
export CFLAGS=`echo "$CFLAGS_SAVE -Wno-error=address" | sed -e 's/-specs=\/usr\/lib\/rpm\/redhat/redhat-annobin-cc1//g'`

%if %build_hyp
%make_build prefix=/usr xen
%endif
unset CFLAGS CXXFLAGS FFLAGS LDFLAGS

%make_build %{?ocaml_flags} prefix=/usr tools
%if %build_docs
make                 prefix=/usr docs
%endif
export RPM_OPT_FLAGS_RED=`echo $RPM_OPT_FLAGS | sed -e 's/-m64//g' -e 's/--param=ssp-buffer-size=4//g' -e's/-fstack-protector-strong//'`
%if %build_stubdom
%ifnarch armv7hl aarch64
make mini-os-dir
make -C stubdom build
%endif
%ifarch x86_64
export EXTRA_CFLAGS_XEN_TOOLS="$RPM_OPT_FLAGS_RED"
XEN_TARGET_ARCH=x86_32 make -C stubdom pv-grub-if-enabled
%endif
%endif


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
cp -prlP dist/install/* %{buildroot}
%if %build_stubdom
%ifnarch armv7hl aarch64
make DESTDIR=%{buildroot} %{?ocaml_flags} prefix=/usr install-stubdom
%endif
%endif
%if %build_efi
mv %{buildroot}/boot/efi/efi %{buildroot}/boot/efi/EFI
%endif
%if %build_xsm
# policy file should be in /boot/flask
mkdir %{buildroot}/boot/flask
mv %{buildroot}/boot/xenpolicy* %{buildroot}/boot/flask
%else
rm -f %{buildroot}/boot/xenpolicy*
%endif

############ debug packaging: list files ############

find %{buildroot} -print | xargs ls -ld | sed -e 's|.*%{buildroot}||' > f1.list

############ kill unwanted stuff ############

# stubdom: newlib
rm -rf %{buildroot}/usr/*-xen-elf

# hypervisor symlinks
rm -rf %{buildroot}/boot/xen-%{hv_abi}.gz
rm -rf %{buildroot}/boot/xen-4.gz
rm -rf %{buildroot}/boot/xen.gz
%if !%build_hyp
rm -rf %{buildroot}/boot
%endif

# silly doc dir fun
rm -fr %{buildroot}%{_datadir}/doc/xen

# Pointless helper
rm -f %{buildroot}%{_bindir}/xen-python-path

# README's not intended for end users
rm -f %{buildroot}/%{_sysconfdir}/xen/README*

# standard gnu info files
rm -rf %{buildroot}/usr/info

# adhere to Static Library Packaging Guidelines
rm -rf %{buildroot}/%{_libdir}/*.a

%if %build_efi
# clean up extra efi files
rm -f %{buildroot}/%{_libdir}/efi/xen-%{hv_abi}.efi
rm -f %{buildroot}/%{_libdir}/efi/xen-4.efi
rm -f %{buildroot}/%{_libdir}/efi/xen.efi
cp -p %{buildroot}/%{_libdir}/efi/xen-%{version}{,.notstripped}.efi
strip -s %{buildroot}/%{_libdir}/efi/xen-%{version}.efi
%endif

%if ! %build_ocaml
rm -rf %{buildroot}/%{_unitdir}/oxenstored.service
%endif

############ fixup files in /etc ############

# logrotate
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# init scripts
%define initdloc %(test -d /etc/rc.d/init.d/ && echo rc.d/init.d || echo init.d )

rm %{buildroot}%{_sysconfdir}/%{initdloc}/xen-watchdog
rm %{buildroot}%{_sysconfdir}/%{initdloc}/xencommons
rm %{buildroot}%{_sysconfdir}/%{initdloc}/xendomains
rm %{buildroot}%{_sysconfdir}/%{initdloc}/xendriverdomain

############ create dirs in /var ############

mkdir -p %{buildroot}%{_localstatedir}/lib/xen/images
mkdir -p %{buildroot}%{_localstatedir}/log/xen/console

############ create symlink for x86_64 for compatibility with 4.4 ############

%if "%{_libdir}" != "/usr/lib"
ln -s %{_libexecdir}/%{name} %{buildroot}/%{_libdir}/%{name}
%endif

############ create symlink to qemu-system-i386 in /usr/bin ############
ln -s ../../../bin/qemu-system-i386 %{buildroot}/%{_libexecdir}/%{name}/bin/qemu-system-i386

############ debug packaging: list files ############

find %{buildroot} -print | xargs ls -ld | sed -e 's|.*%{buildroot}||' > f2.list
diff -u f1.list f2.list || true

############ assemble license files ############

mkdir licensedir
# avoid licensedir to avoid recursion, also stubdom/ioemu and dist
# which are copies of files elsewhere
find . -path licensedir -prune -o -path stubdom/ioemu -prune -o \
  -path dist -prune -o -name COPYING -o -name LICENSE | while read file; do
  mkdir -p licensedir/`dirname $file`
  install -m 644 $file licensedir/$file
done

############ move sbin files to bin

mv %{buildroot}/usr/sbin/* %{buildroot}/usr/bin/

############ remove xen*.efi.elf files to avoid debuginfo failure

%ifarch x86_64
rm dist/install/usr/lib/debug/xen-*.efi.elf
rm %{buildroot}/usr/lib/debug/xen-*.efi.elf
%endif

############ all done now ############

%post
%if %with_systemd_presets
%systemd_post xendomains.service
%else
if [ $1 == 1 ]; then
  /bin/systemctl enable xendomains.service
fi
%endif

%preun
%if %with_systemd_presets
%systemd_preun xendomains.service
%else
if [ $1 == 0 ]; then
/bin/systemctl disable xendomains.service
fi
%endif

%post runtime
%if %with_systemd_presets
%systemd_post xenstored.service xenconsoled.service
%else
if [ $1 == 1 ]; then
  /bin/systemctl enable xenstored.service
  /bin/systemctl enable xenconsoled.service
fi
%endif

%preun runtime
%if %with_systemd_presets
%systemd_preun xenstored.service xenconsoled.service
%else
if [ $1 == 0 ]; then
  /bin/systemctl disable xenstored.service
  /bin/systemctl disable xenconsoled.service
fi
%endif

%posttrans runtime
if [ ! -L /usr/lib/xen -a -d /usr/lib/xen ] && [ -z "$(ls -A /usr/lib/xen)" ]; then
  rmdir /usr/lib/xen
fi
if [ ! -e /usr/lib/xen ]; then
  ln -s /usr/libexec/xen /usr/lib/xen
fi

%ldconfig_scriptlets libs

%if %build_hyp
%post hypervisor
do_it() {
    DIR=$1
    TARGET=$2
    if [ -d $DIR ]; then
      if [ ! -d $TARGET ]; then
        mkdir $TARGET
      fi
      for m in relocator.mod multiboot2.mod elf.mod; do
        if [ -f $DIR/$m ]; then
          if [ ! -f $TARGET/$m ] || ! cmp -s $DIR/$m $TARGET/$m; then
            cp -p $DIR/$m $TARGET/$m
          fi
        fi
      done
    fi
}
if [ $1 == 1 -a -f /sbin/grub2-mkconfig ]; then
  for f in /boot/grub2/grub.cfg; do
    if [ -f $f ]; then
      /sbin/grub2-mkconfig -o $f
      sed -i -e '/insmod module2/d' $f
    fi
  done
fi
if [ -f /sbin/grub2-mkconfig ]; then
  if [ -f /boot/grub2/grub.cfg ]; then
    DIR=/usr/lib/grub/i386-pc
    TARGET=/boot/grub2/i386-pc
    do_it $DIR $TARGET
    DIR=/usr/lib/grub/x86_64-efi
    TARGET=/boot/grub2/x86_64-efi
    do_it $DIR $TARGET
  fi
fi

%postun hypervisor
if [ -f /sbin/grub2-mkconfig ]; then
  for f in /boot/grub2/grub.cfg; do
    if [ -f $f ]; then
      /sbin/grub2-mkconfig -o $f
      sed -i -e '/insmod module2/d' $f
    fi
  done
fi
%endif

%if %build_ocaml
%post ocaml
%if %with_systemd_presets
%systemd_post oxenstored.service
%else
if [ $1 == 1 ]; then
  /bin/systemctl enable oxenstored.service
fi
%endif

%preun ocaml
%if %with_systemd_presets
%systemd_preun oxenstored.service
%else
if [ $1 == 0 ]; then
  /bin/systemctl disable oxenstored.service
fi
%endif
%endif

# Base package only contains XenD/xm python stuff
#files -f xen-xm.lang
%files
%doc COPYING README
%{python3_sitearch}/%{name}
%{python3_sitearch}/xen-*.egg-info

# Guest autostart links
%dir %attr(0700,root,root) %{_sysconfdir}/%{name}/auto
# Autostart of guests
%config(noreplace) %{_sysconfdir}/sysconfig/xendomains

%{_unitdir}/xendomains.service

%files libs
%{_libdir}/libxencall.so.1
%{_libdir}/libxencall.so.1.3
%{_libdir}/libxenctrl.so.4.*
%{_libdir}/libxendevicemodel.so.1
%{_libdir}/libxendevicemodel.so.1.4
%{_libdir}/libxenevtchn.so.1
%{_libdir}/libxenevtchn.so.1.2
%{_libdir}/libxenforeignmemory.so.1
%{_libdir}/libxenforeignmemory.so.1.4
%{_libdir}/libxenfsimage.so.4.*
%{_libdir}/libxengnttab.so.1
%{_libdir}/libxengnttab.so.1.2
%{_libdir}/libxenguest.so.4.*
%{_libdir}/libxenlight.so.4.*
%{_libdir}/libxenstat.so.4.*
%{_libdir}/libxenstore.so.4
%{_libdir}/libxenstore.so.4.1
%{_libdir}/libxentoolcore.so.1
%{_libdir}/libxentoolcore.so.1.0
%{_libdir}/libxentoollog.so.1
%{_libdir}/libxentoollog.so.1.0
%{_libdir}/libxenvchan.so.4.*
%{_libdir}/libxlutil.so.4.*
%{_libdir}/xenfsimage
%{_libdir}/libxenhypfs.so.1
%{_libdir}/libxenhypfs.so.1.0
%{_libdir}/libxenmanage.so.1
%{_libdir}/libxenmanage.so.1.0

# All runtime stuff except for XenD/xm python stuff
%files runtime
# Hotplug rules

%dir %attr(0700,root,root) %{_sysconfdir}/%{name}
%dir %attr(0700,root,root) %{_sysconfdir}/%{name}/scripts/
%config %attr(0700,root,root) %{_sysconfdir}/%{name}/scripts/*

%{_sysconfdir}/bash_completion.d/xl

%{_unitdir}/proc-xen.mount
%{_unitdir}/xenstored.service
%{_unitdir}/xenconsoled.service
%{_unitdir}/xen-watchdog.service
%{_unitdir}/xen-qemu-dom0-disk-backend.service
%{_unitdir}/xendriverdomain.service
%{_modulesloaddir}/xen.conf
%{_systemd_util_dir}/system-sleep/xen-watchdog-sleep.sh

%config(noreplace) %{_sysconfdir}/sysconfig/xencommons
%config(noreplace) %{_sysconfdir}/xen/xl.conf
%config(noreplace) %{_sysconfdir}/xen/cpupool
%config(noreplace) %{_sysconfdir}/xen/xlexample*

# Rotate console log files
%config(noreplace) %{_sysconfdir}/logrotate.d/xen

# Programs run by other programs
%dir %{_libexecdir}/%{name}
%dir %{_libexecdir}/%{name}/bin
%attr(0700,root,root) %{_libexecdir}/%{name}/bin/*

# man pages
%if %build_docs
%{_mandir}/man1/xentop.1*
%{_mandir}/man8/xentrace.8*
%{_mandir}/man1/xl.1*
%{_mandir}/man5/xl.cfg.5*
%{_mandir}/man5/xl.conf.5*
%{_mandir}/man5/xlcpupool.cfg.5*
%{_mandir}/man1/xenstore*
%{_mandir}/man5/xl-disk-configuration.5.gz
%{_mandir}/man7/xen-pci-device-reservations.7.gz
%{_mandir}/man7/xen-tscmode.7.gz
%{_mandir}/man7/xen-vtpm.7.gz
%{_mandir}/man7/xen-vtpmmgr.7.gz
%{_mandir}/man5/xl-network-configuration.5.gz
%{_mandir}/man7/xen-pv-channel.7.gz
%{_mandir}/man7/xl-numa-placement.7.gz
%{_mandir}/man1/xenhypfs.1.gz
%{_mandir}/man7/xen-vbd-interface.7.gz
%{_mandir}/man5/xl-pci-configuration.5.gz
%{_mandir}/man8/xenwatchdogd.8.gz
%endif

%{python3_sitearch}/xenfsimage*.so
%{python3_sitearch}/grub
%{python3_sitearch}/pygrub-*.egg-info

# The firmware
%ifarch x86_64
%dir %{_libexecdir}/%{name}/boot
%{_libexecdir}/xen/boot/hvmloader
%{_libexecdir}/%{name}/boot/xen-shim
/usr/lib/debug%{_libexecdir}/xen/boot/xen-shim-syms
%if %build_stubdom
%{_libexecdir}/xen/boot/xenstore-stubdom.gz
%{_libexecdir}/xen/boot/xenstorepvh-stubdom.gz
%endif
%endif
%if "%{_libdir}" != "/usr/lib"
%{_libdir}/%{name}
%endif
%ghost /usr/lib/%{name}
# General Xen state
%dir %{_localstatedir}/lib/%{name}
%dir %{_localstatedir}/lib/%{name}/dump
%dir %{_localstatedir}/lib/%{name}/images
# Xenstore runtime state
%ghost %{_localstatedir}/run/xenstored

# All xenstore CLI tools
%{_bindir}/xenstore
%{_bindir}/xenstore-*
#%#{_bindir}/remus
# XSM
%{_bindir}/flask-*
# Misc stuff
%ifnarch aarch64
%{_bindir}/xen-detect
%endif
%{_bindir}/xencov_split
%ifnarch aarch64
%{_bindir}/gdbsx
%{_bindir}/xen-kdd
%endif
%ifnarch aarch64
%{_bindir}/xen-hptool
%{_bindir}/xen-hvmcrash
%{_bindir}/xen-hvmctx
%endif
%{_bindir}/xenconsoled
%{_bindir}/xenlockprof
%{_bindir}/xenmon
%{_bindir}/xentop
%{_bindir}/xentrace_setmask
%{_bindir}/xenbaked
%{_bindir}/xenstored
%{_bindir}/xenpm
%{_bindir}/xenpmd
%{_bindir}/xenperf
%{_bindir}/xenwatchdogd
%{_bindir}/xl
%ifnarch aarch64
%{_bindir}/xen-lowmemd
%endif
%{_bindir}/xencov
%ifnarch aarch64
%{_bindir}/xen-mfndump
%endif
%{_bindir}/xenalyze
%{_bindir}/xentrace
%{_bindir}/xentrace_setsize
%ifnarch aarch64
%{_bindir}/xen-cpuid
%endif
%{_bindir}/xen-livepatch
%{_bindir}/xen-diag
%ifnarch armv7hl aarch64
%{_bindir}/xen-ucode
%{_bindir}/xen-memshare
%{_bindir}/xen-mceinj
%{_bindir}/xen-vmtrace
%endif
%{_bindir}/vchan-socket-proxy
%{_bindir}/xenhypfs
%{_bindir}/xen-access

# Xen logfiles
%dir %attr(0700,root,root) %{_localstatedir}/log/xen
# Guest/HV console logs
%dir %attr(0700,root,root) %{_localstatedir}/log/xen/console

%files hypervisor
%if %build_hyp
%ifnarch aarch64
/boot/xen-*.gz
/boot/xen*.config
%else
/boot/xen*
%endif
%if %build_xsm
%dir %attr(0755,root,root) /boot/flask
/boot/flask/xenpolicy*
%endif
/usr/lib/debug/xen*
%endif
%if %build_efi
%{_libdir}/efi/*.efi
%endif

%if %build_docs
%files doc
%doc docs/misc/
%doc dist/install/usr/share/doc/xen/html
%endif

%files devel
%{_includedir}/*.h
%dir %{_includedir}/xen
%{_includedir}/xen/*
%dir %{_includedir}/xenstore-compat
%{_includedir}/xenstore-compat/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files licenses
%doc licensedir/*

%if %build_ocaml
%files ocaml
%{_libdir}/ocaml/xen*
%exclude %{_libdir}/ocaml/xen*/*.a
%exclude %{_libdir}/ocaml/xen*/*.cmxa
%exclude %{_libdir}/ocaml/xen*/*.cmx
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner
%{_bindir}/oxenstored
%config(noreplace) %{_sysconfdir}/xen/oxenstored.conf
%{_unitdir}/oxenstored.service

%files ocaml-devel
%{_libdir}/ocaml/xen*/*.a
%{_libdir}/ocaml/xen*/*.cmxa
%{_libdir}/ocaml/xen*/*.cmx
%{_libdir}/ocaml/xsd_glue/*
%{_libexecdir}/xen/ocaml/xsd_glue/xenctrl_plugin/domain_getinfo_v1.cmxs
%endif

%files test
%{_libexecdir}/xen/tests/*

%changelog
%autochangelog

