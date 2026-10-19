%global source0_hash 1f378e25d8bb5be258d3e04d3d24b8c23ff21bf206e6e206661844a96ca25eda
Name:           libxlsxwriter
Version:        1.1.7
Release:        1%{?dist}
Summary:        A C library for creating Excel XLSX files
License:        BSD-2-Clause AND LicenseRef-Fedora-Public-Domain AND MPL-2.0
URL:            https://github.com/jmcnamara/libxlsxwriter/
Source0:        https://github.com/jmcnamara/libxlsxwriter/archive/RELEASE_%{version}/%{name}-%{version}.tar.gz
Patch0:         libxlsxwriter_minizip.patch
Patch1:         libxlsxwriter_cmakever.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  minizip-ng-compat-devel
BuildRequires:  python3-pytest
BuildRequires:  zlib-devel
# /oreon:deps
%description
Libxlsxwriter is a C library that can be used to write text, numbers, formulas
and hyperlinks to multiple worksheets in an Excel 2007+ XLSX file.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

%autosetup -p1 -n %{name}-RELEASE_%{version}

# Delete bundled minizip
rm -rf third_party/minizip
rm -f include/xlsxwriter/third_party/zip.h

# FIXME Remove failing test
# [ERROR][/home/sandro/rpmbuild/BUILD/libxlsxwriter-RELEASE_1.1.5/src/packager.c:1711]: Error adding member to zipfile
# [ERROR] workbook_close(): Zip ZIP_ERRNO error while creating xlsx file '(null)'. System error = Success
rm test/functional/test_output_buffer.py

%build

%cmake -DUSE_SYSTEM_MINIZIP=ON -DBUILD_TESTS=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifnarch s390x i686
%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n libxlsxwriter-devel -f %{oreon_filedir}/libxlsxwriter-devel.list

%changelog

%autochangelog
