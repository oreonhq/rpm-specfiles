%global source0_hash af1aa8e68699895a841415c007c7f3f48efc06f07c50d219d30f8131a981248e

Name:          muffin
Version:       6.6.3
Release:       1%{?dist}
Summary:       Window and compositing manager based on Clutter

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           https://github.com/linuxmint/%{name}
Source0:       %url/archive/%{version}/%{name}-%{version}.tar.gz

ExcludeArch:   %{ix86}

BuildRequires: meson
BuildRequires: gcc
BuildRequires: cvt
BuildRequires: pkgconfig(graphene-gobject-1.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(fribidi)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gmodule-no-export-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(cinnamon-desktop) >= 6.6.0
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xkeyboard-config)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(x11-xcb)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xcb-randr)
BuildRequires: pkgconfig(xcb-res)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xau)
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(atk)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(xwayland)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(gl)
BuildRequires: mesa-libEGL-devel
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libwacom)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(pangoft2)
BuildRequires: zenity

Requires: dbus-x11
Requires: zenity
Recommends: xorg-x11-server-Xwayland

%description
Muffin is a window and compositing manager that displays and manages
your desktop via OpenGL. Muffin combines a sophisticated display engine
using the Clutter toolkit with solid window-management logic inherited
from the Metacity window manager.

Muffin is very extensible via plugins, which
are used both to add fancy visual effects and to rework the window
management behaviors to meet the needs of the environment.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: mesa-libEGL-devel

%description devel
Header files and libraries for developing Muffin plugins. Also includes
utilities for testing Metacity/Muffin themes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

rm -rf %{buildroot}%{_bindir}/
rm -rf %{buildroot}%{_mandir}/man1/
rm -rf %{buildroot}%{_datadir}/applications/

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md NEWS
%license COPYING
%{_libdir}/libmuffin.so.*
%{_libdir}/muffin/
%{_libexecdir}/muffin-restart-helper
%exclude %{_libdir}/muffin/*.gir
%{_datadir}/glib-2.0/schemas/org.cinnamon.muffin.*.xml

%files devel
%{_includedir}/muffin/
%{_libdir}/libmuffin.so
%{_libdir}/muffin/*.gir
%{_libdir}/pkgconfig/*

%changelog
%autochangelog
