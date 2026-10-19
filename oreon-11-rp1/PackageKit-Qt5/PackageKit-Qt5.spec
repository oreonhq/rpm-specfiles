%global source0_hash bbb8398d0f98c46e2ed7fd3ce526d4f7fc8476f5a449e89269f01b1bc751c4ad
Summary:        Qt5 support library for PackageKit
Name:      PackageKit-Qt5
Version:   1.1.4
Release:        1%{?dist}
License:   LGPL-2.1-only
URL:       http://www.packagekit.org/
Source0:        https://github.com/hughsie/PackageKit-Qt/archive/v%{version}.tar.gz
Recommends: PackageKit
# oreon:deps
BuildRequires:  PackageKit
BuildRequires:  cmake
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  gcc-c++
# /oreon:deps
%description
PackageKit-Qt is a Qt support library for PackageKit

%package devel
Summary: Development files for PackageKit-Qt5
Requires: PackageKit-Qt5%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir PackageKit-Qt-%{version}
%oreon_prep
%build

%cmake -DBUILD_WITH_QT6=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles PackageKit-Qt5-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n PackageKit-Qt5-devel -f %{oreon_filedir}/PackageKit-Qt5-devel.list

%changelog

%autochangelog
