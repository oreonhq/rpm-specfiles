%global source0_hash none

%global qt_module qtserialbus

#global unstable 0
%if 0%{?unstable}
%global prerelease rc
%endif

%global examples 1

Summary: Qt6 - SerialBus component
Name:    qt6-%{qt_module}
Version: 6.11.1
Release: 1%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
%else
Source0:        https://download.qt.io/official_releases/qt/%{qt_version}/submodules/qtserialbus-everywhere-src-%{qt_version}.tar.xz
%endif

## upstreamable patches
# workaround FTBFS against kernel-header-5.2.0+
Patch100: qtserialbus-everywhere-src-5.12.3-SIOCGSTAMP.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-rpm-macros
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
#libQt6Core.so.6(Qt_5_PRIVATE_API)(64bit)
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtserialport-devel >= %{version}

BuildRequires: pkgconfig(xkbcommon) >= 0.5.0

%description
Qt Serial Bus (API) provides classes and functions to access the various
industrial serial buses and protocols, such as CAN, ModBus, and others.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.

%if 0%{?examples}
%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# BuildRequires: qt6-qtserialbus-devel >= %%{version}
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


%ldconfig_scriptlets

%files
%license LICENSES/*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
%{_qt6_libdir}/libQt6SerialBus.so.6*
%{_qt6_bindir}/canbusutil
%{_qt6_plugindir}/canbus

%files devel
%{_qt6_headerdir}/QtSerialBus/
%{_qt6_libdir}/libQt6SerialBus.so
%{_qt6_libdir}/libQt6SerialBus.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtSerialBusTestsConfig.cmake
%dir %{_qt6_libdir}/cmake/Qt6SerialBus/
%dir %{_qt6_libdir}/cmake/Qt6SerialBusPrivate/
%{_qt6_libdir}/cmake/Qt6SerialBus/*.cmake
%{_qt6_libdir}/cmake/Qt6SerialBusPrivate/*.cmake
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
