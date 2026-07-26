%global source0_hash d1ddfd3551e649f7e2d180d5a6a006d90cfde56dcfe1e548c58d95b7f1c87049

%bcond_without compression

%global forgeurl https://github.com/facebook/rocksdb

Name:    rocksdb
Version: 10.2.1
Release: 2%{?dist}
Summary: A Persistent Key-Value Store for Flash and RAM Storage

# Automatically converted from old format: GPLv2 or ASL 2.0 and BSD - review is highly recommended.
License: GPL-2.0-only OR Apache-2.0 AND LicenseRef-Callaway-BSD
URL:     %{forgeurl}

# https://git.alpinelinux.org/aports/tree/community/rocksdb/11-shared-liburing.patch
Patch1: shared-liburing.patch

# Do not build tools with rpath These will be installed semi-manual to usr/bin
# and will use system libraries.
Patch2: https://sources.debian.org/data/main/r/rocksdb/7.6.0-2/debian/patches/no_rpath.patch

Patch3: disable-static.patch

# Fix GCC 15 compile errors
Patch4: https://patch-diff.githubusercontent.com/raw/facebook/rocksdb/pull/13437.patch

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gflags-devel
BuildRequires: liburing-devel

%if %{with compression}
BuildRequires: bzip2-devel
BuildRequires: lz4-devel
BuildRequires: snappy-devel
BuildRequires: zlib-devel
BuildRequires: libzstd-devel
%endif

BuildRequires: /usr/bin/perl
BuildRequires: python3-devel

%forgemeta
Source: %{forgesource}

%description
RocksDB is a library that forms the core building block for a fast key value
server, especially suited for storing data on flash drives. It has a
Log-Structured-Merge-Database (LSM) design with flexible trade offs between
Write-Amplification-Factor (WAF), Read-Amplification-Factor (RAF) and
Space-Amplification-Factor (SAF). It has multi-threaded compaction, making it
specially suitable for storing multiple terabytes of data in a single database.

%package tools
Summary: Utility tools for RocksDB
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Utility tools for RocksDB.

%package devel
Summary: Development files for RocksDB
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for RocksDB.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1

%build
%cmake \
%if %{with compression}
  -DWITH_BZ2=ON \
  -DWITH_SNAPPY=ON \
  -DWITH_LZ4=ON \
  -DWITH_ZSTD=ON \
  -DWITH_ZLIB=ON \
%endif
  -DZSTD_INCLUDE_DIRS=%{_includedir} \
  -DROCKSDB_BUILD_SHARED=ON \
  -DWITH_BENCHMARK_TOOLS=ON \
  -DWITH_CORE_TOOLS=ON \
  -DWITH_TOOLS=ON \
  -DUSE_RTTI=ON \
  -DPORTABLE=1 \
  -DFAIL_ON_WARNINGS=OFF \
  -DWITH_TESTS=ON

%cmake_build

%install
%cmake_install

# Missing steps in build script
install -dD -m 755 %{buildroot}%{_bindir}
install -m 755 %{__cmake_builddir}/cache_bench %{buildroot}%{_bindir}/cache_bench
install -m 755 %{__cmake_builddir}/db_bench %{buildroot}%{_bindir}/db_bench
install -m 755 %{__cmake_builddir}/tools/ldb %{buildroot}%{_bindir}/ldb
install -m 755 %{__cmake_builddir}/tools/sst_dump %{buildroot}%{_bindir}/sst_dump

%files
%doc README.md
%doc HISTORY.md
%doc AUTHORS
%license COPYING
%license LICENSE.Apache
%license LICENSE.leveldb
%{_libdir}/librocksdb.so.10
%{_libdir}/librocksdb.so.10.2.1

%files tools
%doc README.md
%license COPYING
%license LICENSE.Apache
%license LICENSE.leveldb
%{_bindir}/cache_bench
%{_bindir}/db_bench
%{_bindir}/ldb
%{_bindir}/sst_dump

%files devel
%doc README.md
%doc LANGUAGE-BINDINGS.md
%license COPYING
%license LICENSE.Apache
%license LICENSE.leveldb
%{_libdir}/librocksdb.so
%{_libdir}/cmake/rocksdb
%{_libdir}/pkgconfig/rocksdb.pc
%{_includedir}/rocksdb

%changelog
%autochangelog
