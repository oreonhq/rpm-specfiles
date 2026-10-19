%global source0_hash 938dff531d00ace2296557a6599abe6f34599e2f34f0a4a08a397e2ccac8b8f7
%{?mingw_package_header}
Name:           mingw-SDL2_mixer
Version:        2.8.2
Release:        1%{?dist}
Summary:        MinGW Windows port of Simple DirectMedia Layer's Sample Mixer Library
License:        Zlib
URL:            http://www.libSDL.org/projects/SDL_mixer/
Source0:        http://www.libSDL.org/projects/SDL_mixer/release/SDL2_mixer-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-SDL2
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-flac
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-libvorbis
BuildRequires:  mingw64-SDL2
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-flac
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-libvorbis
# /oreon:deps
%description
A simple multi-channel audio mixer for SDL2. It supports 4 channels of
16 bit stereo audio, plus a single channel of music, mixed by the popular
MikMod MOD library.

# Win32
%package -n mingw32-SDL2_mixer
Summary:        MinGW Windows port of Simple DirectMedia Layer's Sample Mixer Library
%description -n mingw32-SDL2_mixer
A simple multi-channel audio mixer for SDL2. It supports 4 channels of
16 bit stereo audio, plus a single channel of music, mixed by the popular
MikMod MOD library.

# Win64
%package -n mingw64-SDL2_mixer
Summary:        MinGW Windows port of Simple DirectMedia Layer's Sample Mixer Library
%description -n mingw64-SDL2_mixer
A simple multi-channel audio mixer for SDL2. It supports 4 channels of
16 bit stereo audio, plus a single channel of music, mixed by the popular
MikMod MOD library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir SDL2_mixer-%{version}
%oreon_prep
%build

%mingw_configure --disable-static
%mingw_make_build
%install
%mingw_make_install
find %{buildroot} -name "*.la" -delete
%oreon_autofiles mingw32-SDL2_mixer usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-SDL2_mixer usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-SDL2_mixer -f %{oreon_filedir}/mingw32-SDL2_mixer.list
%files -n mingw64-SDL2_mixer -f %{oreon_filedir}/mingw64-SDL2_mixer.list

%changelog

%autochangelog
