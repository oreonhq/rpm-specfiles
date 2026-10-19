%global source0_hash 37280cd3874c6f219012b219f9f2c83bd88d750bf25f05bc7f742f41018466f4
%global gtk3_version 3.24.15
%global glib2_version 2.73.2
%global gnome_desktop_version 2.91.2
%global libexif_version 0.6.14
%global libhandy_version 1.5.0
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
Name:    eog
Version: 50.3
Release:        1%{?dist}
Summary:        Eye of GNOME image viewer
License: GPL-2.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:     https://wiki.gnome.org/Apps/EyeOfGnome
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{version}.tar.xz
Patch0:  eog-lower-requires-libpeas-version.patch
%if 0%{?flatpak}
%endif
Requires:      gsettings-desktop-schemas
Requires:      glib2%{?_isa} >= %{glib2_version}
Requires:      gtk3%{?_isa} >= %{gtk3_version}
Requires:      libhandy%{?_isa} >= %{libhandy_version}
Provides:      bundled(libjpeg)
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(x11)
BuildRequires:  zlib-devel
# /oreon:deps
%description
The Eye of GNOME image viewer (eog) is the official image viewer for the
GNOME desktop. It can view single image files in a variety of formats, as
well as large image collections.

eog is extensible through a plugin system.

%package devel
Summary: Support for developing plugins for the eog image viewer
Requires: %{name}%{?_isa} = %{version}-%{release}
Recommends: gi-docgen-fonts
%description devel
The Eye of GNOME image viewer (eog) is the official image viewer for the
GNOME desktop. This package allows you to develop plugins that add new
functionality to eog.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson \
       -Dgtk_doc=true \
       -Dinstalled_tests=true \
    %if ! 0%{?flatpak}
       -Dlibportal=false
    %endif
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/org.gnome.eog.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.eog.desktop
%files -f %{oreon_filedir}/main.list
%files -n eog-devel -f %{oreon_filedir}/eog-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
