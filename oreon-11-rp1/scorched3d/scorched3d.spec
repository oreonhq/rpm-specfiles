%global source0_hash none

%global fonts font(dejavusans) font(dejavusansmono)

Name:           scorched3d
Version:        44
Release:        39%{?dist}
Summary:        Game based loosely on the classic DOS game Scorched Earth
# Automatically converted from old format: GPLv2+ and CC-BY-SA - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            http://www.scorched3d.co.uk/
Source0:        http://downloads.sourceforge.net/%{name}/Scorched3D-%{version}-src.tar.gz
Source1:        %{name}.desktop
# Fake openal-config as openal-soft doesn't have it
Source2:        openal-config
Patch1:         %{name}-syslibs.patch
Patch2:         %{name}-help.patch
Patch3:         %{name}-freetype-buildfix.patch
Patch4:         %{name}-sys-lua.patch
Patch5:         %{name}-returntype.patch
Patch6:         %{name}-wx3.0.patch
Patch7:         %{name}-lua54.patch
Patch8:         %{name}-fix-hang-on-fast-machines.patch
Patch9:         scorched3d-configure-c99.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  wxGTK-devel SDL_net-devel libGLU-devel
BuildRequires:  expat-devel libvorbis-devel glew-devel fftw-devel libjpeg-devel
BuildRequires:  freetype-devel openal-soft-devel freealut-devel >= 1.1.0-10
BuildRequires:  lua-devel libtool autoconf automake
BuildRequires:  ImageMagick desktop-file-utils
BuildRequires:  fontconfig %{fonts}
Requires:       hicolor-icon-theme opengl-games-utils %{fonts}
# Upstream naming compatibility
Provides:       Scorched3D = %{version}-%{release}

%description
Scorched 3D is a game based on the classic DOS game Scorched Earth
"The Mother Of All Games".  Scorched 3D adds amongst other new
features a 3D island environment and LAN and internet play.  At its
lowest level, Scorched 3D is just an artillery game with two+ tanks
taking turns to destroy opponents in an arena.  Choose the angle,
direction and power of each shot, launch your weapon, and try to blow
up other tanks.  But Scorched 3D can be a lot more complex than that,
if you want it to be.  You can earn money from successful battles and
use it to invest in additional weapons and accessories.  You can play
with up to twenty four other players at a time, mixing computer
players with humans.  There's a variety of changing environmental
conditions and terrains to be dealt with.

%prep
%setup -q -c
pushd scorched
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p0
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p2
touch NEWS AUTHORS ChangeLog
autoreconf -ivf
install -m 755 %{SOURCE2} .
# for %%doc
mkdir apoc
cp -a data/globalmods/apoc/*.txt apoc
# ensure we use the system versions of these
rm src/common/common/snprintf.c
rm src/common/lua/l*.{cpp,h}
rm src/common/lua/print.cpp
popd

%build
pushd scorched
export OPENAL_CONFIG=$PWD/openal-config
%configure --disable-dependency-tracking --datadir=%{_datadir}/%{name}
make %{?_smp_mflags}

# Note that tank2.ico has 48x48 and 32x32 icons embedded in it.
# The 48x48 icon ends up in tank2-0.png
convert data/images/tank2.ico tank2.png
popd

%install
pushd scorched
%make_install
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper

ln -f -s $(fc-match -f "%{file}" "sans") \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/data/fonts/dejavusans.ttf
ln -f -s $(fc-match -f "%{file}" "sans:condensed:bold") \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/data/fonts/dejavusconbd.ttf
ln -f -s $(fc-match -f "%{file}" "monospace:bold") \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/data/fonts/dejavusmobd.ttf

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 tank2-0.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
popd

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
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: http://www.scorched3d.co.uk/mantisbt/view.php?id=209
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">scorched3d.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Turn based 3D artillery game</summary>
  <description>
    <p>
      Scorched 3D is a turn-based 3D artillery game where you take control of a
      tank and attack your opponents in a 3D landscape with a range of weapons.
      It also features some real-time elements allowing you to counter opponents
      attacks, and also features online multiplayer modes.
    </p>
  </description>
  <screenshots>
    <screenshot type="default">http://www.scorched3d.co.uk/phpBB3/gallery/image.php?album_id=8&amp;image_id=61&amp;view=no_count</screenshot>
    <screenshot>http://www.scorched3d.co.uk/phpBB3/gallery/image.php?album_id=3&amp;image_id=4&amp;view=no_count</screenshot>
  </screenshots>
  <url type="homepage">http://www.scorched3d.co.uk/</url>
</application>
EOF

%files
%doc scorched/COPYING scorched/apoc
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%changelog
%autochangelog
