%global source0_hash e175c149e7c49827153d5a7810aa463205214007dc5e622914fa11a5c4f39fe7

Name:           SDL_sound
Version:        1.0.3
Release:        44%{?dist}
Summary:        Library handling decoding of several popular sound file formats
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.icculus.org/SDL_sound
# This is:
# http://www.icculus.org/SDL_sound/downloads/%{name}-%{version}.tar.gz
# With PBProjects.tar.gz (contains binaries) removed
Source0:        %{name}-%{version}-clean.tar.gz
BuildRequires: make
BuildRequires:  SDL-devel flac-devel speex-devel libvorbis-devel libogg-devel
BuildRequires:  mikmod-devel libmodplug-devel physfs-devel doxygen
# SDL_sound uses a very stripped down mpg123-libs called mpglib
Provides:       bundled(mpglib)
Provides:       bundled(mpg123-libs)

%description
SDL_sound is a library that handles the decoding of several popular sound file 
formats, such as .WAV and .OGG.

It is meant to make the programmer's sound playback tasks simpler. The 
programmer gives SDL_sound a filename, or feeds it data directly from one of 
many sources, and then reads the decoded waveform data back at her leisure. 
If resource constraints are a concern, SDL_sound can process sound data in 
programmer-specified blocks. Alternately, SDL_sound can decode a whole sound 
file and hand back a single pointer to the whole waveform. SDL_sound can 
also handle sample rate, audio format, and channel conversion on-the-fly 
and behind-the-scenes, if the programmer desires.

%package        devel
Summary:        %{summary}
Requires:       %{name} = %{version}-%{release}
Requires:       SDL-devel

%description    devel
This package contains the headers and libraries for SDL_sound development.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# Avoid lib64 rpaths
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure

%build
export CFLAGS="$RPM_OPT_FLAGS -D__EXPORT__= -Wno-pointer-sign -Wno-deprecated-declarations"
# no smpeg because of patents!
%configure --disable-dependency-tracking --disable-static \
    --disable-smpeg --enable-mpglib --enable-mikmod --enable-ogg \
    --enable-modplug --enable-speex --enable-flac --enable-midi
make %{?_smp_mflags}
doxygen Doxyfile

%install
%make_install
# Avoid conflict with SDL2_sound, users who want this should use SDL2_sound
rm $RPM_BUILD_ROOT%{_bindir}/playsound*

# Add namespaces to man pages (livna bug #1181)
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

mkdir -p $RPM_BUILD_ROOT/%{_mandir}
mv man3 $RPM_BUILD_ROOT/%{_mandir}

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%license COPYING
%doc README TODO
%{_libdir}/libSDL_sound-1.0.so.*

%files devel
%doc docs/html
%{_libdir}/libSDL_sound*.so
%{_includedir}/SDL/SDL_sound.h
%{_mandir}/man3/*

%changelog
%autochangelog
