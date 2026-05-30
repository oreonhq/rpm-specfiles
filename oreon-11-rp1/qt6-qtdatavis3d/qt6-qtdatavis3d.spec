%global source0_hash 1e1a7b9c0a947731655334f5d79252d40cdaf58c1801074ea5e9e0821d6693ac

%global qt_module qtdatavis3d

#global unstable 0
%if 0%{?unstable}
%global prerelease rc
%endif

%global examples 1

Summary: Qt6 - Qt Data Visualization component
Name:    qt6-%{qt_module}
Version: 6.11.1
Release: 1%{?dist}

License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
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
Qt Data Visualization module provides multiple graph types to visualize data in
3D space both with C++ and Qt Quick 2.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qt6-qtdeclarative-devel%{?_isa}
%description devel
%{summary}.

%if 0%{?examples}
%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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
%{_qt6_archdatadir}/sbom/qtdatavisualization-%{qt_version}.spdx
%{_qt6_libdir}/libQt6DataVisualization.so.6*
%{_qt6_libdir}/libQt6DataVisualizationQml.so.6*
%{_qt6_qmldir}/QtDataVisualization/

%files devel
%dir %{_qt6_libdir}/cmake/Qt6DataVisualization
%dir %{_qt6_libdir}/cmake/Qt6DataVisualizationPrivate
%dir %{_qt6_libdir}/cmake/Qt6DataVisualizationQml
%dir %{_qt6_libdir}/cmake/Qt6DataVisualizationQmlPrivate
%{_qt6_headerdir}/QtDataVisualization/
%{_qt6_headerdir}/QtDataVisualizationQml/
%{_qt6_libdir}/libQt6DataVisualization.so
%{_qt6_libdir}/libQt6DataVisualization.prl
%{_qt6_libdir}/libQt6DataVisualizationQml.prl
%{_qt6_libdir}/libQt6DataVisualizationQml.so
%{_qt6_libdir}/cmake/Qt6DataVisualization/*.cmake
%{_qt6_libdir}/cmake/Qt6DataVisualizationPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6DataVisualizationQml/*.cmake
%{_qt6_libdir}/cmake/Qt6DataVisualizationQmlPrivate/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtDataVisualizationTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/pkgconfig/*.pc

%if 0%{?examples}
%files examples
%{_qt6_examplesdir}/
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.11.1-1
- Import
