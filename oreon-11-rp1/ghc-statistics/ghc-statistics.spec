%global source1_hash f7777a7931b40332ebbc716f64abb63697cbab0128e5c1228d47760c5597f2d4
%global source0_hash de716430f95505903a397b4dcbb00c5c82d8956487826ab2e81ffee711b41b42
%global pkg_name statistics
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global denselinearalgebra dense-linear-algebra-0.1.0.0
%global subpkgs %{denselinearalgebra}
Name:           ghc-%{pkg_name}
Version:        0.16.5.0
Release:        24%{?dist}
Summary:        A library of statistical types, data, and functions
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/statistics
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{denselinearalgebra}/%{denselinearalgebra}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-data-default-class-devel
BuildRequires:  ghc-data-default-class-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-math-functions-devel
BuildRequires:  ghc-math-functions-prof
BuildRequires:  ghc-mwc-random-devel
BuildRequires:  ghc-mwc-random-prof
BuildRequires:  ghc-parallel-devel
BuildRequires:  ghc-parallel-prof
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-vector-algorithms-devel
BuildRequires:  ghc-vector-algorithms-prof
BuildRequires:  ghc-vector-binary-instances-devel
BuildRequires:  ghc-vector-binary-instances-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-vector-th-unbox-devel
BuildRequires:  ghc-vector-th-unbox-prof
# /oreon:deps
%description
This library provides a number of common functions and types useful in
statistics. We focus on high performance, numerical robustness, and use of good
algorithms. Where possible, we provide references to the statistical
literature.

The library's facilities can be divided into four broad categories:

* Working with widely used discrete and continuous probability distributions.
(There are dozens of exotic distributions in use; we focus on the most common.)

* Computing with sample data: quantile estimation, kernel density estimation,
histograms, bootstrap methods, significance testing, and regression and
autocorrelation analysis.

* Random variate generation under several different distributions.

* Common statistical tests for significant differences between samples.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides the Haskell %{pkg_name} library development files.

%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem
%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif

%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)
%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif

%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l BSD-2-Clause %{denselinearalgebra}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
# End cabal-rpm setup

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-statistics-devel -f %{oreon_filedir}/ghc-statistics-devel.list
%files -n ghc-statistics-doc -f %{oreon_filedir}/ghc-statistics-doc.list
%files -n ghc-statistics-prof -f %{oreon_filedir}/ghc-statistics-prof.list

%changelog

%autochangelog
