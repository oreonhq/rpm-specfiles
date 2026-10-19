%global source0_hash 8ca55f51eb56ffaa17630b3827fb922a8146cb268464bbfcea9fad76b52ab0d7
%bcond tests 1
%bcond streamtagreader              1
%bcond qpa_qplatformnativeinterface 1
%bcond gpod                         1
%global giturl https://github.com/strawberrymusicplayer/strawberry
Name:           strawberry
Version:        1.2.30
Release:        1%{?dist}
Summary:        Audio player and music collection organizer
License:        Apache-2.0 AND GPL-2.0-or-later AND GPL-3.0-or-later AND MIT
URL:            https://www.strawberrymusicplayer.org/
Source0:        %{giturl}/archive/%{version}/%{name}-%{version}.tar.gz
%if %{with streamtagreader}
%endif
%if %{with gpod}
%endif
%if %{with qpa_qplatformnativeinterface}
%endif
%if %{with tests}
%endif
Requires:       gstreamer1-plugins-good
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6XcbQpaPrivate)
BuildRequires:  cmake(RapidJSON)
BuildRequires:  cmake(kdsingleapplication-qt6)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  pkgconfig(libebur128)
BuildRequires:  pkgconfig(libgpod-1.0)
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsparsehash)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(taglib)
# /oreon:deps
%description
Strawberry is a audio player and music collection organizer.
It is a fork of Clementine. The name is inspired by the band Strawbs.

Features:
  * Play and organize music
  * Supports WAV, FLAC, WavPack, DSF, DSDIFF, Ogg Vorbis, Speex, MPC,
    TrueAudio, AIFF, MP4, MP3 and ASF
  * Audio CD playback
  * Native desktop notifications
  * Playlists in multiple formats
  * Advanced output and device options with support for bit perfect playback
    on Linux
  * Edit tags on music files
  * Fetch tags from MusicBrainz
  * Album cover art from Last.fm, Musicbrainz and Discogs
  * Song lyrics from AudD and API Seeds
  * Support for multiple backends
  * Audio analyzer
  * Equalizer
  * Transfer music to iPod, iPhone, MTP or mass-storage USB player
  * Integrated Tidal support
  * Scrobbler with support for Last.fm, Libre.fm and ListenBrainz

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%if %{with tests}
# Disable tests that need graphical environment and thus don't work in mock
sed -i '/add_test_file(.* true)/d' tests/CMakeLists.txt
%endif

%build

%{cmake} -DBUILD_WERROR:BOOL=OFF \
%if !%{with qpa_qplatformnativeinterface}
         -DENABLE_QPA_QPLATFORMNATIVEINTERFACE=OFF \
%endif
%if !%{with streamtagreader}
         -DENABLE_STREAMTAGREADER=OFF \
%endif
%if !%{with gpod}
         -DENABLE_GPOD=OFF \
%endif
         -DCMAKE_BUILD_TYPE:STRING=Release
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

%if %{with tests}
%{cmake_build} -t run_strawberry_tests
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/org.strawberrymusicplayer.strawberry.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.strawberrymusicplayer.strawberry.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
