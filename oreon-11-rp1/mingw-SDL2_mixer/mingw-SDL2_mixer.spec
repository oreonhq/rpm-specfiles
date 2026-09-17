%global source0_hash cb760211b056bfe44f4a1e180cc7cb201137e4d1572f2002cc1be728efd22660

%{?mingw_package_header}

Name:           mingw-SDL2_mixer
Version:        2.8.1
Release:        3%{?dist}
Summary:        MinGW Windows port of Simple DirectMedia Layer's Sample Mixer Library

License:        Zlib
URL:            http://www.libSDL.org/projects/SDL_mixer/
Source0:        http://www.libSDL.org/projects/SDL_mixer/release/SDL2_mixer-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-SDL2
BuildRequires:  mingw32-libvorbis
BuildRequires:  mingw32-flac

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-SDL2
BuildRequires:  mingw64-libvorbis
BuildRequires:  mingw64-flac

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

%autosetup -p1 -n SDL2_mixer-%{version}

%build
%mingw_configure --disable-static
%mingw_make_build

%install
%mingw_make_install

# Drop all .la files
find %{buildroot} -name "*.la" -delete

# Win32
%files -n mingw32-SDL2_mixer
%license LICENSE.txt
%{mingw32_bindir}/SDL2_mixer.dll
%{mingw32_libdir}/libSDL2_mixer.dll.a
%{mingw32_libdir}/cmake/SDL2_mixer/
%{mingw32_libdir}/pkgconfig/SDL2_mixer.pc
%{mingw32_includedir}/SDL2

# Win64
%files -n mingw64-SDL2_mixer
%license LICENSE.txt
%{mingw64_bindir}/SDL2_mixer.dll
%{mingw64_libdir}/libSDL2_mixer.dll.a
%{mingw64_libdir}/cmake/SDL2_mixer/
%{mingw64_libdir}/pkgconfig/SDL2_mixer.pc
%{mingw64_includedir}/SDL2

%changelog
%autochangelog
