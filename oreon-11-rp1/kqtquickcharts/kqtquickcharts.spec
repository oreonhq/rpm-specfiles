%global stable_kf6 stable
%global source0_hash 6c590488698efca35d0db93b1b03264cc5da1e7c726d19f62272255a7469dc4b
ExcludeArch: %{ix86}
Name:    kqtquickcharts
Summary:        A QtQuick plugin to render beautiful and interactive charts
Version: 25.12.3
Release:        1%{?dist}
License: LGPL-2.1-only
URL:     https://invent.kde.org/libraries/kqtquickcharts
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Provides: %{name}-devel = %{version}-%{release}
Provides: %{name}-devel%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
