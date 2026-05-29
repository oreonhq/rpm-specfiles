%global source0_hash none

%global gtk4_version 4.12
%global libadwaita_version 1.5~beta
%global libgtop2_version 2.41.2

%global tarball_version %(echo %{version} | tr '~' '.')

Name:           gnome-system-monitor
Version:        50.0
Release:        1%{?dist}
Summary:        Process and resource monitor

License:        GPL-2.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/SystemMonitor
Source0: https://download.gnome.org/sources/gnome-system-monitor/50/gnome-system-monitor-%{tarball_version}.tar.xz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(catch2-with-main)
BuildRequires:  pkgconfig(giomm-2.68)
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(gtkmm-4.0)
BuildRequires:  pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:  pkgconfig(libgtop-2.0) >= %{libgtop2_version}
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool

Requires:       hicolor-icon-theme
Requires:       gtk4%{?_isa} >= %{gtk4_version}
Requires:       libadwaita%{?_isa} >= %{libadwaita_version}
Requires:       libgtop2%{?_isa} >= %{libgtop2_version}

%description
gnome-system-monitor allows to graphically view and manipulate the running
processes on your system. It also provides an overview of available resources
such as CPU and memory.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.SystemMonitor.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/gnome-system-monitor-kde.desktop

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/gnome-system-monitor
%{_datadir}/applications/org.gnome.SystemMonitor.desktop
%{_datadir}/applications/gnome-system-monitor-kde.desktop
%{_datadir}/dbus-1/services/org.gnome.SystemMonitor.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-system-monitor.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-system-monitor.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.SystemMonitor*.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.SystemMonitor-symbolic.svg
%{_datadir}/icons/hicolor/symbolic/apps/processes-symbolic.svg
%{_datadir}/icons/hicolor/symbolic/apps/resources-symbolic.svg
%{_metainfodir}/org.gnome.SystemMonitor.metainfo.xml
%{_datadir}/polkit-1/actions/org.gnome.gnome-system-monitor.policy

%{_libexecdir}/gnome-system-monitor/

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Import
