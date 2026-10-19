%global source0_hash 64cb29934660456ec82cebdaa0d3d273a862e10760e8ee80443928d317242484
%global __cmake_in_source_build 1
Name:		xmoto
Version:	0.6.3
Release:        1%{?dist}
Summary:        Challenging 2D Motocross Platform Game
License:	GPL-2.0-or-later
URL:		http://xmoto.sourceforge.net/
Source0:        https://github.com/xmoto/xmoto/archive/v%{version}/%{version}.tar.gz
Source1:	xmoto.desktop
Source2:	xmoto.png
Patch0:		xmoto-0.5.0-helpers-text-includes.patch
Patch1:		xmoto-0.5.0-helpers-log-include.patch
Requires: dejavu-sans-fonts
# oreon:deps
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_net-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libxdg-basedir-devel
BuildRequires:  libxml2-devel
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  ode-devel
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
X-Moto is a challenging 2D motocross platform game, where physics play an all
important role in the gameplay. You need to control your bike to its limit, if
you want to have a chance finishing the more difficult of the challenges.

First you'll try just to complete the levels, while later you'll compete with
yourself and others, racing against the clock.

%prep

%setup -q
%patch -P0 -p0
%patch -P1 -p0

%build

mkdir build
pushd build
%cmake -DPREFER_SYSTEM_BZip2=ON -DPREFER_SYSTEM_Lua=ON -DPREFER_SYSTEM_ODE=ON -DPREFER_SYSTEM_XDG=ON ..
%cmake_build
%install
pushd build
%cmake_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
desktop-file-install  --dir $RPM_BUILD_ROOT%{_datadir}/applications --add-category X-Fedora %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress: neckelmann@gmail.com
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">xmoto.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>2D motocross platform game</summary>
  <description>
    <p>
      xmoto is a side-scrolling 2D motocross platform game where the objective
      is to collect all the floating items in the level and proceed to the
      checkered finishing ball.
      The motocross bike that the player rides in
      xmoto has a lot of bounce, and the if the player hits their head on any
      solid object the level has to be restarted.
    </p>
    <p>
      There are hundreds of levels available in xmoto, both included in the
      initial install, and downloadable from the internet.
      There is also the
      ability to challenge fastest times with other players from around the world.
      and saved ghost data to visually see the runs of other players through the
      levels.
    </p>
  </description>
  <url type="homepage">http://xmoto.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://wiki.xmoto.tuxfamily.org/images/7/7d/Screenshot0022.png</screenshot>
    <screenshot>http://wiki.xmoto.tuxfamily.org/images/6/65/Xmoto01.png</screenshot>
    <screenshot>http://wiki.xmoto.tuxfamily.org/images/0/04/Screenshot0005.png</screenshot>
  </screenshots>
</application>
EOF
rm $RPM_BUILD_ROOT%{_datadir}/xmoto/Textures/Fonts/DejaVuSans.ttf 
ln -s ../../../fonts/dejavu-sans-fonts/DejaVuSans.ttf $RPM_BUILD_ROOT%{_datadir}/xmoto/Textures/Fonts/DejaVuSans.ttf 
popd
%find_lang %{name} %{name}.lang
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
