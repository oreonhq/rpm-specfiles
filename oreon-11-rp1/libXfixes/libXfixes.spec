# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 39f115d72d9c5f8111e4684164d3d68cc1fd21f9b27ff2401b08fddfc0f409ba

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libXfixes
Version:        6.0.2
Release:        1%{?dist}
Summary:        X.Org X11 libXfixes runtime library
License:        MIT
URL:            https://www.x.org
Source0:        https://xorg.freedesktop.org/archive/individual/lib/libXfixes-%{version}.tar.xz
Source1:        libXfixes-6.0.2.tar.xz.sig
Source2:        gpgkey-3AB285232C46AE43D8E192F4DAB0F78EA6E7E2D2.gpg

BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  gnupg2
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(fixesproto)
BuildRequires:  xorg-x11-util-macros

%description
The X.Org X11 libXfixes runtime library.

%package        devel
Summary:        X.Org X11 libXfixes development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libX11-devel
Requires:       xorgproto
Requires:       pkgconfig
Provides:       pkgconfig(xfixes) = %{version}

%description    devel
X.Org X11 libXfixes development package.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%build
%configure --disable-static
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
%{_libdir}/libXfixes.so.3*

%files devel
%{_includedir}/X11/extensions/Xfixes.h
%{_libdir}/libXfixes.so
%{_libdir}/pkgconfig/xfixes.pc
%{_mandir}/man3/*.3*

%changelog
%autochangelog
