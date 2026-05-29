%global source0_hash f71874dacec25c699af2c79cbf4d2bc08dae7d42f3e371812a0cc6fc114e61dc

Summary: X Resource Monitor
Name: xrestop
Version: 0.6
Release: 7%{?dist}
License: GPL-2.0-or-later
URL: http://www.freedesktop.org/Software/xrestop
Source0: https://gitlab.freedesktop.org/xorg/app/xrestop/-/archive/xrestop-%{version}/xrestop-xrestop-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires: ncurses-devel libXres-devel libXext-devel libX11-devel
BuildRequires: libXau-devel

%description
A utility to monitor application usage of X resources in the X Server, and
display them in a manner similar to 'top'.  This is a very useful utility
for tracking down application X resource usage leaks.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n xrestop-xrestop-%{version}

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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6-7
- Import
