%global source0_hash bf243d6389f8bfa71c958534ed2669b29965c47f55c3cbe4983b296d0f99e5d7

Name:           gnome-power-manager
Version:        50.0
Release:        1%{?dist}
Summary:        GNOME power management service

License:        GPL-2.0-or-later
URL:            https://projects.gnome.org/gnome-power-manager/
Source0:        https://download.gnome.org/sources/gnome-power-manager/50/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  docbook-utils
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
GNOME Power Manager uses the information and facilities provided by UPower
displaying icons and handling user callbacks in an interactive GNOME session.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.PowerStats.desktop
appstream-util --nonet validate-relax %{buildroot}%{_datadir}/metainfo/org.gnome.PowerStats.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.md
%{_bindir}/gnome-power-statistics
%{_datadir}/applications/org.gnome.PowerStats.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.power-manager.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.PowerStats*.*
%{_datadir}/metainfo/org.gnome.PowerStats.appdata.xml
%{_mandir}/man1/gnome-power-statistics.1*

%changelog
%autochangelog
