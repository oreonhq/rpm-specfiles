%global source0_hash 4e69e29d5d79a976498ef71eab70c9c88c7014708be4450a9fda7780fe93584e
Name:    lucene++
Summary:        A high-performance, full-featured text search engine written in C++
Version: 3.0.9
Release:        4%{?dist}
License: Apache-2.0 OR LGPL-3.0-or-later
Url:     https://github.com/luceneplusplus/LucenePlusPlus
Source0:        https://github.com/luceneplusplus/LucenePlusPlus/archive/rel_%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: lucene++-3.0.9-fix_install_path_for_liblucene++.pc.patch
Patch1: lucene++-3.0.9-fix_compilation_with_clang-17.patch
Patch2: lucene++-3.0.9-fix_cmake-4.0.patch
Patch3: lucene++-3.0.9-fix_build_with_boost_1.85.0.patch
Patch4: lucene++-3.0.9-migrate_to_boost_asio_io_context.patch
Patch5: lucene++-3.0.9-bitset_partial_fix_for_boost_1.90.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  subversion
BuildRequires:  zlib-devel
# /oreon:deps
%description
An up to date C++ port of the popular Java Lucene library, a high-performance, full-featured text search engine.

%package devel
Summary: Development files for lucene++
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for lucene++, a high-performance, full-featured text search engine written in C++

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir LucenePlusPlus-rel_%{version}
%oreon_prep
%build

%cmake -DCMAKE_BUILD_TYPE:String="release" -DINSTALL_GTEST=OFF
%cmake_build --target lucene++ lucene++-contrib
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
