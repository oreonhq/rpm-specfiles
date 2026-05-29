%global source0_hash none

%global _vpath_srcdir subprojects/extensions-app
%global source_name gnome-shell
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %%(cut -d "." -f 1 <<<%{tarball_version})

%global adwaita_version 1.5.0

Name:          gnome-extensions-app
Version:       49.2
Release:       %autorelease
Summary:       Manage GNOME Shell extensions

License:       GPL-2.0-or-later
URL:           https://gitlab.gnome.org/GNOME/%{source_name}
Source0: https://download.gnome.org/sources/gnome-shell/%%(cut/gnome-shell-%{tarball_version}.tar.xz
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: meson
BuildRequires: git

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: gjs
BuildRequires: desktop-file-utils
BuildRequires: appstream

Requires:      gjs%{_isa}
Requires:      libadwaita%{_isa} >= %{adwaita_version}

%define exec_name gnome-extensions-app
%define bus_name org.gnome.Extensions

%description
GNOME Extensions is an application for configuring and removing
GNOME Shell extensions.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{source_name}-%{tarball_version}
ln --symbolic ../../libshew subprojects/extensions-app/subprojects/libshew

%{_vpath_srcdir}/generate-translations.sh


%build
%meson
%meson_build

%check
%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/%{bus_name}.desktop


%install
%meson_install

%find_lang %{name}

rm -rf %{buildroot}/%{_datadir}/%{name}/gir-1.0

%files -f %{name}.lang
%license COPYING
%{_bindir}/%{exec_name}
%{_datadir}/applications/%{bus_name}.desktop
%{_datadir}/dbus-1/services/%{bus_name}.service
%{_datadir}/glib-2.0/schemas/%{bus_name}.gschema.xml
%{_datadir}/metainfo/%{bus_name}.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/%{bus_name}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{bus_name}.Devel.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{bus_name}-symbolic.svg
%{_datadir}/%{name}/
%{_libdir}/%{name}/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 49.2-1
- Prepare for Oreon 11 (RP1)
