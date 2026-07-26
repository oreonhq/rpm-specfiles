%global source0_hash a7548a6fa68a11f70471ac0326f0a9a233b78ef5e27b3d569f1d6303f430b446

#global         snapshot    1
#global         date        20250317
#global         commit      7e63ae

Name:           xine-ui
Version:        0.99.14
Release:        15%{?snapshot:.%{date}hg%{commit}}%{?dist}
Summary:        A skinned xlib-based gui for xine-lib
License:        GPL-2.0-or-later
URL:            http://www.xine-project.org/
%if ! 0%{?snapshot}
Source0:        http://sourceforge.net/projects/xine/files/xine-ui/%{version}/xine-ui-%{version}.tar.xz
%else
Source0:        xine-ui-%{version}hg.tar.xz
%endif

# Sources for -skins.
Source1:        https://xine.sourceforge.net/skins/Antares.tar.gz
Source2:        https://xine.sourceforge.net/skins/Bambino-Black.tar.gz
Source3:        https://xine.sourceforge.net/skins/Bambino-Blue.tar.gz
Source4:        https://xine.sourceforge.net/skins/Bambino-Green.tar.gz
Source5:        https://xine.sourceforge.net/skins/Bambino-Orange.tar.gz
Source6:        https://xine.sourceforge.net/skins/Bambino-Pink.tar.gz
Source7:        https://xine.sourceforge.net/skins/Bambino-Purple.tar.gz
Source8:        https://xine.sourceforge.net/skins/Bambino-White.tar.gz
Source9:        https://xine.sourceforge.net/skins/blackslim2.tar.gz
Source10:       https://xine.sourceforge.net/skins/Bluton.tar.gz
Source11:       https://xine.sourceforge.net/skins/caramel.tar.gz
Source12:       https://xine.sourceforge.net/skins/CelomaChrome.tar.gz
Source13:       https://xine.sourceforge.net/skins/CelomaGold.tar.gz
Source14:       https://xine.sourceforge.net/skins/CelomaMdk.tar.gz
Source15:       https://xine.sourceforge.net/skins/Centori.tar.gz
Source16:       https://xine.sourceforge.net/skins/cloudy.tar.gz
Source17:       https://xine.sourceforge.net/skins/concept.tar.gz
Source18:       https://xine.sourceforge.net/skins/Crystal.tar.gz
Source19:       https://xine.sourceforge.net/skins/Galaxy.tar.gz
Source20:       https://xine.sourceforge.net/skins/gudgreen.tar.gz
Source21:       https://xine.sourceforge.net/skins/KeramicRH8.tar.gz
Source22:       https://xine.sourceforge.net/skins/Keramic.tar.gz
Source23:       https://xine.sourceforge.net/skins/lcd.tar.gz
Source24:       https://xine.sourceforge.net/skins/mp2k.tar.gz
Source25:       https://xine.sourceforge.net/skins/mplayer.tar.gz
Source26:       https://xine.sourceforge.net/skins/OMS_legacy.tar.gz
Source27:       https://xine.sourceforge.net/skins/pitt.tar.gz
Source28:       https://xine.sourceforge.net/skins/Polaris.tar.gz
Source29:       https://xine.sourceforge.net/skins/Sunset.tar.gz
Source30:       https://xine.sourceforge.net/skins/xinium.tar.gz
Source31:       default.ogv

# AppStream data
Source90:       xine.appdata.xml

# Script to make a xine-ui snapshot
Source100:      make_xineui_snapshot.sh

# Patch to use UTF-8 documentation, BZ #512598
Patch1:         xine-ui-0.99.13-utf8doc.patch

Patch2:         xine-ui-configure-c99.patch

BuildRequires:  aalib-devel >= 1.2.0
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  curl-devel >= 7.10.2
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  libcaca-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel >= 1.5
BuildRequires:  libXft-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXt-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXv-devel
BuildRequires:  libXxf86vm-devel
%{!?_without_lirc:BuildRequires:  lirc-devel}
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  xine-lib-devel >= 1.1.0
BuildRequires:  xorg-x11-proto-devel

# For dir ownership
Requires:       hicolor-icon-theme
#
Requires:       xine-lib-extras

%description
xine-ui is the traditional, skinned GUI for xine-lib. 

%package skins
Summary:        Extra skins for xine-ui
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description skins
This package contains extra skins for xine-ui.

%package aaxine
Summary:        ASCII art player for terminals
Requires:       %{name} = %{version}-%{release}
Requires:       xine-lib-extras

%description aaxine
This package contains the ASCII art player for terminals like the vt100.
It also contains the color ascii art and framebuffer versions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Setup xine
%setup -q -n %{name}-%{version}%{?snapshot:hg}
# Setup skins
%setup -T -q -c -n %{name}-%{version}%{?snapshot:hg}/fedoraskins -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30
# Restore directory
%setup -T -D -n %{name}-%{version}%{?snapshot:hg}

