%global source30_hash 473b074522b779a5ed5e93c1227b6411f6a1fda4077805f5480d7024d9e09472
%global source29_hash 6d285e4cca35af42d67e1fdd3c2ccc5ecca3fe6bb94dba042ea0dbb6622bc6f9
%global source28_hash 9df8dfd7d3c15a32c6759e56e766c9acc18afce0babe0e9e4e77eb9357368b4c
%global source27_hash 4357ffa852132a632a3d8a226ec5834f9827b8fd28517b630d6f9bab92aedd4e
%global source26_hash f67d416f0c5648e88a5978b8b459cce0c4505306c9c203ba50ad3df08efeb77d
%global source25_hash 2de2177545c80b1e36c8be080d76f1f219329f0d63b0e9f134eff41cdf733987
%global source24_hash e6ef8e16dd9c0eaecd40d8af22668ff16f92ea1aec4188109008b0e38af1714a
%global source23_hash dc78dccaa75b78f79437bf702d80f1e0b3c40a0bc9e28c3da5e5d35752c6d1a6
%global source22_hash b7c00095c2a60efd77cd6a625b897053d36f9edc8f67fdc31cc01f91ee10b285
%global source21_hash aec7e9b24c591c500e057d22a020e85c5bfe9bbd8a553ae71ddefc6f84548df3
%global source20_hash a6cfc70325986c4078f1a5d9e60574ccfd274ac1a15f5dd59ed6232916a4d5e6
%global source19_hash 37f7c331b7e918a78a8dfac67aa19c16dfec882b9bc3d62088ead8f6e0d28d07
%global source18_hash 7f24471bb83494df684b59dd8afb91f18f8f2aa5b3bb5bbfb17011fa4a56b40e
%global source17_hash f4d4d86308810f17866adc7e7324fbebd443d51f7aafaec9f448052ce6ea4d3a
%global source16_hash a5a281f603f513ba2db86315767f9b5ff487254463505f9bd42f5fe52c3a3381
%global source15_hash 83591b1ce14ed83afded1292452ad93015cf94e60df7478d79da71bbf304a886
%global source14_hash d09637aecc382142ad8d8790dc0b783b07b7e4481cd50cafa89289378ce23757
%global source13_hash 0207a899f1e35aad923581295ca89a56ae4b2efc0fbaaa4265b1224a02ff51a9
%global source12_hash dbc6d4225e4fb0f1e5c40ab604616e6fa979efd05f48b65f17a1e2f314f30686
%global source11_hash b3a4227cefe881902619f0ad9ce70103d57fd6bec06888b9659a7a824b6bcdd6
%global source10_hash 0741d5143abfb4f313d2e298c7a5cd8022ba9f6e1fe8c1eeaf6b4944c637934c
%global source9_hash a7548a6fa68a11f70471ac0326f0a9a233b78ef5e27b3d569f1d6303f430b446
%global source8_hash b71fe7f80729da846cbffb92e31c9a91d9f895c2c86371ac510f10b2c8e8a1c0
%global source7_hash 487b5dc20846c26fafdf7c8e49bd99cdaf50708bf399f1d980905b93673fc910
%global source6_hash 5a03df13e2a4c4489f246321207f3e799078246ffaa79d058ad099cae20c075c
%global source5_hash 8e940fcbf0f69389412acb83670b855b3be6c63fa06a37aea0b97f35a27aec5d
%global source4_hash 08b8fc48a64e83af39a88d457111cea3516dc303626f94b043254606d8344978
%global source3_hash 99b6d8d877e3cc375c4c6238c83fd7ba2c0e9b774aea26e4150244156f1ec72d
%global source2_hash 5504754263a8427ea2665e606e01f32df8ca15459ef8f92d8af077b43d311eb0
%global source1_hash 9268e381a5ed33858e9077509cbd888a2c3901173be4cf7d85065744235f3d17
%global source0_hash d4d490d5cece70e2bb9849c9e482f2cf87af0302d451b614476fdcc3642cd9c3
Name:           xine-ui
Version:        0.99.14
Release:        1%{?dist}
Summary:        A skinned xlib-based gui for xine-lib
License:        GPL-2.0-or-later
URL:            http://www.xine-project.org/
%if ! 0%{?snapshot}
Source0:        http://sourceforge.net/projects/xine/files/xine-ui/%{version}/xine-ui-%{version}.tar.xz
%else
%endif
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
Source90:       xine.appdata.xml
Source100:      make_xineui_snapshot.sh
Patch1:         xine-ui-0.99.13-utf8doc.patch
Patch2:         xine-ui-configure-c99.patch
%{!?_without_lirc:BuildRequires:  lirc-devel}
Requires:       hicolor-icon-theme
Requires:       xine-lib-extras
# oreon:deps
BuildRequires:  aalib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libXft-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXt-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXv-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcaca-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  lirc-devel
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  xine-lib-devel
BuildRequires:  xorg-x11-proto-devel
# /oreon:deps
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
rm -rf %{buildroot}%{_docdir}/
rm -f %{buildroot}%{_bindir}/xine-bugreport
rm -f %{buildroot}%{_mandir}/*/man1/xine-bugreport.*
rm -f %{buildroot}%{_mandir}/man1/xine-bugreport.*
rm -f %{buildroot}%{_bindir}/xine-check
rm -f %{buildroot}%{_mandir}/*/man1/xine-check.*
rm -f %{buildroot}%{_mandir}/man1/xine-check.*
cp -a fedoraskins/* %{buildroot}%{_datadir}/xine/skins/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n xine-ui-skins -f %{oreon_filedir}/xine-ui-skins.list
%files -n xine-ui-aaxine -f %{oreon_filedir}/xine-ui-aaxine.list

%changelog

%autochangelog
