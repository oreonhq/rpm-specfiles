%global source0_hash 84bad2825d39b8bf701ef644aab16b2dc7e72bb43e3f8702d23eec9613d29637
%global app_id  org.gnome.Nibbles
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:           gnome-nibbles
Version:        4.6.0
Release:        1%{?dist}
Summary:        GNOME Nibbles game
License:        GPL-3.0-or-later AND CC0-1.0 AND CC-BY-SA-3.0
URL:            https://wiki.gnome.org/Apps/Nibbles
Source0:        https://download.gnome.org/sources/%{name}/4.5/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  vala
# /oreon:deps
%description
Pilot a worm around a maze trying to collect diamonds and at the same time
avoiding the walls and yourself. With each diamond your worm grows longer and
navigation becomes more and more difficult. Playable by up to four people.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%find_lang %{name}_libgnome-games-support --with-gnome
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
