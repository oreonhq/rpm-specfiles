%global source0_hash db0e50a80aa3bf64bb45cbca5cf9f75efd9348cf2ac690b907435238c3cf81d7

%{?mingw_package_header}

Name:           mingw-hicolor-icon-theme
Version:        0.18
Release:        3%{?dist}
Summary:        Basic requirement for icon themes in MingGW

License:        GPL-2.0-or-later
URL:            http://icon-theme.freedesktop.org/releases/
Source0:        http://icon-theme.freedesktop.org/releases/hicolor-icon-theme-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  meson

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem

%description
Contains the basic directories and files needed for icon theme support.
This is the MinGW version of this package.

%package -n mingw32-hicolor-icon-theme
Summary:        MinGW hicolor icon theme for MingGW

%description -n mingw32-hicolor-icon-theme
Contains the basic directories and files needed for icon theme support.
This is the MinGW version of this package.

%package -n mingw64-hicolor-icon-theme
Summary:        MinGW hicolor icon theme for MingGW

%description -n mingw64-hicolor-icon-theme
Contains the basic directories and files needed for icon theme support.
This is the MinGW version of this package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n hicolor-icon-theme-%{version}
# for some reason this file is executable in the tarball
chmod 0644 COPYING

%build
%mingw_meson
%mingw_ninja

%install
%mingw_ninja_install

touch %{buildroot}%{mingw32_datadir}/icons/hicolor/icon-theme.cache
touch %{buildroot}%{mingw64_datadir}/icons/hicolor/icon-theme.cache

%files -n mingw32-hicolor-icon-theme
%license COPYING
%doc README.md
%{mingw32_datadir}/icons/hicolor
%ghost %{mingw32_datadir}/icons/hicolor/icon-theme.cache
%{mingw32_datadir}/pkgconfig/default-icon-theme.pc

%files -n mingw64-hicolor-icon-theme
%license COPYING
%doc README.md
%{mingw64_datadir}/icons/hicolor
%ghost %{mingw64_datadir}/icons/hicolor/icon-theme.cache
%{mingw64_datadir}/pkgconfig/default-icon-theme.pc

%changelog
%autochangelog
