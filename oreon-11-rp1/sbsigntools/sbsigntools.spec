%global source0_hash b43a33c755cd0dd3d0610a8234810771b6cea6af24f11c09f533138dca80e06f

%bcond check 0
%define _warning_options -Wall -Werror=format-security -Wno-deprecated-declarations -Wno-maybe-uninitialized

Name:          sbsigntools
Version:       0.9.5
Release:       14%{?dist}
Summary:       Signing utility for UEFI secure boot
# Most source code is GPL-3.0-or-later, except:
# LicenseRef-Fedora-Public-Domain:
#   lib/ccan/ccan/array_size
#   lib/ccan/ccan/build_assert
#   lib/ccan/ccan/check_type
#   lib/ccan/ccan/compiler
#   lib/ccan/ccan/container_of
#   lib/ccan/ccan/hash
#   lib/ccan/ccan/str
#   lib/ccan/ccan/tcon
# LGPL-2.1-or-later:
#   lib/ccan/ccan/endian
#   lib/ccan/ccan/htable
#   lib/ccan/ccan/list
#   lib/ccan/ccan/read_write_all
#   lib/ccan/ccan/talloc
#   lib/ccan/ccan/typesafe_cb
# LGPL-3.0-only:
#   lib/ccan/ccan/failtest
#   lib/ccan/ccan/tlist
# MIT:
#   lib/ccan/ccan/time
License:       GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain AND LGPL-2.1-or-later AND LGPL-3.0-only AND MIT
URL:           https://build.opensuse.org/package/show/home:jejb1:UEFI/sbsigntools
# upstream tarballs don't include bundled ccan
# run sbsigntools-mktarball.sh
Source0:       %{name}-%{version}.tar.xz
Source1:       %{name}-mktarball.sh
# don't fetch ccan or run git from autogen.sh, already done by mktarball.sh
Patch0:        %{name}-no-git.patch
# add Fedora gnu-efi path and link statically against libefi.a/libgnuefi.a
Patch1:        %{name}-gnuefi.patch
# fix wchar_t (a.k.a. CHAR16) abuse
Patch2:        %{name}-no-wchar_t.patch
# revert addition of openssl engine support
Patch3:        %{name}-no-openssl-engines.patch
# avoid wrong --target option usage that's been fixed in recent binutils
Patch4:        %{name}-binutils.patch
# remove unused variable
Patch5:        %{name}-unused-var.patch
# same as gnu-efi
ExclusiveArch: x86_64 aarch64 %{arm} %{ix86} riscv64
BuildRequires: make
BuildRequires: automake
BuildRequires: binutils-devel
BuildRequires: gcc
BuildRequires: gnu-efi-devel >= 1:3.0.18-1
BuildRequires: help2man
BuildRequires: libuuid-devel
%if %{with check}
BuildRequires: openssl
%endif
BuildRequires: openssl-devel
%if 0%{?fedora} >= 41
# https://fedoraproject.org/wiki/Changes/OpensslDeprecateEngine
BuildRequires: openssl-devel-engine
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

%description
Tools to add signatures to EFI binaries and Drivers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
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
