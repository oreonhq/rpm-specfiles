%global source0_hash d78aa0e1fa2167a464745638b05d719f67c9d65d007b6a0186d714f089760d52

%global forgeurl https://gitlab.com/rmnvgr/metadata-cleaner
%global tag v%{version}
%global appid fr.romainvigier.MetadataCleaner
%global gtk_version 4.6

Name:       metadata-cleaner
Version:    2.5.5
%forgemeta
Release:    %autorelease
Summary:    View and clean metadata in files, using mat2

# - The source code is released under the terms of the GNU General Public
#   License 3.0 or later.
# - The original artwork and translations are released under the terms of the
#   Creative Commons Attribution-ShareAlike 4.0 International.
# - Additional icons from the Icon Development Kit of the GNOME Design Team are
#   released under the terms of the CC0 1.0 Universal.
License:    GPL-3.0-or-later AND CC-BY-SA-4.0 AND CC0-1.0
URL:        %{forgeurl}
Source:     %{forgesource}
BuildArch:  noarch

BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig(gtk4) >= %{gtk_version}

Requires:   dbus-common
Requires:   gtk4 >= %{gtk_version}
Requires:   hicolor-icon-theme
Requires:   libadwaita >= 1.2
Requires:   mat2
Requires:   yelp

%global _description %{expand:
Metadata within a file can tell a lot about you. Cameras record data about
when and where a picture was taken and which camera was used. Office
applications automatically add author and company information to documents and
spreadsheets. This is sensitive information and you may not want to disclose
it. This tool allows you to view metadata in your files and to get rid of it,
as much as possible. Under the hood, it relies on mat2 to parse and remove the
metadata.}

%description %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid} --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appid}.desktop

%files -f %{appid}.lang
%license LICENSE.md LICENSES/*
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/scalable/*/%{appid}.svg
%{_datadir}/icons/hicolor/symbolic/*/%{appid}-symbolic.svg
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
%autochangelog
