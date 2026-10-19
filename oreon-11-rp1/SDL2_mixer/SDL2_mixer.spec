%global source0_hash cb760211b056bfe44f4a1e180cc7cb201137e4d1572f2002cc1be728efd22660
Name:           SDL2_mixer
Version:        2.8.1
Release:        4%{?dist}
Summary:        Simple DirectMedia Layer - Sample Mixer Library
License:        Zlib
URL:            https://www.libsdl.org/projects/SDL_mixer/
Source0:        https://www.libsdl.org/projects/SDL_mixer/release/%{name}-%{version}.tar.gz
Provides: bundled(timidity)
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  chrpath
BuildRequires:  flac-devel
BuildRequires:  fluidsynth-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libxmp-devel
BuildRequires:  make
BuildRequires:  mpg123-devel
BuildRequires:  opusfile-devel
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  wavpack-devel
# /oreon:deps
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
%oreon_autofiles SDL2_mixer-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n SDL2_mixer-devel -f %{oreon_filedir}/SDL2_mixer-devel.list

%changelog

%autochangelog
