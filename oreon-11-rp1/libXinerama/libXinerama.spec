# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d00fc1599c303dc5cbc122b8068bdc7405d6fcb19060f4597fc51bd3a8be51d7

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libXinerama
Version:        1.1.6
Release:        1%{?dist}
Summary:        X.Org X11 libXinerama runtime library
License:        MIT
URL:            https://www.x.org
Source0:        https://xorg.freedesktop.org/archive/individual/lib/libXinerama-%{version}.tar.xz
Source1:        libXinerama-1.1.6.tar.xz.sig
Source2:        gpgkey-3AB285232C46AE43D8E192F4DAB0F78EA6E7E2D2.gpg

BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  gnupg2
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  xorg-x11-util-macros

%description
The X.Org X11 libXinerama runtime library.

%package        devel
Summary:        X.Org X11 libXinerama development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libX11-devel
Requires:       libXext-devel
Requires:       xorgproto
Requires:       pkgconfig
Provides:       pkgconfig(xinerama) = %{version}

%description    devel
X.Org X11 libXinerama development package.

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
%doc ChangeLog README.md
%{_libdir}/libXinerama.so.1*

%files devel
%{_includedir}/X11/extensions/Xinerama.h
%{_includedir}/X11/extensions/panoramiXext.h
%{_libdir}/libXinerama.so
%{_libdir}/pkgconfig/xinerama.pc
%{_mandir}/man3/*.3*

%changelog
%autochangelog
