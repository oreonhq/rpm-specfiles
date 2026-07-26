%global source0_hash 3d9d6f8727e9a496cad881a404f85bc576396d0e094437a6b379d83fbc096a4f

Name:           exaile
Version:        4.2.1
Release:        1%{?dist}
Summary:        Simple but powerful Amarok-style music player for GTK users
License:        GPL-2.0-or-later
URL:            http://www.exaile.org
Source0:        https://github.com/exaile/exaile/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-rpm-macros

# Dependencies:
# see also https://github.com/exaile/exaile/blob/master/DEPS
BuildRequires:  cairo-gobject
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gobject-introspection
BuildRequires:  gstreamer1-plugins-base >= 1.16
BuildRequires:  gstreamer1-plugins-good >= 1.16
BuildRequires:  gtk3 >= 3.24
BuildRequires:  help2man
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  python3-bsddb3
BuildRequires:  python3-cairo
BuildRequires:  python3-dbus
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel >= 3.24
BuildRequires:  python3-gstreamer1 >= 1.16
BuildRequires:  python3-mutagen >= 1.44
BuildRequires:  python3-setproctitle
BuildRequires:  python3-pytest

Requires:       python3 >= 3.8
Requires:       python3-bsddb3
Requires:       gtk3 >= 3.24
Requires:       python3-gstreamer1 >= 1.16
Requires:       gstreamer1-plugins-good >= 1.16
Requires:       gstreamer1-plugins-base >= 1.16
Requires:       python3-mutagen >= 1.44
Requires:       python3-dbus
Requires:       python3-gobject >= 3.24
Requires:       python3-cairo
Requires:       cairo-gobject
Requires:       python3-setproctitle

# Device detection:
Recommends:     libudisks2
# DAAP plugins (daapserver and daapclient):
Recommends:     python3-zeroconf
#Not packaged for Fedora
#Recommends:     spydaap
# Last.FM integration:
Recommends:     python3-pylast
# Lyrics from lyricsmania.com (lyricsmania):
Recommends:     python3-lxml
# Lyrics from lyrics.wikia.com (lyricwiki):
Recommends:     python3-beautifulsoup4
# Musicbrainz covers:
Recommends:     python3-musicbrainzngs
# Podcast plugin:
Recommends:     python3-feedparser
# Wikipedia info:
#Not packaged for fedora
#Recommends:     webkit2gtk3
# Xlib-based hotkeys:
Recommends:     keybinder3
# Scalable icons:
Recommends:     librsvg2
# Native Notifications:
Recommends:     libnotify
# Recording streams:
Recommends:     streamripper
# Moodbar plugin:
#FTBFS on Fedora 30+, may be dropped soon
#Recommends:     moodbar
# BPM Counter plugin:
Recommends:     gstreamer1-plugins-bad-free
# CD Info and Musicbrainz covers:
Recommends:     python3-discid
Recommends:     python3-musicbrainzngs

%description
Exaile is a music player with a simple interface and powerful music
management capabilities. Features include automatic fetching of album art,
lyrics fetching, streaming internet radio, tabbed playlists, smart
playlists with extensive filtering/search capabilities, and much more.

Exaile is written using Python and GTK+ and is easily extensible via
plugins. There are over 50 plugins distributed with Exaile that include
advanced track tagging, last.fm scrobbling, support for portable media
players, podcasts, internet radio such as icecast and Soma.FM,
ReplayGain, output via a secondary output device (great for DJs!), and
much more.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%set_build_flags

# Keep timestamps while installing
# Delegate pyc compilation to brp-python-bytecompile
sed -i "s|install -m|\$(INSTALL) -m|;s|all: compile |all: |" Makefile

# Disable plugins that aren't packaged or don't work on Fedora
sed -i "s|BAD = \[\]|BAD = ['daapclient', 'daapserver', 'moodbar', 'winmmkeys', 'wikipedia']|" plugins/list.py

%make_build

%install
%make_install PREFIX=%{_prefix} LIBINSTALLDIR=%{_datadir} PYTHON3_CMD=%{__python3}

desktop-file-install --delete-original \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%check
# this test should be ignored on Fedora/Debian systems and also doesn't work via Koji
rm tests/xl/trax/test_migration.py

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.exaile.exaile.appdata.xml

make test

%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/exaile
%{_metainfodir}/org.exaile.exaile.appdata.xml
%{_datadir}/applications/exaile.desktop
%{_datadir}/bash-completion/completions/exaile
%{_datadir}/fish/vendor_completions.d/exaile.fish
%{_datadir}/icons/hicolor/*/apps/exaile.*
%{_datadir}/exaile/
%{_datadir}/dbus-1/services/org.exaile.Exaile.service
%dir %{_sysconfdir}/xdg/exaile/
%config(noreplace) %{_sysconfdir}/xdg/exaile/settings.ini
%{_mandir}/man1/exaile*.1*

%changelog
%autochangelog
