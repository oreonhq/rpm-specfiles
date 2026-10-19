%global source0_hash e9c9074a5d2de11690484a7e8eef7de9dd7d360ea72185ea35c54976646ef5cf
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}
Name:           funguloids
Version:        1.06
Release:        1%{?dist}
Summary:        Space-Flying-Mushroom-Picking-Simulator game
License:        zlib
URL:            http://funguloids.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-linux-%{version}-4.tar.bz2
Source1:        mpak.py
Source2:        README.Fedora
Source3:        funguloids.desktop
Source4:        funguloids.png
Source5:        funguloids.6
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
Patch12:        %{name}-lua-5.2.patch
Patch13:        %{name}-ogre-1.9.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  freealut-devel
BuildRequires:  gcc-c++
BuildRequires:  libvorbis-devel
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  ogre-devel
BuildRequires:  ois-devel
BuildRequires:  openal-soft-devel
BuildRequires:  python3
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
