%global source0_hash bb7467f8e296279a89fa75909129e128d67195187fe066ed096e9fb6250e37e5
%global debug_package %{nil}
%global middle_release 0
%bcond check 0
%bcond_without test_api
%bcond_without test_header
%bcond_without benchmark
%bcond_with doc
ExclusiveArch: %{power64} x86_64 aarch64
%if 0%{?middle_release}
%global  commit      8c604d98e0d291bc3909ecbad78ca778b3ad5a5c
%global  date        .20230403git
%global  shortcommit %(c=%{commit}; echo ${c:0:8})
%else
%global  commit      %{nil}
%global  date        %{nil}
%global  shortcommit %{nil}
%endif
Name:      seqan3
Summary:        The modern C++ library for sequence analysis
Version:   3.4.2
Release:        1%{?dist}
License:   BSD-3-Clause
URL:       https://www.seqan.de/
%if 0%{?middle_release}
Source0:        https://github.com/seqan/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%else
%endif
%if %{with check}
%endif
%if %{with doc}
%endif
Patch1: %{name}-3.4.0-disable_CPM.patch
Patch2: %{name}-fix_GCC15.patch
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  ccache
BuildRequires:  cereal-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  google-benchmark-devel
BuildRequires:  gtest-devel
BuildRequires:  make
BuildRequires:  range-v3-devel
BuildRequires:  sdsl-lite-devel
BuildRequires:  texlive-newunicodechar
BuildRequires:  zlib-devel
# /oreon:deps
%description
SeqAn3 is the new version of the popular SeqAn template
library for the analysis of biological sequences.
It enables the rapid development of high-performance
solutions by providing generic algorithms and
data structures for:

 - sequence representation and transformation
 - full-text indexing and efficient search
 - sequence alignment
 - input/output of common file formats

%package devel
Summary: SeqAn3 header only files
License:  BSD-3-Clause AND Zlib
Requires: cmake%{?_isa} >= 3.4
Requires: cereal-devel%{?_isa} >= 1.3.2
Requires: sdsl-lite-devel%{?_isa} >= 3.0.1
Requires: zlib-devel%{?_isa} >= 1.2
Requires: bzip2-devel%{?_isa} >= 1.0
Requires: range-v3-devel%{?_isa} >= 0.11.0
Provides: bundled(bzip2stream)
Provides: bundled(zipstream)
%description devel
C++ headers files of SeqAn3, including CMake configuration files.

%package doc
Summary: SeqAn3 documentation
BuildArch: noarch
%description doc
SeqAn3 documentation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -N

%patch 1 -p1 -b .backup
%patch 2 -p1 -b .backup

# Unbundle libraries already available in Fedora
rm -rf submodules/cereal
rm -rf submodules/range-v3
rm -rf submodules/sdsl-lite

# Fix file permissions
find . -type f -name "*.hpp" -exec chmod 0644 '{}' \;

%build

%if %{with check}
%if %{with test_api}
mkdir -p build
export CXXFLAGS="%{build_cxxflags} -std=c++23"
%cmake -S test/unit -B build -DCMAKE_BUILD_TYPE=Release \
 -DCPM_USE_LOCAL_PACKAGES:BOOL=OFF -DCPM_LOCAL_PACKAGES_ONLY:BOOL=OFF \
 -DCPM_DONT_UPDATE_MODULE_PATH:BOOL=ON -DCPM_DONT_CREATE_PACKAGE_LOCK:BOOL=ON \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DSEQAN3_CEREAL:BOOL=ON \
 -DSEQAN3_TEST_BUILD_OFFLINE:BOOL=ON -DFETCHCONTENT_FULLY_DISCONNECTED:BOOL=ON \
 -DFETCHCONTENT_UPDATES_DISCONNECTED:BOOL=ON \
 -DSEQAN3_NO_ZLIB=OFF
%define _vpath_builddir build
%cmake_build
%endif
%if %{with test_header}
mkdir -p build-header
export CXXFLAGS="%{build_cxxflags} -std=c++23"
%cmake -S test/header -B build-header -DCMAKE_BUILD_TYPE=Release \
 -DCPM_USE_LOCAL_PACKAGES:BOOL=OFF -DCPM_LOCAL_PACKAGES_ONLY:BOOL=OFF \
 -DCPM_DONT_UPDATE_MODULE_PATH:BOOL=ON -DCPM_DONT_CREATE_PACKAGE_LOCK:BOOL=ON \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DSEQAN3_CEREAL:BOOL=ON \
 -DSEQAN3_TEST_BUILD_OFFLINE:BOOL=ON -DFETCHCONTENT_FULLY_DISCONNECTED:BOOL=ON \
 -DFETCHCONTENT_UPDATES_DISCONNECTED:BOOL=ON \
 -DSEQAN3_NO_ZLIB=OFF
%define _vpath_builddir build-header
%cmake_build
%endif
%if %{with benchmark}
mkdir -p build-performance
export CXXFLAGS="%{build_cxxflags} -std=c++23"
%cmake -S test/performance -B build-performance -DCMAKE_BUILD_TYPE=Release \
 -DCPM_USE_LOCAL_PACKAGES:BOOL=OFF -DCPM_LOCAL_PACKAGES_ONLY:BOOL=OFF \
 -DCPM_DONT_UPDATE_MODULE_PATH:BOOL=ON -DCPM_DONT_CREATE_PACKAGE_LOCK:BOOL=ON \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DSEQAN3_CEREAL:BOOL=ON \
 -DSEQAN3_TEST_BUILD_OFFLINE:BOOL=ON -DFETCHCONTENT_FULLY_DISCONNECTED:BOOL=ON \
 -DFETCHCONTENT_UPDATES_DISCONNECTED:BOOL=ON \
 -DSEQAN3_NO_ZLIB=OFF
%define _vpath_builddir build-performance
%cmake_build
%endif
%endif
%if %{with doc}
mkdir -p build-doc
%cmake -S test/documentation -B build-doc -DCMAKE_BUILD_TYPE=Release
%define _vpath_builddir build-doc
%cmake_build -- -j1
%endif
%install
mkdir -p %{buildroot}%{_libdir}/cmake/%{name}
cp -a include %{buildroot}%{_prefix}/
rm %{buildroot}%{_includedir}/%{name}/contrib/std/.{clang-format,gitignore}
install -pm 644 cmake/seqan3-config-version.cmake %{buildroot}%{_libdir}/cmake/%{name}/
install -pm 644 cmake/seqan3-config.cmake %{buildroot}%{_libdir}/cmake/%{name}/
%if %{with doc}
mkdir -p build-doc
%cmake -S test/documentation -B build-doc -DCMAKE_BUILD_TYPE=Release
%define _vpath_builddir build-doc
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%if %{with check}
%check

%if %{with test_api}
%define _vpath_builddir build
%ctest
%endif
%if %{with test_header}
%define _vpath_builddir build-header
%ctest
%endif
%if %{with benchmark}
%define _vpath_builddir build-performance
%ctest
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n seqan3-devel -f %{oreon_filedir}/seqan3-devel.list
%files -n seqan3-doc -f %{oreon_filedir}/seqan3-doc.list

%changelog

%autochangelog
