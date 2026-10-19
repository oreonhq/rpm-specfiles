%global source0_hash 5f7d668d7811e21e1bc4b449528f52516687ea3e3b59878a21db055394163a32
%global commit 1be041bc77d2039c5a856352b64deef9693ec316
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20260117
Name:           SDL2_sound
Version:        2.0.5^%{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        An abstract soundfile decoder library
License:        Zlib AND LGPL-2.1-or-later AND (Unlicense OR MIT-0) AND (MIT OR Unlicense) AND LicenseRef-Fedora-Public-Domain
URL:            http://www.icculus.org/SDL_sound
%if 0%{?commit:1}
Source0:        https://github.com/icculus/SDL_sound/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:        https://github.com/icculus/SDL_sound/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%endif
Provides:       bundled(libmodplug) = 0.8.9.1
Provides:       bundled(dr_flac) = 0.13.3
Provides:       bundled(dr_mp3) = 0.7.3
Provides:       bundled(stb_vorbis) = 1.22
Provides:       bundled(timidity) = 0.2i
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  cmake
BuildRequires:  doxygen
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
Requires:       SDL2-devel
Conflicts:      SDL_sound-devel
%description    devel
This package contains the headers and libraries for SDL_sound development.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?commit:1}
%autosetup -n SDL_sound-%{commit} -p1
%else
%autosetup -n SDL_sound-%{version} -p1
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
mv channels.3 Sound_AudioInfo::channels.3
mv decoder.3 Sound_Sample::decoder.3
mv description.3 Sound_DecoderInfo::description.3
mv desired.3 Sound_Sample::desired.3
mv extensions.3 Sound_DecoderInfo::extensions.3
mv flags.3 Sound_Sample::flags.3
mv format.3 Sound_AudioInfo::format.3
mv major.3 Sound_Version::major.3
mv minor.3 Sound_Version::minor.3
mv opaque.3 Sound_Sample::opaque.3
mv patch.3 Sound_Version::patch.3
mv rate.3 Sound_AudioInfo::rate.3
mv url.3 Sound_DecoderInfo::url.3
popd
mkdir -p %{buildroot}/%{_mandir}
mv man3 %{buildroot}/%{_mandir}
%oreon_autofiles SDL2_sound-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n SDL2_sound-devel -f %{oreon_filedir}/SDL2_sound-devel.list

%changelog

%autochangelog
