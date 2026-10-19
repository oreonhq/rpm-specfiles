%global source0_hash 333203a0aa3ea8c7d81e32467aff2b24fe739da942c0d8cd25643a7ba2d845e3
%global usesnapshot 0
%global commit0 5f80bc4c5d0cb532f1a5ad9679d56bd16db89414
%if 0%{?usesnapshot}
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gitdate 20241205
%endif
%global metadata_name org.guayadeque.Guayadeque
Name:           guayadeque
%if 0%{?usesnapshot}
Version:        0.7.5
Release:        1%{?dist}
%else
Version:        0.7.5
Release:        1%{?dist}
%endif
Summary:        Music player
License:        GPL-3.0-or-later AND BSD-3-Clause
URL:            https://codeberg.org/thothix/guayadeque
%if 0%{?usesnapshot}
Source0:        https://codeberg.org/thothix/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
%endif
Source1:        PACKAGE-LICENSING
Suggests:       gstreamer1-libav
Provides:       bundled(md5-polstra)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  libgpod-devel
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(icu-io)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  sqlite-devel
BuildRequires:  taglib-devel
BuildRequires:  wxGTK-devel
BuildRequires:  wxsqlite3-devel
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n guayadeque-langpack-bg -f %{oreon_filedir}/guayadeque-langpack-bg.list
%files -n guayadeque-langpack-ca_ES -f %{oreon_filedir}/guayadeque-langpack-ca_ES.list
%files -n guayadeque-langpack-cs -f %{oreon_filedir}/guayadeque-langpack-cs.list
%files -n guayadeque-langpack-da -f %{oreon_filedir}/guayadeque-langpack-da.list
%files -n guayadeque-langpack-de -f %{oreon_filedir}/guayadeque-langpack-de.list
%files -n guayadeque-langpack-el -f %{oreon_filedir}/guayadeque-langpack-el.list
%files -n guayadeque-langpack-es -f %{oreon_filedir}/guayadeque-langpack-es.list
%files -n guayadeque-langpack-fr -f %{oreon_filedir}/guayadeque-langpack-fr.list
%files -n guayadeque-langpack-hr -f %{oreon_filedir}/guayadeque-langpack-hr.list
%files -n guayadeque-langpack-hu -f %{oreon_filedir}/guayadeque-langpack-hu.list
%files -n guayadeque-langpack-is -f %{oreon_filedir}/guayadeque-langpack-is.list
%files -n guayadeque-langpack-it -f %{oreon_filedir}/guayadeque-langpack-it.list
%files -n guayadeque-langpack-ja -f %{oreon_filedir}/guayadeque-langpack-ja.list
%files -n guayadeque-langpack-lt -f %{oreon_filedir}/guayadeque-langpack-lt.list
%files -n guayadeque-langpack-ms -f %{oreon_filedir}/guayadeque-langpack-ms.list
%files -n guayadeque-langpack-nb -f %{oreon_filedir}/guayadeque-langpack-nb.list
%files -n guayadeque-langpack-nl -f %{oreon_filedir}/guayadeque-langpack-nl.list
%files -n guayadeque-langpack-pl -f %{oreon_filedir}/guayadeque-langpack-pl.list
%files -n guayadeque-langpack-pt -f %{oreon_filedir}/guayadeque-langpack-pt.list
%files -n guayadeque-langpack-pt_BR -f %{oreon_filedir}/guayadeque-langpack-pt_BR.list
%files -n guayadeque-langpack-ru -f %{oreon_filedir}/guayadeque-langpack-ru.list
%files -n guayadeque-langpack-sk -f %{oreon_filedir}/guayadeque-langpack-sk.list
%files -n guayadeque-langpack-sr -f %{oreon_filedir}/guayadeque-langpack-sr.list
%files -n guayadeque-langpack-sv -f %{oreon_filedir}/guayadeque-langpack-sv.list
%files -n guayadeque-langpack-th -f %{oreon_filedir}/guayadeque-langpack-th.list
%files -n guayadeque-langpack-tr -f %{oreon_filedir}/guayadeque-langpack-tr.list
%files -n guayadeque-langpack-uk -f %{oreon_filedir}/guayadeque-langpack-uk.list

%changelog

%autochangelog
