%global source0_hash 31edda1a1f4b713f4c8132d8e437aa3f01911945f1094a371a9f0687c406d7e4

Name:           CriticalMass
Version:        1.5
Release:        42%{?dist}
Summary:        SDL/OpenGL space shoot'em up game also known as critter
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://criticalmass.sourceforge.net/critter.php
Source0:        http://downloads.sourceforge.net/criticalmass/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         CriticalMass-1.0.2-res-change-rh566533.patch
Patch1:         CriticalMass-1.5-libpng15.patch
Patch2:         CriticalMass-1.5-gcc47.patch
Patch3:         CriticalMass-1.5-cflags.patch
Patch4:         CriticalMass-1.5-gcc6.patch
Patch5:         CriticalMass-1.5-ftbfs.patch
BuildRequires:  gcc-c++
BuildRequires:  SDL_image-devel SDL_mixer-devel libpng-devel curl-devel
BuildRequires:  tinyxml-devel desktop-file-utils libtool
BuildRequires: make
Requires:       hicolor-icon-theme opengl-games-utils
# Also known as critter, so make "yum install critter" work
Provides:       critter = %{version}-%{release}

%description
Critical Mass (aka Critter) is an SDL/OpenGL space shoot'em up game. Your
world has been infested by an aggressive army of space critters. Overrun and
unprepared, your government was unable to defend its precious resources. As
a last effort to recapture some of the "goodies", you have been placed into
a tiny spacecraft and sent after them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's/curl-gnutls/curl/g' configure.in
touch NEWS README AUTHORS ChangeLog
autoreconf -ivf

%build
%configure
make %{?_smp_mflags}

%install
%make_install
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/critter-wrapper

# remove unwanted utility
rm $RPM_BUILD_ROOT%{_bindir}/Packer

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps
install -p -m 644 critter.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps

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
EmailAddress: crittermail2005@telus.net
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">CriticalMass.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A top-down space shoot-em-up game</summary>
  <description>
    <p>
      Critical Mass (also known as Critter) is a top-down shoot-em-up game where your home world
      has been infested by an aggressive army of space critters and
      you are required to pilot a small spacecraft to destroy them all.
    </p>
  </description>
  <url type="homepage">http://criticalmass.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://criticalmass.sourceforge.net/images-critter/pics.v100/snap09.jpeg</screenshot>
    <screenshot>http://criticalmass.sourceforge.net/images-critter/pics.v100/snap17.jpeg</screenshot>
    <screenshot>http://criticalmass.sourceforge.net/images-critter/pics.v100/snap13.jpeg</screenshot>
    <screenshot>http://criticalmass.sourceforge.net/images-critter/pics.v100/snap04.jpeg</screenshot>
    <screenshot>http://criticalmass.sourceforge.net/images-critter/pics.v100/snap00.jpeg</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%files
%doc Readme.html TODO
%license COPYING
%{_bindir}/critter*
%{_datadir}/Critical_Mass
%{_mandir}/man6/critter.6*
%{_datadir}/appdata/*%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/critter.png

%changelog
%autochangelog
