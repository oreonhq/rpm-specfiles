# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash e0a774b33324f4d4c05b199ea45050f87206586d81655f8bef4dba434d931288

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libXt
Version:        1.3.1
Release:        1%{?dist}
Summary:        X.Org X11 libXt runtime library
License:        MIT AND HPND-sell-variant AND SMLNJ AND MIT-open-group AND X11
URL:            https://www.x.org
Source0:        https://xorg.freedesktop.org/archive/individual/lib/libXt-%{version}.tar.xz
Source1:        libXt-1.3.1.tar.xz.sig
Source2:        gpgkey-3BB639E56F861FA2E86505690FDD682D974CA72A.gpg

BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  gnupg2
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  xorg-x11-util-macros

%description
The X.Org X11 libXt (X Toolkit Intrinsics) runtime library.

%package        devel
Summary:        X.Org X11 libXt development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libICE-devel
Requires:       libSM-devel
Requires:       libX11-devel
Requires:       xorgproto
Requires:       pkgconfig
Provides:       pkgconfig(xt) = %{version}

%description    devel
X.Org X11 libXt development package.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%build
%configure --disable-static --disable-specs --enable-unit-tests
%make_build

%install
%make_install INSTALL="install -p"
find %{buildroot} -name '*.la' -delete -print
mkdir -p %{buildroot}%{_datadir}/X11/app-defaults
rm -rf %{buildroot}%{_docdir}

%check
make check

%ldconfig_scriptlets

%files
%license COPYING
%doc ChangeLog README.md
%{_libdir}/libXt.so.6*
%dir %{_datadir}/X11/app-defaults

%files devel
%doc specs/*.xml
%{_includedir}/X11/*.h
%{_libdir}/libXt.so
%{_libdir}/pkgconfig/xt.pc
%{_mandir}/man3/*.3*

%changelog
%autochangelog
