%global source0_hash 43d98d3795bc2de7920efe81ef2c5de4e9ed1f903c35c939a7d65adc416d6cb8
Name:		scrub
Version:	2.6.1
Release:        1%{?dist}
Summary:        Disk scrubbing program
License:	GPL-2.0-or-later
URL:		https://github.com/chaos/scrub/
Source0:        https://github.com/chaos/scrub/releases/download/%{version}/scrub-%{version}.tar.gz
Patch0:		scrub-2.6.1-symlinks-to-block-device.patch
Patch1:		scrub-2.6.1-use-libgcrypt.patch
Patch2:		scrub-2.6.1-extentonly.patch
Patch3:		scrub-2.5.2-test-use-power-2-filesizes.patch
Patch4:		scrub-2.6.1-analyzer-fixes.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Scrub writes patterns on files or disk devices to make
retrieving the data more difficult.  It operates in one of three
modes: 1) the special file corresponding to an entire disk is scrubbed
and all data on it is destroyed;  2) a regular file is scrubbed and
only the data in the file (and optionally its name in the directory
entry) is destroyed; or 3) a regular file is created, expanded until
the file system is full, then scrubbed as in 2).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1 -b .symlinks-to-block-devices
%patch -P1 -p1 -b .libgcrypt
%patch -P2 -p1 -b .extent-only
%patch -P3 -p1 -b .test-use-power-2-filesizes
%patch -P4 -p1 -b .analyzer-fixes
autoreconf -ifv --include=config

%build

%configure
%{make_build}
%install
%{make_install}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.6.1-12
- Prepare for Oreon 11 (RP1)
