%global source0_hash f6641deb07fa69165b7815de9008af3ea47eb39b2bb97521fbf74c97aba6e844
%global build64 0
%if 0%{?__isa_bits} == 64
%global build64 1
%endif
%undefine _ld_as_needed
Name:		arpack
Version:	3.9.1
Release:        1%{?dist}
Summary:        Fortran 77 subroutines for solving large scale eigenvalue problems
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/opencollab/arpack-ng
Source0:        https://github.com/opencollab/arpack-ng/archive/%{version}/arpack-ng-%{version}.tar.gz
%if 0%{?__isa_bits} == 64
%endif
Provides:	arpack-ng = %{version}-%{release}
Provides:	arpack-ng%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  eigen3-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(flexiblas)
# /oreon:deps
%description
ARPACK is a collection of Fortran 77 subroutines designed to solve large
scale eigenvalue problems.

The package is designed to compute a few eigenvalues and corresponding
eigenvectors of a general n by n matrix A. It is most appropriate for
large sparse or structured matrices A where structured means that a
matrix-vector product w <- Av requires order n rather than the usual
order n**2 floating point operations. This software is based upon an
algorithmic variant of the Arnoldi process called the Implicitly
Restarted Arnoldi Method (IRAM).

%package devel
Summary:	Files needed for developing arpack based applications
Requires:	arpack%{?_isa} = %{version}-%{release}
Provides:	arpack-ng-devel = %{version}-%{release}
Provides:	arpack-ng-devel%{?_isa} = %{version}-%{release}
%description devel
ARPACK is a collection of Fortran 77 subroutines designed to solve
large scale eigenvalue problems. This package contains the so
library links used for building arpack based applications.

%package doc
Summary:	Examples for the use of arpack
BuildArch:	noarch
%description doc
This package contains examples for the use of arpack.

%package static
Summary:	Static library for developing arpack based applications
Requires:	arpack-devel%{?_isa} = %{version}-%{release}
Provides:	arpack-ng-static = %{version}-%{release}
Provides:	arpack-ng-static%{?_isa} = %{version}-%{release}
%description static
ARPACK is a collection of Fortran 77 subroutines designed to solve
large scale eigenvalue problems. This package contains the static
library and so links used for building arpack based applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc
mv arpack-ng-%{version} src
pushd src
autoreconf -vif
popd
cp -pr src src64

%build

pushd src
%configure --enable-shared --enable-static \
    --with-blas=-lflexiblas \
    --with-lapack=-lflexiblas \
%if 0%{?__isa_bits} == 64
    --enable-eigen \
%endif
    --enable-icb
%make_build
popd
pushd src64
%configure --enable-shared --enable-static \
    LIBSUFFIX=64 \
    INTERFACE64=1 \
    --with-blas=-lflexiblas64 \
    --with-lapack=-lflexiblas64 \
    --enable-eigen \
    --enable-icb
%make_build
popd
%install
pushd src
%make_install
popd
pushd src64
%make_install
popd
rm -r %{buildroot}%{_libdir}/*.la
%oreon_autofiles arpack-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles arpack-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles arpack-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd src
make check
pushd EXAMPLES ; make clean ; popd
popd
pushd src64
make check
pushd EXAMPLES ; make clean ; popd
popd
%files -f %{oreon_filedir}/main.list
%files -n arpack-devel -f %{oreon_filedir}/arpack-devel.list
%files -n arpack-doc -f %{oreon_filedir}/arpack-doc.list
%files -n arpack-static -f %{oreon_filedir}/arpack-static.list

%changelog

%autochangelog
