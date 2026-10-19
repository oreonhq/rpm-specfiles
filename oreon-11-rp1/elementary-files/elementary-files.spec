%global source0_hash a5e1b039d59001a636624315e37fa6aeeee8908cf1b323021d06d3ccd49214f2
%global srcname files
%global appname io.elementary.files
%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$
Name:           elementary-files
Summary:        File manager from elementary
Version:        7.3.2
Release:        1%{?dist}
License:        GPL-3.0-or-later AND GPL-3.0-only AND GPL-2.0-or-later AND LGPL-3.0-or-later AND LGPL-3.0-only AND LGPL-2.1-or-later
URL:            https://github.com/elementary/%{srcname}
Source0:        https://github.com/elementary/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Requires:       dbus-common
Requires:       polkit
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(cloudproviders)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libgit2-glib-1.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk3)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  vala
# /oreon:deps
%description
The simple, powerful, and sexy file manager from elementary.

%package        portal
Summary:        File manager from elementary (flatpak file chooser portal)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dbus-common
Requires:       xdg-desktop-portal
%description    portal
The simple, powerful, and sexy file manager from elementary.

This package contains a file chooser portal implementation for flatpak.

%package        devel
Summary:        File manager from elementary (development headers)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The simple, powerful, and sexy file manager from elementary.

This package contains the development headers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build

%meson -Dwith-zeitgeist=disabled
%meson_build
%install
%meson_install
%find_lang %{appname}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml
%post portal

%systemd_user_post %{appname}.xdg-desktop-portal.service
%preun portal

%systemd_user_preun %{appname}.xdg-desktop-portal.service
%files -f %{oreon_filedir}/main.list
%files -n elementary-files-portal -f %{oreon_filedir}/elementary-files-portal.list
%files -n elementary-files-devel -f %{oreon_filedir}/elementary-files-devel.list

%changelog

%autochangelog
