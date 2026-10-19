%global source0_hash cceb06fac3e9f63b160bed62bf56259b0075c63c425b069bf8ba329057938a14
%global srcname calendar
%global appname io.elementary.calendar
%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$
Name:           elementary-calendar
Summary:        Desktop calendar app designed for elementary
Version:        8.0.2
Release:        1%{?dist}
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later
URL:            https://github.com/elementary/calendar
Source0:        https://github.com/elementary/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(champlain-0.12)
BuildRequires:  pkgconfig(champlain-gtk-0.12)
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libecal-2.0)
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libedataserverui-1.2)
BuildRequires:  pkgconfig(libgeoclue-2.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libical-glib)
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk3)
BuildRequires:  vala
# /oreon:deps
%description

%package        devel
Summary:        The official elementary calendar (devel files)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel

This package contains the development files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{appname}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n elementary-calendar-devel -f %{oreon_filedir}/elementary-calendar-devel.list

%changelog

%autochangelog
