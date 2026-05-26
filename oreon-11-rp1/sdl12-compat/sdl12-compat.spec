%if 0%{?rhel}
# Features disabled for RHEL
%bcond_with static
%else
%bcond_without static
%endif

Name:           sdl12-compat
Version:        1.2.74
Release:        1%{?dist}
Summary:        SDL 1.2 runtime compatibility library using SDL 2.0
# main code is Zlib
# mp3 decoder code is MIT-0 OR Unlicense OR CC0-1.0
# SDL_opengl.h is Zlib AND MIT
# SDL12_compat.c is Zlib AND LicenseRef-Fedora-Public-Domain
License:        Zlib AND (MIT-0 OR Unlicense OR CC0-1.0) AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/libsdl-org/sdl12-compat
Source0:        https://github.com/libsdl-org/sdl12-compat/archive/release-1.2.74/sdl12-compat-1.2.74.tar.gz
# Multilib aware-header stub
Source1:        SDL_config.h

# Backports from upstream (0001~0500)

# Proposed patches (0501~1000)

# Fedora specific patches (1001+)
Patch1001:      sdl12-compat-sdlconfig-multilib.patch
# oreon url source checksums begin
%global source0_sha256 2588686c0972e1785829dc3bf436b543c317e6afa30a9b91d48013dd9c110e81
%global source0_file sdl12-compat-1.2.74.tar.gz
# oreon url source checksums end

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  SDL2-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
# This replaces SDL
Obsoletes:      SDL < 1.2.15-49
Conflicts:      SDL < 1.2.50
Provides:       SDL = %{version}
Provides:       SDL%{?_isa} = %{version}
# This dlopens SDL2 (?!), so manually depend on it
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
# This replaces SDL-devel
Obsoletes:      SDL-devel < 1.2.15-49
Conflicts:      SDL-devel < 1.2.50
Provides:       SDL-devel = %{version}
Provides:       SDL-devel%{?_isa} = %{version}
%if ! %{with static}
# We don't provide the static library, but we want to replace SDL-static anyway
Obsoletes:      SDL-static < 1.2.15-49
Conflicts:      SDL-static < 1.2.50
%endif
# Add deps required to compile SDL apps
## For SDL_opengl.h
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glu)
## For SDL_syswm.h
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
# This replaces SDL-static
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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/sdl12-compat-1.2.74.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2588686c0972e1785829dc3bf436b543c317e6afa30a9b91d48013dd9c110e81" || { echo "oreon: Source0 SHA256 mismatch for sdl12-compat-1.2.74.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{name}-release-%{version} -S git_am


%build
%cmake %{?with_static:-DSTATICDEVEL=ON}
%cmake_build


%install
%cmake_install

# Rename SDL_config.h to SDL_config-<arch>.h to avoid file conflicts on
# multilib systems and install SDL_config.h wrapper
mv %{buildroot}/%{_includedir}/SDL/SDL_config.h %{buildroot}/%{_includedir}/SDL/SDL_config-%{_arch}.h
install -m644 %{SOURCE1} %{buildroot}/%{_includedir}/SDL/SDL_config.h

%if ! %{with static}
# Delete leftover static files
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.74-1
- Prepare for Oreon 11 (RP1)
