%global source0_hash c0957dc7894e1ccbe412cb4784f04b9b261b16252ef154ae66bd4d32aff57e15
Name:           CriticalMass
Version:        1.5
Release:        42%{?dist}
Summary:        SDL/OpenGL space shoot'em up game also known as critter
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
Requires:       hicolor-icon-theme opengl-games-utils
Provides:       critter = %{version}-%{release}
# oreon:deps
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  tinyxml-devel
# /oreon:deps
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
rm $RPM_BUILD_ROOT%{_bindir}/Packer
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps
install -p -m 644 critter.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
