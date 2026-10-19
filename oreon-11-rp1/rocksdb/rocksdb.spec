%global source0_hash d1ddfd3551e649f7e2d180d5a6a006d90cfde56dcfe1e548c58d95b7f1c87049
%bcond_without compression
%global forgeurl https://github.com/facebook/rocksdb
Name:    rocksdb
Version: 11.8.1
Release:        1%{?dist}
Summary:        A Persistent Key-Value Store for Flash and RAM Storage
License: GPL-2.0-only OR Apache-2.0 AND LicenseRef-Callaway-BSD
URL:     %{forgeurl}
Patch1: shared-liburing.patch
Patch2: https://sources.debian.org/data/main/r/rocksdb/7.6.0-2/debian/patches/no_rpath.patch
Patch3: disable-static.patch
Patch4: https://patch-diff.githubusercontent.com/raw/facebook/rocksdb/pull/13437.patch
%if %{with compression}
%endif
%forgemeta
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  /usr/bin/perl
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gflags-devel
BuildRequires:  liburing-devel
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  python3-devel
BuildRequires:  snappy-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
install -dD -m 755 %{buildroot}%{_bindir}
install -m 755 %{__cmake_builddir}/cache_bench %{buildroot}%{_bindir}/cache_bench
install -m 755 %{__cmake_builddir}/db_bench %{buildroot}%{_bindir}/db_bench
install -m 755 %{__cmake_builddir}/tools/ldb %{buildroot}%{_bindir}/ldb
install -m 755 %{__cmake_builddir}/tools/sst_dump %{buildroot}%{_bindir}/sst_dump
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n rocksdb-tools -f %{oreon_filedir}/rocksdb-tools.list
%files -n rocksdb-devel -f %{oreon_filedir}/rocksdb-devel.list

%changelog

%autochangelog
