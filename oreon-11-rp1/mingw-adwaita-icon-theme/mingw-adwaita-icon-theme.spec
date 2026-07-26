%global source0_hash 65166461d1b278aa942f59aa8d0fccf1108d71c65f372c6266e172449791755c

%{?mingw_package_header}

Name:           mingw-adwaita-icon-theme
Version:        49.0
Release:        2%{?dist}
Summary:        Adwaita icon theme for MingGW

License:        LGPL-3.0-or-later OR CC-BY-SA-3.0
URL:            http://www.gnome.org
Source0:        http://download.gnome.org/sources/adwaita-icon-theme/%(v=%{version}; echo ${v/.*/})/adwaita-icon-theme-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  intltool
BuildRequires:  librsvg2
BuildRequires:  /usr/bin/gtk-encode-symbolic-svg

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

%autosetup -p1 -n adwaita-icon-theme-%{version}

%build
%mingw_meson
%mingw_ninja

%install
%mingw_ninja_install

%files -n mingw32-adwaita-icon-theme
%license %{mingw32_datadir}/licenses/adwaita-icon-theme/COPYING
%license %{mingw32_datadir}/licenses/adwaita-icon-theme/COPYING_CCBYSA3
%license %{mingw32_datadir}/licenses/adwaita-icon-theme/COPYING_LGPL
%{mingw32_datadir}/pkgconfig/adwaita-icon-theme.pc
%dir %{mingw32_datadir}/icons/Adwaita
%{mingw32_datadir}/icons/Adwaita/16x16
%{mingw32_datadir}/icons/Adwaita/cursors
%{mingw32_datadir}/icons/Adwaita/scalable
%{mingw32_datadir}/icons/Adwaita/index.theme
%{mingw32_datadir}/icons/Adwaita/symbolic
%ghost %{mingw32_datadir}/icons/Adwaita/icon-theme.cache

%files -n mingw64-adwaita-icon-theme
%license %{mingw64_datadir}/licenses/adwaita-icon-theme/COPYING
%license %{mingw64_datadir}/licenses/adwaita-icon-theme/COPYING_CCBYSA3
%license %{mingw64_datadir}/licenses/adwaita-icon-theme/COPYING_LGPL
%{mingw64_datadir}/pkgconfig/adwaita-icon-theme.pc
%dir %{mingw64_datadir}/icons/Adwaita
%{mingw64_datadir}/icons/Adwaita/16x16
%{mingw64_datadir}/icons/Adwaita/cursors
%{mingw64_datadir}/icons/Adwaita/scalable
%{mingw64_datadir}/icons/Adwaita/index.theme
%{mingw64_datadir}/icons/Adwaita/symbolic
%ghost %{mingw64_datadir}/icons/Adwaita/icon-theme.cache

%changelog
%autochangelog
