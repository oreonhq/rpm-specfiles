# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 155b80cd7ef64e5b10af08eed60b6eab146ea785367ff67e0d8cc8acd511a889
%global source1_hash 20fd8be9936174d2b0a08295a7a1caeb1b6b7c8f4100e5d0188f0a3e52791bfc
%global source2_hash 461636667c815be71e1fd00fbf1784cf83d155546b954fe3a32f879b0b57048c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global sdl3_minver 3.4.0

%if 0%{?rhel}
%bcond_with static
%else
%bcond_without static
%endif

Name:           sdl2-compat
Version:        2.32.74
Release:        1%{?dist}
SourceLicense:  Zlib and Apache-2.0 and MIT and BSD-3-Clause
Summary:        SDL 2.0 runtime compatibility library using SDL 3.0
License:        Zlib
URL:            https://github.com/libsdl-org/sdl2-compat
Source0:        %{url}/archive/release-%{version}/%{name}-%{version}.tar.gz
Source1:        SDL2_config.h
Source2:        SDL2_revision.h

Patch1001:      sdl2-compat-sdlconfig-multilib.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  SDL3-devel >= %{sdl3_minver}
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
Obsoletes:      SDL2 < 2.30.11-2
Conflicts:      SDL2 < 2.32.50~
Provides:       SDL2 = %{version}
Provides:       SDL2%{?_isa} = %{version}
Requires:       SDL3%{?_isa} >= %{sdl3_minver}

%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio device.

This code is a compatibility layer; it provides a binary-compatible API for
programs written against SDL 2.0, but it uses SDL 3.0 behind the scenes.

If you are writing new code, please target SDL 3.0 directly and do not use
this layer.

%package devel
Summary:        Files to develop SDL 2.0 applications using SDL 3.0
License:        Zlib and Apache-2.0 and MIT and BSD-3-Clause
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      SDL2-devel < 2.30.11-2
Conflicts:      SDL2-devel < 2.32.50~
Provides:       SDL2-devel = %{version}
Provides:       SDL2-devel%{?_isa} = %{version}
%if ! %{with static}
Obsoletes:      SDL2-static < 2.30.11-2
Conflicts:      SDL2-static < 2.30.50~
%endif
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glu)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xproto)

%description devel
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio device.

This code is a compatibility layer; it provides a source-compatible API for
programs written against SDL 2.0, but it uses SDL 3.0 behind the scenes.

If you are writing new code, please target SDL 3.0 directly and do not use
this layer.

%if %{with static}
%package static
Summary:        Static library to develop SDL 2.0 applications using SDL 3.0
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Obsoletes:      SDL2-static < 2.30.11-2
Conflicts:      SDL2-static < 2.32.50~
Provides:       SDL2-static = %{version}
Provides:       SDL2-static%{?_isa} = %{version}

%description static
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio device.

This code is a compatibility layer; it provides a static link library for
programs written against SDL 2.0, but it uses SDL 3.0 behind the scenes.
Note that applications that use this library will need to declare SDL2 as
a dependency manually, as the library is dlopen()'d to preserve APIs between
SDL-2.0 and SDL-3.0.

If you are writing new code, please target SDL 3.0 directly and do not use
this layer.
%endif

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%autosetup -n %{name}-release-%{version} -S git_am

%build
%cmake %{?with_static:-DSDL2COMPAT_STATIC=ON}
%cmake_build

%install
%cmake_install

mv %{buildroot}%{_includedir}/SDL2/SDL_config.h %{buildroot}%{_includedir}/SDL2/SDL_config-%{_arch}.h
install -p -m 644 %{SOURCE1} %{buildroot}%{_includedir}/SDL2/SDL_config.h

mv %{buildroot}%{_includedir}/SDL2/SDL_revision.h %{buildroot}%{_includedir}/SDL2/SDL_revision-%{_arch}.h
install -p -m 644 %{SOURCE2} %{buildroot}%{_includedir}/SDL2/SDL_revision.h

%check
%ctest

%files
%license LICENSE.txt
%doc README.md BUGS.md COMPATIBILITY.md
%{_libdir}/libSDL2-2.0.so.*

%files devel
%{_bindir}/sdl2-config
%{_datadir}/aclocal/sdl2.m4
%{_includedir}/SDL2/
%dir %{_libdir}/cmake/SDL2
%{_libdir}/cmake/SDL2/sdl2-config*.cmake
%{_libdir}/cmake/SDL2/SDL2Config*.cmake
%{_libdir}/cmake/SDL2/SDL2Targets*.cmake
%{_libdir}/cmake/SDL2/SDL2mainTargets*.cmake
%{_libdir}/libSDL2-2.0.so
%{_libdir}/libSDL2.so
%{_libdir}/pkgconfig/sdl2-compat.pc
%{_libdir}/libSDL2main.a
%{_libdir}/libSDL2_test.a
%{_libdir}/cmake/SDL2/SDL2_testTargets*.cmake

%if %{with static}
%files static
%{_libdir}/libSDL2.a
%{_libdir}/cmake/SDL2/SDL2-staticTargets*.cmake
%endif

%changelog
%autochangelog
