%global source0_hash 1e048105c082aa78e60ea8f1e3f5415f4108d1982a44aea700a685dea0920312

%global forgeurl https://gitlab.com/armagetronad/armagetronad/
%global tag v0.2.9.2.5

%forgemeta

Name: armacycles-ad
Version: 0.2.9.2.5
Release: 3%{?dist}
Summary: A lightcycle game in 3D

License: GPL-2.0-or-later
URL: %{forgeurl}
Source0: %{forgesource}
Source1: armacycles-logo.jpg
Source2: armacycles-ad.desktop

BuildRequires: libxml2-devel >= 2.6.12, SDL_image-devel, SDL_mixer-devel
BuildRequires: libpng-devel, desktop-file-utils, autoconf, automake, gcc-c++
BuildRequires: make
Requires: libxml2 >= 2.6.12, hicolor-icon-theme

%description
In this game you ride a lightcycle; that is a sort of motorbike that
cannot be stopped and leaves a wall behind it. The main goal of the game
is to make your opponents' lightcycles crash into a wall while avoiding
the same fate.
The focus of the game lies on the multiplayer mode, but it provides
challenging AI opponents for a quick training match.

#dedicated server specification
%package dedicated
Summary: Dedicated server for Armacycles Advanced
requires: libxml2 >= 2.6.12

%Description dedicated
This is a special lightweight server for Armacycles Advanced; it can
be run on a low-spec machine and await connections from
the internet and/or the LAN.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

#insert modified logo
cp %{SOURCE1} textures/title.jpg
# remove krawall logo
rm -f armagetronad-0.2.8.2.1/textures/KGN*

./bootstrap.sh

%build
configure_flags="--disable-sysinstall --disable-games --disable-uninstall"

export progtitle="Armacycles Advanced"
export progname=armacyclesad

mkdir -p bindist
pushd bindist
# <sigh> %%configure really should support this in an easier way
echo -e '#!/bin/bash\nexec ../configure "$@"\n' > configure
chmod +x configure
%configure $configure_flags
make %{?_smp_mflags}
popd

mkdir -p bindist-dedicated
pushd bindist-dedicated
cp -a ../bindist/configure .
%configure $configure_flags --disable-glout
make %{?_smp_mflags}
popd

%install
pushd bindist
# uninstall_location=foobar works around a bug triggered by --disable-uninstall
make install DESTDIR=$RPM_BUILD_ROOT uninstall_location=foobar
rm -r $RPM_BUILD_ROOT%{_datadir}/armacyclesad/desktop
popd

pushd bindist-dedicated
make install DESTDIR=$RPM_BUILD_ROOT uninstall_location=foobar
rm -r $RPM_BUILD_ROOT%{_datadir}/armacyclesad-dedicated/desktop
popd

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
BugReportURL: https://bugs.launchpad.net/armagetronad/+bug/1323628
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">armacycles-ad.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>3D motorcycle battle</summary>
  <description>
    <p>
      Armagetron is a 3D Tron-inspired game where the player controls a motorcycle
      that emits a immovable wall behind it.
      Gameplay consists of 2 of these cycles battling to trap each other to
      force their opponent to crash into the wall.
    </p>
  </description>
  <url type="homepage">http://armagetronad.sf.net</url>
  <screenshots>
    <screenshot type="default">http://armagetronad.org/screenshots/screenshot_2.png</screenshot>
    <screenshot>http://armagetronad.org/screenshots/screenshot_5.png</screenshot>
  </screenshots>
</application>
EOF

# Install icons and desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 desktop/icons/16x16/armagetronad.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
install -p -m 644 desktop/icons/32x32/armagetronad.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 desktop/icons/48x48/armagetronad.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}

#remove extraneous scripts
rm -f $RPM_BUILD_ROOT%{_datadir}/armacyclesad/scripts/relocate
rm -f $RPM_BUILD_ROOT%{_datadir}/armacyclesad/language/update.py

rm -f $RPM_BUILD_ROOT%{_datadir}/armacyclesad-dedicated/scripts/relocate
rm -f $RPM_BUILD_ROOT%{_datadir}/armacyclesad-dedicated/scripts/rcd_config
rm -f $RPM_BUILD_ROOT%{_datadir}/armacyclesad-dedicated/scripts/rcd_startstop
rm -f $RPM_BUILD_ROOT%{_datadir}/armacyclesad-dedicated/language/update.py

%files
%doc %{_datadir}/doc/armacyclesad
%config(noreplace) %{_sysconfdir}/armacyclesad
%{_bindir}/armacyclesad
%{_datadir}/armacyclesad
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/armacycles-ad.desktop
%{_datadir}/icons/hicolor/*/apps/armagetronad.png

%files dedicated
%doc COPYING bindist-dedicated/src/doc/
%exclude %{_datadir}/doc/armacyclesad-dedicated
%config(noreplace) %{_sysconfdir}/armacyclesad-dedicated
%{_bindir}/armacyclesad-dedicated
%{_datadir}/armacyclesad-dedicated

%changelog
%autochangelog
