%global source0_hash febb957baed8445a60660859cd2b845dc166ecf48a03c6d55babe86e88cc0470
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%global blaslib flexiblas
%global cmake_blas_flags -DBLAS_TYPE=FLEXIBLAS -DLAPACK_TYPE=FLEXIBLAS
%else
%global blaslib openblas
%global blasvar o
%global cmake_blas_flags -DBLAS_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so -DLAPACK_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so
%endif
%undefine __cmake_in_source_build
%global soversion 2
Name:           mopac
Version:        23.2.5
Release:        1%{?dist}
Summary:        A semiempirical quantum chemistry program
License:        Apache-2.0
URL:            http://openmopac.net
Source0:        https://github.com/openmopac/mopac/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         mopac-22.0.5-rpath.patch
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
# /oreon:deps
%description
The modern open-source version of the Molecular Orbital PACkage
(MOPAC), a semiempirical quantum chemistry program based on Dewar and
Thiel's NDDO approximation.

%package libs
Summary:        MOPAC runtime libraries
%description libs
This package contains MOPAC's runtime libraries.

%package devel
Summary:        MOPAC development library
Requires:       %{name}-libs%{_isa} = %{version}-%{release}
%description devel
This package contains MOPAC's development library.

%prep

%setup -q
%patch -P1 -p1 -b .rpath

%build

%cmake -DENABLE_MKL=OFF -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=OFF \
       %{cmake_blas_flags}
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export OMP_NUM_THREADS=1
%ctest
%files -f %{oreon_filedir}/main.list
%files -n mopac-libs -f %{oreon_filedir}/mopac-libs.list
%files -n mopac-devel -f %{oreon_filedir}/mopac-devel.list

%changelog

%autochangelog
