%global source0_hash fa93920ef80a406115c1de6f7764ffa4c34e3d1bd7890b9145c36de899a258f5
%bcond check 0
%define _warning_options -Wall -Werror=format-security -Wno-deprecated-declarations -Wno-maybe-uninitialized
Name:          sbsigntools
Version:       0.9.5
Release:        1%{?dist}
Summary:        Signing utility for UEFI secure boot
License:       GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain AND LGPL-2.1-or-later AND LGPL-3.0-only AND MIT
URL:           https://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git
Source0:        https://deb.debian.org/debian/pool/main/s/sbsigntool/sbsigntool_%{version}.orig.tar.gz#/%{name}-%{version}.tar.gz
Source1:       %{name}-mktarball.sh
Patch0:        %{name}-no-git.patch
Patch1:        %{name}-gnuefi.patch
Patch2:        %{name}-no-wchar_t.patch
Patch3:        %{name}-no-openssl-engines.patch
Patch4:        %{name}-binutils.patch
Patch5:        %{name}-unused-var.patch
ExclusiveArch: x86_64 aarch64 %{arm} %{ix86} riscv64
%if %{with check}
%endif
%if 0%{?fedora} >= 41 || 0%{?oreon} >= 11
%endif
Provides: bundled(ccan-array_size)
Provides: bundled(ccan-build_assert)
Provides: bundled(ccan-check_type)
Provides: bundled(ccan-compiler)
Provides: bundled(ccan-container_of)
Provides: bundled(ccan-endian)
Provides: bundled(ccan-failtest)
Provides: bundled(ccan-hash)
Provides: bundled(ccan-htable)
Provides: bundled(ccan-list)
Provides: bundled(ccan-read_write_all)
Provides: bundled(ccan-str)
Provides: bundled(ccan-talloc)
Provides: bundled(ccan-tcon)
Provides: bundled(ccan-time)
Provides: bundled(ccan-tlist)
Provides: bundled(ccan-typesafe_cb)
# oreon:deps
BuildRequires:  automake
BuildRequires:  binutils-devel
BuildRequires:  gcc
BuildRequires:  gnu-efi-devel
BuildRequires:  help2man
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
# /oreon:deps
%description
Tools to add signatures to EFI binaries and Drivers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n sbsigntool-%{version}
%patch -p 1 -P 0
%patch -p 1 -P 1
%patch -p 1 -P 2
%if %{defined el10}
# EL10 disables openssl engines
%patch -p 1 -P 3
%endif
%patch -p 1 -P 4
%patch -p 1 -P 5

%build

./autogen.sh
%configure
%make_build
%install
%make_install
%oreon_autofiles main
%if %{with check}
%check

make check
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
