%global source0_hash 857b51c78f54df42418ff6fa9e62b8554df7f021cb12338c1fc0d85b99c918ef
%global app_id	org.gnome.Gtranslator
Name:		gtranslator
Version:	51.0
Release:        1%{?dist}
Summary:        Gettext po file editor for GNOME
License:	GPL-2.0-or-later AND GPL-3.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:		https://wiki.gnome.org/Apps/Gtranslator
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{version}.tar.xz
Requires:	hicolor-icon-theme
Requires:	gsettings-desktop-schemas
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libspelling-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
# /oreon:deps
%description
gtranslator is an enhanced gettext po file editor for the GNOME
desktop environment. It handles all forms of gettext po files and
features many comfortable everyday usage features like find and
replace functions, auto translation, and translation learning,

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
