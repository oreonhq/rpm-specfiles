%global source0_hash 9c6babf88a53a5bc99d49770af5040a2b6cc963803414fa6943c73e7f4c6f7ae
Name:           nwg-launchers
Version:        0.7.1
Release:        10%{?dist}
Summary:        GTK-based launchers for sway and other window managers
License:        GPL-3.0-or-later
URL:            https://github.com/nwg-piotr/%{name}
Source0:        https://github.com/nwg-piotr/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       librsvg2%{?_isa}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gtkmm-3.0)
# /oreon:deps
%description
GTK-based launchers: application grid, button bar, menu, dmenu
for sway and other window managers.
The project priorities are:
 - it must work well on sway;
 - it should work as well as possible on Wayfire, i3, dwm and Openbox.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
