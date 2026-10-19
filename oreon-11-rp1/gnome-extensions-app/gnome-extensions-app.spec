%global source0_hash c60998fab1f67e73fcebeaa40c5806dc1ebffd6e1eb16e3b7472dc42691c85e6
%global adwaita_version 1.5.0
%define bus_name org.gnome.Extensions
Name:          gnome-extensions-app
Version:       51~alpha
Release:        1%{?dist}
Summary:        Manage GNOME Shell extensions
License:       GPL-2.0-or-later
URL:           https://gitlab.gnome.org/GNOME/%{name}
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-51.alpha.tar.xz
Requires:      gjs%{_isa}
Requires:      libadwaita%{_isa} >= %{adwaita_version}
# oreon:deps
BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  gjs
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
# /oreon:deps
%description
GNOME Extensions is an application for configuring and removing
GNOME Shell extensions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{gnome_tarball_version}

%build

%meson
%meson_build
%check

%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/%{bus_name}.desktop
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
