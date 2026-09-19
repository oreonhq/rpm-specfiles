%global source0_hash none

%global upload_hash 4a5dcb11cec0b0438ad575db08aa755c

Name:           fragments
Version:        3.0.1
Release:        4%{?dist}
Summary:        Easy to use BitTorrent client which follows the GNOME HIG

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/Fragments
Source0:        %{url}/uploads/%{upload_hash}/fragments-%{version}.tar.xz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

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
BuildRequires:  cargo-rpm-macros >= 24

Requires: adwaita-icon-theme
Requires: transmission-daemon

%description
Fragments is an easy to use BitTorrent client which follows the GNOME HIG and
includes well thought-out features.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%doc README.md
%license COPYING.md
%{_bindir}/fragments
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/dbus-1/services/*.service
%{_datadir}/fragments/*.gresource
%{_datadir}/icons/hicolor/*/*/*
%{_metainfodir}/*.xml

%changelog
%autochangelog
