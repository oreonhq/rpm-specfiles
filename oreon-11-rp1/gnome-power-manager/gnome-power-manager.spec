%global source0_hash bf243d6389f8bfa71c958534ed2669b29965c47f55c3cbe4983b296d0f99e5d7
Name:           gnome-power-manager
Version:        50.0
Release:        1%{?dist}
Summary:        GNOME power management service
License:        GPL-2.0-or-later
URL:            https://projects.gnome.org/gnome-power-manager/
Source0:        https://download.gnome.org/sources/gnome-power-manager/50/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(upower-glib)
# /oreon:deps
%description
GNOME Power Manager uses the information and facilities provided by UPower
displaying icons and handling user callbacks in an interactive GNOME session.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.PowerStats.desktop
appstream-util --nonet validate-relax %{buildroot}%{_datadir}/metainfo/org.gnome.PowerStats.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
