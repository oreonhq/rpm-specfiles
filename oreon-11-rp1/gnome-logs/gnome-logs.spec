%global source0_hash none

%global tarball_version %(echo %{version} | tr '~' '.')

Name:           gnome-logs
Version:        50.0
Release:        1%{?dist}
Summary:        Log viewer for the systemd journal

# data/org.gnome.Logs.metainfo.xml.in is CC0-1.0
# data/icons/scalable/org.gnome.Logs.svg is CC-BY-3.0
License:        GPL-3.0-or-later AND CC0-1.0 AND CC-BY-3.0
URL:            https://wiki.gnome.org/Apps/Logs
Source0: https://download.gnome.org/sources/gnome-logs/50/gnome-logs-%{tarball_version}.tar.xz
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
BuildRequires:  /usr/bin/appstream-util
Requires:       gsettings-desktop-schemas

%description
A log viewer for the systemd journal.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson -Dman=true
%meson_build


%install
%meson_install
%find_lang %{name} --with-gnome


%check
%meson_test


%files -f %{name}.lang
%doc AUTHORS README NEWS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Logs.desktop
%{_datadir}/dbus-1/services/org.gnome.Logs.service
%{_datadir}/glib-2.0/schemas/org.gnome.Logs.*.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Logs.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Logs-symbolic.svg
%{_datadir}/metainfo/org.gnome.Logs.metainfo.xml
%{_mandir}/man1/gnome-logs.1*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
