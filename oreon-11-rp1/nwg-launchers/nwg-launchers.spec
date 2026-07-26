%global source0_hash 9c6babf88a53a5bc99d49770af5040a2b6cc963803414fa6943c73e7f4c6f7ae

Name:           nwg-launchers
Version:        0.7.1
Release:        10%{?dist}
Summary:        GTK-based launchers for sway and other window managers

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/nwg-piotr/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  meson

BuildRequires:  cmake(nlohmann_json)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0) >= 0.5.0
BuildRequires:  pkgconfig(gtkmm-3.0)

# Gdk-pixbuf loader for svg icons
Requires:       librsvg2%{?_isa}

%description
GTK-based launchers: application grid, button bar, menu, dmenu
for sway and other window managers.
The project priorities are:
 - it must work well on sway;
 - it should work as well as possible on Wayfire, i3, dwm and Openbox.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

# This set of application launchers is written for minimalistic keyboard-oriented
# environments and is not intended to be used with major DEs such as GNOME or KDE.
# Therefore, upstream does not provide .desktop files and we're not generating
# them downstream
%files
%license LICENSE
%doc %{_datadir}/%{name}/README.md
%doc examples
%{_bindir}/nwgbar
%{_bindir}/nwgdmenu
%{_bindir}/nwggrid
%{_bindir}/nwggrid-server
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/icon-missing.{png,svg}
%{_datadir}/%{name}/nwgbar/
%{_datadir}/%{name}/nwgdmenu/
%{_datadir}/%{name}/nwggrid/

%changelog
%autochangelog
