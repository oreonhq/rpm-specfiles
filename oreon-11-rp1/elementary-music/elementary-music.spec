%global source0_hash 1d0e567e203551a0ce7f7868db7e26a69112291f7520d87da1aae8b02fbf45ec
%global srcname music
%global appname io.elementary.music
%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$
Name:           elementary-music
Summary:        Music player and library designed for elementary
Version:        8.1.0
Release:        1%{?dist}
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://github.com/elementary/%{srcname}
Source0:        https://github.com/elementary/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  vala
# /oreon:deps
%description
Quickly queue up and listen to your local music files without any extra
frills. See embedded album artwork. Control playback with media keys or
in the system audio indicator.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{appname}
%oreon_autofiles main

%check

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
