%global source0_hash b65f32c44bd126cea5e1b5a6eb7cb0eb517277cb8de06675fa6be624b7da381a
Name:    kquickimageeditor
Version: 0.7.0.1
Release:        1%{?dist}
Summary:        QtQuick components providing basic image editing capabilities
License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:     https://invent.kde.org/libraries/%{name}
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(OpenCV)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
%{summary}

%package qt6
Summary: Qt6 QtQuick components providing basic image editing capabilities
%description qt6
%{summary}

%package qt6-devel
Summary: Development files for %{name}-qt6
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-devel
The %{name}-qt6-devel package contains cmake and mkspecs for developing
applications that use %{name}-qt6.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kquickimageeditor-qt6 -f %{oreon_filedir}/kquickimageeditor-qt6.list
%files -n kquickimageeditor-qt6-devel -f %{oreon_filedir}/kquickimageeditor-qt6-devel.list

%changelog

%autochangelog

