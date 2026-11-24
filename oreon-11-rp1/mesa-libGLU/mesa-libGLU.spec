# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash bd43fe12f374b1192eb15fe20e45ff456b9bc26ab57f0eee919f96ca0f8a330f
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           mesa-libGLU
Version:        9.0.3
Release:        %{autorelease}
Summary:        Mesa libGLU library

License:        X11
URL:            http://mesa3d.org/
Source0:        https://archive.mesa3d.org/glu/glu-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires:  clang
BuildRequires:  gcc-c++
BuildRequires:  libglvnd-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  meson
Provides: libGLU

%description
Mesa implementation of the standard GLU OpenGL utility API.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:	libGLU-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%autosetup -p1 -n glu-%{version}

%build
%meson -Dgl_provider=glvnd
%meson_build

%install
%meson_install
find $RPM_BUILD_ROOT -name '*.a' -delete

%ldconfig_scriptlets

%files
%{_libdir}/libGLU.so.1
%{_libdir}/libGLU.so.1.3.*

%files devel
%{_includedir}/GL/glu*.h
%{_libdir}/libGLU.so
%{_libdir}/pkgconfig/glu.pc

%changelog
%autochangelog
