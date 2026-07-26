%global source0_hash 1644308279a975799049e4826af2cfc787cad2abb11aa14562e402521f86992a

%{?mingw_package_header}

Name:           mingw-SDL_mixer
Version:        1.2.12
Release:        28%{?dist}
Summary:        MinGW Windows port of Simple DirectMedia Layer's Sample Mixer Library

License:        Zlib
URL:            http://www.libsdl.org/projects/SDL_mixer/
Source0:        http://www.libsdl.org/projects/SDL_mixer/release/SDL_mixer-%{version}.tar.gz
# Fix incompatible pointer types
Patch0:         sdl-mixer-incompatible-pointer-types.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-SDL
BuildRequires:  mingw32-libvorbis

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-SDL
BuildRequires:  mingw64-libvorbis

%description
A simple multi-channel audio mixer for SDL. It supports 4 channels of
16 bit stereo audio, plus a single channel of music, mixed by the popular
MikMod MOD library.

# Win32
%package -n mingw32-SDL_mixer
Summary:        MinGW Windows port of Simple DirectMedia Layer's Sample Mixer Library
Requires:       pkgconfig

%description -n mingw32-SDL_mixer
A simple multi-channel audio mixer for SDL. It supports 4 channels of
16 bit stereo audio, plus a single channel of music, mixed by the popular
MikMod MOD library.

# Win64
%package -n mingw64-SDL_mixer
Summary:        MinGW Windows port of Simple DirectMedia Layer's Sample Mixer Library
Requires:       pkgconfig

%description -n mingw64-SDL_mixer
A simple multi-channel audio mixer for SDL. It supports 4 channels of
16 bit stereo audio, plus a single channel of music, mixed by the popular
MikMod MOD library.

# Automatically create a debuginfo package
%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n SDL_mixer-%{version}

%build
%mingw_configure \
    --disable-music-flac \
    --disable-static

%mingw_make_build

%install
%mingw_make_install

# Drop all .la files
find %{buildroot} -name "*.la" -delete

# Win32
%files -n mingw32-SDL_mixer
%doc README CHANGES COPYING
%{mingw32_bindir}/SDL_mixer.dll
%{mingw32_libdir}/libSDL_mixer.dll.a
%{mingw32_libdir}/pkgconfig/SDL_mixer.pc
%{mingw32_includedir}/SDL

# Win64
%files -n mingw64-SDL_mixer
%doc README CHANGES COPYING
%{mingw64_bindir}/SDL_mixer.dll
%{mingw64_libdir}/libSDL_mixer.dll.a
%{mingw64_libdir}/pkgconfig/SDL_mixer.pc
%{mingw64_includedir}/SDL

%changelog
%autochangelog
