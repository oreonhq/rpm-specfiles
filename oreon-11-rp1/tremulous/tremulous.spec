%global source0_hash 396c0e930b4ba09e3787373d560ae17651627abcba123a67cce3544170523ef4

Name:           tremulous
Version:        1.2.0
Release:        0.41.beta1%{?dist}
Summary:        First Person Shooter game based on the Quake 3 engine
ExcludeArch:    %{ix86}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://tremulous.net
# To get the source tarball:
# svn export svn://svn.icculus.org/tremulous/tags/RELEASE_GPP1/ tremulous-1.2.beta1
# rm -rf tremulous-1.2.beta1/src/tools/lcc/
# tar -czf tremulous-1.2.0.beta1.tar.gz tremulous-1.2.beta1
Source0:        tremulous-1.2.0.beta1.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         tremulous-1.2.0-dll-overwrite.patch
Patch1:         tremulous-getstatus-dos.patch
Patch2:         tremulous-aarch64.patch
Patch3:         tremulous-i686.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  openal-soft-devel
BuildRequires:  SDL-devel
BuildRequires:  speex-devel
%if ! 0%{?rhel}
BuildRequires:  speexdsp-devel
%endif
BuildRequires:  zlib-devel
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

Requires:       tremulous-data = %{version}
Requires:       hicolor-icon-theme opengl-games-utils

%description
Tremulous is a free, open source game that blends a team based FPS with elements
of an RTS. Players can choose from 2 unique races, aliens and humans. 
Players on both teams are able to build working structures in-game like an RTS.
These structures provide many functions, the most important being spawning.
The designated builders must ensure there are spawn structures or other players
 will not be able to rejoin the game after death. Other structures provide 
automated base defense (to some degree), healing functions and much more...

Player advancement is different depending on which team you are on.
As a human, players are rewarded with credits for each alien kill.
These credits may be used to purchase new weapons and upgrades from the Armoury
The alien team advances quite differently. Upon killing a human foe,
the alien is able to evolve into a new class. The more kills gained the more 
powerful the classes available.

The overall objective behind Tremulous is to eliminate the opposing team.
This is achieved by not only killing the opposing players but also 
removing their ability to respawn by destroying their spawn structures.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n tremulous-1.2.beta1
%patch -P0 -p1 -b .dll-overwrite
%patch -P1 -p1 -b .getstatus-dos
%patch -P2 -p1 -b .aarch64
%patch -P3 -p1 -b .i686

# Rip out the bundled libraries and use the
# system versions instead
rm -r src/SDL12 src/AL src/libcurl src/libspeex src/libs

%build
# This package uses top level ASM constructs which are incompatible with LTO.
# Top level ASMs are often used to implement symbol versioning.  gcc-10
# introduces a new mechanism for symbol versioning which works with LTO.
# Converting packages to use that mechanism instead of toplevel ASMs is
# recommended.
# Disable LTO
%define _lto_cflags %{nil}

# the CROSS_COMPILING=1 is a hack to not build q3cc and qvm files
# since we've stripped out q3cc as this is not Free Software.
make %{?_smp_mflags} \
    OPTIMIZE="$RPM_OPT_FLAGS -fno-strict-aliasing -ffast-math" \
    DEFAULT_BASEDIR=%{_datadir}/%{name} USE_CODEC_VORBIS=1 \
    USE_LOCAL_HEADERS=0 BUILD_GAME_SO=0 GENERATE_DEPENDENCIES=0 \
    CROSS_COMPILING=1 USE_INTERNAL_SPEEX=0 USE_INTERNAL_ZLIB=0

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 build/release-linux-*/tremded.* \
  $RPM_BUILD_ROOT%{_bindir}/tremded
install -m 0755 build/release-linux-*/tremulous.* \
  $RPM_BUILD_ROOT%{_bindir}/%{name}
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps

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
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
EmailAddress: #tremulous on freenode
SentUpstream: 2014-09-23
-->
<application>
  <id type="desktop">tremulous.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <description>
    <p>
      Tremulous is a free, open source game that blends a team based FPS with
      elements of an RTS.
    </p>
    <p>
      Players can choose from 2 unique races, aliens and humans.
      Players on both teams are able to build working structures in-game like an
      RTS.
    </p>
  </description>
  <url type="homepage">http://www.tremulous.net</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/tremulous/a.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/tremulous/b.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/tremulous/c.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/tremulous/d.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/tremulous/e.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/tremulous.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/tremulous.desktop

%files
%license COPYING GPL
%{_bindir}/%{name}*
%{_bindir}/tremded
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%changelog
%autochangelog
