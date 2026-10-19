%global source0_hash 8ddb23147e4677c759d36a65ae50f6b0d0d79fa8590ac89576b91f572918b481
%global qt_module qtquick3dphysics
%if 0%{?unstable}
%global prerelease rc
%endif
%global examples 1
Summary:        Qt6 - Quick3D Physics Libraries and utilities
Name:    qt6-%{qt_module}
Version: 6.12.0
Release:        1%{?dist}
License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)
%if 0%{?unstable}
Source0:        https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-s%{prerelease}-%{version}.tar.xz
%else
%endif
ExclusiveArch: aarch64 i686 x86_64
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtquick3d-devel
BuildRequires:  qt6-qtshadertools-devel
BuildRequires:  qt6-rpm-macros
# /oreon:deps
%description
The Qt 6 Quick3D Physics library.

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
  -DQT_BUILD_EXAMPLES=%{?examples:ON}%{!?examples:OFF} \
  -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF}
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt6-qtquick3dphysics-devel -f %{oreon_filedir}/qt6-qtquick3dphysics-devel.list
%files -n qt6-qtquick3dphysics-examples -f %{oreon_filedir}/qt6-qtquick3dphysics-examples.list

%changelog

%autochangelog
