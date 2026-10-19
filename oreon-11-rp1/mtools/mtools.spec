%global source0_hash 10cd1111da87bf2400a380c1639a6cba8bfb937a24f9c51f5f88d393ae5f6f76
Summary:        Programs for accessing MS-DOS disks without mounting the disks
Name: mtools
Version: 4.0.49
Release:        1%{?dist}
License: GPL-3.0-or-later
Source0:        https://mirrors.kernel.org/gnu/mtools/mtools-%{version}.tar.gz
Url: https://www.gnu.org/software/mtools/
Patch0: mtools-3.9.6-config.patch
%if ! 0%{?flatpak}
Requires: glibc-gconv-extra
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  texinfo
# /oreon:deps
%description
Mtools is a collection of utilities for accessing MS-DOS files.
Mtools allow you to read, write and move around MS-DOS filesystem
files (normally on MS-DOS floppy disks).  Mtools supports Windows95
style long file names, OS/2 XDF disks, and 2m disks

Mtools should be installed if you need to use MS-DOS disks

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}
%patch -P0 -p1 -b .conf

%build

autoreconf -fiv
%configure --disable-floppyd
%make_build
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc $RPM_BUILD_ROOT/%{_infodir}
%make_install
install -m644 mtools.conf $RPM_BUILD_ROOT/etc
gzip -9f $RPM_BUILD_ROOT/%{_infodir}/*
find $RPM_BUILD_ROOT -name "floppyd*" -exec rm {} \;
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir.gz
ln -s mtools.5.gz %{buildroot}%{_mandir}/man5/mtools.conf.5.gz
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Fri Apr 03 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0.49-1
- Use HTTPS for GNU mtools tarball (spectool and firewalls often block FTP)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0.49-1
- Prepare for Oreon 11 (RP1)
