%global source0_hash 6e39dbfa1e6ad3730b006c8953a43cc6da3dfc91f00edeb68a641d364703b773
%global with_check 0
Name: qrmumps
Version: 3.1
Release:        1%{?dist}
Summary:        A multithreaded multifrontal QR solver
License: LGPL-3.0-or-later
URL: http://buttari.perso.enseeiht.fr/qr_mumps/
Source0:        https://gitlab.com/qr_mumps/qr_mumps/-/archive/%{version}/qr_mumps-%{version}.tar.gz
Requires: gcc-gfortran%{?_isa}
Provides: qr_mumps = 0:%{version}-%{release}
Obsoletes: qr_mumps < 0:3.0-1
Patch0:   %{name}-fix_libpaths+libsoname.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  flexiblas-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  metis-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  scotch-devel
BuildRequires:  suitesparse-devel
# /oreon:deps
%description
qr_mumps is a software package for the solution of sparse,
linear systems on multicore computers.
It implements a direct solution method based on the QR
factorization of the input matrix. Therefore, it is suited
to solving sparse least-squares problems and to computing
the minimum-norm solution of sparse, underdetermined problems.
It can obviously be used for solving square problems in which
case the stability provided by the use of orthogonal transformations
comes at the cost of a higher operation count with respect to solvers
based on, e.g., the LU factorization.
qr_mumps supports real and complex, single or double precision arithmetic.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Shared links and header files of %{name}.

%package benchmarks
Summary: Benchmark files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description benchmarks
Benchamrks to evaluate the performance of QRM are provided in
the =timing/= directory. These allow for running experiments on the
solution of dense and sparse linear systems through the $QR$ and
Cholesky factorizations. Use the =-h= command line argument to get
help on using these benchmarks.

%package doc
Summary: PDF/HTML documentation files of %{name}
BuildArch: noarch
%description doc
PDF documentation files of %{name}.

########################################################

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n qr_mumps-%{version} -p1

# Those files should actually be the ones provided by CMake itself.
rm -f aux/find/Find{BLAS,LAPACK}.cmake

%build

%cmake -Wno-dev -DQRM_VERSION:STRING=%{version} \
%if "%{?_lib}" == "lib64"
 %{?_cmake_lib_suffix64} \
%endif
 -DARITH="d;s;z;c" -DCMAKE_BUILD_TYPE:STRING=Release \
 -DQRM_ORDERING_AMD:BOOL=ON -DQRM_ORDERING_METIS:BOOL=ON \
 -DQRM_ORDERING_SCOTCH:BOOL=ON -DQRM_WITH_STARPU:BOOL=OFF \
 -DQRM_WITH_CUDA:BOOL=OFF -DAMD_INCLUDE_DIRS:PATH=%{_includedir}/suitesparse \
 -DBLA_VENDOR=FlexiBLAS \
 -DBLAS_VERBOSE:BOOL=ON -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DINCLUDE_INSTALL_DIR:PATH=%{_includedir}/qrm -DLIB_INSTALL_DIR:PATH=%{_libdir}
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if 0%{?with_check}
%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n qrmumps-devel -f %{oreon_filedir}/qrmumps-devel.list
%files -n qrmumps-benchmarks -f %{oreon_filedir}/qrmumps-benchmarks.list
%files -n qrmumps-doc -f %{oreon_filedir}/qrmumps-doc.list

%changelog

%autochangelog
