# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0b4a3649ee8d683b9cce2ef094df4fb039d276c0cef7e49337c43d3b297b9f42

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libva
Version:        2.24.1
Release:        2%{?dist}
Summary:        Video Acceleration (VA) API for Linux

License:        MIT AND HPND-sell-variant AND ICU
URL:            https://github.com/intel/libva
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-%{version}.tar.gz.asc
# Intel Media Stack Release, 421E5C3C1148E3DB9372378E8B99990502A81421
Source2:        gpgkey-421E5C3C1148E3DB9372378E8B99990502A81421.gpg

BuildRequires:  oreon-rpm-macros
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  libudev-devel
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libdrm-devel
BuildRequires:  libpciaccess-devel
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(wayland-client) >= 1
BuildRequires:  pkgconfig(wayland-scanner) >= 1
%if %{without bootstrap}
BuildRequires:  pkgconfig(gl)
%endif
Recommends:     mesa-filesystem%{?_isa}

%description
Libva is a library providing the VA API video acceleration API.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%build
%meson \
 -Dwith_legacy=nvctrl \
 -Ddriverdir="%{_libdir}/dri-nonfree:%{_libdir}/dri-freeworld:%{_libdir}/dri" \
%if %{with bootstrap}
 -Dwith_glx=no \
%endif
 %{nil}
%meson_build

%install
%meson_install

sed -i -e 's|driverdir=.*|driverdir=%{_libdir}/dri|' %{buildroot}%{_libdir}/pkgconfig/libva.pc

mkdir -p %{buildroot}%{_libdir}/dri-{freeworld,nonfree}

%ldconfig_scriptlets

%files
%doc NEWS
%license COPYING
%ghost %{_sysconfdir}/libva.conf
%dir %{_libdir}/dri-*
%{_libdir}/libva.so.2*
%{_libdir}/libva-drm.so.2*
%{_libdir}/libva-wayland.so.2*
%{_libdir}/libva-x11.so.2*
%if %{without bootstrap}
%{_libdir}/libva-glx.so.2*
%endif

%files devel
%{_includedir}/va
%{_libdir}/libva*.so
%{_libdir}/pkgconfig/libva*.pc

%changelog
%autochangelog
