%global source0_hash 5aeedbe1caf896267256cb5e57a2ee402ab7d4f5b9865bbd9ee8ef44f3706910
%global commit b00e4a318fc7e4074b67f75dbb22373e1e07c56b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20260117
%bcond bundled_dr_libs 0
Name:           SDL3_sound
Version:        3.0.0~%{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        An abstract soundfile decoder library
License:        Zlib AND LGPL-2.1-or-later AND (Unlicense OR MIT-0) AND (MIT OR Unlicense) AND LicenseRef-Fedora-Public-Domain
URL:            https://www.icculus.org/SDL_sound
Source0:        https://github.com/icculus/SDL_sound/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         %{name}-unbundle-dr_libs.patch
Provides:       bundled(libmodplug) = 0.8.9.1
%if %{with bundled_dr_libs}
Provides:       bundled(dr_flac) = 0.13.3
Provides:       bundled(dr_mp3) = 0.7.3
%else
%endif
Provides:       bundled(stb_vorbis) = 1.22
Provides:       bundled(timidity) = 0.2i
# oreon:deps
BuildRequires:  SDL3-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  dr_flac-static
BuildRequires:  dr_mp3-static
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
SDL_sound is a library that handles the decoding of several popular sound
file formats, such as .WAV and .OGG. It is meant to make the programmer's
sound playback tasks simpler. The programmer gives SDL_sound a filename,
or feeds it data directly from one of many sources, and then reads the
decoded waveform data back at her leisure. If resource constraints are a
concern, SDL_sound can process sound data in programmer-specified blocks.
Alternately, SDL_sound can decode a whole sound file and hand back a
single pointer to the whole waveform. SDL_sound can also handle sample
rate, audio format, and channel conversion on-the-fly and
behind-the-scenes, if the programmer desires.

%package        devel
Summary:        %{summary}
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       cmake-filesystem
Requires:       pkgconfig
Requires:       SDL3-devel
Conflicts:      SDL_sound-devel
Conflicts:      SDL2_sound-devel
%description    devel
This package contains the headers and libraries for SDL_sound development.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SDL_sound-%{commit}
%if %{without bundled_dr_libs}
%patch -P0 -p1 -b .orig
# Unbundle dr_flac and dr_mp3, from dr_libs.
rm src/dr_flac.h src/dr_mp3.h
%endif

%build

%cmake \
    -DSDLSOUND_BUILD_STATIC:BOOL=OFF \
    -DSDLSOUND_DECODER_MIDI:BOOL=ON \
%cmake_build
doxygen docs/Doxyfile
%install
%cmake_install
rm -rf man3
cp -a docs/man/man3 man3
pushd man3
mv actual.3 Sound_Sample::actual.3
mv author.3 Sound_DecoderInfo::author.3
mv buffer.3 Sound_Sample::buffer.3
mv buffer_size.3 Sound_Sameple::buffer_size.3
mv decoder.3 Sound_Sample::decoder.3
mv description.3 Sound_DecoderInfo::description.3
mv desired.3 Sound_Sample::desired.3
mv extensions.3 Sound_DecoderInfo::extensions.3
mv flags.3 Sound_Sample::flags.3
mv opaque.3 Sound_Sample::opaque.3
mv url.3 Sound_DecoderInfo::url.3
popd
mkdir -p %{buildroot}/%{_mandir}
mv man3 %{buildroot}/%{_mandir}
%oreon_autofiles SDL3_sound-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n SDL3_sound-devel -f %{oreon_filedir}/SDL3_sound-devel.list

%changelog

%autochangelog
