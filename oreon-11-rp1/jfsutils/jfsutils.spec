%global source0_hash 244a15f64015ce3ea17e49bdf6e1a0fb4f9af92b82fa9e05aa64cb30b5f07a4d

%define _legacy_common_support 1

Summary: Utilities for managing the JFS filesystem
Name: jfsutils
Version: 1.1.15
Release: 32%{?dist}
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0: jfsutils-1.1.15_stdint.patch
Patch1: jfsutils_format-security_ftbs.patch
Patch2: jfsutils_sysmacros.patch
URL: http://jfs.sourceforge.net/
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Buildrequires: libuuid-devel

BuildRequires:  gcc
BuildRequires: make
%description
The jfsutils package contains a number of utilities for creating,
checking, modifying, and correcting any inconsistencies in JFS
filesystems.  The following utilities are available: fsck.jfs - initiate
replay of the JFS transaction log, and check and repair a JFS formatted
device; logdump - dump a JFS formatted device's journal log; logredo -
"replay" a JFS formatted device's journal log;  mkfs.jfs - create a JFS
formatted partition; xchkdmp - dump the contents of a JFS fsck log file
created with xchklog; xchklog - extract a log from the JFS fsck workspace
into a file;  xpeek - shell-type JFS file system editor.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
find . -type f -name *.[ch] -exec chmod -x {} \;
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%configure 
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_sbindir}/*
%{_mandir}/man8/*
%doc AUTHORS COPYING NEWS ChangeLog

%changelog
%autochangelog
