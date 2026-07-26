%global source0_hash 21c2bbef88c40473c355003582f9331d2f9b8a01efdcce0935edfc5f6b023a3e

Name:           waybar
Version:        0.15.0
Release:        1%{?dist}
Summary:        Highly customizable Wayland bar for Sway and Wlroots based compositors
# Source files/overall project licensed as MIT, but
# - BSL-1.0
#   * include/util/clara.hpp
# - HPND-sell-variant
#   * protocol/ext-workspace-unstable-v1.xml
#   * protocol/wlr-foreign-toplevel-management-unstable-v1.xml
#   * protocol/wlr-layer-shell-unstable-v1.xml
# - ISC
#   * protocol/river-control-unstable-v1.xml
#   * protocol/river-status-unstable-v1.xml
#   * src/util/rfkill.cpp
License:        MIT AND BSL-1.0 AND ISC
URL:            https://github.com/Alexays/Waybar
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Downstream changes to the configuration:
#  - Fix missing or incorrectly rendered icons
#  - Remove several modules from the config
#  - Switch font to monospace
Patch:          waybar-fedora-config-changes.patch

# Fix for hot update loop that can spike CPU and
# destabilize rendering in drawer/group setups
# https://github.com/Alexays/Waybar/pull/4838
Patch:          fix-treat-missing-interval-as-once.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.59.0
BuildRequires:  scdoc
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(catch2)
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(fmt) >= 8.1.1
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0) >= 0.9.0
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libgps)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(playerctl)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(spdlog) >= 1.10.0
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wireplumber-0.5)
BuildRequires:  pkgconfig(xkbregistry)

Enhances:       sway
Recommends:     font(fontawesome6free)
Recommends:     font(fontawesome6brands)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Waybar-%{version}

%build
%meson \
    -Dcava=disabled  \
    -Dsndio=disabled
%meson_build

%install
%meson_install

%check
%meson_test

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/xdg/%{name}
%config(noreplace) %{_sysconfdir}/xdg/%{name}/config.jsonc
%config(noreplace) %{_sysconfdir}/xdg/%{name}/style.css
%{_bindir}/%{name}
%{_mandir}/man5/%{name}*
%{_userunitdir}/%{name}.service

%changelog
%autochangelog
