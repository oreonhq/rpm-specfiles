Summary: X Resource Monitor
Name: xrestop
Version: 0.6
Release: 7%{?dist}
License: GPL-2.0-or-later
URL: http://www.freedesktop.org/Software/xrestop
Source0: %{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires: ncurses-devel libXres-devel libXext-devel libX11-devel
BuildRequires: libXau-devel

%description
A utility to monitor application usage of X resources in the X Server, and
display them in a manner similar to 'top'.  This is a very useful utility
for tracking down application X resource usage leaks.

%prep
%setup -q

%build
%configure
make
# SUBDIRS=

%install
rm -rf "$RPM_BUILD_ROOT"
make DESTDIR="$RPM_BUILD_ROOT" install
#SUBDIRS=

%files
%doc AUTHORS COPYING NEWS README.md
%{_bindir}/xrestop
%{_mandir}/man1/xrestop.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6-7
- Prepare for Oreon 11 (RP1)
