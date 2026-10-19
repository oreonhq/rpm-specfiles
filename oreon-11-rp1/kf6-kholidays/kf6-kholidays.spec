%global source1_hash 0334ec4c02203a76c24db514d256c0d09d9e5342dbb640124f3a123de4a99ff6
%global source0_hash 02bfbc33296fe86b364491f6d5cad9d83360bb4fdd2923386a325b309eac0b9b
%global		framework kholidays
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:		kf6-%{framework}
Version:	6.30.0
Release:        1%{?dist}
Summary:        The KHolidays Library
License:	BSD-2-Clause AND CC0-1.0 AND GPL-3.0-or-later AND LGPL-2.0-or-later WITH Bison-exception-2.2
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
# oreon:deps
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  make
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  qt6-qttools-static
# /oreon:deps
%description
The KHolidays library provides a C++ API that determines holiday
and other special events for a geographical region.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang_kf6 libkholidays6_qt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-kholidays-devel -f %{oreon_filedir}/kf6-kholidays-devel.list

%changelog

%autochangelog
