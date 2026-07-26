%global source0_hash 90e2b78d43cc32fb3f6af027788162dc9d272941f9630b43fc34f203a55c86a7

Name:           netpanzer
Version:        0.8.7
Release:        29%{?dist}
Summary:        An Online Multiplayer Tactical Warfare Game

License:        GPL-2.0-or-later
URL:            http://www.netpanzer.info
Source0:	http://www.netpanzer.info/Download/NetPanzer/Releases/0.8.7/netpanzer-0.8.7-source.zip
Source1:	netpanzer.desktop
Patch4:         netpanzer-0.8.2-MapSelectionView-memory.patch
Patch6:         netpanzer-0.8.7-ccflags.patch
Patch8:		netpanzer-0.8.7-syslibs.patch
Patch9:         netpanzer-python3.patch

BuildRequires:  gcc-c++
BuildRequires:  physfs-devel >= 0.1.9, desktop-file-utils, doxygen, python3-scons
BuildRequires:  SDL-devel >= 1.2.5, SDL_mixer-devel >= 1.2, SDL_image-devel >= 1.2
BuildRequires:  compat-lua-devel
Obsoletes:      netpanzer-data <= 0.8
Provides:       netpanzer-data = %{version}-%{release}

%description
netPanzer is an online multiplayer tactical warfare game designed for FAST
ACTION combat. Gameplay concentrates on the core -- no resource management is
needed. The game is based on quick tactical action and unit management in
real-time. Battles progress quickly and constantly as destroyed players respawn
with a set of new units. Players can join or leave multiplayer games at any
time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qcn netpanzer-0.8.7
%patch -P4 -p0
%patch -P6 -p1
%patch -P8 -p1
%patch -P9 -p0
rm -r src/Lib/lua src/Lib/physfs

%build
CCFLAGS="%{optflags} -std=c++14" scons datadir=%{_datadir}/netpanzer %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 netpanzer $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr cache/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr maps/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr pics/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr powerups/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr scripts/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr units/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr wads/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/
cp -pr sound/ $RPM_BUILD_ROOT%{_datadir}/netpanzer/

# Install desktop item
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/netpanzer.desktop
rm -f $RPM_BUILD_ROOT%{_datadir}/pixmaps/netpanzer.xpm

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mv netpanzer.png \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

desktop-file-install \
	--dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

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
<!-- Copyright 2014 William Moreno Reyes <williamjmoreno@gmail.com> -->
<!--
EmailAddress: admin@netpanzer.info
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">netpanzer.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Multiplayer war game in real time</summary>
  <description>
    <p>
      Play a on line tactical game over the internet or a LAN, with one vs one
      option using a direct connect or modem.
      netPanzer in designed for a fast game mode, without the need of collect
      resources, any player can play until his last unit is destroyed.
    </p>
  </description>
  <url type="homepage">http://netpanzer.berlios.de</url>
  <screenshots>
    <screenshot type="default">http://www.netpanzer.info/public/netpanzer.info/images/netpanzer-game/screenshot63.jpg</screenshot>
  </screenshots>
</application>
EOF

%files
%doc COPYING README* docs/
%{_bindir}/netpanzer
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/netpanzer.desktop
%{_datadir}/icons/hicolor/48x48/apps/netpanzer.png
%{_datadir}/netpanzer

%changelog
%autochangelog
