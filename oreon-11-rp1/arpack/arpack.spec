%global source0_hash f6641deb07fa69165b7815de9008af3ea47eb39b2bb97521fbf74c97aba6e844

%global build64 0
%if 0%{?__isa_bits} == 64
%global build64 1
%endif

# We are linking FORTRAN symbols.  Thus we cannot link --as-needed.
%undefine _ld_as_needed

Name:		arpack
Version:	3.9.1
Release:	9%{dist}
Summary:	Fortran 77 subroutines for solving large scale eigenvalue problems

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/opencollab/arpack-ng
Source0:	https://github.com/opencollab/arpack-ng/archive/%{version}/arpack-ng-%{version}.tar.gz

%if 0%{?__isa_bits} == 64
BuildRequires:	eigen3-devel
%endif
BuildRequires:	gcc-c++
BuildRequires:	gcc-gfortran
BuildRequires:	pkgconfig(flexiblas)
BuildRequires:	libtool >= 2.4.2
BuildRequires:	make
Provides:	arpack-ng = %{version}-%{release}
Provides:	arpack-ng%{?_isa} = %{version}-%{release}

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
%if %{build64}
cp -pr src src64
%endif

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
%if %{build64}
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
%endif

%install
pushd src
%make_install
popd
%if %{build64}
pushd src64
%make_install
popd
%endif
# Get rid of .la files
rm -r %{buildroot}%{_libdir}/*.la

%check
# Run tests sequentially until upstream issue is fixed
# https://github.com/opencollab/arpack-ng/issues/439
pushd src
make check
pushd EXAMPLES ; make clean ; popd
popd
%if %{build64}
pushd src64
make check
pushd EXAMPLES ; make clean ; popd
popd
%endif

%files
%doc src/CHANGES src/README.md
%license src/COPYING
%{_libdir}/libarpack.so.2{,.*}
%if %{build64}
%{_libdir}/libarpack64.so.2{,.*}
%endif

%files devel
%{_libdir}/pkgconfig/arpack.pc
%{_libdir}/pkgconfig/parpack.pc
%{_libdir}/libarpack.so
%if %{build64}
%{_libdir}/pkgconfig/arpack64.pc
%{_libdir}/pkgconfig/parpack64.pc
%{_libdir}/libarpack64.so
%endif
%{_includedir}/arpack/

%files doc
%doc src/EXAMPLES/ src/DOCUMENTS/
%doc src/CHANGES src/README.md
%license src/COPYING

%files static
%{_libdir}/libarpack.a
%if %{build64}
%{_libdir}/libarpack64.a
%endif

%changelog
%autochangelog
