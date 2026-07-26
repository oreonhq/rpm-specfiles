%global source0_hash 88c41eaba03107ebe79052fdbd66e419e903d331a2616a51849018e13648ab83

%global boost_version 1.69.0
%global rapidjson_version 1.1.0
%global geometry_version 1.0.0

%global testcommit a623c19a91947a9d29f9ec5625ce620ab42325dc

%global debug_package %{nil}

Name:           wagyu
Version:        0.5.0
Release:        12%{?dist}
Summary:        A general library for geometry operations of union, intersections, difference, and xor

License:        BSL-1.0 AND BSD-3-Clause
URL:            https://github.com/mapbox/wagyu
Source0:        https://github.com/mapbox/wagyu/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/mapnik/geometry-test-data/archive/%{testcommit}/geometry-test-data-%{testcommit}.tar.gz
# Remove benchmarking support to avoid libbenchmark dependency
Patch0:         wagyu-benchmark.patch
# Rip out mason stuff - we use our own packages
Patch1:         wagyu-mason.patch
# https://github.com/mapbox/wagyu/pull/109
Patch2:         wagyu-cxx14.patch

BuildRequires:  cmake make
BuildRequires:  gcc-c++
BuildRequires:  catch1-devel
BuildRequires:  boost-devel >= %{boost_version}
BuildRequires:  boost-static >= %{boost_version}
BuildRequires:  rapidjson-devel >= %{rapidjson_version}
BuildRequires:  rapidjson-static >= %{rapidjson_version}
BuildRequires:  geometry-hpp-devel >= %{geometry_version}
BuildRequires:  geometry-hpp-static >= %{geometry_version}

%description
Wagyu is a general library for the following basic geometric operations:

    Union
    Intersection
    Difference
    XOR

The output geometry from each of these operations is guaranteed to
be valid and simple as per the OGC.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

Requires:       geometry-hpp-devel >= %{geometry_version}

%description    devel
Wagyu is a general library for the following basic geometric operations:

    Union
    Intersection
    Difference
    XOR

The output geometry from each of these operations is guaranteed to
be valid and simple as per the OGC.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n wagyu-%{version}
tar --directory=tests/geometry-test-data --strip-components=1 --gunzip --extract --file=%{SOURCE1}
rm -f tests/catch.hpp

%build
%make_build release CXXFLAGS="-I$PWD/include %{optflags}" WERROR=False

%install
mkdir -p %{buildroot}%{_includedir}
cp -pr include/mapbox %{buildroot}%{_includedir}

%check
%make_build test CXXFLAGS="-I$PWD/include %{optflags}" WERROR=False

%files devel
%doc README.md
%license LICENSE
%{_includedir}/mapbox

%changelog
%autochangelog
