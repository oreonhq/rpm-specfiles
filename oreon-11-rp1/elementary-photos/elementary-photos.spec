%global source0_hash a9108a9ac135076fadb526c23c2277ba7a69a4bbf3eeaa9d2ba041504e5c1799
%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$
%global srcname photos
%global appname io.elementary.%{srcname}
Name:           elementary-photos
Summary:        Photo manager and viewer from elementary
Version:        8.0.2
Release:        1%{?dist}
License:        LGPL-2.1-or-later
URL:            https://github.com/elementary/photos
Source0:        https://github.com/elementary/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libgphoto2)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk3)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  vala
# /oreon:deps
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
%oreon_autofiles main

%check

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.viewer.desktop
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
