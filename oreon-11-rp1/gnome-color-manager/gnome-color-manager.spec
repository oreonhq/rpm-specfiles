%global source0_hash 3904d42abb4ea566df0b880e82bf0b9f86386c692f15b318469a4c7be33a887f
Name:      gnome-color-manager
Version:   3.36.2
Release:        3%{?dist}
Summary:        Color management tools for GNOME
License:   GPL-2.0-or-later
URL:       https://gitlab.gnome.org/GNOME/gnome-color-manager
Source0:        http://download.gnome.org/sources/gnome-color-manager/3.36/%{name}-%{version}.tar.xz
Requires: shared-mime-info
Obsoletes: gnome-color-manager-devel <= 3.1.1
Provides: gnome-color-manager-devel
# oreon:deps
BuildRequires:  colord-devel
BuildRequires:  docbook-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  itstool
BuildRequires:  lcms2-devel
BuildRequires:  meson
# /oreon:deps
%description
gnome-color-manager is a session framework that makes it easy to manage, install
and generate color profiles in the GNOME desktop.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %name --with-gnome
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.36.2-3
- Prepare for Oreon 11 (RP1)
