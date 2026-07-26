%global source0_hash 7839b19ac15ba554e1a1fc1dbe898f62cf2fd4db3dcdc126515facc6b929746f

Name:		cpmtools
Version:	2.23
Release:	12%{?dist}
Summary:	Programs for accessing CP/M disks

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://www.moria.de/~michael/cpmtools/
Source0:	http://www.moria.de/~michael/cpmtools/files/cpmtools-%{version}.tar.gz
Patch0:		cpmtools-2.23-nostrip.patch
Patch1: cpmtools-configure-c99.patch

BuildRequires:	gcc
BuildRequires:	ncurses-devel, libdsk-devel
BuildRequires:	make
#Requires:

%description
This package allows to access CP/M file systems similar to the well-known
mtools package, which accesses MSDOS file systems. I use it for file
exchange with a Z80-PC simulator, but it works on floppy devices as well.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%patch -P0 -p1 -b .nostrip
%patch -P1 -p1
sed -i -e "s!@datarootdir@/diskdefs!\$\(DATADIR\)/diskdefs!" Makefile.in
#modify path contained in man files
sed -i -e "s!@DATADIR@!%{_datadir}/%{name}!" *.1.in

%build
%configure --datarootdir=%{_datadir}/%{name} --with-libdsk
make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man{1,5}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
make install BINDIR=$RPM_BUILD_ROOT%{_bindir} MANDIR=$RPM_BUILD_ROOT%{_mandir} DATADIR=$RPM_BUILD_ROOT%{_datadir}/%{name} INSTALL="install -p"

%files
%doc COPYING NEWS README
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/*

%changelog
%autochangelog
