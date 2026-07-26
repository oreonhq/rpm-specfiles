%global source0_hash a23c202f90faaf6aebb97a9c02ee21fb3c8164b07755514349ccb3e1acb81ab5

Name:           qmmp-plugin-pack
Version:        2.3.0
Release:        4%{?dist}
Summary:        A set of extra plugins for Qmmp

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://qmmp.ylsoftware.com/plugins.php
Source0:        %{url}/files/{%name}/2.3/%{name}-%{version}.tar.bz2

BuildRequires:  qmmp-devel >= 2.3.0
BuildRequires:  cmake
BuildRequires:  ffmpeg-free-devel
BuildRequires:  libmms-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  mpv-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  taglib-devel

Recommends:     yt-dlp

# Do not check .so files in an application-specific library directory
%global __provides_exclude_from ^%{_libdir}/qmmp/.*\\.so$

%description
Plugin pack is a set of extra plugins for Qmmp.

 * FFap - enhanced Monkey's Audio (APE) decoder
   (24-bit samples and embedded cue support)
 * FFVideo - video playback engine based on FFmpeg library
 * Goom - audio visualization based on goom project
 * MMS - MMS protocol support (uses libmms library)
 * ModPlug - module player with use of the libmodplug library
 * Mpv - video playback using mpv
 * SRC - sample rate converter
 * Ytb - audio playback from YouTube (uses yt-dlp or youtube-dl)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%cmake \
        -D USE_MPLAYER:BOOL=FALSE \
        -D PLUGIN_DIR=%{_lib}/qmmp
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS ChangeLog.rus README README.RUS
%license COPYING
%{_libdir}/qmmp/Effect/*.so
%{_libdir}/qmmp/Engines/*.so
%{_libdir}/qmmp/Input/*.so
%{_libdir}/qmmp/Transports/*.so
%{_libdir}/qmmp/Visual/*.so
%{_metainfodir}/%{name}.appdata.xml

%changelog
%autochangelog
