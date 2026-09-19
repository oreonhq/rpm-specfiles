%global source0_hash 3893de9a8ebe5543b9b11c4b575075e59509ddb0f26e6229b2554ee625d25687

Name:           cpdup
Version:        1.18
Release:        23%{?dist}
Summary:        Filesystem mirroring utility

%if 0%{?el5}
%endif
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://apollo.backplane.com/FreeSrc/
Source0:        http://apollo.backplane.com/FreeSrc/cpdup-%{version}.tgz
Source1:        Makefile.linux
Patch0:         cpdup-c99.patch

BuildRequires:  gcc
BuildRequires: make

%description
The cpdup utility makes an exact mirror copy of the source in the
destination, creating and deleting files and directories as necessary.
UTimes, hardlinks, softlinks, devices, permissions, and flags are
mirrored.  By default, cpdup asks for confirmation if any file or
directory needs to be removed from the destination and does not copy
files which it believes to have already been synchronized (by
observing that the source and destination file’s size and mtimes
match).  cpdup does not cross mount points in either the source or the
destination.  As a safety measure, cpdup refuses to replace a
destination directory with a file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}
# we don't want this to get compiled
mv md5.c{,.off}
# make scripts non-executable for cleanliness
chmod -x scripts/*

%build
make %{?_smp_mflags} CFLAGS="${RPM_OPT_FLAGS}" -f %{SOURCE1}

%install
make install DESTDIR=$RPM_BUILD_ROOT -f %{SOURCE1}

%files
%doc BACKUPS PORTING scripts
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
