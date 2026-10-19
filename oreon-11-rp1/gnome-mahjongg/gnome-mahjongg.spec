%global source0_hash 2ef9a1cd246d8ccc9ccd27fa435f972a81def9cf3eccc4c880cbb8929ffb8821
%global tarball_version %%(echo %{version} | tr '~' '.')
%define major_version %(c=%{version}; echo $c | cut -d. -f1 | cut -d~ -f1)
Name:           gnome-mahjongg
Version:        51.1
Release:        1%{?dist}
Summary:        GNOME Mahjongg game
License:        GPL-2.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Mahjongg
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  vala
# /oreon:deps
%description
Mahjongg is a simple pattern recognition game. You score points by
matching identical tiles.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
