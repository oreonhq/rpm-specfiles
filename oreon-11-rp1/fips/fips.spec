%global source0_hash 7042a0bb7d5d3b9578fdb6a2699b2a0bac5a76df6f967c433f196533bf75f30e
Name:           fips
Version:        3.5.0
Release:        1%{?dist}
Summary:        OpenGL-based FITS image viewer
License:        LGPL-3.0-or-later
Url:            https://github.com/matwey/fips3
Source0:        https://github.com/matwey/fips3/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
FIPS is a cross-platform FITS viewer with responsive user interface. Unlike
other FITS viewers FIPS uses GPU hardware via OpenGL to provide usual
functionality such as zooming, panning and level adjustments. OpenGL 2.1 and
later is supported.

FIPS supports all 2D image formats (except for floating point formats on OpenGL
2.1). FITS image extension has basic limited support.
FITS image extension has basic limited support.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n fips3-%{version}

%build

%cmake
%cmake_build
%install
%cmake_install
desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/space.fips.Fips.desktop
%oreon_autofiles main

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
