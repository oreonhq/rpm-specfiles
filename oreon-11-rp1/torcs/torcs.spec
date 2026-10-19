%global source0_hash f9c69e86d290295467451b01d7838d85005ba613644a6fe8a3f85a7c6a03cd4c
Name:           torcs
Version:        1.3.9
Release:        1%{?dist}
Summary:        The Open Racing Car Simulator
License:        GPL-2.0-or-later
URL:            http://torcs.org/
Source0:        http://downloads.sf.net/torcs/torcs-%{version}.tar.bz2
Source1:        torcs.png
Patch1:         torcs-1.3.8-abort-crash.patch
Patch2:         format-argument.patch
Patch3:         torcs-freeglut.patch
Requires:       hicolor-icon-theme
Requires:       torcs-data = %{version}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  freealut-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libGL-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  openal-soft-devel
BuildRequires:  plib-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse.

%prep

%autosetup -p1

# Prevent useless executable files in the debuginfo package (as of 1.3.1)
chmod -x src/libs/learning/policy.*

%build

%configure
make
%install
%make_install
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/torcs.png
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
    --remove-category Application \
    --add-category Simulation \
    --dir %{buildroot}%{_datadir}/applications \
    torcs.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/torcs.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
EmailAddress: torcs-devel@lists.sourceforge.net
SentUpstream: 2014-05-22
-->
<application>
  <id type="desktop">torcs.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>GPL-2.0+</project_license>
  <description>
    <p>
     TORCS is a highly portable multi platform car racing simulation.
     It is used as ordinary car racing game, as AI racing game and as research
     platform.
    </p>
    <p>
     TORCS features many different cars, tracks, and opponents to race against.
     You can steer with a joystick, steering wheel, mouse or the keyboard.
     Graphic features lighting, smoke, skid marks and glowing brake disks.
     The simulation features a simple damage model, collisions, tire and wheel
     properties, aerodynamics and much more.
    </p>
    <p>
     The game play allows different types of races from the simple practice
     session up to the championship.
     Enjoy racing against your friends in the split screen mode with up to four
     human players.
    </p>
  </description>
  <releases>
    <release version="1.3.7" date="2016-05-19"/>
  </releases>
  <content_rating type="oars-1.1">
    <content_attribute id="violence-cartoon">none</content_attribute>
    <content_attribute id="violence-fantasy">none</content_attribute>
    <content_attribute id="violence-realistic">none</content_attribute>
    <content_attribute id="violence-bloodshed">none</content_attribute>
    <content_attribute id="violence-sexual">none</content_attribute>
    <content_attribute id="violence-desecration">none</content_attribute>
    <content_attribute id="violence-slavery">none</content_attribute>
    <content_attribute id="violence-worship">none</content_attribute>
    <content_attribute id="drugs-alcohol">none</content_attribute>
    <content_attribute id="drugs-narcotics">none</content_attribute>
    <content_attribute id="drugs-tobacco">none</content_attribute>
    <content_attribute id="sex-nudity">none</content_attribute>
    <content_attribute id="sex-themes">none</content_attribute>
    <content_attribute id="sex-homosexuality">none</content_attribute>
    <content_attribute id="sex-prostitution">none</content_attribute>
    <content_attribute id="sex-adultery">none</content_attribute>
    <content_attribute id="sex-appearance">none</content_attribute>
    <content_attribute id="language-profanity">none</content_attribute>
    <content_attribute id="language-humor">none</content_attribute>
    <content_attribute id="language-discrimination">none</content_attribute>
    <content_attribute id="social-chat">none</content_attribute>
    <content_attribute id="social-info">none</content_attribute>
    <content_attribute id="social-audio">none</content_attribute>
    <content_attribute id="social-location">none</content_attribute>
    <content_attribute id="social-contacts">none</content_attribute>
    <content_attribute id="money-purchasing">none</content_attribute>
    <content_attribute id="money-gambling">none</content_attribute>
  </content_rating>
  <screenshots>
    <screenshot type="default">http://a.fsdn.com/con/app/proj/torcs/screenshots/torcs-20121025123603.png</screenshot>
    <screenshot>http://a.fsdn.com/con/app/proj/torcs/screenshots/torcs-20121025125922.png</screenshot>
  </screenshots>
  <url type="homepage">http://torcs.sourceforge.net/</url>
</application>
EOF
find %{buildroot}%{_libdir}/torcs/ -name '*.so' | xargs %{__chmod} +x
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
