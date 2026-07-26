%global source0_hash 2456f1c5a4110b0c594e10cdab8098308dd166be4c93e16d98ae58eebbe31b24

Name:           hexglass
Version:        1.2.1
Release:        37%{?dist}
Summary:        Block falling puzzle game based on a hexagonal grid 
Summary(de):    Puzzlespiel mit fallenden Blöcken auf einem sechseckigen Raster

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://code.google.com/p/hexglass
Source0:        http://hexglass.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop

# Let the application search for locale files in
# /usr/share/hexglass/translations/
Patch0:         %{name}-%{version}-locale-path.patch

BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  qt4-devel
BuildRequires: make

%description
HexGlass is a Tetris-like puzzle game. Ten different types of blocks 
continuously fall from above and you must arrange them to make horizontal 
rows of hexagonal bricks. Completing any row causes those hexagonal blocks 
to disappear and the rest above move downwards. The blocks above gradually 
fall faster and the game is over when the screen fills up and blocks can 
no longer fall from the top. 

%description -l de
HexGlass ist ein Tetris-ähnliches Puzzlespiel. Zehn verschiedene Blocktypen
fallen fortwährend nach unten und müssen so angeordnet werden, dass horizontale
Zeilen aus sechseckigen Elementen gebildet werden. Nach Vervollständigen einer
Zeile verschwinden die Blöcke, wodurch die übrigen nach unten verschoben
werden. Mit steigendem Schwierigkeitsgrad fallen die Blöcke schneller. 
Das Spiel ist vorbei, sobald das Spielfeld vollständig gefüllt ist und keine 
Blöcke mehr fallen können.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build
%{qmake_qt4} hexglass.pro
make %{?_smp_mflags}

%install
install -D hexglass %{buildroot}%{_bindir}/hexglass
install -d %{buildroot}%{_datadir}/%{name}/translations
install -m 644 -p translations/*.qm %{buildroot}%{_datadir}/%{name}/translations
install -D -m 644 -p resources/about_icon.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

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
<!-- Copyright 2014 Tim Waugh <twaugh@redhat.com> -->
<!--
BugReportURL: https://code.google.com/p/hexglass/issues/detail?id=1
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">hexglass.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Drop shapes to the bottom without leaving gaps</summary>
  <description>
    <p>
      In HexGlass the object is to rotate shaped pieces as the fall to the bottom
      so that they don't leave gaps.
      The pieces are made of small numbers of hexagons stuck together, and it is
      hard to work out the right way to rotate each piece as there are 6
      possible orientations.
    </p>
    <p>
      When a row is completed without any gaps, it is removed and all the
      hexagonal blocks above it move down one row.
      As the pieces fall faster, make sure not to let the screen fill up!
    </p>
  </description>
  <url type="homepage">http://code.google.com/p/hexglass</url>
  <screenshots>
    <screenshot type="default">http://hexglass.googlecode.com/svn/wiki/preview.png</screenshot>
  </screenshots>
</application>
EOF

%find_lang %{name} --with-qt

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}

%files -f %{name}.lang
%doc CHANGES COPYING README
%{_bindir}/hexglass
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/translations/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm

%changelog
%autochangelog
