%global source0_hash 2588686c0972e1785829dc3bf436b543c317e6afa30a9b91d48013dd9c110e81

%{?mingw_package_header}

%global origname sdl12-compat

Name:           mingw-%{origname}
Version:        1.2.74
Release:        1%{?dist}
Summary:        MinGW Windows port of SDL 1.2 runtime compatibility library using SDL 2.0
# mp3 decoder code is MIT-0/PD
# SDL_opengl.h is zlib and MIT
License:        Zlib AND MIT AND (MIT-0 OR LicenseRef-Fedora-Public-Domain)
URL:            https://github.com/libsdl-org/%{origname}
Source0:        %{url}/archive/release-%{version}/%{origname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  make

BuildArch:      noarch

%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio device.

This code is a compatibility layer; it provides a binary-compatible API for
Windows programs written against SDL 1.2, but it uses SDL 2.0 behind the scenes.

If you are writing new code, please target SDL 2.0 directly and do not use
this layer.

%package -n mingw32-%{origname}
Summary:        MinGW 32-bit Windows port of SDL 1.2 compatibility library using SDL 2.0
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-SDL2
# This replaces SDL
Obsoletes:      mingw32-SDL < 1.2.15-19
Conflicts:      mingw32-SDL < 1.2.50
Provides:       mingw32-SDL = %{version}
# This dlopens SDL2 (?!), so manually depend on it
Requires:       mingw32-SDL2 >= 2.0.18

%description -n mingw32-%{origname}
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio device.

This code is a compatibility layer; it provides a binary-compatible API for
Windows 32-bit programs written against SDL 1.2, but it uses SDL 2.0 behind
the scenes.

If you are writing new code, please target SDL 2.0 directly and do not use
this layer.

%package -n mingw64-%{origname}
Summary:        MinGW 64-bit Windows port of SDL 1.2 compatibility library using SDL 2.0
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-SDL2
# This replaces SDL
Obsoletes:      mingw64-SDL < 1.2.15-19
Conflicts:      mingw64-SDL < 1.2.50
Provides:       mingw64-SDL = %{version}
# This dlopens SDL2 (?!), so manually depend on it
Requires:       mingw64-SDL2 >= 2.0.18

%description -n mingw64-%{origname}
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio device.

This code is a compatibility layer; it provides a binary-compatible API for
Windows 64-bit programs written against SDL 1.2, but it uses SDL 2.0 behind
the scenes.

If you are writing new code, please target SDL 2.0 directly and do not use
this layer.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{origname}-release-%{version} -S git_am

%build
%mingw_cmake
%mingw_make_build

%install
%mingw_make_install

# These exist in the native sdl12-compat package
rm -rf %{buildroot}%{mingw32_datadir}/aclocal
rm -rf %{buildroot}%{mingw64_datadir}/aclocal

%files -n mingw32-%{origname}
%license LICENSE.txt
%doc README.md BUGS.md COMPATIBILITY.md
%{mingw32_bindir}/SDL.dll
%{mingw32_bindir}/sdl-config
%{mingw32_libdir}/libSDL.dll.a
%{mingw32_libdir}/libSDLmain.a
%{mingw32_libdir}/pkgconfig/sdl12_compat.pc
%{mingw32_includedir}/SDL/

%files -n mingw64-%{origname}
%license LICENSE.txt
%doc README.md BUGS.md COMPATIBILITY.md
%{mingw64_bindir}/SDL.dll
%{mingw64_bindir}/sdl-config
%{mingw64_libdir}/libSDL.dll.a
%{mingw64_libdir}/libSDLmain.a
%{mingw64_libdir}/pkgconfig/sdl12_compat.pc
%{mingw64_includedir}/SDL/

%changelog
%autochangelog
