%global source0_hash 4c92f2d1a3d454ec1f5fb05ef08ca34df9c743af64c8b5965c35884d46cb005c

Name:          gupnp-tools
Version:       0.12.2
Release:       3%{?dist}
Summary:       A collection of dev tools utilising GUPnP and GTK+

License:       GPL-2.0-or-later
URL:           https://wiki.gnome.org/Projects/GUPnP
Source0:       https://download.gnome.org/sources/%{name}/0.12/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: meson
BuildRequires: pkgconfig(gupnp-1.6)
BuildRequires: pkgconfig(gupnp-av-1.0)
BuildRequires: pkgconfig(gssdp-1.6)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtksourceview-4)
BuildRequires: pkgconfig(libsoup-3.0)

Requires: hicolor-icon-theme

%description
GUPnP is an object-oriented open source framework for creating UPnP 
devices and control points, written in C using GObject and libsoup. 
The GUPnP API is intended to be easy to use, efficient and flexible. 

GUPnP-tools is a collection of developer tools utilising GUPnP and GTK+. 
It features a universal control point application as well as a sample 
DimmableLight v1.0 implementation. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/gupnp-av-cp.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/gupnp-network-light.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/gupnp-universal-cp.desktop

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/gupnp-tools/
%dir %{_datadir}/gupnp-tools/pixmaps/
%dir %{_datadir}/gupnp-tools/xml/
%{_bindir}/gssdp-discover
%{_bindir}/gupnp-av-cp
%{_bindir}/gupnp-event-dumper
%{_bindir}/gupnp-network-light
%{_bindir}/gupnp-universal-cp
%{_bindir}/gupnp-upload
%{_datadir}/applications/gupnp-av-cp.desktop
%{_datadir}/applications/gupnp-network-light.desktop
%{_datadir}/applications/gupnp-universal-cp.desktop
%{_datadir}/gupnp-tools/pixmaps/*.png
%{_datadir}/gupnp-tools/xml/*.xml
%{_datadir}/icons/hicolor/*/apps/av-cp.png
%{_datadir}/icons/hicolor/*/apps/network-light.png
%{_datadir}/icons/hicolor/*/apps/universal-cp.png

%changelog
%autochangelog
