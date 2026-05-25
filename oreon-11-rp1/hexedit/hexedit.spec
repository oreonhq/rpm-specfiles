%global forgeurl https://github.com/pixel/hexedit

Version: 1.6
%forgemeta

Summary: A hexadecimal file viewer and editor
Name: hexedit
Release: 10%{?dist}
License: GPL-2.0-or-later
URL: http://rigaux.org/hexedit.html
Source: %{forgesource}

Patch1: hexedit-1.2.13-config.patch
# Document --color option.  Sent upstream 2013-04-05.
Patch2: hexedit-1.6-fix-lsm.patch

BuildRequires: ncurses-devel
BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf

%description
Hexedit shows a file both in ASCII and in hexadecimal. The file can be a device
as the file is read a piece at a time. Hexedit can be used to modify the file
and search through it.

%prep
%forgesetup

%patch -P1 -p1 -b .config
%patch -P2 -p1

%build
./autogen.sh
%configure
make %{_smp_mflags}

%install
make install \
  mandir=$RPM_BUILD_ROOT%{_mandir} \
  bindir=$RPM_BUILD_ROOT%{_bindir} \
  INSTALL='install -p'

%files
%doc hexedit.lsm COPYING Changes
%{_bindir}/hexedit
%{_mandir}/man1/hexedit.1*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6-10
- Import
