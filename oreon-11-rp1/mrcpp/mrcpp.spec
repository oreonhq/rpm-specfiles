%global source0_hash ae3f66b25809751a17abe1695a7be74a52c51e3ba5b698800d456b397e1437b9
%global soname 1
Name:           mrcpp
Version:        1.5.0
Release:        10%{?dist}
Summary:        A numerical mathematics library based on multiresolution analysis
License:        LGPL-3.0-or-later
URL:            https://github.com/MRChemSoft/mrcpp/
Source0:        https://github.com/MRChemSoft/mrcpp/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         mrcpp-1.4.0-eigen3.patch
Patch1:         mrcpp-1.4.0-rpath.patch
Patch2:         mrcpp-1.5.0-catchv3.patch
Patch3:         mrcpp-1.5.0-cassert.patch
Requires:       %{name}-data = %{version}-%{release}
ExcludeArch:    s390x
# oreon:deps
BuildRequires:  catch-devel
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  eigen3-static
BuildRequires:  gcc-c++
BuildRequires:  json-devel
BuildRequires:  make
BuildRequires:  xcfun-devel
# /oreon:deps
%description
The MultiResolution Computation Program Package (MRCPP) is a general
purpose numerical mathematics library based on multiresolution
analysis and the multiwavelet basis which provide low-scaling
algorithms as well as rigorous error control in numerical
computations.

%package devel
Summary:        Development headers and libraries for mrcpp
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The MultiResolution Computation Program Package (MRCPP) is a general
purpose numerical mathematics library based on multiresolution
analysis and the multiwavelet basis which provide low-scaling
algorithms as well as rigorous error control in numerical
computations.

This package contains the development headers and libraries.

%package data
Summary:        Runtime data for mrcpp
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description data
The MultiResolution Computation Program Package (MRCPP) is a general
purpose numerical mathematics library based on multiresolution
analysis and the multiwavelet basis which provide low-scaling
algorithms as well as rigorous error control in numerical
computations.

This package contains the runtime data.

%prep

%setup -q
# EPEL still can't handle the new patch style
%patch -P0 -p1 -b .eigen3
%patch -P1 -p1 -b .rpath
%patch -P2 -p1 -b .catchv3
%patch -P3 -p1 -b .cassert
# Remove bundled catch
rm -rf external/catch/

%build

export CXXFLAGS="%{optflags} -I%{_includedir}/catch2"
%cmake -DENABLE_ARCH_FLAGS=OFF -DENABLE_OPENMP=ON -DCMAKE_BUILD_TYPE=Release
%cmake_build
%install
%cmake_install
rm %{buildroot}%{_bindir}/mrcpp-tests
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n mrcpp-devel -f %{oreon_filedir}/mrcpp-devel.list
%files -n mrcpp-data -f %{oreon_filedir}/mrcpp-data.list

%changelog

%autochangelog
