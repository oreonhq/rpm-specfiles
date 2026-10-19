%global source0_hash e3a30957757f2830a12514baff94382c90565e5013107ece33b0b1dfbde2c055
%global upload_hash 4a5dcb11cec0b0438ad575db08aa755c
Name:           fragments
Version:        3.0.1
Release:        1%{?dist}
Summary:        Easy to use BitTorrent client which follows the GNOME HIG
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/Fragments
Source0:        https://gitlab.gnome.org/World/Fragments/uploads/%{upload_hash}/%{name}-%{version}.tar.xz
ExcludeArch:    %{ix86}
Requires: adwaita-icon-theme
Requires: transmission-daemon
# oreon:deps
BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
Fragments is an easy to use BitTorrent client which follows the GNOME HIG and
includes well thought-out features.

%prep
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
