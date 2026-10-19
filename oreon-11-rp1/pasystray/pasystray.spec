%global source0_hash 9c6fc5859a203f0a6dd8ce2038fea85b7bac44b1baff5c4cf73643229fafa641
Name:           pasystray
Version:        0.8.2
Release:        1%{?dist}
Summary:        PulseAudio system tray
License:        LGPL-2.1-or-later
URL:            https://github.com/christophgysin/pasystray
Source0:        https://github.com/christophgysin/pasystray/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          pasystray-0.8.2-gcc15.patch
Patch:          pasystray-0.8.0-wayland.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(x11)
# /oreon:deps
%description
A replacement for the deprecated padevchooser.
pasystray allows setting the default PulseAudio source/sink and moving streams
on the fly between sources/sinks without restarting the client applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -i
%configure
%make_build
%install
%make_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}%{_metainfodir}
cat > %{buildroot}%{_metainfodir}/%{name}.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="desktop">
  <id>io.github.christophgysin.pasystray</id>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>LGPL-2.1-or-later</project_license>
  <name>PulseAudio System Tray</name>
  <developer_name>Christoph Gysin</developer_name>
  <summary>Tray icon for controlling PulseAudio</summary>
  <url type="homepage">https://github.com/christophgysin/pasystray/</url>
  <content_rating type="oars-1.1" />
  <description>
    <p>PulseAudio System Tray (pasystray) allows setting the default PulseAudio
       source/sink and moving streams on the fly between sources/sinks without
       restarting the client applications.</p>
  </description>
  <launchable type="desktop-id">pasystray.desktop</launchable>
  <provides>
    <binary>pasystray</binary>
  </provides>
  <releases>
    <release version="%{version}" date="%(date +%F -r %{SOURCE0})"/>
  </releases>
</component>
EOF
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
