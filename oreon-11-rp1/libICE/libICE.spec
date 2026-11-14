# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 974e4ed414225eb3c716985df9709f4da8d22a67a2890066bc6dfc89ad298625

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libICE
Version:        1.1.2
Release:        1%{?dist}
Summary:        X.Org X11 ICE runtime library
License:        MIT
URL:            https://www.x.org
Source0:        https://xorg.freedesktop.org/archive/individual/lib/libICE-%{version}.tar.xz
Source1:        libICE-1.1.2.tar.xz.sig
Source2:        gpgkey-4A193C06D35E7C670FA4EF0BA2FB9E081F2D130E.gpg

BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  gnupg2
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  xorg-x11-util-macros

%description
The X.Org X11 ICE (Inter-Client Exchange) runtime library.

%package        devel
Summary:        X.Org X11 libICE development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       xorgproto
Requires:       pkgconfig
Provides:       pkgconfig(ice) = %{version}

%description    devel
X.Org X11 libICE development package.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%build
%configure --disable-static --disable-docs --disable-specs
%make_build

%install
%make_install INSTALL="install -p"
find %{buildroot} -name '*.la' -delete -print
rm -rf %{buildroot}%{_docdir}

%check
make check

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_libdir}/libICE.so.6*

%files devel
%doc doc/ICElib.xml specs/ice.xml
%{_includedir}/X11/ICE/*.h
%{_libdir}/libICE.so
%{_libdir}/pkgconfig/ice.pc

%changelog
%autochangelog
