%global source0_hash 61fdfd9d63c355d46545b0445d3d815e6d2d597d3e4bf3fe0464db95d0d8970d
%global rdnn    org.heliumos.bootc_gtk
Name:           bootc-gtk
Version:        0.3
Release:        1%{?dist}
Summary:        A GTK4 interface for bootc
License:        GPL-2.0-or-later
URL:            https://codeberg.org/HeliumOS/bootc-gtk
BuildArch:      noarch
Source0:        https://codeberg.org/HeliumOS/%{name}/archive/%{version}.tar.gz#/%{name}.tar.gz
Requires:       bootc
Requires:       gtk4
Requires:       hicolor-icon-theme
Requires:       libadwaita
Requires:       python3-gobject
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel
# /oreon:deps
%description
A GTK4 interface for bootc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n bootc-gtk
sed -r \
    -e '/\b(glib_compile_schemas|gtk_update_icon_cache|update_desktop_database)\b/ s/true/false/' \
    -i meson.build

%build

%meson
%meson_build
%install
%meson_install
%py3_shebang_fix %{buildroot}%{_bindir}/%{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnn}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rdnn}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
