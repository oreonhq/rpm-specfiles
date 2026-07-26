%global source0_hash 8b602df74c7be83d501532565deafd1b7881946d94789122f24c309a669298ab

%global soname 2

Name:    xcfun
Version: 2.1.1
Release: 21%{?dist}
Summary: A library of approximate exchange-correlation functionals
License: MPL-2.0
URL:     https://xcfun.readthedocs.io
Source0: https://github.com/dftlibs/xcfun/archive/v%{version}/%{name}-%{version}.tar.gz

# Patch out potential array overflow
Patch0:  https://github.com/dftlibs/xcfun/pull/154.patch
# Fix build on 32-bit architectures
Patch1:  https://github.com/dftlibs/xcfun/pull/155.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gcc-gfortran
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: pybind11-devel

# For tests
BuildRequires: python3-numpy
BuildRequires: python3-pytest

%description
XCFun is a library of approximate exchange-correlation functionals,
used in the Density Functional Theory description of electronic
structure. Because XCFun is based on automatic differentiation the
library can provide arbitrary order derivatives of all supported
functionals. Only the exchange-correlation energy expression needs to
be implemented, which is a huge gain in productivity (and also
efficiency). For this reason the library is very well suited for high
order time dependent DFT or for the development of new functionals.

%package devel
Summary:  Development headers and libraries for XCFun
Requires: %{name}%{?_isa} = %{version}-%{release}
# For dir ownership
Requires: cmake

%description devel
XCFun is a library of approximate exchange-correlation functionals,
used in the Density Functional Theory description of electronic
structure. Because XCFun is based on automatic differentiation the
library can provide arbitrary order derivatives of all supported
functionals. Only the exchange-correlation energy expression needs to
be implemented, which is a huge gain in productivity (and also
efficiency). For this reason the library is very well suited for high
order time dependent DFT or for the development of new functionals.

This package contains the development headers and libraries necessary
to compile code against XCFun.

%package -n python3-xcfun
Summary:  Python bindings for XCFun

%description -n python3-xcfun
XCFun is a library of approximate exchange-correlation functionals,
used in the Density Functional Theory description of electronic
structure. Because XCFun is based on automatic differentiation the
library can provide arbitrary order derivatives of all supported
functionals. Only the exchange-correlation energy expression needs to
be implemented, which is a huge gain in productivity (and also
efficiency). For this reason the library is very well suited for high
order time dependent DFT or for the development of new functionals.

This package contains the Python bindings for XCFun.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .overflow
%patch -P1 -p1 -b .32bit

%build
%cmake -B %{_host} -DCMAKE_BUILD_TYPE=RelWithDebInfo -DLIB=%{_lib} -DXCFUN_PYTHON_INTERFACE=ON -DPYMOD_INSTALL_LIBDIR=../../%{python3_sitearch}
%make_build -C %{_host}

%install
%make_install -C %{_host}
# Fix test permissions
chmod u=rwX,og=rX -R %{buildroot}%{python3_sitearch}/xcfun/tests

%check
cd %{_host}
ctest --output-on-failure

%files
%license LICENSE.md
%doc CHANGELOG.md README.md
%{_libdir}/libxcfun.so.%{soname}*

%files devel
%{_datadir}/cmake/XCFun/
%{_includedir}/XCFun/
%{_libdir}/libxcfun.so

%files -n python3-xcfun
%{python3_sitearch}/xcfun

%changelog
%autochangelog
