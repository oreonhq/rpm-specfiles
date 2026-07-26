%global source0_hash a61d1c1faa9c411c75292a5710999182b918831b8f0f200c87149e3ff353bea9

Name:		qmmp
Version:	2.3.1
Release:	2%{?dist}
Summary:	Qt-based multimedia player

License:	GPL-2.0-or-later AND CC-BY-SA-4.0
URL:		http://qmmp.ylsoftware.com/
Source:		http://qmmp.ylsoftware.com/files/%{name}-%{version}.tar.bz2

BuildRequires:	alsa-lib-devel
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	enca-devel
BuildRequires:	ffmpeg-free-devel
BuildRequires:	flac-devel
BuildRequires:	game-music-emu-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libarchive-devel
BuildRequires:	libbs2b-devel
BuildRequires:	libcddb-devel
BuildRequires:	libcdio-paranoia-devel
BuildRequires:	libcurl-devel
BuildRequires:	libmad-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libogg-devel
BuildRequires:	libprojectM-devel
BuildRequires:	librcd-devel
BuildRequires:	libshout-devel
BuildRequires:	libsidplayfp-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxmp-devel
BuildRequires:	mpg123-devel
BuildRequires:	openssl-devel
BuildRequires:	opusfile-devel
BuildRequires:	pipewire-devel
BuildRequires:	qt6-qtmultimedia-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	soxr-devel
BuildRequires:	taglib-devel >= 1.10
BuildRequires:	wavpack-devel
BuildRequires:	wildmidi-devel

# /usr/share/solid/actions owner
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
Requires:	kde-filesystem
%elif %{undefined flatpak}
Requires:	kf5-filesystem
%endif

Recommends:	qmmp-plugin-pack
# some external tools listed in
# https://sourceforge.net/p/qmmp-dev/code/HEAD/tree/trunk/qmmp/src/plugins/General/converter/presets.conf
Recommends:	vorbis-tools
Recommends:	lame
Recommends:	opus-tools
Recommends:	wavpack
Recommends:	flac

# Do not check .so files in an application-specific library directory
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$

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
# filter out unsupported formats from MimeType
sed -i -e "s#audio/aac;##" \
       -e "s#audio/x-aac;##" \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
sed -i -e "s#audio/aac;##" \
       -e "s#audio/x-aac;##" \
    %{buildroot}/%{_datadir}/applications/%{name}-enqueue.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-dir.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-enqueue.desktop
# the validator makes assumptions not mandated by the standard
# https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html
# as of today, 2020-07-31
#desktop-file-validate %%{buildroot}/%%{_datadir}/solid/actions/%%{name}-opencda.desktop

%files
%doc AUTHORS ChangeLog ChangeLog.rus README README.RUS
%license COPYING COPYING.CC-by-sa_V4
%{_bindir}/qmmp
%{_libdir}/qmmp
%{_libdir}/libqmmp*.so.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-dir.desktop
%{_datadir}/applications/%{name}-enqueue.desktop
%{_datadir}/solid/actions/%{name}-opencda.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}/
%{_metainfodir}/com.ylsoftware.%{name}.metainfo.xml

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/qmmp*
%{_libdir}/libqmmp*.so

%changelog
%autochangelog
