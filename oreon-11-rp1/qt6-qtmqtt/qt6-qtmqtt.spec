%global source0_hash 884925fc6fa116f0cc4f1db80335daaf249ada5fbba30186536ed6329dc6032a

%global qt_module qtmqtt

#global unstable 0
%if 0%{?unstable}
%global tar_prerelease rc1
%global prerelease rc
%endif

%global examples 1

Summary: Qt6 - Mqtt module
Name:    qt6-%{qt_module}
Version: 6.10.2
Release: 1%{?dist}

License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
Source0: https://github.com/qt/%{qt_module}/archive/refs/tags/v%{qt_version-%{tar_prerelease}}/%{qt_module}-%{qt_version}-%{tar_prerelease}.tar.gz
%else
Source0: https://github.com/qt/%{qt_module}/archive/refs/tags/v%{version}/%{qt_module}-%{version}.tar.gz
%endif

BuildRequires:  cmake >= 3.16
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-rpm-macros
BuildRequires:  qt6-qtbase-private-devel
#libQt6Core.so.6(Qt_6_PRIVATE_API)(64bit)
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

%description
MQTT is a machine-to-machine (M2M) protocol utilizing the publish-and-subscribe
paradigm, and provides a channel with minimal communication overhead.
The Qt MQTT module provides a standard compliant implementation of the MQTT 
protocol specification. It enables applications to act as telemetry displays 
and devices to publish telemetry data.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}

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
%{_qt6_libdir}/libQt6Mqtt.so.6*

%files devel
%{_qt6_libdir}/libQt6Mqtt.prl
%{_qt6_libdir}/libQt6Mqtt.so
%{_qt6_libdir}/pkgconfig/Qt6Mqtt.pc
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_headerdir}/QtMqtt/*
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%dir %{_qt6_libdir}/cmake/Qt6Mqtt/
%dir %{_qt6_libdir}/cmake/Qt6MqttPrivate/
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtMqttTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Mqtt/*.cmake
%{_qt6_libdir}/cmake/Qt6MqttPrivate/*.cmake

%dir %{_qt6_headerdir}/QtMqtt

%files examples
%{_qt6_examplesdir}

%changelog
%autochangelog
