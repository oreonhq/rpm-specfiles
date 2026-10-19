%global source0_hash 73fe63cca4f96e2d355480d03bc0b2904e83a0abdf65fe8c52db5cc3cca88fa0
Name:           neverball
Version:        1.6.0
Release:        1%{?dist}
Summary:        Common files for neverball and neverputt
License:        GPL-2.0-or-later
URL:            http://neverball.org
Source0:        http://neverball.org/neverball-%{version}.tar.gz
Source1:        neverball.desktop
Source2:        neverputt.desktop
# oreon:deps
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libGL-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  physfs-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
This package provides common files needed by both the Neverball and Neverputt
games.

%package neverputt
Summary: Minigolf like game
Requires: opengl-games-utils dejavu-sans-fonts
Requires: %{name}%{?_isa} = %{version}-%{release}
%description neverputt
A hot-seat multiplayer miniature golf game, built on the physics and graphics
engine of Neverball.

%package neverball
Summary: Roll a ball through an obstacle course
Requires: opengl-games-utils dejavu-sans-fonts
Requires: %{name}%{?_isa} = %{version}-%{release}
%description neverball
Tilt the floor to roll a ball through an obstacle course within the
given time.  If the ball falls or time expires, a ball is lost.

Collect 100 coins to save your progress and earn an extra ball.  Red
coins are worth 5.  Blue coins are worth 10.

%prep

%setup -q
#%patch0 -p0
#%patch1 -p0

%build

make CFLAGS="$RPM_OPT_FLAGS -ansi `sdl2-config --cflags` -fcommon" DATADIR=%{_datadir}/%{name} LOCALEDIR=%{_datadir}/locale ENABLE_NLS=1 %{?_smp_mflags}
%install
install -p -D -m0755 neverball $RPM_BUILD_ROOT/%{_bindir}/neverball
install -p -D -m0755 neverputt $RPM_BUILD_ROOT/%{_bindir}/neverputt
install -p -d -m0755 $RPM_BUILD_ROOT/%{_datadir}/%{name}/
cp -ap  data/* $RPM_BUILD_ROOT/%{_datadir}/%{name}/
install -p -D -m0644 dist/neverball_128.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/128x128/apps/neverball.png
install -p -D -m0644 dist/neverball_16.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/16x16/apps/neverball.png
install -p -D -m0644 dist/neverball_24.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/24x24/apps/neverball.png
install -p -D -m0644 dist/neverball_256.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/256x256/apps/neverball.png
install -p -D -m0644 dist/neverball_32.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/neverball.png
install -p -D -m0644 dist/neverball_48.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/neverball.png
install -p -D -m0644 dist/neverball_512.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/512x512/apps/neverball.png
install -p -D -m0644 dist/neverball_64.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/64x64/apps/neverball.png
install -p -D -m0644 dist/neverputt_128.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/128x128/apps/neverputt.png
install -p -D -m0644 dist/neverputt_16.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/16x16/apps/neverputt.png
install -p -D -m0644 dist/neverputt_24.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/24x24/apps/neverputt.png
install -p -D -m0644 dist/neverputt_256.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/256x256/apps/neverputt.png
install -p -D -m0644 dist/neverputt_32.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/neverputt.png
install -p -D -m0644 dist/neverputt_48.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/neverputt.png
install -p -D -m0644 dist/neverputt_512.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/512x512/apps/neverputt.png
install -p -D -m0644 dist/neverputt_64.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/64x64/apps/neverputt.png
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/ttf/DejaVuSans-Bold.ttf
ln -s %{_datadir}/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf $RPM_BUILD_ROOT%{_datadir}/%{name}/ttf/DejaVuSans-Bold.ttf
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/neverball-wrapper
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/neverputt-wrapper
desktop-file-install \
  --dir $RPM_BUILD_ROOT/%{_datadir}/applications \
%{SOURCE1}
desktop-file-install \
  --dir $RPM_BUILD_ROOT/%{_datadir}/applications \
%{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
BugReportURL: http://forum.nevercorner.net/viewtopic.php?pid=31145
SentUpstream: 2014-09-22
-->
<application>
  <id type="desktop">neverball.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <description>
    <p>
      Tilt the floor to roll a ball through an obstacle course before time runs
      out.
      Neverball is part puzzle game, part action game, and entirely a test of
      skill.
    </p>
    <p>
      The current version includes 141 Neverball levels and 134 Neverputt holes.
    </p>
  </description>
  <url type="homepage">http://neverball.org/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/neverball/a.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/neverball/b.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/neverball/c.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/neverputt.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 William Moreno Reyes <williamjmorenor@gmail.com> -->
<!--
BugReportURL: http://forum.nevercorner.net/viewtopic.php?pid=31149#p31149
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">neverputt.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Guide a ball around the obstacles tilting the floor</summary>
  <description>
    <p>
      In Neverball you must guide a ball around the obstacle tilting the floor
      before the time is over.
    </p>
    <p>
      Neverball is very similar to Super Monkey Ball, you must guide the ball to
      the end point of each level getting all coins as you can.
    </p>
  </description>
  <url type="homepage">http://neverball.org</url>
</application>
EOF
mkdir -p %{buildroot}%{_datadir}/locale
cp -pr locale/* %{buildroot}%{_datadir}/locale/
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n neverball-neverputt -f %{oreon_filedir}/neverball-neverputt.list
%files -n neverball-neverball -f %{oreon_filedir}/neverball-neverball.list

%changelog

%autochangelog
