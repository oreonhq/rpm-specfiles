# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 072cda4b59dd098bba8c2363a6247299db1fa89411dc221c8b81b8ee8192e623
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond_with check

Name: libepoxy
Version: 1.5.10
Release: 1%{?dist}
Summary: epoxy runtime library
License: MIT
URL: https://github.com/anholt/libepoxy
Source0:        https://download.gnome.org/sources/%{name}/1.5/%{name}-%{version}.tar.xz

Patch0:        Fix-dlwrap-on-riscv64.patch

BuildRequires: oreon-rpm-macros
BuildRequires: meson
BuildRequires: clang
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(egl)
BuildRequires: libGL-devel
BuildRequires: libEGL-devel
BuildRequires: libX11-devel
BuildRequires: pkgconfig(glesv2)
BuildRequires: python3
%if %{with check}
BuildRequires: mesa-dri-drivers
BuildRequires: mutter
BuildRequires: xwayland-run
%endif

%description
A library for handling OpenGL function pointer management.

%package devel
Summary: Development files for libepoxy
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%if %{with check}
xwfb-run -c mutter -- ninja -C %{_vpath_builddir} test || \
    (cat %{_vpath_builddir}/meson-logs/testlog.txt ; exit 1)
%endif

%files
%license COPYING
%doc README.md
%{_libdir}/libepoxy.so.0*

%files devel
%{_includedir}/epoxy/
%{_libdir}/libepoxy.so
%{_libdir}/pkgconfig/epoxy.pc

%changelog
%autochangelog
