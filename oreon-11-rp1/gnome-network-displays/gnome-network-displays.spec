%global source0_hash cdec68c8f9b326baaee545374a8c2b93ca919e48f4b8a42461cb0eb2398dab27

%global major_minor_version %%(cut -d "." -f 1,2 <<<%{version})

Name:           gnome-network-displays
Version:        0.97.0
Release:        3%{?dist}
Summary:        Screencasting for GNOME

# The icon is licensed CC-BY-SA
License:        GPL-3.0-or-later AND CC-BY-SA-4.0
URL:            https://gitlab.gnome.org/GNOME/gnome-network-displays
Source0:        https://download.gnome.org/sources/%{name}/%{major_minor_version}/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  firewalld-filesystem
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-gobject)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.14
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 1.14
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-rtsp-1.0) >= 1.14
BuildRequires:  pkgconfig(gstreamer-rtsp-server-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.14
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.0.0
BuildRequires:  pkgconfig(libnm) >= 1.15.1
BuildRequires:  pkgconfig(libportal-gtk4) >= 0.7
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsoup-3.0)

# Versioned library deps
Requires: gnome-desktop3
Requires: gstreamer1-rtsp-server
Requires: gtk4
Requires: hicolor-icon-theme
Requires: NetworkManager-libnm > 1.16.0
%if !0%{?flatpak}
Requires: NetworkManager-wifi
Requires: pipewire-gstreamer
%endif

%description
GNOME Network Displays allows you to cast your desktop to a remote display.
Supports the Miracast and Chromecast protocols.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%find_lang %{name} --all-name --with-gnome

%post
%firewalld_reload

%postun
%firewalld_reload

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/gnome-network-displays
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.NetworkDisplays.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.NetworkDisplays-symbolic.svg
%{_metainfodir}/org.gnome.NetworkDisplays.appdata.xml
%{_prefix}/lib/firewalld/zones/P2P-WiFi-Display.xml

%changelog
%autochangelog
