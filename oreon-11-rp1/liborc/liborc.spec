%global source0_hash 4214bfc8e01316305e915a3bd7d2675bf3b95d79243aa5fb6c471ea0765add8e

Summary: Library for producing small, fast columnar storage for Hadoop workloads
Name:    liborc
Version: 2.2.2
Release: 2%{?dist}
License: Apache-2.0
URL:     http://orc.apache.org/
Source:  https://downloads.apache.org/orc/orc-%{version}/orc-%{version}.tar.gz
Source1: https://downloads.apache.org/orc/orc-format-1.1.1/orc-format-1.1.1.tar.gz
Patch:	0001-cmake.patch
Patch:	0002-c++-src-CpuInfoUtil.cc.patch

# Apache ORC has numerous compile errors and apparently assumes a 64-bit
# build and runtime environment. The only consumer of this package is 
# Ceph (by way of Apache Arrow) which is also 64-bit only
ExcludeArch:   i686 armv7hl
BuildRequires: gnupg2
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: protobuf-devel
BuildRequires: zlib-devel
BuildRequires: libzstd-devel
BuildRequires: lz4-devel
BuildRequires: snappy-devel

%description
ORC is a self-describing type-aware columnar file format designed
for Hadoop workloads. It is optimized for large streaming reads,
but with integrated support for finding required rows quickly.
Storing data in a columnar format lets the reader read, decompress,
and process only the values that are required for the current query.
Because ORC files are type-aware, the writer chooses the most
appropriate encoding for the type and builds an internal index as
the file is written. Predicate pushdown uses those indexes to
determine which stripes in a file need to be read for a particular
query and the row indexes can narrow the search to a particular set
of 10,000 rows. ORC supports the complete set of types in Hive,
including the complex types: structs, lists, maps, and unions.

%package -n %{name}2
Summary: Library for producing small, fast columnar storage for Hadoop workloads
Provides: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: %{name}1 < %{version}-%{release}

%description -n %{name}2
ORC is a self-describing type-aware columnar file format designed
for Hadoop workloads. It is optimized for large streaming reads,
but with integrated support for finding required rows quickly.
Storing data in a columnar format lets the reader read, decompress,
and process only the values that are required for the current query.
Because ORC files are type-aware, the writer chooses the most
appropriate encoding for the type and builds an internal index as
the file is written. Predicate pushdown uses those indexes to
determine which stripes in a file need to be read for a particular
query and the row indexes can narrow the search to a particular set
of 10,000 rows. ORC supports the complete set of types in Hive,
including the complex types: structs, lists, maps, and unions.

%package devel
Summary:  Header files, libraries and development documentation for %{name}
Requires: %{name}2 = %{version}-%{release}

%description devel
ORC is a self-describing type-aware columnar file format designed
for Hadoop workloads. It is optimized for large streaming reads,
but with integrated support for finding required rows quickly.
Storing data in a columnar format lets the reader read, decompress,
and process only the values that are required for the current query.
Because ORC files are type-aware, the writer chooses the most
appropriate encoding for the type and builds an internal index as
the file is written. Predicate pushdown uses those indexes to
determine which stripes in a file need to be read for a particular
query and the row indexes can narrow the search to a particular set
of 10,000 rows. ORC supports the complete set of types in Hive,
including the complex types: structs, lists, maps, and unions.

Contains header files for developing applications that use the %{name}
library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n orc-%{version}

%build

echo "RPM_OPT_FLAGS: $RPM_OPT_FLAGS"
# https://src.fedoraproject.org/rpms/protobuf/pull-request/26#comment-183002
export CXXFLAGS="$RPM_OPT_FLAGS -Wno-error=dangling-reference -Wno-error=stringop-overflow"

%cmake \
    -DOVERRIDE_INSTALL_PREFIX=/usr \
    -DCMAKE_COLOR_MAKEFILE:BOOL=OFF \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
    -DINSTALL_LIBDIR:PATH=%{_libdir} \
    -DBUILD_SHARED_LIBS:BOOL=on \
    -DBUILD_LIBHDFSPP:BOOL=off \
    -DSNAPPY_HOME="$(pkg-config --variable=prefix snappy)" \
    -DLZ4_HOME="$(pkg-config --variable=prefix liblz4)" \
    -DZLIB_HOME="$(pkg-config --variable=prefix zlib)" \
    -DZSTD_HOME="$(pkg-config --variable=prefix libzstd)" \
    -DGTEST_HOME="$(pkg-config --variable=prefix gtest)" \
    -DPROTOBUF_HOME="$(pkg-config --variable=prefix protobuf)" \
    -Dorc_VERSION="%{version}" \
    -DBUILD_CPP_TESTS=off \
    -DBUILD_TOOLS=off \
    -DBUILD_JAVA=off \
    -DANALYZE_JAVA=off \
    "-GUnix Makefiles"
%cmake_build

%check

%install
%cmake_install
mkdir %{buildroot}%{_docdir}/%{name}2
mv %{buildroot}%{_docdir}/orc/NOTICE %{buildroot}%{_docdir}/%{name}2/
mkdir -p %{buildroot}/%{_defaultlicensedir}/%{name}2
mv %{buildroot}%{_docdir}/orc/LICENSE %{buildroot}/%{_defaultlicensedir}/%{name}2/
rm -f %{buildroot}/%{_includedir}/orc/._*.hh
rm -f %{buildroot}/%{_includedir}/orc/sargs/._*.hh

%ldconfig_scriptlets

%files -n %{name}2
%license LICENSE
%doc README.md NOTICE
%{_libdir}/liborc.so.*
%{_libdir}/cmake/orc/orcConfig*
%exclude %{_libdir}/cmake/orc/*
%exclude %{_libdir}/orcTargets*

%files devel
%dir %{_includedir}/orc
     %{_includedir}/orc/*.hh
%dir %{_includedir}/orc/sargs
     %{_includedir}/orc/sargs/*.hh
     %{_libdir}/liborc.so

%changelog
%autochangelog
