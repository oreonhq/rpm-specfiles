%global source0_hash 16437fd0786562c3ae3f0041fabdbad20dee5b3b454d0e1c662458399a7fc4ff

%global app_id com.toolstack.Folio

Name:           folio
Version:        25.02
Release:        %autorelease
Summary:        A markdown note-taking app for GNOME

License:        GPL-3.0-or-later
URL:            https://github.com/toolstack/Folio
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
Patch0:         storage-location.patch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  gettext
BuildRequires:  blueprint-compiler
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Folio-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{app_id}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml

%files -f %{app_id}.lang
%license COPYING
%doc README.md
%{_bindir}/%{app_id}
%{_bindir}/%{name}-search-provider
%{_datadir}/applications/%{app_id}-editor.desktop
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/dbus-1/services/%{app_id}.SearchProvider.service
%{_datadir}/dbus-1/services/%{app_id}.service
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/gnome-shell/search-providers/%{app_id}.SearchProvider-search-provider.ini
%{_datadir}/gtksourceview-5/language-specs/markdownpp.lang
%{_datadir}/gtksourceview-5/styles/%{name}_markdown.xml
%{_datadir}/gtksourceview-5/styles/%{name}_markdown_dark.xml
%{_datadir}/icons/hicolor/scalable/apps/%{app_id}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{app_id}-symbolic.svg
%{_metainfodir}/%{app_id}.appdata.xml

%changelog
%autochangelog
