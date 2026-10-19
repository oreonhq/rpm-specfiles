%global source0_hash 01c3a63a285d75626a33ab19a998a9b115432933a9f84e8cb94b142c01ef6d6f
Name:    fwts
Version: 26.03.00
Release:        1%{?dist}
Summary:        Firmware Test Suite
URL: https://wiki.ubuntu.com/FirmwareTestSuite
License: GPL-2.0-only AND LicenseRef-Callaway-LGPLv2 AND (GPL-2.0-only OR Intel-ACPI)
Source0:        http://fwts.ubuntu.com/release/fwts-V%{version}.tar.gz
Patch0: fwts-Remove-Werror-from-build.patch
ExclusiveArch: x86_64 aarch64 riscv64 ppc64le
# oreon:deps
BuildRequires:  acpica-tools
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  dkms
BuildRequires:  flex
BuildRequires:  glib2-devel
BuildRequires:  json-c-devel
BuildRequires:  kernel-devel
BuildRequires:  libbsd-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pciutils-devel
# /oreon:deps
%description
Firmware Test Suite (FWTS) is a test suite that performs sanity checks on
Intel/AMD PC firmware. It is intended to identify BIOS and ACPI errors and if
appropriate it will try to explain the errors and give advice to help
workaround or fix firmware bugs. It is primarily intended to be a Linux-specific
firmware troubleshooting tool.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%define _lto_cflags %{nil}
autoreconf -ivf
%configure
%make_build -j1
%check

%make_build check
%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
find %{buildroot} -type f -name "*.a" -delete
find %{buildroot} -type f -name "*.so" -delete
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
