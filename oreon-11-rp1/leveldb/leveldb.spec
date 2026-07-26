%global source0_hash 9a37f8a6174f09bd622bc723b55881dc541cd50747cbd08831c2a82d620f6d76

%undefine __cmake_in_source_build
Name:           leveldb
Version:        1.23
Release:        14%{?dist}
Summary:        A fast and lightweight key/value database library by Google
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/google/leveldb
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# available in https://github.com/fusesource/leveldbjni/blob/leveldb.patch
Patch0001:      0001-Allow-leveldbjni-build.patch
# https://github.com/fusesource/leveldbjni/issues/34
# https://code.google.com/p/leveldb/issues/detail?id=184
# Add DB::SuspendCompactions() and DB:: ResumeCompactions() methods
Patch0002:      0002-Added-a-DB-SuspendCompations-and-DB-ResumeCompaction.patch
# Cherry-picked from Basho's fork
Patch0003:      0003-allow-Get-calls-to-avoid-copies-into-std-string.patch
# https://groups.google.com/d/topic/leveldb/SbVPvl4j4vU/discussion
Patch0004:      0004-bloom_test-failure-on-big-endian-archs.patch
# -fno-rtti breaks ABI compatibility
Patch0006:      0006-revert-no-rtti.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  snappy-devel
BuildRequires:  sqlite-devel

%description
LevelDB is a fast key-value storage library written at Google that provides an
ordered mapping from string keys to string values.

%package devel
Summary:        Development files for %{name}
Requires:       cmake-filesystem
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

cat > %{name}.pc << EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: %{name}
Description: %{summary}
Version: %{version}
Libs: -l%{name}
EOF

%build
%cmake -DLEVELDB_BUILD_TESTS:BOOL=OFF \
       -DLEVELDB_BUILD_BENCHMARKS:BOOL=OFF
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_libdir}/pkgconfig
cp -a %{name}.pc %{buildroot}%{_libdir}/pkgconfig/

%check
%ctest

%ldconfig_scriptlets

%files
%license LICENSE
%doc AUTHORS README.md NEWS
%{_libdir}/lib%{name}.so.*

%files devel
%doc doc/ CONTRIBUTING.md TODO
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/

%changelog
%autochangelog
