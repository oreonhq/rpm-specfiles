%global source0_hash 18c4e968785447051d94b01f8e3c975e31ddc46065c0777443cecc50753a4d8c
%global qt_module qtgraphs
%if 0%{?unstable}
%global prerelease rc
%endif
%global examples 1
%ifarch aarch64
%global examples 0
%endif
%global __provides_exclude_from ^%{_qt6_qmldir}/QtGraphs/.*\\.so$
Summary:        Qt6 - Graphs (2D/3D visualization) module
Name:    qt6-%{qt_module}
Version: 6.12.0
Release:        1%{?dist}
License: BSD-3-Clause AND GFDL-1.3-no-invariants-only AND GPL-3.0-only
Url:     https://doc.qt.io/qt-6/qtgraphs-index.html
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)
%if 0%{?unstable}
%else
Source0:        https://download.qt.io/a%{prerelease}hive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-s%{prerelease}-%{version}.tar.xz
%endif
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtquick3d-devel
BuildRequires:  qt6-rpm-macros
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt6-qtgraphs-devel -f %{oreon_filedir}/qt6-qtgraphs-devel.list
%files -n qt6-qtgraphs-examples -f %{oreon_filedir}/qt6-qtgraphs-examples.list

%changelog

%autochangelog
