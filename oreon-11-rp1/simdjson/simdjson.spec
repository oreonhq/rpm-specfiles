%global source0_hash d0af071f2f4187d8b26b556e83ef832b634bd5feb4e2f537b9dabbd334d4e334

%global lib_version 25.0.0
%global lib_soversion 25
Name:		simdjson
Version:	3.12.3
Release:	%autorelease
Summary:	Parsing gigabytes of JSON per second

License:	Apache-2.0 AND MIT
URL:		https://simdjson.org
Source0:	https://github.com/simdjson/simdjson/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake >= 3.1
BuildRequires:	gcc-c++

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

%autosetup -p1 -n %{name}-%{version}

%build
%cmake -DSIMDJSON_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_libdir}/lib%{name}*.so.%{lib_soversion}
%{_libdir}/lib%{name}*.so.%{lib_version}

%files devel
%license LICENSE
%{_includedir}/%{name}.h
%{_libdir}/cmake/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%license LICENSE
%doc doc

%changelog
%autochangelog
