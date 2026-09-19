%global source0_hash 30f37fc734572c1dbaa2504585bc23ba6b8fd7df767ae7155995b2ca0ebed960

Summary: Utility for creating romfs file systems
Name: genromfs
Version: 0.5.2
Release: 38%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://romfs.sourceforge.net/
Source: http://downloads.sourceforge.net/romfs/%{name}-%{version}.tar.gz
Patch: genromfs-0.5.2-Makefile.patch

BuildRequires: gcc
BuildRequires: make

%description
Genromfs is a tool for creating romfs file systems, which are
lightweight, read-only file systems supported by the Linux
kernel. Romfs file systems are mainly used for the initial RAM disks
used during installation.

Install genromfs if you need to create romfs file systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# the macro %{?_smp_mflags} was not considered useful as there is only one
# module to be built
make CFLAGS="$RPM_OPT_FLAGS"' -Wall -DVERSION=\"$(VERSION)\"' LDFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf ${RPM_BUILD_ROOT}

%makeinstall

%files
%doc COPYING NEWS
%{_bindir}/*
%{_mandir}/man8/*

%changelog
%autochangelog
