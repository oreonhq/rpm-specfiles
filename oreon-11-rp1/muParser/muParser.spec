%global source0_hash 20b43cc68c655665db83711906f01b20c51909368973116dfc8d7b3c4ddb5dd4

%global lcname muparser
%global owner beltoforion
Name:           muParser
Summary:        A fast math parser library
Version:        2.3.5
Release:        5%{?dist}
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
License:        BSD-2-Clause
URL:            https://beltoforion.de/en/muparser/
Source0:        https://github.com/%{owner}/%{lcname}/archive/v%{version}/%{lcname}-%{version}.tar.gz

%package devel
Summary:        Development and doc files for %{name}
Requires:       %{name} = %{version}-%{release} pkgconfig

%description
Many applications require the parsing of mathematical expressions.
The main objective of this project is to provide a fast and easy way
of doing this. muParser is an extensible high performance math parser
library. It is based on transforming an expression into a bytecode
and precalculating constant parts of it.

%description devel
Development files and the documentation

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{lcname}-%{version}

%build
%cmake .. -DENABLE_SAMPLES=ON -DENABLE_OPENMP=ON -DBUILD_SHARED_LIBS=ON -DCMAKE_POLICY_VERSION_MINIMUM=3.5
# -DENABLE_WIDE_CHAR=ON
%cmake_build

%install
%cmake_install
%ldconfig_scriptlets

%files
%doc CHANGELOG README*
%license LICENSE
%{_libdir}/lib%{lcname}.so.*

%files devel
%{_includedir}/*
%{_libdir}/lib%{lcname}.so
%{_libdir}/pkgconfig/muparser.pc
%{_libdir}/cmake/muparser/*.cmake

%changelog
%autochangelog
