Name:		scrub
Version:	2.6.1
Release:	12%{?dist}
Summary:	Disk scrubbing program
License:	GPL-2.0-or-later
URL:		https://github.com/chaos/scrub/
Source0:	https://github.com/chaos/scrub/releases/download/%{version}/scrub-%{version}.tar.gz
# https://github.com/chaos/scrub/commit/b90fcb2330d00dbd1e9aeaa2e1a9807f8b80b922.patch
Patch0:		scrub-2.6.1-symlinks-to-block-device.patch
# https://github.com/chaos/scrub/commit/27f6452a658f057e3ba6bf9dfda070b6dffc6798.patch
Patch1:		scrub-2.6.1-use-libgcrypt.patch
Patch2:		scrub-2.6.1-extentonly.patch
Patch3:		scrub-2.5.2-test-use-power-2-filesizes.patch
# https://github.com/chaos/scrub/commit/864a454f16ac3e47103064b0e4fe3a9111593e49
Patch4:		scrub-2.6.1-analyzer-fixes.patch
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	libgcrypt-devel
BuildRequires:	autoconf, automake, libtool

%description
Scrub writes patterns on files or disk devices to make
retrieving the data more difficult.  It operates in one of three
modes: 1) the special file corresponding to an entire disk is scrubbed
and all data on it is destroyed;  2) a regular file is scrubbed and
only the data in the file (and optionally its name in the directory
entry) is destroyed; or 3) a regular file is created, expanded until
the file system is full, then scrubbed as in 2).

%prep
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

%files
%license COPYING
%doc DISCLAIMER
%doc README ChangeLog
%{_bindir}/scrub
%{_mandir}/man1/scrub.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.6.1-12
- Prepare for Oreon 11 (RP1)
