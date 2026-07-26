%global source0_hash b49c1f19ab93564937db33ec2dfefd9d37bc793558a1b0ceaf9a958cac0adaab

%global _hardened_build 1
%global dpver 20230620

%global dqmirror1 http://distcache.freebsd.org/ports-distfiles/quake-data/quakesw-1.0.6.tar.gz
%global dqmirror2 https://www.libsdl.org/projects/quake/data/quakesw-1.0.6.tar.gz

Summary: Multiplayer, deathmatch oriented first person shooter
Name: xonotic
Version: 0.8.6
Release: 7%{?dist}
License: GPL-2.0-or-later and LGPL-2.0-or-later
URL: http://www.xonotic.org/
# Custom tarball:
# wget http://dl.xonotic.org/xonotic-%{version}.zip
# unzip xonotic-%{version}.zip
# cd Xonotic/source/
# cp ../misc/logos/icons_png/xonotic_256.png darkplaces/
# tar -cJf darkplaces-%{version}.tar.xz darkplaces/
Source0: darkplaces-%{version}.tar.xz
Source1: %{name}.desktop
Source10: darkplaces-quake.sh
Source11: darkplaces-quake.autodlrc
Source12: darkplaces-quake.desktop
Patch0: %{name}-gcc11.patch
BuildRequires: make
BuildRequires: gcc
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: file
BuildRequires: libX11-devel
BuildRequires: mesa-libGL-devel
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires: libjpeg-devel
%else
BuildRequires: libjpeg-turbo-devel
%endif
BuildRequires: libXext-devel 
BuildRequires: libXpm-devel
BuildRequires: libXxf86dga-devel
BuildRequires: libXxf86vm-devel
BuildRequires: SDL2-devel
BuildRequires: zlib-devel
Requires: xonotic-data = %{version}
Requires: darkplaces = %{dpver}-%{release}
Requires: opengl-games-utils

%description
Xonotic is a fast-paced, chaotic, and intense multiplayer first person shooter, 
focused on providing basic, old style deathmatches.

%package server
Summary: Dedicated server for the Xonotic first person shooter
Requires: xonotic-data = %{version}
Requires: darkplaces-server = %{dpver}-%{release}

%description server
Xonotic is a fast-paced, chaotic, and intense multiplayer first person shooter, 
focused on providing basic, old style deathmatches.

This is the Xonotic dedicated server required to host network games.

%package -n darkplaces
Summary: Modified Quake engine
Version: %{dpver}
# This is necessary as these libraries are loaded during runtime
# and therefore it isn't picked up by RPM during build
Requires: zlib libvorbis libjpeg curl
Recommends: d0_blind_id

%description -n darkplaces
DarkPlaces is a modified Quake engine.

%package -n darkplaces-server
Summary: Quake engine server
Version: %{dpver}
# This is necessary as these libraries are loaded during runtime
# and therefore it isn't picked up by RPM during build
Requires: zlib curl

%description -n darkplaces-server
DarkPlaces Quake engine server.

%package -n darkplaces-quake
Summary: Multiplayer, deathmatch oriented first person shooter
Version: %{dpver}
Requires: autodownloader
Requires: opengl-games-utils
Requires: darkplaces = %{dpver}-%{release}

%description -n darkplaces-quake
Rage through levels of sheer terror and fully immersive sound and
lighting.  Arm yourself against the cannibalistic Ogre, fiendish Vore
and indestructible Schambler using letal nails, fierce Thunderbolts
and abominable Rocket and Grenade Launchers.

%package -n darkplaces-quake-server
Summary: Dedicated DarkPlaces Quake server
Version: %{dpver}
Requires: darkplaces-server = %{dpver}-%{release}

%description -n darkplaces-quake-server
DarkPlaces server required for hosting multiplayer network Quake games.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n darkplaces

cp %{SOURCE11} .
sed -i 's,MIRROR1,%{dqmirror1},g' $(basename %{SOURCE11})
sed -i 's,MIRROR2,%{dqmirror2},g' $(basename %{SOURCE11})

sed -i 's/\r//' darkplaces.txt
sed -i 's,/usr/X11R6/,/usr/,g' makefile makefile.inc
sed -i 's/nexuiz/xonotic/g' makefile makefile.inc

%patch -P 0 -p2

%build
export DP_FS_BASEDIR=%{_datadir}/xonotic
#export DP_CRYPTO_STATIC_LIBDIR="." 
#export DP_CRYPTO_RIJNDAEL_STATIC_LIBDIR="."
make release OPTIM_RELEASE="$RPM_OPT_FLAGS -std=gnu17" STRIP=:
make cl-xonotic OPTIM_RELEASE="$RPM_OPT_FLAGS -std=gnu17" STRIP=:
make sdl-xonotic OPTIM_RELEASE="$RPM_OPT_FLAGS -std=gnu17" STRIP=:
make sv-xonotic OPTIM_RELEASE="$RPM_OPT_FLAGS -std=gnu17" STRIP=:

