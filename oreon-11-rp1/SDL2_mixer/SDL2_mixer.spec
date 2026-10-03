%global source0_hash cb760211b056bfe44f4a1e180cc7cb201137e4d1572f2002cc1be728efd22660

Name:           SDL2_mixer
Version:        2.8.1
Release:        4%{?dist}
Summary:        Simple DirectMedia Layer - Sample Mixer Library

License:        Zlib
URL:            https://www.libsdl.org/projects/SDL_mixer/
Source0:        https://www.libsdl.org/projects/SDL_mixer/release/%{name}-%{version}.tar.gz

BuildRequires:  SDL2-devel
BuildRequires:  libvorbis-devel
BuildRequires:  flac-devel
BuildRequires:  chrpath
BuildRequires:  pkgconfig(libmodplug) >= 0.8.8
BuildRequires:  fluidsynth-devel
BuildRequires:  make
BuildRequires:  mpg123-devel
BuildRequires:  opusfile-devel
%if 0%{?fedora}
BuildRequires:  libxmp-devel
%endif
BuildRequires:  wavpack-devel

Provides: bundled(timidity)

%description
SDL_mixer is a sample multi-channel audio mixer library.
It supports any number of simultaneously playing channels of 16 bit stereo
audio, plus a single channel of music, mixed by the popular FLAC,
MikMod MOD, Timidity MIDI, Ogg Vorbis, and SMPEG MP3 libraries.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i -e 's/\r//g' README.txt CHANGES.txt LICENSE.txt
rm -vrf external/

%build
%configure --disable-dependency-tracking \
           --disable-static
%make_build

%install
%make_install install-bin
for i in playmus playwave
do
  chrpath -d %{buildroot}%{_bindir}/${i}
  mv %{buildroot}%{_bindir}/${i} %{buildroot}%{_bindir}/${i}2
done

find %{buildroot} -name '*.la' -print -delete

%ldconfig_scriptlets

%files
%license LICENSE.txt
%doc CHANGES.txt
%{_bindir}/playmus2
%{_bindir}/playwave2
%{_libdir}/libSDL2_mixer-2.0.so.0*

%files devel
%doc README.txt
%{_libdir}/libSDL2_mixer.so
%{_libdir}/cmake/SDL2_mixer/
%{_libdir}/pkgconfig/SDL2_mixer.pc
%{_includedir}/SDL2/SDL_mixer.h

%changelog
%autochangelog
