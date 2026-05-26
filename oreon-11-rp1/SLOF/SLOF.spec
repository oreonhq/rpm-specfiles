%undefine _auto_set_build_flags

%global gittagdate 20220719
%global gittagcommit 6b6c16b4

# Disable debuginfo because it is of no use to us.
%global debug_package %{nil}

%define cross 1
%define targetdir qemu

Name:           SLOF
Version:        %{gittagdate}
Release:        10.git%{gittagcommit}%{?dist}
Summary:        Slimline Open Firmware

License:        BSD-3-Clause
URL:            http://www.openfirmware.info/SLOF

Source0:        https://github.com/aik/SLOF/archive/qemu-slof-%{gittagdate}.tar.gz

# the bundled libc stdbool.h is not compatible with C23
# https://github.com/aik/SLOF/pull/5
Patch0:         0001-libc-fix-build-in-C23-mode.patch
# oreon url source checksums begin
%global source0_sha256 7314788415369b2a66a22eb49cf76472305def2053eea886811039e018100a69
%global source0_file qemu-slof-20220719.tar.gz
# oreon url source checksums end

%if 0%{?cross:1}
BuildArch:      noarch
BuildRequires:  gcc-powerpc64-linux-gnu
%else
ExclusiveArch:  ppc64le
BuildArch: noarch
%endif

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(Data::Dumper)

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/qemu-slof-20220719.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7314788415369b2a66a22eb49cf76472305def2053eea886811039e018100a69" || { echo "oreon: Source0 SHA256 mismatch for qemu-slof-20220719.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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


%files
%doc LICENSE
%doc README
%dir %{_datadir}/%{targetdir}
%{_datadir}/%{targetdir}/slof.bin


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{gittagdate}-10.git
- Prepare for Oreon 11 (RP1)
