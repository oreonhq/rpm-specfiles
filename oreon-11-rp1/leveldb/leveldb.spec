%global source0_hash 9a37f8a6174f09bd622bc723b55881dc541cd50747cbd08831c2a82d620f6d76
%undefine __cmake_in_source_build
Name:           leveldb
Version:        1.23
Release:        14%{?dist}
Summary:        A fast and lightweight key/value database library by Google
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/google/leveldb
Source0:        https://github.com/google/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0001:      0001-Allow-leveldbjni-build.patch
Patch0002:      0002-Added-a-DB-SuspendCompations-and-DB-ResumeCompaction.patch
Patch0003:      0003-allow-Get-calls-to-avoid-copies-into-std-string.patch
Patch0004:      0004-bloom_test-failure-on-big-endian-archs.patch
Patch0006:      0006-revert-no-rtti.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  snappy-devel
BuildRequires:  sqlite-devel
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n leveldb-devel -f %{oreon_filedir}/leveldb-devel.list

%changelog

%autochangelog
