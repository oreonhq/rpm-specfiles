%global source0_hash 97e855b04abe4ad65845309626f265536b450b10d58c64f9c26f9e419ef20ece
Name:    aisleriot
Epoch:   1
Version: 3.22.35
Release:        1%{?dist}
Summary:        A collection of card games
License: GPL-3.0-or-later AND LGPL-3.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://wiki.gnome.org/Apps/Aisleriot
Source0:        https://gitlab.gnome.org/GNOME/${name}/-/archive/%{version}/%{name}-%{version}.tar.xz
Patch0:  aisleriot-3.22.19-appdata-namespace.patch
# oreon:deps
BuildRequires:  appdata-tools
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(guile-3.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  yelp-tools
# /oreon:deps
%description
Aisleriot is a collection of over 80 card games programmed in scheme.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
       -Dtheme_kde=false
%meson_build
%install
%meson_install
appstream-util replace-screenshots %{buildroot}%{_datadir}/metainfo/sol.metainfo.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/sol/a.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/sol/b.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/sol/c.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/sol/d.png 
rm %{buildroot}%{_libdir}/valgrind/aisleriot.supp
%find_lang %{name} --with-gnome
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/sol.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
