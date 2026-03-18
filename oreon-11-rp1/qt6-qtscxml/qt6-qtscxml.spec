
%global qt_module qtscxml

#global unstable 0
%if 0%{?unstable}
%global prerelease rc
%endif

%global examples 1

Summary: Qt6 - ScXml component
Name:    qt6-%{qt_module}
Version: 6.10.2
Release: 1%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
Source0: https://download.qt.io/development_releases/qt/%{majmin}/%{qt_version}/submodules/%{qt_module}-everywhere-src-%{qt_version}-%{prerelease}.tar.xz
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
BuildRequires: openssl-devel

%description
The Qt SCXML module provides functionality to create state machines from SCXML files.
This includes both dynamically creating state machines loading the SCXML file and instantiating states and transitions)
and generating a C++ file that has a class implementing the state machine.
It also contains functionality to support data models and executable content.

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
# BuildRequires: qt6-qtscxml-devel >= %{version}
%description examples
%{summary}.
%endif

%prep
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1


%build
%cmake_qt6 \
  -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF} \
  -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF}

%cmake_build

%install
%cmake_install


%files
%license LICENSES/*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
%{_qt6_libdir}/libQt6Scxml.so.6*
%{_qt6_libdir}/libQt6ScxmlQml.so.6*
%{_qt6_libdir}/libQt6StateMachineQml.so.6*
%{_qt6_libdir}/libQt6StateMachine.so.6*
%{_qt6_libexecdir}/qscxmlc
%{_qt6_qmldir}/QtScxml/
%{_qt6_qmldir}/QtQml/
%dir %{_qt6_plugindir}/scxmldatamodel
%{_qt6_plugindir}/scxmldatamodel/libqscxmlecmascriptdatamodel.so

%files devel
%{_qt6_headerdir}/QtScxml/
%{_qt6_headerdir}/QtScxmlGlobal/
%{_qt6_headerdir}/QtScxmlQml/
%{_qt6_headerdir}/QtStateMachineQml
%{_qt6_headerdir}/QtStateMachine/
%{_qt6_libdir}/libQt6Scxml.so
%{_qt6_libdir}/libQt6Scxml.prl
%{_qt6_libdir}/libQt6ScxmlQml.prl
%{_qt6_libdir}/libQt6ScxmlQml.so
%{_qt6_libdir}/libQt6StateMachine.prl
%{_qt6_libdir}/libQt6StateMachine.so
%{_qt6_libdir}/libQt6StateMachineQml.prl
%{_qt6_libdir}/libQt6StateMachineQml.so
%dir %{_qt6_libdir}/cmake/Qt6Scxml
%dir %{_qt6_libdir}/cmake/Qt6ScxmlGlobalPrivate
%dir %{_qt6_libdir}/cmake/Qt6ScxmlPrivate
%dir %{_qt6_libdir}/cmake/Qt6ScxmlQml
%dir %{_qt6_libdir}/cmake/Qt6ScxmlQmlPrivate
%dir %{_qt6_libdir}/cmake/Qt6ScxmlTools
%dir %{_qt6_libdir}/cmake/Qt6StateMachine
%dir %{_qt6_libdir}/cmake/Qt6StateMachinePrivate
%dir %{_qt6_libdir}/cmake/Qt6StateMachineQml/
%dir %{_qt6_libdir}/cmake/Qt6StateMachineQmlPrivate/
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtScxmlTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/cmake/Qt6Scxml/*.cmake
%{_qt6_libdir}/cmake/Qt6ScxmlGlobalPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6ScxmlPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6ScxmlQml/*.cmake
%{_qt6_libdir}/cmake/Qt6ScxmlQmlPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6ScxmlTools/*.cmake
%{_qt6_libdir}/cmake/Qt6StateMachine/*.cmake
%{_qt6_libdir}/cmake/Qt6StateMachinePrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6StateMachineQml/*.cmake
%{_qt6_libdir}/cmake/Qt6StateMachineQmlPrivate/*.cmake
%{_qt6_archdatadir}/mkspecs/features/qscxmlc.prf
%{_qt6_archdatadir}/mkspecs/modules/*
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/pkgconfig/*.pc

%if 0%{?examples}
%files examples
%{_qt6_examplesdir}/
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-1
- Prepare for Oreon 11 (RP1)
