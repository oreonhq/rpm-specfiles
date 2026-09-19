%global source0_hash e9c60fddb2614f113ab59ec620799d961db73979845e6e637c4a6fb72aee51cc

%ifarch s390x
%bcond libcerf 0
%else
%bcond libcerf 1
%endif

Name:           libecpint
Version:        1.0.7
Release:        17%{?dist}
Summary:        Efficient evaluation of integrals over ab initio effective core potentials
License:        MIT
Url:            https://github.com/robashaw/libecpint
Source0:        https://github.com/robashaw/libecpint/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Fix build with libcerf 3 - https://github.com/robashaw/libecpint/pull/66
Patch:          libecpint-cerf3.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.12
BuildRequires:  pugixml-devel
BuildRequires:  gtest-devel
%if %{with libcerf}
BuildRequires:  libcerf-devel >= 1.17
%else
Provides:       bundled(Faddeeva}
%endif
BuildRequires:  python3
BuildRequires:  doxygen
BuildRequires:  sphinx
Requires:       %{name}-common = %{version}-%{release}

%description
Libecpint is a C++ library for the efficient evaluation of integrals over ab
initio effective core potentials, using a mixture of generated, recursive
code and Gauss-Chebyshev quadrature. It is designed to be standalone and
generic.

%package common
Summary:        Architecture independent data files for libecpint
BuildArch:      noarch

%description common
This package contains architecture independent data files for libecpint

%package devel
Summary:        Devel package for libecpint
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libcerf-devel >= 1.17

%description devel
This package contains development headers and libraries for libecpint.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# gtest 1.17.0 requires C++17 or later
# https://github.com/robashaw/libecpint/issues/58
sed -r -i 's/\b(CMAKE_CXX_STANDARD[[:blank:]]+)11\b/\117/' CMakeLists.txt

%build
%cmake %{?with_libcerf:-DLIBECPINT_USE_CERF=ON}
%cmake_build

%install
%cmake_install

%check
%ctest %{?testargs}

%files
%doc README.md CITATION
%{_libdir}/lib*.so.*

%files common
%{_datadir}/%{name}
%license LICENSE

%files devel
%{_includedir}/libecpint/
%{_includedir}/libecpint.hpp
%{_libdir}/cmake/ecpint
%{_libdir}/lib*.so

%changelog
%autochangelog
