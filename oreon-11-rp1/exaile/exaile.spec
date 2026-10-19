%global source0_hash 77b7782e3dda26784c5ed1e0c73b29d9aca619ad8d3af2131dd40989cf452bab
Name:           exaile
Version:        4.2.2
Release:        1%{?dist}
Summary:        Simple but powerful Amarok-style music player for GTK users
License:        GPL-2.0-or-later
URL:            http://www.exaile.org
Source0:        https://github.com/exaile/exaile/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
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
Recommends:     libudisks2
Recommends:     python3-zeroconf
Recommends:     python3-pylast
Recommends:     python3-lxml
Recommends:     python3-beautifulsoup4
Recommends:     python3-musicbrainzngs
Recommends:     python3-feedparser
Recommends:     keybinder3
Recommends:     librsvg2
Recommends:     libnotify
Recommends:     streamripper
Recommends:     gstreamer1-plugins-bad-free
Recommends:     python3-discid
Recommends:     python3-musicbrainzngs
# oreon:deps
BuildRequires:  cairo-gobject
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gobject-introspection
BuildRequires:  gstreamer1-plugins-base
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  gtk3
BuildRequires:  help2man
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  python3-bsddb3
BuildRequires:  python3-cairo
BuildRequires:  python3-dbus
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-gstreamer1
BuildRequires:  python3-mutagen
BuildRequires:  python3-pytest
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-setproctitle
# /oreon:deps
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
%oreon_prep
%build

%set_build_flags
sed -i "s|install -m|\$(INSTALL) -m|;s|all: compile |all: |" Makefile
sed -i "s|BAD = \[\]|BAD = ['daapclient', 'daapserver', 'moodbar', 'winmmkeys', 'wikipedia']|" plugins/list.py
%make_build
%install
%make_install PREFIX=%{_prefix} LIBINSTALLDIR=%{_datadir} PYTHON3_CMD=%{__python3}
desktop-file-install --delete-original \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
%oreon_autofiles main

%check

rm tests/xl/trax/test_migration.py
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.exaile.exaile.appdata.xml
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
