%global source0_hash b7ff8b9b8c26a811103ea22cce542ec93d7a15f4c66afb4e244096d58f7f52d0

Name: QXlsx
Version:  1.4.10
Release:  7%{?dist}
Summary:  Excel/XLSX file reader/writer library for Qt

License: MIT
URL: https://github.com/QtExcel/QXlsx
Source0: %{url}/archive/v%{version}/QtXslx-%{version}.tar.gz

Patch0:  qxlsx-fix-build-against-qt-6-10.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  libxkbcommon-devel

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

%patch -P0 -p1 -b .fix-build-against-qt-6-10

%build

%cmake QXlsx -DBUILD_SHARED_LIBS=ON -DQT_VERSION_MAJOR=6
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README*
%{_libdir}/libQXlsxQt6.so.0*
%{_libdir}/libQXlsxQt6.so.1*

%files devel
%{_libdir}/libQXlsxQt6.so
%{_includedir}/QXlsxQt6/
%{_libdir}/cmake/QXlsxQt6/

%changelog
%autochangelog