%install
rm -rf %{buildroot}

# Install the main programs
mkdir -p %{buildroot}%{_bindir}
for i in darkplaces xonotic; do
        install -pm 0755 $i-glx %{buildroot}%{_bindir}/$i-glx
        install -pm 0755 $i-sdl %{buildroot}%{_bindir}/$i-sdl
        install -pm 0755 $i-dedicated %{buildroot}%{_bindir}/$i-dedicated
done
install -pm 0755 darkplaces-dedicated %{buildroot}%{_bindir}/darkplaces-dedicated

# Install the desktop files
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE1}
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE12}

for s in 16 24 32 48 64 72 ; do
       install -Dpm 0644 darkplaces${s}x${s}.png \
       %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/darkplaces.png
done
install -Dpm 0655 xonotic_256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/xonotic.png

ln -s opengl-game-wrapper.sh %{buildroot}%{_bindir}/xonotic-sdl-wrapper
ln -s opengl-game-wrapper.sh %{buildroot}%{_bindir}/darkplaces-sdl-wrapper
ln -s opengl-game-wrapper.sh %{buildroot}%{_bindir}/darkplaces-quake-sdl-wrapper

for i in glx sdl dedicated ; do
    install -Dpm 755 %{SOURCE10} %{buildroot}%{_bindir}/darkplaces-quake-$i
done

install -Dpm 644 $(basename %{SOURCE11}) %{buildroot}%{_datadir}/darkplaces/quake.autodlrc

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/darkplaces-quake.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
BugReportURL: Bug reports not accepted
-->
<application>
  <id type="desktop">darkplaces-quake.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A fast paced deathmatch oriented first person shooter (FPS)</summary>
  <description>
    <p>
      Darkplaces-quake is a fast paced, multiplayer, deathmatch oriented shooter
      similar to the popular FPS game Quake.
    </p>
  </description>
  <url type="homepage">http://www.xonotic.org/</url>
</application>
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
EmailAddress: http://www.xonotic.org/team/contact/
SentUpstream: 2014-09-23
-->
<application>
  <id type="desktop">xonotic.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <description>
    <p>
      Xonotic is a free and fast-paced first person shooter which combines
      addictive, arena-style gameplay with rapid movement and a wide array of
      weapons.
    </p>
    <p>
      Xonotic is easy to learn, but hard to master! Besides thrilling action for
      the casual player, the game also provides e-sport opportunities for those
      interested in its competitive aspects.
      From mapping contests and monthly quick cups to sponsored tournaments,
      Xonotic allows every e-sport enthusiast to participate in competitions
      hosted by its open-minded community.
    </p>
    <p>
      Features such as simple items, fully customizable configs and servers, a
      functioning anticheat system, the spectator mode, and the opportunity to
      watch and record games makes Xonotic attractive to competitive players.
    </p>
  </description>
  <url type="homepage">http://www.xonotic.org/</url>
  <screenshots>
    <screenshot type="default">http://www.xonotic.org/m/uploads/2012/07/frontpage_005.jpg</screenshot>
    <screenshot>http://www.xonotic.org/m/uploads/2012/07/frontpage_006.jpg</screenshot>
    <screenshot>http://www.xonotic.org/m/uploads/2012/07/frontpage_007.jpg</screenshot>
    <screenshot>http://www.xonotic.org/m/uploads/2012/07/frontpage_008.jpg</screenshot>
    <screenshot>http://www.xonotic.org/m/uploads/2012/07/frontpage_003.jpg</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%files
%{_bindir}/xonotic-sdl-wrapper
%{_bindir}/xonotic-glx
%{_bindir}/xonotic-sdl
#%{_bindir}/blind_id
%{_datadir}/icons/hicolor/*/apps/xonotic.png
%{_datadir}/appdata/*%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop

%files server
%{_bindir}/xonotic-dedicated

%files -n darkplaces
%{_bindir}/darkplaces-sdl-wrapper
%{_bindir}/darkplaces-glx
%{_bindir}/darkplaces-sdl
%doc COPYING darkplaces.txt
%{_datadir}/icons/hicolor/*/apps/darkplaces.png

%files -n darkplaces-server
%doc COPYING darkplaces.txt
%{_bindir}/darkplaces-dedicated

%files -n darkplaces-quake
%{_bindir}/darkplaces-quake-glx
%{_bindir}/darkplaces-quake-sdl
%{_bindir}/darkplaces-quake-sdl-wrapper
%{_datadir}/darkplaces/
%{_datadir}/appdata/*darkplaces-quake.appdata.xml
%{_datadir}/applications/*darkplaces-quake.desktop

%files -n darkplaces-quake-server
%doc COPYING darkplaces.txt
%{_bindir}/darkplaces-quake-dedicated

%changelog
%autochangelog
