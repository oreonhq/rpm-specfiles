%global source0_hash 3fe3ed318c2a86d1417c5c29cf7494275e8fd4b537cd37453f5599c57365515c

%global qt_module qtcharts

#global unstable 0
%if 0%{?unstable}
%global prerelease rc
%endif

%global examples 1

Summary: Qt6 - Charts component
Name:    qt6-%{qt_module}
Version: 6.11.1
Release: 1%{?dist}

License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
%else
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel >= %{version}
BuildRequires: pkgconfig(xkbcommon)

%description
Qt Charts module provides a set of easy to use chart components. It uses the Qt Graphics View Framework, therefore charts can be easily
integrated to modern user interfaces. Qt Charts can be used as QWidgets, QGraphicsWidget, or QML types.
Users can easily create impressive graphs by selecting one of the charts themes.

%package devel
Summary: Development files for %{name}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.

%if 0%{?examples}
%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# BuildRequires: qt6-qtcharts-devel >= %%{version}
%description examples
%{summary}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1


%build
%cmake_qt6 \
    -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF} \
    -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF}

%cmake_build

%install
%cmake_install


%files
%license LICENSES/GPL*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
%{_qt6_libdir}/libQt6Charts.so.6*
%{_qt6_libdir}/libQt6ChartsQml.so.6*
%{_qt6_qmldir}/QtCharts/

%files devel
%{_qt6_headerdir}/QtCharts/
%{_qt6_headerdir}/QtChartsQml/
%{_qt6_libdir}/libQt6Charts.so
%{_qt6_libdir}/libQt6Charts.prl
%{_qt6_libdir}/libQt6ChartsQml.so
%{_qt6_libdir}/libQt6ChartsQml.prl
%dir %{_qt6_libdir}/cmake/Qt6Charts/
%{_qt6_libdir}/cmake/Qt6Charts/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6ChartsPrivate/
%{_qt6_libdir}/cmake/Qt6ChartsPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtChartsTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6qtchartsqml2*.cmake
%dir %{_qt6_libdir}/cmake/Qt6ChartsQml/
%{_qt6_libdir}/cmake/Qt6ChartsQml/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6ChartsQmlPrivate/
%{_qt6_libdir}/cmake/Qt6ChartsQmlPrivate/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/pkgconfig/*.pc

%if 0%{?examples}
%files examples
%{_qt6_examplesdir}/
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.11.1-1
- Import
