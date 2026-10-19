%global source0_hash 51fa063f82af0e17436948290caea0964edb04c581186d360ea3ac45973d4203
%global         desktop_id org.gnome.SimpleScan
Name:           simple-scan
Version:        50.0
Release:        1%{?dist}
Summary:        Simple scanning utility
License:        GPL-3.0-or-later AND CC-BY-SA-3.0
URL:            https://gitlab.gnome.org/GNOME/simple-scan
%global         gittag %{version}
Source0:        https://gitlab.gnome.org/GNOME/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
%if ! 0%{?flatpak}
%endif
Requires:       xdg-utils
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gusb)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpmux)
BuildRequires:  pkgconfig(packagekit-glib2)
BuildRequires:  pkgconfig(sane-backends)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
Simple Scan is an easy-to-use application, designed to let users connect their
scanner and quickly have the image/document in an appropriate format.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{gittag}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-man --with-gnome
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{desktop_id}.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{desktop_id}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
