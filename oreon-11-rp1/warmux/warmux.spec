%global source0_hash none

Name:           warmux
Version:        11.04.1
Release:        43%{?dist}
Summary:        2D turn-based artillery game

# fixedpoint library seems to be under BSD license
# Some parts of src/tool/xml_document.cpp are taken from libxml2 (released under the MIT license)
# Automatically converted from old format: GPLv2+ and BSD and MIT - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            http://gna.org/projects/warmux/
Source0:        http://download.gna.org/warmux/warmux-%{version}.tar.bz2

# Remove Superman logo due to copyright
Source1:        superman.png
Source2:        supertux_ico.png
Source3:        supertux.png

Patch1:         warmux-zlib.patch
Patch2:         warmux-gcc47.patch
Patch3:         warmux-gcc60.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  SDL_image-devel SDL_gfx-devel SDL_mixer-devel
BuildRequires:  SDL_ttf-devel SDL_net-devel curl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(dbus-1)

BuildRequires:  gettext libxml++-devel desktop-file-utils
BuildRequires:  zlib-devel
Requires:       warmux-data = %{version}
Requires:       hicolor-icon-theme

Provides:       wormux = %{version}-%{release}
Obsoletes:      wormux < 0.9.2.1-9

%description
Let's begin the WAR of Mascots from UniX!
They'll represent your favorite free software titles while battling it out
in the arena using dynamite, grenades, baseball bats and other bazookas...
Exterminate your opponent in a 2D environment with toon-style scenery.
Each player controls the team of his choice (penguin, gnu, firefox, wilber,...)
and must destroy his adversary using more or less casual weapons.
Although a minimum of strategy is required to vanquish, WarMUX is pre-eminently
a "convivial mass murder" game where, turn by turn, each member of each team.

The project was started as Wormux, and was renamed to Warmux in November 2010.

%package data
Summary: Data files for warmux
Requires: %{name} = %{version}
BuildArch: noarch
Provides:  wormux-data = %{version}-%{release}
Obsoletes: wormux-data < 0.9.2.1-9

%description data
Data files for warmux

%prep
%setup -q -n warmux-11.04
%patch -P1 -p1 -b .zlib
%patch -P2 -p1 -b .gcc47
%patch -P3 -p0 -b .gcc60

# Remove a backup file
rm -f data/game_mode/rope_objects.xml~
rm -f data/game_mode/skin_viewer.xml~

%build
%configure --enable-fribidi
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

sed -i -e 's/Icon=.*/Icon=warmux/' \
        %{buildroot}%{_datadir}/applications/warmux.desktop

desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications/ \
        --remove-category=Application \
        --remove-category=ArcadeGame \
        --add-category=StrategyGame \
        --delete-original \
        %{buildroot}%{_datadir}/applications/warmux.desktop

install -d %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -p -m 644 data/icon/warmux_128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/warmux.png

install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/warmux/weapon/supertux/superman.png
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/warmux/weapon/supertux/supertux_ico.png
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/warmux/weapon/supertux/supertux.png

rm -f %{buildroot}%{_datadir}/applications/warmux_files.desktop
rm -f %{buildroot}%{_datadir}/warmux/.nomedia

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
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
SentUpstream: Dead!
-->
<application>
  <id type="desktop">warmux.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <description>
    <p>
      WarMUX is a free and open-source turn-based game and can be played online
      in public or private mode.
    </p>
    <p>
      Players can play together each one in the commande of a team in a senario
      that puts free software mascots in a battle using dynamite, grenades,
      baseball bats, and bazookas.
    </p>
  </description>
  <url type="homepage">http://sourceforge.net/projects/warmux/</url>
  <screenshots>
    <screenshot type="default">http://a.fsdn.com/con/app/proj/warmux.mirror/screenshots/Warmux.jpg</screenshot>
    <screenshot>http://a.fsdn.com/con/app/proj/warmux.mirror/screenshots/warmux.png</screenshot>
    <screenshot>http://a.fsdn.com/con/app/proj/warmux.mirror/screenshots/Warmux1.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/warmux
%{_bindir}/warmux-list-games
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/warmux.desktop
%{_datadir}/icons/hicolor/128x128/apps/warmux.png
%{_datadir}/pixmaps/warmux*.png
%{_mandir}/man6/*.6.gz

%files data
%{_datadir}/warmux

%changelog
%autochangelog
