%global source0_hash none

%global qt_module qtgraphs

#global unstable 0
%if 0%{?unstable}
%global prerelease rc
%endif

%global examples 1
%ifarch aarch64
%global examples 0
%endif

# QML plugin .so is not a system library; avoid bogus provides
%global __provides_exclude_from ^%{_qt6_qmldir}/QtGraphs/.*\\.so$

Summary: Qt6 - Graphs (2D/3D visualization) module
Name:    qt6-%{qt_module}
Version: 6.10.3
Release: 1%{?dist}

License: BSD-3-Clause AND GFDL-1.3-no-invariants-only AND GPL-3.0-only
Url:     https://doc.qt.io/qt-6/qtgraphs-index.html
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
%else
Source0:        https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-rpm-macros
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel >= %{version}
BuildRequires: qt6-qtquick3d-devel >= %{version}
BuildRequires: pkgconfig(xkbcommon)

%description
The Qt Graphs module enables visualization of data in 2D and 3D. It builds on
Qt Quick and Qt Quick 3D.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qt6-qtdeclarative-devel%{?_isa}
Requires: qt6-qtquick3d-devel%{?_isa}
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
%if ! 0%{?examples}
rm -rf %{buildroot}%{_qt6_examplesdir}/graphs
%endif


%ldconfig_scriptlets

%files
%license LICENSES/*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
%{_qt6_libdir}/libQt6Graphs.so.6*
%{_qt6_libdir}/libQt6GraphsWidgets.so.6*
%{_qt6_qmldir}/QtGraphs/

%files devel
%{_qt6_headerdir}/QtGraphs/
%{_qt6_headerdir}/QtGraphsWidgets/
%{_qt6_libdir}/libQt6Graphs.so
%{_qt6_libdir}/libQt6GraphsWidgets.so
%{_qt6_libdir}/libQt6Graphs.prl
%{_qt6_libdir}/libQt6GraphsWidgets.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtGraphsTestsConfig.cmake
%dir %{_qt6_libdir}/cmake/Qt6Graphs/
%{_qt6_libdir}/cmake/Qt6Graphs/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6GraphsPrivate/
%{_qt6_libdir}/cmake/Qt6GraphsPrivate/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6GraphsWidgets/
%{_qt6_libdir}/cmake/Qt6GraphsWidgets/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6GraphsWidgetsPrivate/
%{_qt6_libdir}/cmake/Qt6GraphsWidgetsPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6Graphsplugin*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/pkgconfig/*.pc

%if 0%{?examples}
%files examples
%{_qt6_examplesdir}/
%endif


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-1
- Add qt6-qtgraphs (PySide6 / gcompris-qt)
