%global source0_hash 91637845649f3ca709d29f71ee775b946d1112087209f32264e8fad21a0ca0e2

Name:           gnome-klotski
Version:        3.38.2
Release:        15%{?dist}
Summary:        GNOME Klotski game

# Automatically converted from old format: GPLv2+ and CC-BY-SA - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            https://wiki.gnome.org/Apps/Klotski
Source0:        https://download.gnome.org/sources/%{name}/3.38/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgnome-games-support-1)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  vala

%description
A series of sliding block puzzles. Try and solve them in the least number of
moves.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%license COPYING
%{_bindir}/gnome-klotski
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.gnome.Klotski.service
%{_datadir}/glib-2.0/schemas/org.gnome.Klotski.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Klotski.*
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Klotski-symbolic.svg
%{_datadir}/metainfo/org.gnome.Klotski.appdata.xml
%{_mandir}/man6/gnome-klotski.6*

%changelog
%autochangelog
