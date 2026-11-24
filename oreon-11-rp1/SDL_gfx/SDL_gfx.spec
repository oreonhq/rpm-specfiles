# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash dfb15ac5f8ce7a4952dc12d2aed9747518c5e6b335c0e31636d23f93c630f419
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary: SDL graphics drawing primitives and other support functions
Name: SDL_gfx
Version: 2.0.27
Release: 1%{?dist}
License: Zlib
URL: http://www.ferzkopp.net/Software/SDL_gfx-2.0/
Source0:        http://www.ferzkopp.net/Software/SDL_gfx-2.0/SDL_gfx-%{version}.tar.gz
Patch0: SDL_gfx-2.0.13-ppc.patch
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: make
BuildRequires: SDL-devel
BuildRequires: libXt-devel

%description
Library providing SDL graphics drawing primitives and other support functions
wrapped up in an addon library for the Simple Direct Media (SDL) cross-platform
API layer.

%package devel
Summary: Development files for SDL_gfx
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: SDL-devel

%description devel
This package contains the files required to develop programs which use SDL_gfx.

%prep
%oreon_sha256
%setup -q
%patch -P 0 -p1 -b .ppc

%build
%configure \
%ifnarch %{ix86} x86_64
    --disable-mmx \
%endif
    --disable-static
make %{?_smp_mflags}

%install
%make_install

%ldconfig_scriptlets

%files
%doc LICENSE README AUTHORS COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/SDL/*.h
%exclude %{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
%autochangelog
