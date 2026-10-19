%global source0_hash 7314788415369b2a66a22eb49cf76472305def2053eea886811039e018100a69
%undefine _auto_set_build_flags
%global gittagdate 20220719
%global gittagcommit 6b6c16b4
%global debug_package %{nil}
%define cross 1
%define targetdir qemu
Name:           SLOF
Version:        %{gittagdate}
Release:        1%{?dist}
Summary:        Slimline Open Firmware
License:        BSD-3-Clause
URL:            http://www.openfirmware.info/SLOF
Source0:        https://github.com/aik/%{name}/archive/refs/tags/%{targetdir}-slof-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-libc-fix-build-in-C23-mode.patch
%if 0%{?cross:1}
BuildArch:      noarch
%else
ExclusiveArch:  ppc64le
BuildArch: noarch
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-powerpc64-linux-gnu
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Slimline Open Firmware (SLOF) is initialization and boot source code
based on the IEEE-1275 (Open Firmware) standard, developed by
engineers of the IBM Corporation.

The SLOF source code provides illustrates what's needed to initialize
and boot Linux or a hypervisor on the industry Open Firmware boot
standard.

Note that you normally wouldn't need to install this package
separately.  It is a dependency of qemu-system-ppc64.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n SLOF-qemu-slof-%{gittagdate}
%autopatch -p1

%build

%if 0%{?cross:1}
export CROSS="powerpc64-linux-gnu-"
%else
export CROSS=""
%endif
%make_build qemu V=2
%install
mkdir -p %{buildroot}%{_datadir}/%{targetdir}
install -c -m 0644 boot_rom.bin %{buildroot}%{_datadir}/%{targetdir}/slof.bin
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{gittagdate}-10.git
- Prepare for Oreon 11 (RP1)
