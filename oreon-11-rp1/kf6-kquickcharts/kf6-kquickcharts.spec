%global		framework kquickcharts
%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:		kf6-%{framework}
Summary:	A QtQuick module providing high-performance charts
Version:	6.24.0
Release:	2%{?dist}

License:	BSD-2-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}

Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6ShaderTools)
BuildRequires:	make
BuildRequires:	pkgconfig(xkbcommon)

%description
The Quick Charts module provides a set of charts that can be used from QtQuick
applications. They are intended to be used for both simple display of data as
well as continuous display of high-volume data (often referred to as plotters).
The charts use a system called distance fields for their accelerated rendering,
which provides ways of using the GPU for rendering 2D shapes without loss of
quality.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf6 \
    -DQDOC_BIN=/bin/true
%cmake_build_kf6

%install
%cmake_install_kf6

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_qmldir}/org/kde/quickcharts/
%{_libdir}/libQuickCharts.so.*
%{_libdir}/libQuickChartsControls.so*

%files devel
%{_kf6_libdir}/cmake/KF6QuickCharts/
%{_libdir}/libQuickCharts.so
%{_libdir}/libQuickChartsControls.so

%changelog
* Fri Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Pass -DQDOC_BIN=/bin/true to work around qdoc segfault until kf6-rpm-macros is deployed

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)
