%global source0_hash 52626fde3909921ac586cc4cc10f30f123aaf6155a177ef8861ca0e55d6de850
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:          polari
Version:       50.0
Release:        1%{?dist}
Summary:        Internet Relay Chat client for GNOME
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           https://wiki.gnome.org/Apps/Polari
Source0:        http://download.gnome.org/sources/%{name}/45/%{name}-%{version}.tar.xz
Requires: libsoup3%{?_isa}
Requires: libsecret%{?_isa}
Requires: telepathy-filesystem
Requires: telepathy-mission-control
Requires: telepathy-idle
Recommends: google-noto-emoji-fonts
%define bus_name org.gnome.Polari
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  glib2
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(girepository-2.0)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(telepathy-glib)
BuildRequires:  pkgconfig(tracker-sparql-3.0)
# /oreon:deps
%description
Polari is an Internet Relay Chat client for the GNOME desktop.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
rm -rf %{buildroot}/%{_datadir}/%{name}/gir-1.0
%oreon_autofiles main

%check

%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
