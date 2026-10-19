%global source0_hash da9b4353c595e91dc3311591d8cac090e325531877067794902659a884df9843
Name:           maui-mauiman
Version:        4.0.2
Release:        1%{?dist}
License:        LGPL-3.0-or-later
Summary:        Maui Manager Library
Url:            https://invent.kde.org/maui/mauiman
Source0:        https://invent.kde.org/maui/mauiman/-/archive/v%{version}/mauiman-v%{version}.tar.gz
Requires: dbus-common
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  dbus-common
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
MauiMan stands for Maui Manager, and exists for setting,
saving, and syncing the configuration preferences for the
Maui Apps & Shell ecosystem.

%package devel
Summary:        MauiMan development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Required headers to build components using
MauiMan.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mauiman-v%{version}
%oreon_prep
%build

%cmake_kf6 -DBUILD_WITH_QT6=ON -DBUILD_WITH_QT5=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n maui-mauiman-devel -f %{oreon_filedir}/maui-mauiman-devel.list

%changelog

%autochangelog
