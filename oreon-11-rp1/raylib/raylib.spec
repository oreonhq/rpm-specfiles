%global source0_hash aea98ecf5bc5c5e0b789a76de0083a21a70457050ea4cc2aec7566935f5e258e
Name:           raylib
Version:        5.5
Release:        1%{?dist}
Summary:        A simple and easy-to-use library to enjoy videogames programming
License:        Zlib AND MIT
URL:            https://github.com/raysan5/%{name}
Source0:        https://github.com/raysan5/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libXcursor-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  pkgconfig
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
# /oreon:deps
%description
raylib is a simple and easy-to-use library to enjoy videogames programming.

raylib is highly inspired by Borland BGI graphics lib and by XNA framework and
it's especially well suited for prototyping, tooling, graphical applications,
embedded systems and education.

NOTE for ADVENTURERS: raylib is a programming library to enjoy videogames
                      programming; no fancy interface, no visual helpers,
                      no debug button
                      ...just coding in the most pure spartan-programmers way.

Ready to learn? Jump to https://www.raylib.com/examples.html

# Devel subapackage
%package devel
Summary: Devel files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires: libXcursor-devel
Requires: libXi-devel
Requires: libXinerama-devel
Requires: libXrandr-devel
Requires: mesa-libGL-devel
Requires: wayland-devel
Requires: libxkbcommon-devel
Requires: wayland-protocols-devel
%description devel
The %{name}-devel package contains header files for developing with %{name}.

%prep
%oreon_prep
%build

%cmake \
    -DBUILD_EXAMPLES=ON \
    -DBUILD_SHARED_LIBS=ON \
    -DUSE_EXTERNAL_GLFW=OFF \
    -DOpenGL_GL_PREFERENCE=GLVND \
    -DUSE_WAYLAND=ON \
    -DBUILD_EXAMPLES=ON \
    -DPLATFORM=Desktop
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n raylib-devel -f %{oreon_filedir}/raylib-devel.list

%changelog

%autochangelog
