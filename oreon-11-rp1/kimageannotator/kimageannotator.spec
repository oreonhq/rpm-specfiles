%undefine __cmake_in_source_build

Name:           kimageannotator
Version:        0.7.2
Release:        1%{?dist}
Summary:        Image annotation widget library for Qt (ksnip)
License:        LGPL-3.0-or-later
URL:            https://github.com/ksnip/kImageAnnotator

Source0:        https://github.com/ksnip/kImageAnnotator/archive/refs/tags/v%{version}.tar.gz#/kImageAnnotator-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  libX11-devel
BuildRequires:  kcolorpicker-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
kImageAnnotator provides a Qt widget for drawing arrows, text, blur, and
similar annotations on images. Used by Gwenview, ksnip, and other apps.

%package libs
Summary:        Qt6 kImageAnnotator shared library

%description libs
Shared library and translation files for kImageAnnotator.

%package devel
Summary:        Development files for kimageannotator
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Widgets)
Requires:       cmake(Qt6Svg)
Requires:       kcolorpicker-devel

%description devel
Headers and CMake package kImageAnnotator-Qt6 for downstream builds.

%prep
%autosetup -p1 -n kImageAnnotator-%{version}

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_WITH_QT6=ON \
  -DBUILD_EXAMPLE=OFF \
  -DBUILD_TESTS=OFF
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets libs

%files
%license LICENSE
%doc README.md CHANGELOG.md

%files libs
%{_libdir}/libkImageAnnotator.so.0*
%{_datadir}/kImageAnnotator/translations/*.qm

%files devel
%{_includedir}/kImageAnnotator-Qt6/
%{_libdir}/libkImageAnnotator.so
%{_libdir}/cmake/kImageAnnotator-Qt6/

%changelog
* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.2-1
- Add kImageAnnotator Qt6 (cmake kImageAnnotator-Qt6 for Gwenview)
