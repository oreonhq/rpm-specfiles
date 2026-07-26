%global source0_hash 84bad2825d39b8bf701ef644aab16b2dc7e72bb43e3f8702d23eec9613d29637

%global app_id  org.gnome.Nibbles
%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-nibbles
Version:        4.5.1
Release:        %autorelease
Summary:        GNOME Nibbles game
# Source code is under GPLv3+, help is under CC-BY-SA, Appdata is under CC0.
License:        GPL-3.0-or-later AND CC0-1.0 AND CC-BY-SA-3.0
URL:            https://wiki.gnome.org/Apps/Nibbles
Source0:        https://download.gnome.org/sources/gnome-nibbles/4.5/gnome-nibbles-%{tarball_version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0) >= 2.78.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.78.0
BuildRequires:  pkgconfig(gsound) >= 1.0.2
BuildRequires:  pkgconfig(gtk4) >= 4.13.4
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5.0

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

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml

%files -f %{name}.lang -f %{name}_libgnome-games-support.lang
%license COPYING
%doc NEWS
%{_bindir}/gnome-nibbles
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/dbus-1/services/%{app_id}.service
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/*/%{app_id}*
%{_metainfodir}/%{app_id}.metainfo.xml
%{_mandir}/man6/gnome-nibbles.6*

%changelog
%autochangelog
