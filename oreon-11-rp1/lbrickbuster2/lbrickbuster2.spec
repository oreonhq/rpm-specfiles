%global source0_hash 9104d6175553da3442dc6a5fc407a669e2f5aff3eedc5d30409eb003b7a78d6f
%define realname lbreakout2
Name:           lbrickbuster2
Version:        2.6.5
Release:        26%{?dist}
Summary:        Brickbuster arcade game
License:        GPL-2.0-or-later
URL:            http://lgames.sourceforge.net/
Source0:        http://downloads.sourceforge.net/lgames/%{realname}-%{version}.tar.gz
Source1:        %{name}-art.tar.gz
Patch0:         lbrickbuster2-rebrand-images.patch  
Patch1:         lbrickbuster2-default-fullscreen.patch
Patch2:         lbrickbuster2-fix-fortify-source.patch
Requires:       hicolor-icon-theme
Obsoletes:      lbreakout2 <= %{version}-%{release}
Provides:       lbreakout2 = %{version}-%{release}
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  SDL_mixer-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libpng-devel
BuildRequires:  make
# /oreon:deps
%description
The successor to LBrickBuster offers you a new challenge in more than 50 levels
with loads of new bonuses (goldshower, joker, explosive balls, bonus magnet
...), maluses (chaos, darkness, weak balls, malus magnet ...) and special
bricks (growing bricks, explosive bricks, regenerative bricks ...). If you
are still hungry for more after that you can create your own levelsets with
the integrated level editor.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -a 1 -n %{realname}-%{version}
# fully automated rebrand to lbrickbuster
for i in `find -type f -not -name "*.png" -not -name "*.wav"`; do
  touch -r $i $i.stamp
  sed -i -e 's/Breakout/Brickbuster/g' -e 's/breakout/brickbuster/g' $i
  touch -r $i.stamp $i
  rm $i.stamp
done
# and rename some files to match
mv client/lbreakout.h client/lbrickbuster.h
mv client/levels/LBreakout1 client/levels/LBrickbuster1
mv client/levels/LBreakout2 client/levels/LBrickbuster2
# install replacement art and remove themes overrides
mv fr_top.png menuback.png client/gfx/AbsoluteB
mv client/gfx/AbsoluteB/fr_*.png client/gfx/AbsoluteB/menuback.png client/gfx
rm client/gfx/Oz/fr_*.png client/gfx/Moiree/fr_*.png
mv lbreakout32.gif lbrickbuster32.gif
mv lbreakout48.gif lbrickbuster48.gif
mv lbreakout2.desktop.in lbrickbuster2.desktop.in
# rebranding done, other fixes / cleanups below
sed -i 's|/usr/doc/%{name}|%{_defaultdocdir}/%{name}|g' po/*.po client/help.c
iconv -f ISO_8859-1 -t utf-8 ChangeLog > ChangeLog.tmp
touch -r ChangeLog ChangeLog.tmp
mv ChangeLog.tmp ChangeLog

%build

%configure --localstatedir=%{_var}/games --with-docdir=%{_defaultdocdir}
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
install -p -m 644 AUTHORS ChangeLog README TODO \
  $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}
%find_lang %{name}
rm $RPM_BUILD_ROOT%{_datadir}/icons/lbrickbuster48.gif
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
sed -i 's|/usr/share/icons/lbrickbuster48.gif|%{name}|' \
    $RPM_BUILD_ROOT%{_datadir}/applications/lbrickbuster2.desktop
desktop-file-install \
    --delete-original \
    --add-category=ArcadeGame --add-category=BlocksGame \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
    $RPM_BUILD_ROOT%{_datadir}/applications/lbrickbuster2.desktop
convert lbrickbuster32.gif \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
touch -r lbrickbuster32.gif \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
convert lbrickbuster48.gif \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
touch -r lbrickbuster48.gif \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Edgar Muniz Berlinck <edgar.vv@gmail.com> -->
<!--
EmailAddress: wolfgang@rohdewald.de
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">lbrickbuster2.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Free version of Breakout</summary>
  <description>
    <p>
      Break all the tiles and don't let your ball fall.
      Simple and fun.
    </p>
  </description>
  <url type="homepage">http://lgames.sourceforge.net/index.php?project=LBreakout2</url>
  <screenshots>
    <screenshot type="default">http://lgames.sourceforge.net/LBreakout2/ss2.jpg</screenshot>
  </screenshots>
</application>
EOF
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
