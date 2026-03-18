Name:    pinfo
Version: 0.6.13
Release: 10%{?dist}
Summary: An info file viewer
License: GPL-2.0-only

URL:    https://github.com/baszoetekouw/pinfo
Source: %{url}/archive/refs/tags/v%{version}.tar.gz

Patch1: pinfo-0.6.9-infopath.patch
Patch2: pinfo-0.6.9-xdg.patch
Patch3: pinfo-0.6.10-man.patch
Patch4: pinfo-0.6.13-fnocommon.patch
Patch5: pinfo-0.6.13-gccwarn.patch
Patch6: pinfo-0.6.13-nogroup.patch
Patch7: pinfo-0.6.13-stringop-overflow.patch
Patch8: pinfo-configure-c99.patch

BuildRequires: automake
BuildRequires: gcc
BuildRequires: gettext-devel
BuildRequires: libtool
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: texinfo

Requires: xdg-utils

%description
Pinfo is an info file (or man page) viewer with a user interface
similar to the Lynx Web browser's interface.  Pinfo supports searching
using regular expressions, and is based on the ncurses library.

%prep
%autosetup -p1

%build
./autogen.sh
%configure --without-readline
%make_build

%install
%make_install

# This file should not be packaged
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md TECHSTUFF
%config(noreplace) %{_sysconfdir}/pinforc
%{_bindir}/pinfo
%{_infodir}/pinfo.info*
%{_mandir}/man1/pinfo.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.13-10
- Prepare for Oreon 11 (RP1)
