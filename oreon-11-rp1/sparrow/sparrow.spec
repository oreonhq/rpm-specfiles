%global source0_hash 586c34c0f46ca878a735db0d2f3e7c6ce78390a65eb42f028bfe5d34dbeeb7b6

Name:           sparrow
Version:        0.6.0
Release:        %autorelease
Summary:        C++20 idiomatic APIs for the Apache Arrow Columnar Format
License:        Apache-2.0
URL:            https://github.com/man-group/sparrow
%global github  https://github.com/man-group/sparrow
Source:         %{github}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  doctest-devel

Patch0: 0001-Remove-tests-that-depend-on-nanoarrow.patch

%global _description \
sparrow is an implementation of the Apache Arrow Columnar format in C++. It \
provides array structures with idiomatic APIs and convenient conversions from \
and to the C interface.

%description %_description

%package devel
Summary:        %{summary}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}

%description devel %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -DBUILD_TESTS=ON -DUSE_DATE_POLYFILL=OFF
%cmake_build

%install
%cmake_install

%check
%cmake_build --target test_sparrow_lib
%cmake_build --target run_tests

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_datadir}/cmake/%{name}
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
