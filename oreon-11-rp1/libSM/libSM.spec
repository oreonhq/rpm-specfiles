# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash be7c0abdb15cbfd29ac62573c1c82e877f9d4047ad15321e7ea97d1e43d835be

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libSM
Version:        1.2.6
Release:        1%{?dist}
Summary:        X.Org X11 SM runtime library
License:        MIT
URL:            https://www.x.org
Source0:        https://xorg.freedesktop.org/archive/individual/lib/libSM-%{version}.tar.xz
Source1:        libSM-1.2.6.tar.xz.sig
Source2:        gpgkey-4A193C06D35E7C670FA4EF0BA2FB9E081F2D130E.gpg

BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  gnupg2
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  libuuid-devel
BuildRequires:  xorg-x11-util-macros

%description
The X.Org X11 SM (Session Management) runtime library.

%package        devel
Summary:        X.Org X11 libSM development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libICE-devel
Requires:       xorgproto
Requires:       pkgconfig
Provides:       pkgconfig(sm) = %{version}

%description    devel
X.Org X11 libSM development package.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%build
%configure --disable-static --disable-docs --with-libuuid
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
%{_libdir}/libSM.so.6*

%files devel
%doc doc/SMlib.xml doc/xsmp.xml
%{_includedir}/X11/SM/*.h
%{_libdir}/libSM.so
%{_libdir}/pkgconfig/sm.pc

%changelog
%autochangelog
