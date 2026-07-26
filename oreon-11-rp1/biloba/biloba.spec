%global source0_hash a088d91bf1df8e2df643da95b5b55494dca82e5e64f28b2ffa9308bd47e12c61

Name:           biloba
Version:        0.9.3
Release:        37%{?dist}
Summary:        A tactical board game

License:        GPL-2.0-or-later
URL:            http://biloba.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        biloba.desktop

BuildRequires:  gcc autoconf automake
BuildRequires:  desktop-file-utils ImageMagick SDL_image-devel SDL_mixer-devel
BuildRequires: make
Requires:       hicolor-icon-theme

%description
Biloba is a very innovative tactical board game. It can be played
by 2, 3 or 4 players and against the computer (AI).
You will be able to play on the same computer or online against
your opponents.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
export CFLAGS="$CFLAGS -fcommon -g -std=c17"
autoreconf -if
%configure --prefix=%{_prefix}
make %{?_smp_mflags}

iconv -f iso-8859-1 -t utf-8 ChangeLog -o ChangeLog.char
mv ChangeLog.char ChangeLog

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{64x64,32x32,16x16}/apps
cp -p biloba_icon.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/biloba.png
convert -scale 32x32 biloba_icon.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/biloba.png
convert -scale 16x16 biloba_icon.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/biloba.png

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
EmailAddress: colin@colino.net
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">biloba.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Strategic board game</summary>
  <description>
    <p>
      Biloba is a board game for 2 to 4 players that involves moving pawns around on
      an octagonal board with square cells. The goal of bilboa is to remove all of your
      opponent's pawns. Bilboa can be played both against AI and real opponents.
    </p>
  </description>
  <url type="homepage">http://biloba.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://biloba.sourceforge.net/2p.png</screenshot>
    <screenshot>http://biloba.sourceforge.net/3p.png</screenshot>
    <screenshot>http://biloba.sourceforge.net/4p.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

desktop-file-install                    \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications         \
  %{SOURCE1}

%files
%doc AUTHORS ChangeLog COPYING 
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/??x??/apps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