%if ! 0%{?snapshot}
%patch -P1 -p1
%patch -P2 -p1

# assure use of system getopt
rm -f src/common/getopt.{c,h}

# Fix file encoding
for f in doc/man/{de,es,fr}/*.1* ; do
    iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 && \
    touch -r $f $f.utf8 && \
    mv $f.utf8 $f
done
for f in doc/man/pl/*.1* src/xitk/xine-toolkit/README ; do
    iconv -f iso-8859-2 -t utf-8 $f > $f.utf8 && \
    touch -r $f $f.utf8 && \
     mv $f.utf8 $f
done
%endif

# By default aaxine dlopen()'s a nonversioned libX11.so, however in Fedora
# it's provided by libX11-devel => version the dlopen()
libx11so=$(ls -1 %{_libdir}/libX11.so.? | tail -n 1)
if [ -n "$libx11so" -a -f "$libx11so" ] ; then
    sed -i -e "s/\"libX11\\.so\"/\"$(basename $libx11so)\"/" src/aaui/main.c
fi

cp -a src/xitk/xine-toolkit/README doc/README.xitk

%build
./autogen.sh noconfig
%if 0%{!?_without_lirc}
export LIRC_CFLAGS="-llirc_client"
export LIRC_LIBS="-llirc_client"
%endif
export XINE_DOCPATH=%{_docdir}/%{name}-%{version}
%configure --disable-dependency-tracking \
           --enable-vdr-keys \
           --with-aalib
%make_build

%install
%make_install
%find_lang 'xi\(ne-ui\|tk\)'

desktop-file-install --remove-category="Application" --vendor="" \
    --add-category="Audio" --add-category="Video" \
    --dir %{buildroot}%{_datadir}/applications misc/desktops/xine.desktop

install -D -m0644 %{SOURCE90} %{buildroot}%{_metainfodir}/xine.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/xine.appdata.xml

# Remove automatically installed documentation (listed in %%doc)
rm -rf %{buildroot}%{_docdir}/

# Remove misdesigned xine-check
rm -f %{buildroot}%{_bindir}/xine-bugreport
rm -f %{buildroot}%{_mandir}/*/man1/xine-bugreport.*
rm -f %{buildroot}%{_mandir}/man1/xine-bugreport.*
rm -f %{buildroot}%{_bindir}/xine-check
rm -f %{buildroot}%{_mandir}/*/man1/xine-check.*
rm -f %{buildroot}%{_mandir}/man1/xine-check.*

# Install extra skins
cp -a fedoraskins/* %{buildroot}%{_datadir}/xine/skins/

%files -f 'xi\(ne-ui\|tk\)'.lang
%license COPYING
%doc ChangeLog doc/README*
%{_bindir}/xine
%{_bindir}/xine-remote
%dir %{_datadir}/xine/
%dir %{_datadir}/xine/skins/
%{_datadir}/xine/skins/xinetic/
%{_datadir}/xine/skins/missing.png
%{_datadir}/xine/skins/xine_64.png
%{_datadir}/xine/skins/xine_splash.png
%{_datadir}/xine/skins/xine-ui_logo.mpg
%{_datadir}/xine/skins/xine-ui_logo.png
%{_datadir}/xine/oxine/
%{_datadir}/xine/visuals/
%{_datadir}/mime/packages/xine-ui.xml
%{_datadir}/applications/*xine.desktop
%{_datadir}/icons/hicolor/*x*/apps/xine.png
%{_datadir}/icons/hicolor/scalable/apps/xine.svgz
%{_datadir}/pixmaps/xine.xpm
%{_datadir}/pixmaps/xine_32.xpm
%{_mandir}/man1/xine*
%{_metainfodir}/xine.appdata.xml
%lang(de) %{_mandir}/de/man1/xine*
%lang(es) %{_mandir}/es/man1/xine*
%lang(fr) %{_mandir}/fr/man1/xine*
%lang(nl) %{_mandir}/nl/man1/xine*
%lang(pl) %{_mandir}/pl/man1/xine*

%files skins
%{_datadir}/xine/skins/*
%exclude %{_datadir}/xine/skins/xinetic/
%exclude %{_datadir}/xine/skins/missing.png
%exclude %{_datadir}/xine/skins/xine_64.png
%exclude %{_datadir}/xine/skins/xine_splash.png
%exclude %{_datadir}/xine/skins/xine-ui_logo.mpg
%exclude %{_datadir}/xine/skins/xine-ui_logo.png

%files aaxine
%{_bindir}/aaxine
%{_bindir}/cacaxine
%{_bindir}/fbxine
%{_mandir}/man1/aaxine*
%lang(de) %{_mandir}/de/man1/aaxine*
%lang(es) %{_mandir}/es/man1/aaxine*
%lang(nl) %{_mandir}/nl/man1/aaxine*
%lang(pl) %{_mandir}/pl/man1/aaxine*

%changelog
%autochangelog
