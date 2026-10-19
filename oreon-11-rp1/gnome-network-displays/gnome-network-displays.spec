%global source0_hash 1ece4a1bc822c7ebf725e8847b8ce8998b47d1ec1715a4b4ddb9ddd71691ed85
%global major_minor_version %%(cut -d "." -f 1,2 <<<%{version})
Name:           gnome-network-displays
Version:        0.99.0
Release:        1%{?dist}
Summary:        Screencasting for GNOME
License:        GPL-3.0-or-later AND CC-BY-SA-4.0
URL:            https://gitlab.gnome.org/GNOME/gnome-network-displays
Source0:        https://download.gnome.org/sources/%{name}/0.99/%{name}-%{version}.tar.xz
Requires: gnome-desktop3
Requires: gstreamer1-rtsp-server
Requires: gtk4
Requires: hicolor-icon-theme
Requires: NetworkManager-libnm > 1.16.0
%if !0%{?flatpak}
Requires: NetworkManager-wifi
Requires: pipewire-gstreamer
%endif
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  firewalld-filesystem
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-gobject)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-rtsp-1.0)
BuildRequires:  pkgconfig(gstreamer-rtsp-server-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsoup-3.0)
# /oreon:deps
%description
GNOME Network Displays allows you to cast your desktop to a remote display.
Supports the Miracast and Chromecast protocols.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%find_lang %{name} --all-name --with-gnome
%oreon_autofiles main

%post

%firewalld_reload
%postun

%firewalld_reload
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
