%global source3_hash 3d4b74d802923dc17491980b32e27e70ad93405432f254997f877beda794a24d
%global source2_hash cc75dca35e8473d6e0c7419fd5a577c2cbb202b3ae0d8af237756c2aeb7cdfe2
%global source1_hash 39fbae9e8c2a5193c07afeea34173e5022f82885d6cbb32062b5f1645c44408d
%global source0_hash d613d80c91b40058e90b7ee11c4bb27ca73aae27da4885d03237fd156408e038
%global pkg_name criterion
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global binaryorphans binary-orphans-1.0.5
%global criterionmeasurement criterion-measurement-0.2.3.0
%global subpkgs %{binaryorphans} %{criterionmeasurement}
%bcond tests 0
Name:           ghc-%{pkg_name}
Version:        1.6.5.0
Release:        1%{?dist}
Summary:        Robust, reliable performance measurement and analysis
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/criterion
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{binaryorphans}/%{binaryorphans}.tar.gz
Source2:        https://hackage.haskell.org/package/%{criterionmeasurement}/%{criterionmeasurement}.tar.gz
Source3:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Glob-devel
BuildRequires:  ghc-Glob-prof
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-compat-batteries-devel
BuildRequires:  ghc-base-compat-batteries-prof
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-base-compat-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-cassava-devel
BuildRequires:  ghc-cassava-prof
BuildRequires:  ghc-code-page-devel
BuildRequires:  ghc-code-page-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-js-chart-devel
BuildRequires:  ghc-js-chart-prof
BuildRequires:  ghc-microstache-devel
BuildRequires:  ghc-microstache-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-mwc-random-devel
BuildRequires:  ghc-mwc-random-prof
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-optparse-applicative-prof
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-prettyprinter-ansi-terminal-devel
BuildRequires:  ghc-prettyprinter-ansi-terminal-prof
BuildRequires:  ghc-prettyprinter-devel
BuildRequires:  ghc-prettyprinter-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-statistics-devel
BuildRequires:  ghc-statistics-prof
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-compat-devel
BuildRequires:  ghc-transformers-compat-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-vector-algorithms-devel
BuildRequires:  ghc-vector-algorithms-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
# /oreon:deps
%description
This library provides a powerful but simple way to measure software
performance. It provides both a framework for executing and analysing
benchmarks and a set of driver functions that makes it easy to build and run
benchmarks, and to analyse their results.

The fastest way to get started is to read the
<http://www.serpentine.com/criterion/tutorial.html online tutorial>, followed
by the documentation and examples in the "Criterion.Main" module.

For examples of the kinds of reports that criterion generates, see
<http://www.serpentine.com/criterion the home page>.

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
%ghc_lib_subpackage -l BSD-3-Clause %{binaryorphans}
%ghc_lib_subpackage -l BSD-3-Clause %{criterionmeasurement}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1 -a2
dos2unix -k -n %{SOURCE3} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
PATH=%{buildroot}%{_bindir}:$PATH
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-criterion-devel -f %{oreon_filedir}/ghc-criterion-devel.list
%files -n ghc-criterion-doc -f %{oreon_filedir}/ghc-criterion-doc.list
%files -n ghc-criterion-prof -f %{oreon_filedir}/ghc-criterion-prof.list

%changelog

%autochangelog
