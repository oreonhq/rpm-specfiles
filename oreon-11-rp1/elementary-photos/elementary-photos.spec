%global source0_hash da069c0db19371c74a7a0195c6ae8c6cb5f50f484babf37abb2bcb54d314feab

%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$

%global srcname photos
%global appname io.elementary.%{srcname}

Name:           elementary-photos
Summary:        Photo manager and viewer from elementary
Version:        8.0.1
Release:        %autorelease
License:        LGPL-2.1-or-later

URL:            https://github.com/elementary/photos
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.57.0
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8) >= 0.8.5
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(gexiv2) >= 0.4.90
BuildRequires:  pkgconfig(gio-2.0) >= 2.20
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.20
BuildRequires:  pkgconfig(glib-2.0) >= 2.30.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.24.0
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.6.0
BuildRequires:  pkgconfig(gudev-1.0) >= 145
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libexif) >= 0.6.16
BuildRequires:  pkgconfig(libgphoto2) >= 2.4.2
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk3)
BuildRequires:  pkgconfig(libraw) >= 0.13.2
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.26.0
BuildRequires:  pkgconfig(libwebp) >= 0.4.4
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.32
BuildRequires:  pkgconfig(rest-0.7) >= 0.7
BuildRequires:  pkgconfig(sqlite3) >= 3.5.9
BuildRequires:  pkgconfig(webkit2gtk-4.1) >= 2.0.0

Requires:       hicolor-icon-theme

%description
The elementary continuation of Shotwell, originally written by Yorba
Foundation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{appname}

%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.viewer.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml

%files -f %{appname}.lang
%license COPYING
%doc README.md

%{_bindir}/%{appname}

%{_libdir}/%{appname}/

%{_libexecdir}/%{appname}/

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/applications/%{appname}.viewer.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/icons/hicolor/*/apps/%{appname}.viewer.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml

%changelog
%autochangelog
