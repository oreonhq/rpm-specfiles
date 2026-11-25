# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ea79bc5feffc254c87291980c2d0bce9acebb68c4983b79f961dcd2cb8a611a0

Name:           glfw
Version:        3.5.1
Release:        1%{?dist}
Summary:        Library for OpenGL, Vulkan, and window input
License:        Zlib
URL:            https://www.glfw.org/
Source0:        https://github.com/glfw/glfw/releases/download/%{version}/glfw-%{version}.zip

BuildRequires:  oreon-rpm-macros
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  unzip
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  kernel-headers

%description
GLFW is a library for creating windows, OpenGL and Vulkan contexts, and
reading keyboard, mouse, and joystick input.

%package devel
Summary:        Development files for GLFW
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(gl)

%description devel
Headers and pkg-config files for applications that use GLFW.

%prep
%oreon_sha256
%autosetup

%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%license LICENSE.md
%doc README.md
%{_libdir}/libglfw.so.3*

%files devel
%{_includedir}/GLFW/
%{_libdir}/libglfw.so
%{_libdir}/pkgconfig/glfw3.pc
%{_libdir}/cmake/glfw3/
