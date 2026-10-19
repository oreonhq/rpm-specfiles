%global source0_hash e889ac9c7e8a6bdfc31972bf1f1254b84882cb52931608bada62e8febbf0270b
%bcond_without static
Name:           sdl12-compat
Version:        1.2.76
Release:        1%{?dist}
Summary:        SDL 1.2 runtime compatibility library using SDL 2.0
License:        Zlib AND (MIT-0 OR Unlicense OR CC0-1.0) AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/libsdl-org/sdl12-compat
Source0:        https://github.com/libsdl-org/sdl12-compat/archive/refs/tags/release-1.2.76.tar.gz#/sdl12-compat-1.2.76.tar.gz
Source1:        SDL_config.h
Patch1001:      sdl12-compat-sdlconfig-multilib.patch
Obsoletes:      SDL < 1.2.15-49
Conflicts:      SDL < 1.2.50
Provides:       SDL = %{version}
Provides:       SDL%{?_isa} = %{version}
Requires:       SDL2%{?_isa} >= 2.0.18
# oreon:deps
BuildRequires:  SDL2-devel
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-release-%{version}
%oreon_prep
%build

%cmake %{?with_static:-DSTATICDEVEL=ON}
%cmake_build
%install
%cmake_install
mv %{buildroot}/%{_includedir}/SDL/SDL_config.h %{buildroot}/%{_includedir}/SDL/SDL_config-%{_arch}.h
install -m644 %{SOURCE1} %{buildroot}/%{_includedir}/SDL/SDL_config.h
%if ! %{with static}
rm -rf %{buildroot}%{_libdir}/*.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n sdl12-compat-devel -f %{oreon_filedir}/sdl12-compat-devel.list
%files -n sdl12-compat-static -f %{oreon_filedir}/sdl12-compat-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.74-1
- Prepare for Oreon 11 (RP1)
