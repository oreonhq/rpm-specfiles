%global source0_hash c6383d22f19d4f821b2d0c03fdb2f374a0d8b86faee08643cfa9af0e5c275714

# -*-Mode: rpm-spec -*-

Name:     wlr-sunclock
Version:  1.0.0
Release:  11%{?dist}
Summary:  Show the sun's shadows on earth

# src/astro.[ch] are by John Walker in 1988 and placed in the Public Domain.
# Otherwise it's LGPLv3.
# Automatically converted from old format: LGPLv3 and Public Domain - review is highly recommended.
License:  LGPL-3.0-only AND LicenseRef-Callaway-Public-Domain

URL:      https://github.com/sentriz/wlr-sunclock
Source:   %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: meson
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel
BuildRequires: pkgconfig(gtk+-wayland-3.0)
BuildRequires: pkgconfig(gtk-layer-shell-0)
BuildRequires: librsvg2-devel

%description

Wayland desktop widget to show the sun's shadows on earth. Uses
gtk-layer-shell and the layer shell protocol to render on your
desktop, behind your windows.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}

%doc README.md

%license LICENCE

%changelog
%autochangelog
