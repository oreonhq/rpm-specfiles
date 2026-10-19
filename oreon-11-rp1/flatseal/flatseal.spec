%global source0_hash ece97bce5f036d32405528f1b55e00895cce4c8a19d0424e868021e73b78ee62
%global app_id  com.github.tchx84.Flatseal
Name:           flatseal
Version:        2.4.1
Release:        1%{?dist}
Summary:        Manage Flatpak permissions
License:        GPL-3.0-or-later
URL:            https://github.com/tchx84/Flatseal
Source0:        https://github.com/tchx84/Flatseal/archive/v%{version}/Flatseal-%{version}.tar.gz
Requires:       gjs
Requires:       appstream >= 1.0
Requires:       gtk4
Requires:       libadwaita >= 1.8
Requires:       webkitgtk6.0 >= 2.40
BuildArch:      noarch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gjs
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(webkitgtk-6.0)
# /oreon:deps
%description
Flatseal is a graphical utility to review and modify permissions from your
Flatpak applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Flatseal-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
