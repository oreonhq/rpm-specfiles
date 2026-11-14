# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 72b922c2e765434e9e9f0960148070bd4504b288263e2868a4ccce1b7cf2767a

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libXrandr
Version:        1.5.5
Release:        1%{?dist}
Summary:        X.Org X11 libXrandr runtime library
License:        HPND-sell-variant
URL:            https://www.x.org
Source0:        https://xorg.freedesktop.org/archive/individual/lib/libXrandr-%{version}.tar.xz
Source1:        libXrandr-1.5.5.tar.xz.sig
Source2:        gpgkey-3AB285232C46AE43D8E192F4DAB0F78EA6E7E2D2.gpg

BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  gnupg2
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  xorg-x11-util-macros

%description
The X.Org X11 libXrandr runtime library.

%package        devel
Summary:        X.Org X11 libXrandr development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libX11-devel
Requires:       libXext-devel
Requires:       libXrender-devel
Requires:       xorgproto
Requires:       pkgconfig
Provides:       pkgconfig(xrandr) = %{version}

%description    devel
X.Org X11 libXrandr development package.

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
%{_libdir}/libXrandr.so.2*

%files devel
%{_includedir}/X11/extensions/Xrandr.h
%{_libdir}/libXrandr.so
%{_libdir}/pkgconfig/xrandr.pc
%{_mandir}/man3/*.3*

%changelog
%autochangelog
