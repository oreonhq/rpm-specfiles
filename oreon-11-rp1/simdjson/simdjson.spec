%global source0_hash 61d948fc24f0d793829ad658058e7597d064988a89b4607ea02e401a82df98ff
%global lib_version 25.0.0
%global lib_soversion 25
Name:		simdjson
Version:	4.6.11
Release:        1%{?dist}
Summary:        Parsing gigabytes of JSON per second
License:	Apache-2.0 AND MIT
URL:		https://simdjson.org
Source0:        https://github.com/simdjson/simdjson/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
JSON is everywhere on the Internet. Servers spend a *lot* of time parsing it.
We need a fresh approach. The simdjson library uses commonly available 
SIMD instructions and microparallel algorithms to parse JSON 4x faster than
RapidJSON and 25x faster than JSON for Modern C++.

%package devel
Summary: Development files for %{name}
Requires:	%{name} = %{version}-%{release}
%description devel
The package contains libraries and header files for developing applications
that use %{name}.

%package doc
Summary: Documents for %{name}
%description doc 
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake -DSIMDJSON_TESTS=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n simdjson-devel -f %{oreon_filedir}/simdjson-devel.list
%files -n simdjson-doc -f %{oreon_filedir}/simdjson-doc.list

%changelog

%autochangelog
