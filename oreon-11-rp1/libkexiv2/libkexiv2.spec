%global source0_hash 8ed6de46cdd084a834dd0f2049d6490977a8eedc50a2e59f715fb1cecf6653ec
%global stable_kf6 stable
%undefine __cmake_in_source_build
Name:           libkexiv2
Version:        25.12.3
Release:        5%{?dist}
Summary:        KDE wrapper around Exiv2 (Qt 6)
License:        GPL-2.0-or-later
URL:            https://invent.kde.org/graphics/libkexiv2
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Requires:       libkexiv2-qt6%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
Library for reading and writing image metadata (EXIF, IPTC, XMP) using Exiv2
with a Qt 6 API.

%package -n libkexiv2-qt6
Summary:        libkexiv2 Qt 6 shared library
%description -n libkexiv2-qt6
%{summary}.

%package -n libkexiv2-qt6-devel
Summary:        Development files for libkexiv2 Qt 6
Requires:       libkexiv2-qt6%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(exiv2)
%description -n libkexiv2-qt6-devel
Headers and CMake files for libkexiv2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libkexiv2-%{version}
%oreon_prep
%build

%cmake_kf6 \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_TESTING=OFF \
  -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles libkexiv2-qt6 usr/*/lib*.so.*
%oreon_autofiles libkexiv2-qt6-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libkexiv2-qt6 -f %{oreon_filedir}/libkexiv2-qt6.list
%files -n libkexiv2-qt6-devel -f %{oreon_filedir}/libkexiv2-qt6-devel.list

%changelog

* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-2
- Add libkexiv2 Qt 6 from KDE release service
