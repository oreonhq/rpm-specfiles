# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ddd6057b89a91903bc2f884d55c8467440906945e482c36547260dff28661afc

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libXi
Version:        1.8.4
Release:        1%{?dist}
Summary:        X.Org X11 libXi runtime library
License:        MIT AND X11
URL:            https://www.x.org
Source0:        https://xorg.freedesktop.org/archive/individual/lib/libXi-%{version}.tar.xz
Source1:        libXi-1.8.4.tar.xz.sig
Source2:        gpgkey-3AB285232C46AE43D8E192F4DAB0F78EA6E7E2D2.gpg

BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  gnupg2
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  xorg-x11-util-macros

%description
The X.Org X11 libXi runtime library.

%package        devel
Summary:        X.Org X11 libXi development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libX11-devel
Requires:       libXext-devel
Requires:       libXfixes-devel
Requires:       xorgproto
Requires:       pkgconfig
Provides:       pkgconfig(xi) = %{version}

%description    devel
X.Org X11 libXi development package.

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
%doc ChangeLog README.md
%{_libdir}/libXi.so.6*

%files devel
%doc specs/encoding.xml specs/inputlib.xml specs/library.xml
%{_includedir}/X11/extensions/XInput.h
%{_includedir}/X11/extensions/XInput2.h
%{_libdir}/libXi.so
%{_libdir}/pkgconfig/xi.pc
%{_mandir}/man3/*.3*

%changelog
%autochangelog
