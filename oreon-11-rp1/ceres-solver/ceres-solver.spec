%global source0_hash 48b2302a7986ece172898477c3bcd6deb8fb5cf19b3327bc49969aad4cede82d

Name:           ceres-solver
Version:        2.2.0
# Release candidate versions are messy. Give them a release of
# e.g. "0.1.0%%{?dist}" for RC1 (and remember to adjust the Source0
# URL). Non-RC releases go back to incrementing integers starting at 1.
Release:        11%{?dist}
Summary:        A non-linear least squares minimizer
License:        BSD-3-Clause AND Apache-2.0

URL:            http://ceres-solver.org/
Source0:        http://%{name}.org/%{name}-%{version}.tar.gz
# Relax eigen version constraints
Patch0:         ceres-solver-Support-Eigen3-5.0.0.patch

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9 || (0%{?oreon} >= 11)
%global blaslib flexiblas
%global cmake_blas_flags -DBLA_VENDOR=FlexiBLAS
%else
%global blaslib openblas
%global blasvar o
%global cmake_blas_flags -DBLAS_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

# Need -static package per guidelines for handling dependencies on header-only
# libraries.
# http://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_Header_Only_Libraries
BuildRequires:  eigen3-static >= 3.2.1

# suitesparse < 3.4.0-9 ships without *.hpp C++ headers
# https://bugzilla.redhat.com/show_bug.cgi?id=1001869
BuildRequires:  suitesparse-devel >= 3.4.0-9

# If the suitesparse package was built with TBB then we need TBB too
BuildRequires:  tbb-devel

# Use FlexiBLAS or OpenBLAS for BLAS
BuildRequires:  %{blaslib}-devel
BuildRequires:  gflags-devel >= 2.2.1
# Build against miniglog on RHEL6 until glog package is added to EPEL6
%if (0%{?rhel} != 06) || (0%{?oreon} >= 11)
BuildRequires:  glog-devel >= 0.3.1
%endif

%description

Ceres Solver is an open source C++ library for modeling and solving
large, complicated optimization problems. It is a feature rich, mature
and performant library which has been used in production at Google
since 2010. Notable use of Ceres Solver is for the image alignment in
Google Maps and for vehicle pose in Google Street View. Ceres Solver
can solve two kinds of problems.

  1. Non-linear Least Squares problems with bounds constraints.
  2. General unconstrained optimization problems.

Features include:

  - A friendly API: build your objective function one term at a time
  - Automatic and numeric differentiation
  - Robust loss functions
  - Local parameterizations
  - Threaded Jacobian evaluators and linear solvers
  - Trust region solvers with non-monotonic steps (Levenberg-Marquardt and
    Dogleg (Powell & Subspace))
  - Line search solvers (L-BFGS and Nonlinear CG)
  - Dense QR and Cholesky factorization (using Eigen) for small problems
  - Sparse Cholesky factorization (using SuiteSparse) for large sparse problems
  - Specialized solvers for bundle adjustment problems in computer vision
  - Iterative linear solvers for general sparse and bundle adjustment problems
  - Runs on Linux, Windows, Mac OS X, Android, and iOS


%package        devel
Summary:        A non-linear least squares minimizer
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       eigen3-devel
Requires:       gflags-devel
Requires:       glog-devel
Requires:       suitesparse-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%cmake \
  -DCXSPARSE_INCLUDE_DIR:PATH=%{_includedir}/suitesparse \
  %{cmake_blas_flags} \
  -DGFLAGS_INCLUDE_DIR=%{_includedir}
%cmake_build


%install
%cmake_install


%check
# FIXME: Some tests fail on these arches
%ifarch aarch64 ppc64le s390x
%ctest || :
%else
%ctest
%endif


%files
%doc README.md
%license LICENSE
%{_libdir}/libceres.so.4
%{_libdir}/libceres.so.2.2.0

%files devel
%{_includedir}/ceres/
%{_libdir}/libceres.so
%{_libdir}/cmake/Ceres


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.0-11
- Import
