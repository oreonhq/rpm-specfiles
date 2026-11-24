# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash fa93920ef80a406115c1de6f7764ffa4c34e3d1bd7890b9145c36de899a258f5
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond_without check
%define _warning_options -Wall -Werror=format-security -Wno-deprecated-declarations -Wno-maybe-uninitialized

Name:          sbsigntools
Version:       0.9.5
Release:       1%{?dist}
Summary:       Signing utility for UEFI secure boot
License:       GPL-3.0-or-later AND LicenseRef-Oreon-Public-Domain AND LGPL-2.1-or-later AND LGPL-3.0-only AND MIT
URL:           https://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git
Source0:       https://deb.debian.org/debian/pool/main/s/sbsigntool/sbsigntool_%{version}.orig.tar.gz#/%{name}-%{version}.tar.gz
Patch0:        %{name}-no-git.patch
Patch1:        %{name}-gnuefi.patch
Patch2:        %{name}-no-wchar_t.patch
Patch3:        %{name}-no-openssl-engines.patch
Patch4:        %{name}-binutils.patch
Patch5:        %{name}-unused-var.patch
Patch6:        %{name}-intermediate-cert-verify.patch
ExclusiveArch: x86_64 aarch64 %{arm} %{ix86} riscv64
BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: automake
BuildRequires: binutils-devel
BuildRequires: clang
BuildRequires: gnu-efi-devel >= 1:3.0.18-1
BuildRequires: help2man
BuildRequires: libuuid-devel
%if %{with check}
BuildRequires: openssl
%endif
BuildRequires: openssl-devel
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

%description
Tools to add signatures to EFI binaries and Drivers.

%prep
%oreon_sha256
%setup -q -n sbsigntool-%{version}
%patch -p 1 -P 0
%patch -p 1 -P 1
%patch -p 1 -P 2
%patch -p 1 -P 3
%patch -p 1 -P 4
%patch -p 1 -P 5
%patch -p 1 -P 6

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%if %{with check}
%check
make check
%endif

%files
%license COPYING LICENSE.GPLv3 lib/ccan/licenses/*
%doc AUTHORS ChangeLog
%{_bindir}/sbattach
%{_bindir}/sbkeysync
%{_bindir}/sbsiglist
%{_bindir}/sbsign
%{_bindir}/sbvarsign
%{_bindir}/sbverify
%{_mandir}/man1/sbattach.1.*
%{_mandir}/man1/sbkeysync.1.*
%{_mandir}/man1/sbsiglist.1.*
%{_mandir}/man1/sbsign.1.*
%{_mandir}/man1/sbvarsign.1.*
%{_mandir}/man1/sbverify.1.*

%changelog
%autochangelog
