%global source0_hash 2f8b48e492c7e022316907cdd98460eb24f8d29e18f5df1869841e0513f5e26a
Name:		cpmtools
Version:	2.24
Release:        1%{?dist}
Summary:        Programs for accessing CP/M disks
License:	GPL-3.0-or-later
URL:		http://www.moria.de/~michael/cpmtools/
Source0:        http://www.moria.de/~michael/cpmtools/files/cpmtools-%{version}.tar.gz
Patch0:		cpmtools-2.23-nostrip.patch
Patch1: cpmtools-configure-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libdsk-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
