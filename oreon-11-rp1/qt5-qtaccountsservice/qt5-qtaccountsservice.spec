%global source0_hash 39f9494489e63579596f430ef04575a4a0f0c8f9c75bf1d46f44fa2dc203ef12
%global qt_module qtaccountsservice
Name:           qt5-%{qt_module}
Summary:        Qt5 - AccountService addon
Version:        0.6.0
Release:        1%{?dist}
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/hawaii-desktop/qtaccountsservice
Source0:        https://github.com/hawaii-desktop/%{qt_module}/releases/download/v%{version}/%{qt_module}-%{version}.tar.gz
%global __provides_exclude_from ^%{_kf5_qmldir}/QtAccountsService/.*\\.so$
# oreon:deps
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
Qt-style API for freedesktop.org's AccountsService DBus service (see 
http://www.freedesktop.org/wiki/Software/AccountsService).

%package devel
Summary:    Development files for Qt Account Service Addon
Requires:   %{name}%{?isa} = %{version}-%{release}
Requires:   extra-cmake-modules
%description devel
Files for development using Qt Account Service Addon.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{qt_module}-%{version} -p1

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_kf5
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n qt5-qtaccountsservice-devel -f %{oreon_filedir}/qt5-qtaccountsservice-devel.list

%changelog

%autochangelog
