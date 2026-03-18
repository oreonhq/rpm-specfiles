%global pkgname xbitmaps

%global debug_package %{nil}

Summary: X.Org X11 application bitmaps
Name: xorg-x11-%{pkgname}
Version: 1.1.3
Release: 6%{?dist}
License: HPND AND ICU
URL: http://www.x.org
BuildArch: noarch

Source0: https://www.x.org/pub/individual/data/xbitmaps-%{version}.tar.xz

BuildRequires: make
BuildRequires: automake gcc
Requires: pkgconfig

%description
X.Org X11 application bitmaps

%prep
%setup -q -n xbitmaps-%{version}

%build
%configure
%make_build

%install
%make_install

%files
%doc COPYING
%{_includedir}/X11
%{_datadir}/pkgconfig/xbitmaps.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.3-6
- Prepare for Oreon 11 (RP1)
