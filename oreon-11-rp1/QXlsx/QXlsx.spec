%global source0_hash de04e8b5ce17a207c10f70111d482375d3b3f86b6ab88e2b39cc4fcb1ef91e2f
Name: QXlsx
Version:  1.5.1
Release:        1%{?dist}
Summary:        Excel/XLSX file reader/writer library for Qt
License: MIT
URL: https://github.com/QtExcel/QXlsx
Source0:        https://github.com/QtExcel/%{name}/archive/v%{version}/QtXslx-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libxkbcommon-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
%package devel
Summary: Development files for QtXslx
Requires: %{name} = %{version}-%{release}
%description
QXlsx is excel file(*.xlsx) reader/writer library.

%description devel
QXlsx is excel file(*.xlsx) reader/writer library.

These are the development files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%cmake QXlsx -DBUILD_SHARED_LIBS=ON -DQT_VERSION_MAJOR=6
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}%{_libdir}/cmake/QXlsxQt6/libQXlsx*.so* %{buildroot}%{_libdir}/
%oreon_autofiles QXlsx-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n QXlsx-devel -f %{oreon_filedir}/QXlsx-devel.list

%changelog

%autochangelog
