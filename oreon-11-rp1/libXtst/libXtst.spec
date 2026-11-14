# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f94f0b37c07d80d877f3eda2c2405cc7e62aa9842f6310354aa349e3d66a4fe5

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libXtst
Version:        1.2.6
Release:        1%{?dist}
Summary:        X.Org X11 libXtst runtime library
License:        MIT AND X11
URL:            https://www.x.org
Source0:        https://xorg.freedesktop.org/archive/individual/lib/libXtst-%{version}.tar.xz
Source1:        libXtst-1.2.6.tar.xz.sig
Source2:        gpgkey-3AB285232C46AE43D8E192F4DAB0F78EA6E7E2D2.gpg

BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  gnupg2
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(recordproto)
BuildRequires:  xorg-x11-util-macros

%description
The X.Org X11 libXtst (XTEST and RECORD extensions) runtime library.

%package        devel
Summary:        X.Org X11 libXtst development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libX11-devel
Requires:       libXext-devel
Requires:       libXi-devel
Requires:       xorgproto
Requires:       pkgconfig
Provides:       pkgconfig(xtst) = %{version}

%description    devel
X.Org X11 libXtst development package.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%build
%configure --disable-static --disable-specs
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
%doc ChangeLog README.md
%{_libdir}/libXtst.so.6*

%files devel
%doc specs/recordlib.xml specs/xtestlib.xml
%{_includedir}/X11/extensions/XTest.h
%{_includedir}/X11/extensions/record.h
%{_libdir}/libXtst.so
%{_libdir}/pkgconfig/xtst.pc
%{_mandir}/man3/*.3*

%changelog
%autochangelog
