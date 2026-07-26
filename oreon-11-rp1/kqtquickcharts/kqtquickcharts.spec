%global source0_hash 6c590488698efca35d0db93b1b03264cc5da1e7c726d19f62272255a7469dc4b

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kqtquickcharts
Summary: A QtQuick plugin to render beautiful and interactive charts
Version: 25.12.3
Release: 1%{?dist}

# KDE e.V. may determine that future LGPL versions are accepted
License: LGPL-2.1-only
URL:     https://invent.kde.org/libraries/kqtquickcharts

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)

# header/cmake stuff included here -- rex
Provides: %{name}-devel = %{version}-%{release}
Provides: %{name}-devel%{?_isa} = %{version}-%{release}

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build

%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS
%license COPYING
%{_kf6_qmldir}/org/kde/charts/
# -devel type stuff, doesn't warrant a separate subpkg (yet)
%{_kf6_includedir}/kqtquickcharts_version.h
%dir %{_kf6_libdir}/cmake/
%dir %{_kf6_libdir}/cmake/KQtQuickCharts/
%{_kf6_libdir}/cmake/KQtQuickCharts/KQtQuickChartsConfigVersion.cmake
%{_kf6_libdir}/cmake/KQtQuickCharts/KQtQuickChartsConfig.cmake

%changelog
%autochangelog
