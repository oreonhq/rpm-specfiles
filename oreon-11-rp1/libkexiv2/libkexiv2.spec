%undefine __cmake_in_source_build

Name:           libkexiv2
Version:        25.12.3
Release:        5%{?dist}
Summary:        KDE wrapper around Exiv2 (Qt 6)
License:        GPL-2.0-or-later
URL:            https://invent.kde.org/graphics/libkexiv2
Source0:        https://download.kde.org/stable/release-service/%{version}/src/libkexiv2-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  qt6-qtbase-devel

Requires:       libkexiv2-qt6%{?_isa} = %{version}-%{release}

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
%autosetup -n libkexiv2-%{version} -p1


%build
%cmake_kf6 \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_TESTING=OFF \
  -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%{_datadir}/qlogging-categories6/libkexiv2.categories

%files -n libkexiv2-qt6
# Installed file uses lib KExiv2 version in the name (e.g. .so.5.1.0); SONAME is still .so.0
%{_libdir}/libKExiv2Qt6.so.*

%files -n libkexiv2-qt6-devel
%{_includedir}/KExiv2Qt6
%{_libdir}/libKExiv2Qt6.so
%{_libdir}/cmake/KExiv2Qt6


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-2
- Add libkexiv2 Qt 6 from KDE release service
