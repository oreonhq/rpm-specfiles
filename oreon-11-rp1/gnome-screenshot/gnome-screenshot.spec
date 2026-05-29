%global source0_hash none

%global tarball_version %(echo %{version} | tr '~' '.')

Name:           gnome-screenshot
Version:        41.0
Release:        13%{?dist}
Summary:        A screenshot utility for GNOME

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-screenshot
Source0: https://download.gnome.org/sources/gnome-screenshot/41/gnome-screenshot-%{tarball_version}.tar.xz
# Fix the build with meson 0.60
# https://gitlab.gnome.org/GNOME/gnome-screenshot/-/merge_requests/57
Patch0:         57.patch

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  /usr/bin/desktop-file-validate

%description
gnome-screenshot lets you take pictures of your screen.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n gnome-screenshot-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Screenshot.desktop


%files -f %{name}.lang
%license COPYING
%{_bindir}/gnome-screenshot
%{_datadir}/metainfo/org.gnome.Screenshot.metainfo.xml
%{_datadir}/applications/org.gnome.Screenshot.desktop
%{_datadir}/dbus-1/services/org.gnome.Screenshot.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-screenshot.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Screenshot.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Screenshot-symbolic.svg
%{_mandir}/man1/gnome-screenshot.1*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 41.0-13
- Prepare for Oreon 11 (RP1)
