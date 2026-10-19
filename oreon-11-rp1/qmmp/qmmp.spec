%global source0_hash a61d1c1faa9c411c75292a5710999182b918831b8f0f200c87149e3ff353bea9
Name:		qmmp
Version:	2.4.2
Release:        1%{?dist}
Summary:        Qt-based multimedia player
License:	GPL-2.0-or-later AND CC-BY-SA-4.0
URL:		http://qmmp.ylsoftware.com/
Source0:        http://qmmp.ylsoftware.com/files/%{name}-%{version}.tar.bz2
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
Requires:	kde-filesystem
%elif %{undefined flatpak}
Requires:	kf5-filesystem
%endif
Recommends:	qmmp-plugin-pack
Recommends:	vorbis-tools
Recommends:	lame
Recommends:	opus-tools
Recommends:	wavpack
Recommends:	flac
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  enca-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  flac-devel
BuildRequires:  game-music-emu-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libarchive-devel
BuildRequires:  libbs2b-devel
BuildRequires:  libcddb-devel
BuildRequires:  libcdio-paranoia-devel
BuildRequires:  libcurl-devel
BuildRequires:  libmad-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  libogg-devel
BuildRequires:  libprojectM-devel
BuildRequires:  librcd-devel
BuildRequires:  libshout-devel
BuildRequires:  libsidplayfp-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libxmp-devel
BuildRequires:  mpg123-devel
BuildRequires:  openssl-devel
BuildRequires:  opusfile-devel
BuildRequires:  pipewire-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  soxr-devel
BuildRequires:  taglib-devel
BuildRequires:  wavpack-devel
BuildRequires:  wildmidi-devel
# /oreon:deps
%package devel
Summary:	Development files for qmmp
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description
This program is an audio-player, written with help of Qt library.
The user interface is similar to winamp or xmms.
Main opportunities:

	* Winamp and xmms skins support
	* plugins support
	* MPEG1 layer 2/3 support
	* Ogg Vorbis support
	* native FLAC support
	* WavePack support
	* ModPlug support
	* PCM WAVE support
	* CD Audio support
	* CUE sheet support
	* ALSA sound output
	* JACK sound output
	* OSS sound output
	* PipeWire output
	* Last.fm/Libre.fm scrobbler
	* D-Bus support
	* Spectrum Analyzer
	* projectM visualization
	* sample rate conversion
	* bs2b dsp effect
	* streaming support
	* removable device detection
	* MPRIS support
	* global hotkey support
	* lyrics support

%description devel
QMMP is Qt-based audio player. This package contains its development files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%cmake \
	-D USE_AAC:BOOL=FALSE \
	-D USE_LIBRCD:BOOL=TRUE \
	-D QMMP_DEFAULT_OUTPUT=pipewire \
	-D CMAKE_INSTALL_PREFIX=%{_prefix} \
	-D LIB_DIR=%{_lib} \
	-D PLUGIN_DIR=%{_lib}/%{name}
%cmake_build
%install
%cmake_install
sed -i -e "s#audio/aac;##" \
       -e "s#audio/x-aac;##" \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
sed -i -e "s#audio/aac;##" \
       -e "s#audio/x-aac;##" \
    %{buildroot}/%{_datadir}/applications/%{name}-enqueue.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-dir.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-enqueue.desktop
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n qmmp-devel -f %{oreon_filedir}/qmmp-devel.list

%changelog

%autochangelog
