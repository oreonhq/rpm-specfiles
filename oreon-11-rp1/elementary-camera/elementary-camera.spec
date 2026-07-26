%global source0_hash 8cb7a8cccf5d45c2ddea3b98394e889318fedbd3b790c9a77713942d2ac52605

%global srcname camera
%global appname io.elementary.camera

Name:           elementary-camera
Summary:        Camera app designed for elementary
Version:        8.0.2
Release:        %autorelease
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/camera
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.57
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite-7) >= 7.2.0
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libcanberra)

Requires:       hicolor-icon-theme

%description
Camera is a simple app to take photos with a webcam.

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

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml

%files -f %{appname}.lang
%license COPYING
%doc README.md

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml

%changelog
%autochangelog
