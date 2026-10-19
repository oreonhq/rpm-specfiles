%global source0_hash 5d23bed00132ab58d2c8fd7f588b75ba6a4b3593cfa4a1f1475f2e9b79a725a1
Name:     wlr-sunclock
Version:  1.2.0
Release:        1%{?dist}
Summary:        Show the sun's shadows on earth
License:  LGPL-3.0-only AND LicenseRef-Callaway-Public-Domain
URL:      https://github.com/sentriz/wlr-sunclock
Source0:        https://github.com/sentriz/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  librsvg2-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-wayland-3.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
# /oreon:deps
%description

Wayland desktop widget to show the sun's shadows on earth. Uses
gtk-layer-shell and the layer shell protocol to render on your
desktop, behind your windows.

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
