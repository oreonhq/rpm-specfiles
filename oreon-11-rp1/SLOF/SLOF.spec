# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 7314788415369b2a66a22eb49cf76472305def2053eea886811039e018100a69
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

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
%oreon_verify_sources
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
