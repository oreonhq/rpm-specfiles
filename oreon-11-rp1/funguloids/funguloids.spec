%global source0_hash e9c9074a5d2de11690484a7e8eef7de9dd7d360ea72185ea35c54976646ef5cf

#
# Fedora spec file for package funguloids
#
# Adapted from the openSUSE spec file and patches, which are:
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           funguloids
Version:        1.06
Release:        50%{?dist}
Summary:        Space-Flying-Mushroom-Picking-Simulator game
License:        zlib
URL:            http://funguloids.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-linux-%{version}-4.tar.bz2
# From Debian, as the openSUSE srpm has v1.4, which lacks a clear license
Source1:        mpak.py
# README.openSUSE modified for Fedora
Source2:        README.Fedora
Source3:        funguloids.desktop
Source4:        funguloids.png
# Shamelessly borrowed from Debian
Source5:        funguloids.6
# All the below patches where taken from the openSUSE srpm
# funguloids-ogre-1.6.patch has been extended with some bits from the more
# complete ogre-1.6.1.patch from Debian
Patch0:         %{name}-size_chunks_reverse.patch
Patch1:         %{name}-alc_error.patch
Patch2:         %{name}-missing_includes.patch
Patch3:         %{name}-ogre-1.6.patch
Patch4:         %{name}-lua.patch
Patch5:         %{name}-destdir.patch
Patch6:         %{name}-honor_autotools_paths.patch
Patch7:         %{name}-strcmp.patch
Patch8:         %{name}-optional_cg.patch
Patch9:         %{name}-ogre-1.7.0.patch
Patch10:        %{name}-gcc47.patch
Patch11:        %{name}-ogre-1.8.patch
# Fix for Lua 5.2
Patch12:        %{name}-lua-5.2.patch
# Build with ogre-1.9
Patch13:        %{name}-ogre-1.9.patch
BuildRequires:  automake desktop-file-utils gcc-c++ python3 make
BuildRequires:  freealut-devel libvorbis-devel lua-devel
BuildRequires:  ogre-devel >= 1.9 ois-devel openal-soft-devel
Requires:       hicolor-icon-theme

%description
Never before has collecting mushrooms been this mildly entertaining. At least
not in outer space. It's more of a lifestyle than a game, really. Now with
graphics and sound, too!

Seriously though, we like to think the game as a
space-flying-mushroom-picking-simulator. Well no, "Those Funny Funguloids!" is
actually a nice little piece of entertainment. You collect mushrooms, bring them
back to your home base and profit! That's the basic idea in a nutshell. It has
smooth, appealing 3d graphics and nice atmospheric sound effects. Go ahead and
try it out - it has sounds too!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
%patch -P0
%patch -P1
%patch -P2
%patch -P3
%patch -P4
%patch -P5
%patch -P6
%patch -P7
%patch -P8
%patch -P9
%patch -P10
%patch -P11
%patch -P12 -p1
%patch -P13 -p1
autoreconf -fi
# docs fixup
sed -i 's/\r$//' bin/docs/stylesheet.css
sed -i 's/\r$//' README
# mpk file fixup
%{SOURCE1} -e -f bin/bootstrap.mpk -p _bootstrap
%{SOURCE1} -e -f bin/funguloids.mpk -p _gamedata
sed -ri '/^[A-Z]/ s/(.*)/overlay \1/' _bootstrap/*.overlay _gamedata/*.overlay
sed -ri '/^[A-Z]/ s/(.*)/particle_system \1/' _gamedata/*.particle
# This last one looks like a bug in ogre, should be removed when fixed
# The problem is that green and blue mushrooms have a square instead of a glow
sed -ri 's/^(\t\t\t)(texture_unit) 1/\1\2\n\1{\n\1}\n\1\2/' _gamedata/materials.material
%{SOURCE1} -c -f bin/bootstrap.mpk _bootstrap/*
%{SOURCE1} -c -f bin/funguloids.mpk _gamedata/*
rm -rf _bootstrap _gamedata

%build
%configure --docdir=%{_pkgdocdir} --without-mad --without-fmod
make %{?_smp_mflags}

%install
%make_install
cp -p README %{SOURCE2} $RPM_BUILD_ROOT%{_pkgdocdir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE3}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{48x48,256x256}/apps
mv $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
cp -p %{SOURCE5} $RPM_BUILD_ROOT%{_mandir}/man6

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
<!-- Copyright 2014 Edgar Muniz Berlinck <edgar.vv@gmail.com> -->
<!--
BugReportURL: https://sourceforge.net/p/funguloids/support-requests/2/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">funguloids.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>3D casual game</summary>
  <description>
    <p>
      Those Funny Funguloids! 3d is a casual game where you must travel through
      various worlds offered by the game and capture all the mushrooms you find.
      Beware of enemies, they will do anything to make you fail!
    </p>
  </description>
  <url type="homepage">http://funguloids.sourceforge.net</url>
  <screenshots>
    <screenshot type="default">http://funguloids.sourceforge.net/shot02.jpg</screenshot>
    <screenshot>http://funguloids.sourceforge.net/shot01.jpg</screenshot>
    <screenshot>http://funguloids.sourceforge.net/shot03.jpg</screenshot>
    <screenshot>http://funguloids.sourceforge.net/shot04.jpg</screenshot>
    <screenshot>http://funguloids.sourceforge.net/shot06.jpg</screenshot>
    <screenshot>http://funguloids.sourceforge.net/shot07.jpg</screenshot>
    <screenshot>http://funguloids.sourceforge.net/shot05.jpg</screenshot>
    <screenshot>http://funguloids.sourceforge.net/shot08.jpg</screenshot>
  </screenshots>
</application>
EOF

%files
%doc %{_pkgdocdir}
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6*

%changelog
%autochangelog
