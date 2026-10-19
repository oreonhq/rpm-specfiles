%global source0_hash ea85207d11f38d0da8980163eb7bbfd03ce4636c40a8d25112559bb1d381bbca
%global sdl3_minver 3.4.0
%if 0%{?rhel} || (0%{?oreon} >= 11)
%bcond_with static
%else
%bcond_without static
%endif
Name:           sdl2-compat
Version:        2.32.72
Release:        1%{?dist}
SourceLicense:  Zlib and Apache-2.0 and MIT and BSD-3-Clause
Summary:        SDL 2.0 runtime compatibility library using SDL 3.0
License:        Zlib
URL:            https://github.com/libsdl-org/sdl2-compat
Source0:        https://github.com/libsdl-org/sdl2-compat/archive/refs/tags/release-2.32.72.tar.gz#/sdl2-compat-2.32.72.tar.gz
Source1:        SDL2_config.h
Source2:        SDL2_revision.h
Patch1001:      sdl2-compat-sdlconfig-multilib.patch
Obsoletes:      SDL2 < 2.30.11-2
Conflicts:      SDL2 < 2.32.50~
Provides:       SDL2 = %{version}
Provides:       SDL2%{?_isa} = %{version}
Requires:       SDL3%{?_isa} >= %{sdl3_minver}
# oreon:deps
BuildRequires:  SDL3-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-release-%{version}
%oreon_prep
%build

%cmake %{?with_static:-DSDL2COMPAT_STATIC=ON}
%cmake_build
%install
%cmake_install
mv %{buildroot}%{_includedir}/SDL2/SDL_config.h %{buildroot}%{_includedir}/SDL2/SDL_config-%{_arch}.h
install -p -m 644 %{SOURCE1} %{buildroot}%{_includedir}/SDL2/SDL_config.h
mv %{buildroot}%{_includedir}/SDL2/SDL_revision.h %{buildroot}%{_includedir}/SDL2/SDL_revision-%{_arch}.h
install -p -m 644 %{SOURCE2} %{buildroot}%{_includedir}/SDL2/SDL_revision.h
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n sdl2-compat-devel -f %{oreon_filedir}/sdl2-compat-devel.list
%files -n sdl2-compat-static -f %{oreon_filedir}/sdl2-compat-static.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.32.68-1
- Import
