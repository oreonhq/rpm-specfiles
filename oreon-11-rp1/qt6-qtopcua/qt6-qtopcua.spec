%global source0_hash 375b1b13c28753a14f7c6360fd6dc5790f63ec34a37355694618530268ec2c2a

%global qt_module qtopcua

#global unstable 0
%if 0%{?unstable}
%global tar_prerelease rc1
%global prerelease rc
%endif

%global examples 1

Summary: Qt6 - OPC UA component
Name:    qt6-%{qt_module}
Version: 6.10.2
Release: 1%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
Source0: https://github.com/qt/%{qt_module}/archive/refs/tags/v%{qt_version}-%{tar_prerelease}/%{qt_module}-%{qt_version}-%{tar_prerelease}.tar.gz
%else
Source0: https://github.com/qt/%{qt_module}/archive/refs/tags/v%{version}/%{qt_module}-%{version}.tar.gz
%endif

## upstreamable patches

BuildRequires: cmake
BuildRequires: gcc-c++	
BuildRequires: ninja-build
BuildRequires: qt6-rpm-macros
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
#libQt6Core.so.6(Qt_6_PRIVATE_API)(64bit)
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel >= %{version}
BuildRequires: openssl-devel
BuildRequires: mbedtls-devel
#BuildRequires: open62541-devel

%description
Qt OPC UA (API) provides classes and functions to access the OPC UA protocol

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%if 0%{?examples}
%package examples
Summary: Programming examples for %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description examples
%{summary}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{qt_module}-%{qt_version}%{?unstable:-%{tar_prerelease}} -p1

%build
%cmake_qt6 \
        -DQT_BUILD_EXAMPLES=%{?examples:ON}%{!?examples:OFF} \
        -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF}

%cmake_build

%install
%cmake_install

%files
%license LICENSES/*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
%{_qt6_bindir}/qopcuaxmldatatypes2cpp
%{_qt6_libdir}/libQt6OpcUa.so.*
%{_qt6_plugindir}/opcua/libopen62541_backend.so
%{_qt6_libdir}/libQt6DeclarativeOpcua.so.*
%{_qt6_qmldir}/QtOpcUa/*

%files devel
%{_qt6_headerdir}/QtOpcUa/
%{_qt6_headerdir}/QtDeclarativeOpcua/
%{_qt6_libdir}/libQt6OpcUa.so
%{_qt6_libdir}/libQt6OpcUa.prl
%{_qt6_libdir}/libQt6DeclarativeOpcua.so
%{_qt6_libdir}/libQt6DeclarativeOpcua.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtOpcUaTestsConfig.cmake
%dir %{_qt6_libdir}/cmake/Qt6OpcUa/
%dir %{_qt6_libdir}/cmake/Qt6DeclarativeOpcua/
%dir %{_qt6_libdir}/cmake/Qt6DeclarativeOpcuaPrivate/
%dir %{_qt6_libdir}/cmake/Qt6OpcUaPrivate
%dir %{_qt6_libdir}/cmake/Qt6OpcUaTools
%{_qt6_libdir}/cmake/Qt6OpcUa/*.cmake
%{_qt6_libdir}/cmake/Qt6DeclarativeOpcua/*.cmake
%{_qt6_libdir}/cmake/Qt6DeclarativeOpcuaPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6OpcUaPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6OpcUaTools/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/pkgconfig/*.pc

%if 0%{?examples}
%files examples
%{_qt6_examplesdir}/
%endif

%changelog
%autochangelog
