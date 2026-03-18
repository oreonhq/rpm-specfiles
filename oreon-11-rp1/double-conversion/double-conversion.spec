Summary:        Library providing binary-decimal and decimal-binary routines for IEEE doubles
Name:           double-conversion
Version:        3.4.0
Release:        3%{?dist}

License:        BSD-3-Clause
URL:            https://github.com/google/double-conversion
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
Provides binary-decimal and decimal-binary routines for IEEE doubles.
The library consists of efficient conversion routines that have been
extracted from the V8 JavaScript engine. The code has been re-factored
and improved so that it can be used more easily in other projects.

%package devel
Summary:        %{summary}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-static < 3.1.5-10

%description devel
Contains header files for developing applications that use the %{name}
library.

There is extensive documentation in src/double-conversion.h. Other
examples can be found in test/cctest/test-conversions.cc.

%prep
%autosetup -p1

%build
%cmake -DBUILD_TESTING=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md AUTHORS Changelog
%{_libdir}/libdouble-conversion.so.3{,.*}

%files devel
%{_libdir}/libdouble-conversion.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/
%{_includedir}/%{name}/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.4.0-3
- Prepare for Oreon 11 (RP1)
