%global source0_hash f60c1e627c977ce0785af88046d8b9487cb50ea99630072ec5fce8e4347d5dc1

%global srcname calculator
%global appname io.elementary.calculator

Name:           elementary-calculator
Summary:        Calculator app designed for elementary
Version:        8.0.1
Release:        %autorelease
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.56
BuildRequires:  vala

BuildRequires:  pkgconfig(granite-7) >= 7.0.0
BuildRequires:  pkgconfig(gtk4)

Requires:       hicolor-icon-theme

%description
A simple calculator for everyday use.

It supports basic and some scientific calculations, including trigonometry
functions (sin, cos, and tan).

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
%meson_test

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
