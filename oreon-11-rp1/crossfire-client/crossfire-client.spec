%global source0_hash a3cbf0a3fa73ccc61b643a6477e2fe8d45543c75a2c835c069a3514ad6858b0d
%global __cmake_in_source_build 1
Name: crossfire-client
Version: 1.75.5
Release:        1%{?dist}
Summary:        Client for connecting to crossfire servers
License: GPL-2.0-or-later
URL: http://crossfire.real-time.com
Source0:        http://downloads.sourceforge.net/crossfire/%{name}-%{version}.tar.gz
Requires: crossfire-client-images
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel
BuildRequires:  libpng-devel
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  vala
# /oreon:deps
%description
Crossfire is a graphical role-playing adventure game with
characteristics reminiscent of rogue, nethack, omega, and gauntlet. 
It has multiplayer capability and presently runs under X11.

Client for playing the new client/server based version of Crossfire.
This package allows you to connect to crossfire servers around the world.
You do not need install the crossfire program in order to use this
package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

for size in 48x48 32x32 16x16 ; do 
    convert -transparent white pixmaps/${size}.png temp.png
    mv temp.png pixmaps/${size}.png
done

%build

export  LDFLAGS+=" -lX11"
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
%install
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -d $RPM_BUILD_ROOT%{_datadir}/icons/locolor/16x16/apps
install -d $RPM_BUILD_ROOT%{_datadir}/icons/locolor/32x32/apps
install -d $RPM_BUILD_ROOT%{_datadir}/icons/locolor/48x48/apps
%cmake_install
install -m 644 pixmaps/16x16.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/crossfire-client.png
install -m 644 pixmaps/32x32.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/crossfire-client.png
install -m 644 pixmaps/48x48.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/crossfire-client.png
install -m 644 pixmaps/16x16.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/locolor/16x16/apps/crossfire-client.png
install -m 644 pixmaps/32x32.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/locolor/32x32/apps/crossfire-client.png
install -m 644 pixmaps/48x48.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/locolor/48x48/apps/crossfire-client.png
sed -i -e 's/^Name=.*/Name=Crossfire/' gtk-v2/crossfire-client.desktop
desktop-file-install                            \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
        --add-category Game                                     \
        --add-category RolePlaying                              \
        gtk-v2/crossfire-client.desktop
mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
cat > $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
EmailAddress: crossfire@metalforge.org
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">crossfire-client.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A multiplayer co-operative RPG involving exploration, magic and treasure hunting</summary>
  <description>
    <p>
      Crossfire is an open source RPG with numerous maps that can be explored
      for treasures and artifacts.
    </p>
  </description>
  <url type="homepage">http://crossfire.real-time.com</url>
  <screenshots>
    <screenshot type="default">http://crossfire.real-time.com/clients/gtkv2images/caelestis_790x600.png</screenshot>
  </screenshots>
</application>
EOF
mkdir -p $RPM_BUILD_ROOT%{_libdir}
cp common/libcfclient.so $RPM_BUILD_ROOT%{_libdir}/
%ldconfig_scriptlets
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
