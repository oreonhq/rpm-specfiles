%global source1_hash 2bf9ab1798e7d3f82a372a3fae26a5c7699d1c57263253dce66f07fa418b702b
%global source0_hash 3abf61c4a7bd921988596a2239d76a5800fc94d8fd84dcc82c720d4d4f84cf0f
Name:           BlockOutII
Version:        2.5
Release:        34%{?dist}
Summary:        A free adaptation of the original BlockOut DOS game
License:        GPL-2.0-or-later
URL:            http://www.blockout.net/blockout2/
Source0:        http://downloads.sourceforge.net/blockout/bl25-src.tar.gz
Source1:        http://downloads.sourceforge.net/blockout/bl25-linux-x86.tar.gz
Source2:        %{name}.desktop
Patch0:         BlockOutII-2.3-syslibs.patch
Patch1:         BlockOutII-2.3-bl2Home.patch
Patch2:         BlockOutII-2.3-restore-resolution.patch
Patch3:         BlockOutII-2.3-libpng15.patch
Patch4:         BlockOutII-2.3-format-security.patch
Patch5:		BlockOutII-c99.patch
Requires:       hicolor-icon-theme opengl-games-utils
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  SDL_mixer-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  make
# /oreon:deps
%description
BlockOut II is a free adaptation of the original BlockOut
DOS game edited by California Dreams in 1989. BlockOut II
has the same features than the original game with few graphic
improvements. The score calculation is also nearly similar to
the original game. BlockOut II has been designed by an addicted
player for addicted players. BlockOut II is an open source
project available for both Windows and Linux.

Blockout is a registered trademark of Kadon Enterprises, Inc.,
used by permission for the BlockOut II application by Jean-Luc
Pons.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n BL_SRC -a 1
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

# Convert the README and put it somewhere we can use it from %%doc
iconv -f ISO8859-1 -t UTF8 BlockOut/README.txt > t;
sed -i 's/\r//' t
touch -r BlockOut/README.txt t
mv t BlockOut/README.txt

# Remove bundled png library
rm -r ImageLib/src/png/png ImageLib/src/png/zlib

%build

pushd ImageLib/src
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -Dlinux -c" \
    CXXFLAGS="$RPM_OPT_FLAGS -Dlinux -c"
popd
pushd BlockOut
make %{?_smp_mflags} \
    CXXFLAGS="$RPM_OPT_FLAGS -Dlinux `sdl-config --cflags` -I../ImageLib/src -c" \
    ADD_LIBS="-L../ImageLib/src -limagelib -lpng -lz"
popd
convert BlockOut/block_icon.ico BlockOutII.png
convert BlockOutII-2.png -resize 64x64 BlockOutII-64x64.png
%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/images
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds
install -m 755 BlockOut/blockout $RPM_BUILD_ROOT%{_bindir}/%{name}
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper
install -p -m 644 blockout/images/* $RPM_BUILD_ROOT%{_datadir}/%{name}/images
install -p -m 644 blockout/sounds/* $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
install -D -p -m 644 %{name}-1.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -D -p -m 644 %{name}-0.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -D -p -m 644 %{name}-2.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -D -p -m 644 %{name}-64x64.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress: jlp_38@yahoo.com
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">BlockOutII.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A free adaptation of the original BlockOut game</summary>
  <description>
    <p>
      BlockOut II is a game where the player moves and rotate 3D polycubes
      that are constantly falling with the objective of clearing layers of
      blocks.
      It is a free adaptation of the original BlockOut game released in 1989.
    </p>
  </description>
  <url type="homepage">http://www.blockout.net/blockout2/</url>
  <screenshots>
    <screenshot type="default">http://www.blockout.net/blockout2/screenshots/scr1.jpg</screenshot>
    <screenshot>http://www.blockout.net/blockout2/screenshots/scr2.jpg</screenshot>
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
