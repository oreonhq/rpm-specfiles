%global source0_hash 4e69e29d5d79a976498ef71eab70c9c88c7014708be4450a9fda7780fe93584e

Name:    lucene++
Summary: A high-performance, full-featured text search engine written in C++
Version: 3.0.9
Release: 4%{?dist}

# Automatically converted from old format: ASL 2.0 or LGPLv3+ - review is highly recommended.
License: Apache-2.0 OR LGPL-3.0-or-later
Url:     https://github.com/luceneplusplus/LucenePlusPlus
Source:  https://github.com/luceneplusplus/LucenePlusPlus/archive/rel_%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Fix install path for liblucene++.pc
# https://github.com/luceneplusplus/LucenePlusPlus/commit/f40f59c
Patch0: lucene++-3.0.9-fix_install_path_for_liblucene++.pc.patch

# Fix compilation with clang-17
# https://github.com/luceneplusplus/LucenePlusPlus/commit/b77d1c7
Patch1: lucene++-3.0.9-fix_compilation_with_clang-17.patch

# Fix build with CMake 4.0
# https://github.com/luceneplusplus/LucenePlusPlus/commit/2857419
Patch2: lucene++-3.0.9-fix_cmake-4.0.patch

# Fix build with boost 1.85.0
# https://github.com/luceneplusplus/LucenePlusPlus/commit/c18ead2
Patch3: lucene++-3.0.9-fix_build_with_boost_1.85.0.patch

# Migrate to boost::asio::io_context
# https://github.com/luceneplusplus/LucenePlusPlus/commit/e6a3768
Patch4: lucene++-3.0.9-migrate_to_boost_asio_io_context.patch

# BitSet: Partial fix for Boost 1.90
# github.com/luceneplusplus/LucenePlusPlus/pull/222
Patch5: lucene++-3.0.9-bitset_partial_fix_for_boost_1.90.patch

BuildRequires: boost-devel
BuildRequires: cmake >= 3.5
BuildRequires: gcc-c++
BuildRequires: pkgconfig
BuildRequires: subversion
BuildRequires: zlib-devel

%description
An up to date C++ port of the popular Java Lucene library, a high-performance, full-featured text search engine.

%package devel
Summary: Development files for lucene++
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for lucene++, a high-performance, full-featured text search engine written in C++

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n LucenePlusPlus-rel_%{version}

%build
%cmake -DCMAKE_BUILD_TYPE:String="release" -DINSTALL_GTEST=OFF
%cmake_build --target lucene++ lucene++-contrib

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc AUTHORS README* REQUESTS
%license COPYING APACHE.license GPL.license LGPL.license
%{_libdir}/liblucene++.so.0*
%{_libdir}/liblucene++.so.%{version}
%{_libdir}/liblucene++-contrib.so.0*
%{_libdir}/liblucene++-contrib.so.%{version}

%files devel
%{_includedir}/lucene++/
%{_libdir}/liblucene++.so
%{_libdir}/liblucene++-contrib.so
%{_libdir}/pkgconfig/liblucene++.pc
%{_libdir}/pkgconfig/liblucene++-contrib.pc
%{_libdir}/cmake/liblucene++/
%{_libdir}/cmake/liblucene++-contrib/

%changelog
%autochangelog
