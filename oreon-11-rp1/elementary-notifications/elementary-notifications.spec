%global source0_hash 8d837736ba545e51e2bf4694020c5c7d948fead98d55835d2bfc9d82cffadd59
%global srcname notifications
%global appname io.elementary.notifications
Name:           elementary-notifications
Version:        8.1.2
Release:        1%{?dist}
Summary:        GTK Notifications Server
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/notifications
Source0:        https://github.com/elementary/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-wayland)
BuildRequires:  pkgconfig(gtk4-x11)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  vala
# /oreon:deps
%description
elementary Notifications is a GTK notification server for Pantheon.

%package demo
Summary:        GTK Notifications Server (demo application)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description demo
elementary Notifications is a GTK notification server for Pantheon.

This package contains a demo application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir notifications-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n elementary-notifications-demo -f %{oreon_filedir}/elementary-notifications-demo.list

%changelog

%autochangelog
