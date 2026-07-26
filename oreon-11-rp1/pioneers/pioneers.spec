%global source0_hash 9a358d88548e3866e14c46c2707f66c98f8040a7857d47965e1ed9805aeb631d

Name:           pioneers
Version:        15.6
Release:        14%{?dist}
Summary:        Turnbased board strategy game (colonize an island)
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://pio.sourceforge.net/
Source0:        http://downloads.sourceforge.net/pio/%{name}-%{version}.tar.gz
Patch0:         pioneers-15.6-sanitize.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libgnome-devel gtk2-devel gettext scrollkeeper intltool
BuildRequires:  itstool
BuildRequires:  perl(XML::Parser) desktop-file-utils
Requires:       hicolor-icon-theme
Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description
Pioneers is a computerized version of a well known strategy board game. The
goal of the game is to colonize an island. The players play the first
colonists hence the name pioneers.

Pioneers is a networkbased multiplayer game, this package contains the GUI
client as well as both a GUI and CLI version of the server for local games.

%package editor
Summary:        Pioneers Game Editor
Requires:       pioneers = %{version}-%{release}

%description editor
Pioneers is a computerized version of a well known strategy board game. The
goal of the game is to colonize an island. The players play the first
colinists hence the name pioneers.

The game editor allows maps and game descriptions to be created and
edited graphically.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# pioneers uses some GNU extensions
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE"
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

# Remove the too much like the original splashscreen
rm $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}/splash.png

# Reinstall the .desktop files
desktop-file-install --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-editor.desktop \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-server-gtk.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Eduardo Mayorga <e@mayorgalinux.com> -->
<!--
BugReportURL: https://sourceforge.net/p/pio/bugs/286/
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">pioneers.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Multiplayer board game inspired by The Settlers of Catan</summary>
  <description>
    <p>
      Pioneers is a free videogame implementation of the famous German game Settlers of Catan.
      The goal is to build towns, cities and roads on a board that is different every time, while accumulating various types of cards.
      It can be played online.
    </p>
  </description>
  <url type="homepage">http://pio.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://pio.sourceforge.net/screenshots0.11/client.png</screenshot>
  </screenshots>
</application>
EOF

%check
if grep Catan `find $RPM_BUILD_ROOT ! -path "$RPM_BUILD_ROOT/usr/src/debug*"`;
  then
  exit 1
fi

%post
scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :

%postun
scrollkeeper-update -q || :

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README NEWS
%{_bindir}/%{name}
%{_bindir}/%{name}ai
%{_bindir}/%{name}-metaserver
%{_bindir}/%{name}-server-console
%{_bindir}/%{name}-server-gtk
%{_datadir}/games/%{name}
%{_datadir}/pixmaps/%{name}
%{_datadir}/help/C/%{name}
%{_mandir}/man6/%{name}*.6.gz
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-server-gtk.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}-server.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}-server.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}-server.svg
%{_datadir}/icons/hicolor/scalable/actions/%{name}*.svg

%files editor
%{_bindir}/%{name}-editor
%{_datadir}/applications/%{name}-editor.desktop
%{_datadir}/pixmaps/%{name}-editor.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}-editor.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}-editor.svg

%changelog
%autochangelog
