%global source0_hash 123a461d81c9eecd7af1528a81aa5e8ddd65bb2c8268f09fe888a6c69ee28079

%global usesnapshot 0
%global commit0 5f80bc4c5d0cb532f1a5ad9679d56bd16db89414
%if 0%{?usesnapshot}
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gitdate 20241205
%endif
%global metadata_name org.guayadeque.Guayadeque

Name:           guayadeque
%if 0%{?usesnapshot}
Version:        0.6.2
Release:        0.7.beta6.git%{shortcommit0}%{dist}
%else
Version:        0.7.5
Release:        4%{?dist}
%endif
Summary:        Music player
# The entire source code is GPL-3.0-or-later except hmac/ which is BSD-3-Clause
License:        GPL-3.0-or-later AND BSD-3-Clause
URL:            https://codeberg.org/thothix/guayadeque
%if 0%{?usesnapshot}
Source0:        %url/archive/%{commit0}/%{name}-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%else
Source0:        %url/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif
# For a breakdown of the licensing, see PACKAGE-LICENSING
Source1:        PACKAGE-LICENSING

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  taglib-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgpod-devel
BuildRequires:  pkgconfig(icu-io)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  sqlite-devel
BuildRequires:  wxGTK-devel
BuildRequires:  wxsqlite3-devel
BuildRequires:  dbus-devel
BuildRequires:  gettext-devel
Suggests:       gstreamer1-libav

Provides:       bundled(md5-polstra)

%description
Guayadeque is a lightweight and easy-to-use music player and music collection
organizer that can easily manage large music collections and supports smart
playlists.
In the technical side, it's written in C++, uses the wxWidget toolkit and the
Gstreamer media framework.

Main features include:

  - Play mp3, ogg, flac, wav, wma, mpc, mp4, ape, ...
  - Read and write tags in all supported formats.
  - Smart play mode that add tracks that fit your music taste using the tracks
    in the playlist.
  - Allow to catalogue your music using labels. Any track, artist or album can
    have as many labels you want.
  - Allow fast access to any music file by genre, artist, album
  - Audio equalizer
  - Configurable cross fader engine
  - Configurable Silence detector to avoid listening to silence between tracks
  - Dynamic and static playlists management.
  - Tracks tag editor with automatically fetching of tags information for easily
    completion.
  - Ability to download covers manually or automatically
  - Lyrics downloads from different lyrics providers.
  - You can rate the tracks from 0 to 5 stars.
  - Desktop notifications.
  - MPRIS D-Bus interface support so it can easily controlled from music applets
    for example.
  - Allow to resume play status and position when closed and reopened.
  - Allow to subscribe to podcasts and download all new episodes automatically
    or manually.
  - Play and Record shoutcast radios
  - Suggest music using last.fm service.
  - Last.fm audioscrobbling support.
  - Easily expandable contextual links support. With it you can find information
    about a track, an artist or an album on your favourite site.
  - Easily expandable contextual commands support. For example you can right
    click on any album and click in option to record the album in a burning
     application.
  - Option to copy the selection you want to a directory or device like USB
    players and IPod using a configurable pattern.
  - Partial GNOME session support to detect when GNOME session is about to
    close and save the play list so it can continue next time with the same
    tracks.
  - and many more.

%define         lang_subpkg() \
%package        langpack-%{1}\
Summary:        %{2} language data for %{name}\
BuildArch:      noarch \
Requires:       %{name} = %{version}-%{release}\
Supplements:    (%{name} = %{version}-%{release} and langpacks-%{1})\
\
%description    langpack-%{1}\
%{2} language data for %{name}.\
\
%files          langpack-%{1}\
%{_datadir}/locale/%{1}*/LC_MESSAGES/%{name}.mo

%lang_subpkg bg Bulgarian
%lang_subpkg ca_ES Catalan
%lang_subpkg cs Czech
%lang_subpkg da Danish
%lang_subpkg de German
%lang_subpkg el Greek
%lang_subpkg es Spanish
%lang_subpkg fr French
%lang_subpkg hr Croatian
%lang_subpkg hu Hungarian
%lang_subpkg is Icelandic
%lang_subpkg it Italian
%lang_subpkg ja Japanese
%lang_subpkg lt Lithuanian
%lang_subpkg ms "Malay (Malaysia)"
%lang_subpkg nb Norwegian
%lang_subpkg nl Dutch
%lang_subpkg pl Polish
%lang_subpkg pt Portuguese
%lang_subpkg pt_BR Brazil
%lang_subpkg ru Russian
%lang_subpkg sk Slovakian
%lang_subpkg sr "Serbian (Cyrillic and Latin)"
%lang_subpkg sv Swedish
%lang_subpkg th Thai
%lang_subpkg tr Turkish
%lang_subpkg uk Ukrainian

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?usesnapshot}
%autosetup -p1 -n %{name}-%{commit0}
%else
%autosetup -p1 -n %{name}-%{version}
%endif
cp -p %{SOURCE1} PACKAGE-LICENSING

%build
%cmake .                                                       \
 -DCMAKE_BUILD_TYPE='Release'                                  \
 -DCMAKE_CXX_FLAGS="%{optflags}"                               \
 -D_GUREVISION_:STRING="%{release}"
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/{applications,appdata}
desktop-file-install --delete-original  \
        --dir %{buildroot}%{_datadir}/applications   \
        --remove-category Application \
        %{buildroot}%{_datadir}/applications/%{metadata_name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

%files
%doc README
%license INSTALL.md LICENSE PACKAGE-LICENSING
%{_bindir}/%{name}
%{_datadir}/%{name}/*.conf
%{_datadir}/%{name}/*.xml
%dir %{_datadir}/%{name}
%exclude %{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/applications/%{metadata_name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/metainfo/%{metadata_name}.metainfo.xml

%changelog
%autochangelog
