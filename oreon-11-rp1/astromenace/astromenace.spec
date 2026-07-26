%global source0_hash none

Name: astromenace
Version:  1.4.3
Release:  4%{?dist}
Summary: Hardcore 3D space shooter with spaceship upgrade possibilities  

License: GPL-3.0-only
URL: http://www.viewizard.com/
Source0: https://github.com/viewizard/astromenace/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: astromenace.desktop
Source2: astromenace.png
ExcludeArch: ppc64 s390x

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake, SDL2-devel, libogg-devel
BuildRequires: libvorbis-devel, libjpeg-devel, desktop-file-utils
BuildRequires: openal-soft-devel freealut-devel
BuildRequires: glew-devel
BuildRequires: libXinerama-devel
BuildRequires: freetype-devel
BuildRequires: linux-libertine-fonts
BuildRequires: ninja-build
Requires: linux-libertine-fonts
Requires: opengl-games-utils

%description
Space is a vast area, an unbounded territory where it seems there is a 
room for everybody, but reversal of fortune put things differently. The 
hordes of hostile creatures crawled out from the dark corners of the
universe, craving to conquer your homeland. Their force is compelling,
their legions are interminable. However, humans didn't give up without
a final showdown and put their best pilot to fight back. These malicious
invaders chose the wrong galaxy to conquer and you are to prove it! 
Go ahead and make alien aggressors regret their insolence.

%prep
%setup -q

%build
%cmake %_vpath_srcdir -G Ninja -DDATADIR="%{_datadir}/astromenace" -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%__cmake_builddir/astromenace --pack --rawdata=./gamedata --dir=./

%install
mkdir -p  %{buildroot}%{_bindir}
install -m 755 %__cmake_builddir/astromenace %{buildroot}%{_bindir}/astromenace
mkdir -p %{buildroot}%{_datadir}/astromenace
install -m 644 gamedata.vfs %{buildroot}%{_datadir}/astromenace/
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps

ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper

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
<!-- Copyright 2014 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
EmailAddress: viewizard@viewizard.com
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">astromenace.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A fast paced and intense 3D scrolling space shooter</summary>
  <description>
    <p>
      Astromenace is a 3D scrolling space shooter with amazing graphics and
      intense gameplay.
    </p>
    <p>
      You have a range of vehicles to choose from and numerous weapons that can
      be upgraded as you repel wave after wave of spaceships and dodge space
      objects.
    </p>
  </description>
  <url type="homepage">http://www.viewizard.com/</url>
  <screenshots>
    <screenshot type="default">http://www.viewizard.com/astromenace/am3.jpg</screenshot>
    <screenshot>http://www.viewizard.com/astromenace/am6.jpg</screenshot>
    <screenshot>http://www.viewizard.com/astromenace/am10.jpg</screenshot>
  </screenshots>
</application>
EOF

%files
%{_bindir}/astromenace
%{_bindir}/%{name}-wrapper
%doc CHANGELOG.md LICENSE.md README.md docs/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/astromenace.desktop
%{_datadir}/icons/hicolor/64x64/apps/astromenace.png
%{_datadir}/astromenace/

%changelog
%autochangelog
