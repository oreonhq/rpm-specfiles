%global source0_hash d78aa0e1fa2167a464745638b05d719f67c9d65d007b6a0186d714f089760d52
%global forgeurl https://gitlab.com/rmnvgr/metadata-cleaner
%global tag v%{version}
%global appid fr.romainvigier.MetadataCleaner
%global gtk_version 4.6
Name:       metadata-cleaner
Version:    2.5.6
%forgemeta
Release:        1%{?dist}
Summary:        View and clean metadata in files, using mat2
License:    GPL-3.0-or-later AND CC-BY-SA-4.0 AND CC0-1.0
URL:        %{forgeurl}
Source0:        %{forgeurl}/-/archive/%{tag}/%{name}-%{tag}.tar.bz2
BuildArch:  noarch
Requires:   dbus-common
Requires:   gtk4 >= %{gtk_version}
Requires:   hicolor-icon-theme
Requires:   libadwaita >= 1.2
Requires:   mat2
Requires:   yelp
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
# /oreon:deps
%description

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{appid} --with-gnome
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appid}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
