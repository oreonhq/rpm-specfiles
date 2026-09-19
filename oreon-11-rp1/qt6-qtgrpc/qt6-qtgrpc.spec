%global source0_hash 7386bfc9c10c7920e5ff22dcf067e95f379bb379e4d916269f4465ab295ed136

%global qt_module qtgrpc

#global unstable 0
%if 0%{?unstable}
%global prerelease rc
%endif

%global examples 1

Summary: Qt6 - Support for using gRPC and Protobuf
Name:    qt6-%{qt_module}
Version: 6.10.2
Release: 1%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
Source0: https://download.qt.io/development_releases/qt/%{majmin}/%{qt_version}/submodules/%{qt_module}-everywhere-src-%{qt_version}-%{prerelease}.tar.xz
%else
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

# filter plugin provides
%global __provides_exclude_from ^%{_qt6_plugindir}/.*\\.so$

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtdeclarative-devel >= %{version}
%if 0%{?examples}
BuildRequires: cmake(absl)
%endif
BuildRequires: pkgconfig(grpc++)
BuildRequires: pkgconfig(libprotobuf-c)
BuildRequires: pkgconfig(protobuf)
BuildRequires: zlib-static

BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

%description
Protocol Buffers (Protobuf) is a cross-platform data format used to
serialize structured data. gRPC provides a remote procedure call
framework based on Protobuf. Qt provides tooling and classes to
use these technologies.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: pkgconfig(grpc++)
Requires: pkgconfig(protobuf)
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
%license LICENSES/GPL* LICENSES/LGPL*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
%{_qt6_libdir}/libQt6Grpc.so.6*
%{_qt6_libdir}/libQt6Protobuf.so.6*
%{_qt6_libdir}/libQt6ProtobufQtCoreTypes.so.6*
%{_qt6_libdir}/libQt6ProtobufQtGuiTypes.so.6*
%{_qt6_libdir}/libQt6ProtobufWellKnownTypes.so.6*
%{_qt6_libdir}/libQt6GrpcQuick.so.6*
%{_qt6_libdir}/libQt6ProtobufQuick.so.6*
%{_qt6_archdatadir}/qml/QtGrpc
%{_qt6_archdatadir}/qml/QtProtobuf

%files devel
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_headerdir}/QtGrpc/
%{_qt6_headerdir}/QtProtobuf/
%{_qt6_headerdir}/QtProtobufQtCoreTypes/
%{_qt6_headerdir}/QtProtobufQtGuiTypes/
%{_qt6_headerdir}/QtProtobufWellKnownTypes/
%{_qt6_headerdir}/QtGrpcQuick
%{_qt6_headerdir}/QtProtobufQuick
%{_qt6_libdir}/libQt6Grpc.so
%{_qt6_libdir}/libQt6Protobuf.so
%{_qt6_libdir}/libQt6ProtobufQtCoreTypes.so
%{_qt6_libdir}/libQt6ProtobufQtGuiTypes.so
%{_qt6_libdir}/libQt6ProtobufWellKnownTypes.so
%{_qt6_libdir}/libQt6Grpc.prl
%{_qt6_libdir}/libQt6Protobuf.prl
%{_qt6_libdir}/libQt6ProtobufWellKnownTypes.prl
%{_qt6_libdir}/libQt6ProtobufQtCoreTypes.prl
%{_qt6_libdir}/libQt6ProtobufQtGuiTypes.prl
%{_qt6_libdir}/libQt6GrpcQuick.so
%{_qt6_libdir}/libQt6GrpcQuick.prl
%{_qt6_libdir}/libQt6ProtobufQuick.so
%{_qt6_libdir}/libQt6ProtobufQuick.prl
%dir %{_qt6_libdir}/cmake/Qt6Grpc/
%dir %{_qt6_libdir}/cmake/Qt6GrpcPrivate
%dir %{_qt6_libdir}/cmake/Qt6GrpcQuick
%dir %{_qt6_libdir}/cmake/Qt6GrpcQuickPrivate
%dir %{_qt6_libdir}/cmake/Qt6GrpcTools/
%dir %{_qt6_libdir}/cmake/Qt6Protobuf/
%dir %{_qt6_libdir}/cmake/Qt6ProtobufPrivate
%dir %{_qt6_libdir}/cmake/Qt6ProtobufQtCoreTypes/
%dir %{_qt6_libdir}/cmake/Qt6ProtobufQtCoreTypesPrivate
%dir %{_qt6_libdir}/cmake/Qt6ProtobufQtGuiTypes/
%dir %{_qt6_libdir}/cmake/Qt6ProtobufQtGuiTypesPrivate
%dir %{_qt6_libdir}/cmake/Qt6ProtobufQuick
%dir %{_qt6_libdir}/cmake/Qt6ProtobufQuickPrivate
%dir %{_qt6_libdir}/cmake/Qt6ProtobufTools/
%dir %{_qt6_libdir}/cmake/Qt6ProtobufWellKnownTypes/
%dir %{_qt6_libdir}/cmake/Qt6ProtobufWellKnownTypesPrivate
%dir %{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtGrpcTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Grpc/*.cmake
%{_qt6_libdir}/cmake/Qt6GrpcPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6GrpcQuick/*.cmake
%{_qt6_libdir}/cmake/Qt6GrpcQuickPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6GrpcTools/*.cmake
%{_qt6_libdir}/cmake/Qt6Protobuf/*.cmake*
%{_qt6_libdir}/cmake/Qt6ProtobufPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6ProtobufQtCoreTypes/*.cmake
%{_qt6_libdir}/cmake/Qt6ProtobufQtCoreTypesPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6ProtobufQtGuiTypes/*.cmake
%{_qt6_libdir}/cmake/Qt6ProtobufQtGuiTypesPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6ProtobufQuick/*.cmake
%{_qt6_libdir}/cmake/Qt6ProtobufQuickPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6ProtobufTools/*.cmake
%{_qt6_libdir}/cmake/Qt6ProtobufWellKnownTypes/*.cmake
%{_qt6_libdir}/cmake/Qt6ProtobufWellKnownTypesPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/pkgconfig/*.pc
%{_qt6_libexecdir}/qtgrpcgen
%{_qt6_libexecdir}/qtprotobufgen

%if 0%{?examples}
%files examples
%{_qt6_examplesdir}/
%endif

%changelog
%autochangelog
