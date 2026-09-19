%global source0_hash 39f9494489e63579596f430ef04575a4a0f0c8f9c75bf1d46f44fa2dc203ef12

%global qt_module qtaccountsservice

Name:           qt5-%{qt_module}
Summary:        Qt5 - AccountService addon
Version:        0.6.0
Release:        29%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/hawaii-desktop/qtaccountsservice
Source0:        https://github.com/hawaii-desktop/qtaccountsservice/releases/download/v%{version}/%{qt_module}-%{version}.tar.gz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  cmake
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

%global __provides_exclude_from ^%{_kf5_qmldir}/QtAccountsService/.*\\.so$

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
# TODO: Please submit an issue to upstream (rhbz#2381395)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_kf5

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%{_libdir}/libQtAccountsService.so.*
%{_kf5_qmldir}/QtAccountsService/
%doc README.md
%license LICENSE.LGPL

%files devel
%{_includedir}/QtAccountsService/
%{_libdir}/cmake/QtAccountsService/
%{_libdir}/libQtAccountsService.so

%changelog
%autochangelog
