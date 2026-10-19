%global source0_hash ba561cf3c96305a47179fa5605856ad695c9238ea07f7093aebd9ba80c4e323b
%{?mingw_package_header}
Name:           mingw-adwaita-icon-theme
Version:        51.0
Release:        1%{?dist}
Summary:        Adwaita icon theme for MingGW
License:        LGPL-3.0-or-later OR CC-BY-SA-3.0
URL:            http://www.gnome.org
Source0:        http://download.gnome.org/sources/adwaita-icon-theme/51/adwaita-icon-theme-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  /usr/bin/gtk-encode-symbolic-svg
BuildRequires:  intltool
BuildRequires:  librsvg2
BuildRequires:  meson
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
This package contains the Adwaita icon theme used by the GNOME desktop.
This is the MinGW version of this package.

%package -n mingw32-adwaita-icon-theme
Summary:        MinGW Adwaita icon theme for MingGW
Requires:       pkgconfig
%description -n mingw32-adwaita-icon-theme
This package contains the icons and pkgconfig file for applications that use
the Adwaita icon theme.

%package -n mingw64-adwaita-icon-theme
Summary:        MinGW Adwaita icon theme for MingGW
Requires:       pkgconfig
%description -n mingw64-adwaita-icon-theme
This package contains the icons and pkgconfig file for applications that use
the Adwaita icon theme.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir adwaita-icon-theme-%{version}
%oreon_prep
%build

%mingw_meson
%mingw_ninja
%install
%mingw_ninja_install
%oreon_autofiles mingw32-adwaita-icon-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-adwaita-icon-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-adwaita-icon-theme -f %{oreon_filedir}/mingw32-adwaita-icon-theme.list
%files -n mingw64-adwaita-icon-theme -f %{oreon_filedir}/mingw64-adwaita-icon-theme.list

%changelog

%autochangelog
