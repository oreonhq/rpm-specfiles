%global source0_hash 8887b03427230ac0816d4b0c801ce6628ad1fc9139ed3072914e9faa881ba868
%global gtk4_version 4.12
%global libadwaita_version 1.5~beta
%global libgtop2_version 2.41.2
%global tarball_version %(echo %{version} | tr '~' '.')
Name:           gnome-system-monitor
Version:        51.0
Release:        1%{?dist}
Summary:        Process and resource monitor
License:        GPL-2.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/SystemMonitor
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
Requires:       hicolor-icon-theme
Requires:       gtk4%{?_isa} >= %{gtk4_version}
Requires:       libadwaita%{?_isa} >= %{libadwaita_version}
Requires:       libgtop2%{?_isa} >= %{libgtop2_version}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(catch2-with-main)
BuildRequires:  pkgconfig(giomm-2.68)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtkmm-4.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxml-2.0)
# /oreon:deps
%description
gnome-system-monitor allows to graphically view and manipulate the running
processes on your system. It also provides an overview of available resources
such as CPU and memory.

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

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.SystemMonitor.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/gnome-system-monitor-kde.desktop
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Import
