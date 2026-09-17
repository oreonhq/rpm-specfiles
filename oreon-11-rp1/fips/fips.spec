%global source0_hash 74eacb0eb944db6d32f3e97ba9243e76fda3a99539a911ac1ee6fae8393bb0c6

Name:           fips
Version:        3.4.0
Release:        22%{?dist}
Summary:        OpenGL-based FITS image viewer
License:        LGPL-3.0-or-later
Url:            https://github.com/matwey/fips3
Source:         https://github.com/matwey/fips3/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.0
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel >= 5.6
Requires:       hicolor-icon-theme

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

%check
%ctest

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/space.fips.Fips.desktop
%{_datadir}/metainfo/space.fips.Fips.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/space.fips.Fips.*

%changelog
%autochangelog
