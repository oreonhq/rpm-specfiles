%global source0_hash 771852c4e5fbeb3d7c3b2a9aacc13db9efe942a46e7d1454ec1f16092ec3ef9c
%global qt_module qtgrpc
%if 0%{?unstable}
%global prerelease rc
%endif
%global examples 1
Summary:        Qt6 - Support for using gRPC and Protobuf
Name:    qt6-%{qt_module}
Version: 6.12.0
Release:        1%{?dist}
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)
%if 0%{?unstable}
Source0:        https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-s%{prerelease}-%{version}.tar.xz
%else
%endif
%global __provides_exclude_from ^%{_qt6_plugindir}/.*\\.so$
%if 0%{?examples}
%endif
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(absl)
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(grpc++)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  zlib-static
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt6-qtgrpc-devel -f %{oreon_filedir}/qt6-qtgrpc-devel.list
%files -n qt6-qtgrpc-examples -f %{oreon_filedir}/qt6-qtgrpc-examples.list

%changelog

%autochangelog
