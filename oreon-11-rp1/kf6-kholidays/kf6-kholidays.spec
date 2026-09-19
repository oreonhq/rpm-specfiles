%global source0_hash bcb204c0cca063b071e4bc986ef418b03b57e28cfc7fea45e368d1cb8b56b3f2

%global		framework kholidays

%global stable_kf6 stable
%global majmin_ver_kf6 6.29


Name:		kf6-%{framework}
Version:	6.29.0
Release:        1%{?dist}
Summary:	The KHolidays Library

License:	BSD-2-Clause AND CC0-1.0 AND GPL-3.0-or-later AND LGPL-2.0-or-later WITH Bison-exception-2.2
URL:		https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	cmake
BuildRequires:	gcc-c++

BuildRequires: 	pkgconfig(Qt6Core)
BuildRequires: 	pkgconfig(Qt6Qml)
BuildRequires: 	qt6-qttools-static
BuildRequires:	make
BuildRequires:  flex
BuildRequires:  bison

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

%files -f libkholidays6_qt.lang
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6Holidays.so.*
%{_kf6_qmldir}/org/kde/kholidays/

%files devel
%{_kf6_includedir}/KHolidays/
%{_kf6_libdir}/cmake/KF6Holidays/
%{_kf6_libdir}/libKF6Holidays.so


%changelog
%autochangelog
