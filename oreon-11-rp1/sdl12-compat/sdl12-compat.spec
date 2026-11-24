# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash e889ac9c7e8a6bdfc31972bf1f1254b84882cb52931608bada62e8febbf0270b
%global source1_hash fcf578674426bdbde39adf076ce0ff10f0e8c2f88413128096a63f8292414d1e
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if 0%{?rhel}
%bcond_with static
%else
%bcond_without static
%endif

Name:           sdl12-compat
Version:        1.2.76
Release:        1%{?dist}
Summary:        SDL 1.2 runtime compatibility library using SDL 2.0
License:        Zlib AND (MIT-0 OR Unlicense OR CC0-1.0) AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/libsdl-org/sdl12-compat
Source0:        %{url}/archive/release-%{version}/%{name}-%{version}.tar.gz
Source1:        SDL_config.h

Patch1001:      sdl12-compat-sdlconfig-multilib.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  SDL2-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
Obsoletes:      SDL < 1.2.15-49
Conflicts:      SDL < 1.2.50
Provides:       SDL = %{version}
Provides:       SDL%{?_isa} = %{version}
Requires:       SDL2%{?_isa} >= 2.0.18

%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio device.

This code is a compatibility layer; it provides a binary-compatible API for
programs written against SDL 1.2, but it uses SDL 2.0 behind the scenes.

If you are writing new code, please target SDL 2.0 directly and do not use
this layer.

%package devel
Summary:        Files to develop SDL 1.2 applications using SDL 2.0
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      SDL-devel < 1.2.15-49
Conflicts:      SDL-devel < 1.2.50
Provides:       SDL-devel = %{version}
Provides:       SDL-devel%{?_isa} = %{version}
%if ! %{with static}
Obsoletes:      SDL-static < 1.2.15-49
Conflicts:      SDL-static < 1.2.50
%endif
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glu)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xproto)

%description devel
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio device.

This code is a compatibility layer; it provides a source-compatible API for
programs written against SDL 1.2, but it uses SDL 2.0 behind the scenes.

If you are writing new code, please target SDL 2.0 directly and do not use
this layer.

%if %{with static}
%package static
Summary:        Static library to develop SDL 1.2 applications using SDL 2.0
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Obsoletes:      SDL-static < 1.2.15-49
Conflicts:      SDL-static < 1.2.50
Provides:       SDL-static = %{version}
Provides:       SDL-static%{?_isa} = %{version}

%description static
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio device.

This code is a compatibility layer; it provides a static link library for
programs written against SDL 1.2, but it uses SDL 2.0 behind the scenes.
Note that applications that use this library will need to declare SDL2 as
a dependency manually, as the library is dlopen()'d to preserve APIs between
SDL-1.2 and SDL-2.0.

If you are writing new code, please target SDL 2.0 directly and do not use
this layer.
%endif

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -n %{name}-release-%{version} -S git_am

%build
%cmake %{?with_static:-DSTATICDEVEL=ON}
%cmake_build

%install
%cmake_install

mv %{buildroot}/%{_includedir}/SDL/SDL_config.h %{buildroot}/%{_includedir}/SDL/SDL_config-%{_arch}.h
install -m644 %{SOURCE1} %{buildroot}/%{_includedir}/SDL/SDL_config.h

%if ! %{with static}
rm -rf %{buildroot}%{_libdir}/*.a
%endif

%files
%license LICENSE.txt
%doc README.md BUGS.md COMPATIBILITY.md
%{_libdir}/libSDL-1.2.so.*

%files devel
%{_bindir}/sdl-config
%{_datadir}/aclocal/sdl.m4
%{_includedir}/SDL/
%{_libdir}/libSDL-1.2.so
%{_libdir}/libSDL.so
%{_libdir}/pkgconfig/sdl12_compat.pc

%if %{with static}
%files static
%{_libdir}/libSDL.a
%{_libdir}/libSDLmain.a
%endif

%changelog
%autochangelog
