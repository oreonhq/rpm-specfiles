%global source0_hash b466c6660155521ba8135339c6df080a0e071a46f9911b99172b21f9e2dfd808
%global tarball_version %(echo %{version} | tr '~' '.')
Name:           gnome-logs
Version:        50.0
Release:        1%{?dist}
Summary:        Log viewer for the systemd journal
License:        GPL-3.0-or-later AND CC0-1.0 AND CC-BY-3.0
URL:            https://wiki.gnome.org/Apps/Logs
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{version}.tar.xz
Requires:       gsettings-desktop-schemas
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  itstool
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libsystemd)
# /oreon:deps
%description
A log viewer for the systemd journal.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson -Dman=true
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main

%check

%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
