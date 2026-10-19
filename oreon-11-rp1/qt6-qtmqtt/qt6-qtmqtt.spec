%global source0_hash 55b2ac2938c6057aebd1df5366860d277ebda445f960111fba0998fedeced700
%global qt_module qtmqtt
%if 0%{?unstable}
%global tar_prerelease rc1
%global prerelease rc
%endif
%global examples 1
Summary:        Qt6 - Mqtt module
Name:    qt6-%{qt_module}
Version: 6.12.0
Release:        1%{?dist}
License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)
%if 0%{?unstable}
Source0:        https://github.com/qt/%{qt_module}/a%{prerelease}hive/refs/tags/v%{version}/%{qt_module}-%{version}.tar.gz
%else
%endif
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-rpm-macros
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt6-qtmqtt-devel -f %{oreon_filedir}/qt6-qtmqtt-devel.list
%files -n qt6-qtmqtt-examples -f %{oreon_filedir}/qt6-qtmqtt-examples.list

%changelog

%autochangelog
