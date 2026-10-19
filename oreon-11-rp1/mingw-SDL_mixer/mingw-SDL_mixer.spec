%global source0_hash 1644308279a975799049e4826af2cfc787cad2abb11aa14562e402521f86992a
%{?mingw_package_header}
Name:           mingw-SDL_mixer
Version:        1.2.12
Release:        1%{?dist}
Summary:        MinGW Windows port of Simple DirectMedia Layer's Sample Mixer Library
License:        Zlib
URL:            http://www.libsdl.org/projects/SDL_mixer/
Source0:        http://www.libsdl.org/projects/SDL_mixer/release/SDL_mixer-%{version}.tar.gz
Patch0:         sdl-mixer-incompatible-pointer-types.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-SDL
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-libvorbis
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw64-SDL
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-libvorbis
BuildRequires:  mingw64-win-iconv
# /oreon:deps
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
%global oreon_srcdir SDL_mixer-%{version}
%oreon_prep
%build

%mingw_configure \
    --disable-music-flac \
    --disable-static
%mingw_make_build
%install
%mingw_make_install
find %{buildroot} -name "*.la" -delete
%oreon_autofiles mingw32-SDL_mixer usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-SDL_mixer usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-SDL_mixer -f %{oreon_filedir}/mingw32-SDL_mixer.list
%files -n mingw64-SDL_mixer -f %{oreon_filedir}/mingw64-SDL_mixer.list

%changelog

%autochangelog
