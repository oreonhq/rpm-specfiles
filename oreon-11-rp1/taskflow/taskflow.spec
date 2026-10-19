%global source0_hash none
%global debug_package %{nil}
%global forgeurl https://github.com/taskflow/taskflow
Version: 3.4.0
%forgemeta
Name: taskflow
Release:        1%{?dist}
License: MIT and BSL-1.0 and MPL-2.0
Summary:        Header library for writing parallel and heterogeneous with C++
URL: https://taskflow.github.io/
Source0:        %{name}-%{version}-norefpdfs.tar.gz
Source1: generate-tarball.sh
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doctest-devel
BuildRequires:  gcc-c++
# /oreon:deps
%description

%package devel
Summary: Development files for the Taskflow library
Provides: taskflow-static = %{version}-%{release}
%description devel
Taskflow is a C++ header library which helps you quickly write parallel and
heterogeneous task programs with high performance and simultaneous high
productivity. It is faster, more expressive, fewer lines of code, and easier
for drop-in integration than many of existing task programming libraries.

%package doc
Summary: Documentation for the Taskflow library
BuildArch: noarch
%description doc
Taskflow is a C++ header library which helps you quickly write parallel and
heterogeneous task programs with high performance and simultaneous high
productivity. It is faster, more expressive, fewer lines of code, and easier
for drop-in integration than many of existing task programming libraries.

%prep

%autosetup
# Safety check to help make sure PDFs don't sneak their way into the package.
pdfs=$(find -name "*.pdf")
if [ -n "$pdfs" ]; then
    echo "PDFs should not be present due to license terms!"
    exit 1
fi

# Most of these bundled libraries are only used by code in sandbox/, thus the
# bundled code can be removed.
rm -fr 3rd-party
# doctest is used by unittests, but point to the system version instead
sed -i \
    -e 's,include(.*/doctest.cmake),include(%{_libdir}/cmake/doctest/doctest.cmake),' \
    -e 's,\${TF_3RD_PARTY_DIR}/doctest,%{_includedir}/doctest,' \
    unittests/CMakeLists.txt

%build

%cmake
%cmake_build
mv docs html
sed -i 's,href="\([^/]\+\.pdf\)",href="%{forgeurl}/raw/v%{version}/docs/\1",g' \
    html/*.html
rm -rf html/xml
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n taskflow-devel -f %{oreon_filedir}/taskflow-devel.list
%files -n taskflow-doc -f %{oreon_filedir}/taskflow-doc.list

%changelog

%autochangelog
