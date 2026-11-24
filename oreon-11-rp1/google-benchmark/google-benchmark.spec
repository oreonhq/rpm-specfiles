# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash acc5c7c0fbed855c4aaa2d7c3c36fb82b0c15c28f4e151e3f679c2fc0aa404af
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond ctest 1
%bcond libpfm 1

Name:           google-benchmark
Version:        1.10.0
%global so_version 1
Release:        %{autorelease}

License:        Apache-2.0
Summary:        A microbenchmark support library
URL:            https://github.com/google/benchmark
Source0:        %{url}/archive/v%{version}/benchmark-%{version}.tar.gz

Patch:          %{url}/pull/2342.patch

BuildSystem:    cmake

BuildOption(conf): -DCMAKE_BUILD_TYPE=Release
BuildOption(conf): -DGIT_VERSION='%{version}'
BuildOption(conf): -DBENCHMARK_DOWNLOAD_DEPENDENCIES:BOOL=OFF
BuildOption(conf): -DBENCHMARK_ENABLE_ASSEMBLY_TESTS:BOOL=OFF
BuildOption(conf): -DBENCHMARK_ENABLE_DOXYGEN:BOOL=OFF
BuildOption(conf): -DBENCHMARK_ENABLE_INSTALL:BOOL=ON
BuildOption(conf): -DBENCHMARK_INSTALL_DOCS:BOOL=OFF
BuildOption(conf): -DBENCHMARK_INSTALL_TOOLS:BOOL=OFF
BuildOption(conf): -DBENCHMARK_USE_BUNDLED_GTEST:BOOL=OFF
BuildOption(conf): -DBENCHMARK_ENABLE_LIBPFM:BOOL=%{with libpfm}
BuildOption(conf): -DBENCHMARK_ENABLE_GTEST_TESTS:BOOL=%{with ctest}
BuildOption(conf): -DBENCHMARK_ENABLE_TESTING:BOOL=%{with ctest}

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
%if %{with libpfm}
BuildRequires:  libpfm-devel
%endif

%if %{with ctest}
BuildRequires:  cmake(GTest)
BuildRequires:  gmock-devel
BuildRequires:  glibc-langpack-en
%endif

%description
A library to support the benchmarking of functions, similar to unit-tests.

%package devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%if %{with libpfm}
Requires:       libpfm-devel%{?_isa}
%endif
Obsoletes:      %{name}-doc < 1.9.4-9

%description devel
%{summary}.

%prep -a
sed --in-place \
    --expression='/get_git_version/d' \
    --expression='/-Werror/d' \
    CMakeLists.txt

%files
%license AUTHORS
%license CONTRIBUTORS
%license LICENSE

%doc README.md

%{_libdir}/libbenchmark*.so.%{so_version}{,.*}

%files devel
%{_libdir}/libbenchmark*.so
%{_includedir}/benchmark/
%{_libdir}/cmake/benchmark/
%{_libdir}/pkgconfig/benchmark*.pc

%changelog
%autochangelog
