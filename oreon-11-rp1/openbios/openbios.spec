%global source0_hash c15375bcca5e465e5716bfc3ac74d819020e5fc120b855280f767fa91697c894
%global hash c3a19c1
%global date 20240913
%undefine _auto_set_build_flags
%global _binaries_in_noarch_packages_terminate_build 0
Name:           openbios
Version:        %{date}
Release:        1%{?dist}
Epoch:          1
Summary:        OpenBIOS implementation of IEEE 1275-1994
License:        GPL-2.0-only
URL:            http://www.openfirmware.info/OpenBIOS
BuildArch:      noarch
Source0:        %{name}-%{version}-git%{hash}.tar.xz
# oreon:deps
BuildRequires:  fcode-utils
BuildRequires:  gcc
BuildRequires:  gcc-powerpc64-linux-gnu
BuildRequires:  gcc-sparc64-linux-gnu
BuildRequires:  libxslt
BuildRequires:  make
# /oreon:deps
%description
The OpenBIOS project provides you with most free and open source Open
Firmware implementations available. Here you find several
implementations of IEEE 1275-1994 (Referred to as Open Firmware)
compliant firmware. Among its features, Open Firmware provides an
instruction set independent device interface. This can be used to boot
the operating system from expansion cards without native
initialization code.

It is Open Firmware's goal to work on all common platforms, like x86,
AMD64, PowerPC, ARM and Mips. With its flexible and modular design,
Open Firmware targets servers, workstations and embedded systems,
where a sane and unified firmware is a crucial design goal and reduces
porting efforts noticably.

Open Firmware is found on many servers and workstations and there are
sever commercial implementations from SUN, Firmworks, CodeGen, Apple,
IBM and others.

In most cases, the Open Firmware implementations provided on this site
rely on an additional low-level firmware for hardware initialization,
such as coreboot or U-Boot.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{date}-git%{hash}

%build

sed -i -e "s/-Werror/-Wno-error/" Makefile.target
/bin/sh config/scripts/switch-arch ppc
make build-verbose V=1 %{?_smp_mflags}
/bin/sh config/scripts/switch-arch sparc32
make build-verbose V=1 %{?_smp_mflags}
/bin/sh config/scripts/switch-arch sparc64
make build-verbose V=1 %{?_smp_mflags}
%install
qemudir=$RPM_BUILD_ROOT%{_datadir}/qemu
mkdir -p $qemudir
cp -a obj-ppc/openbios-qemu.elf $qemudir/openbios-ppc
cp -a obj-sparc32/openbios-builtin.elf $qemudir/openbios-sparc32
cp -a obj-sparc64/openbios-builtin.elf $qemudir/openbios-sparc64
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
