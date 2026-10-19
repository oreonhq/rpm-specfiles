%global source0_hash baa0c17431e85eeede5e649f53162f70b4eb1e7c7a6f16a4ecaa3027b6531578
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:           lightsoff
Version:        50.0
Release:        1%{?dist}
Summary:        GNOME Lightsoff game
License:        GPL-2.0-or-later AND CC-BY-SA-3.0
URL:            https://wiki.gnome.org/Apps/Lightsoff
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  vala
# /oreon:deps
%description
A puzzle played on an 5X5 grid with the aim to turn off all the lights. Each
click on a tile toggles the state of the clicked tile and its non-diagonal
neighbors.

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

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.LightsOff.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
