%global source0_hash f6ef4059090802713979ed7f8c526fe60fd80354251b6cfd75d79b5bfc43479d
%global pkg_name mwc-random
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%ifnarch i686 armv7hl
%bcond tests 0
%endif
Name:           ghc-%{pkg_name}
Version:        0.15.3.0
Release:        1%{?dist}
Summary:        Fast, high quality pseudo random number generation
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/mwc-random
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-doctest-devel
BuildRequires:  ghc-math-functions-devel
BuildRequires:  ghc-math-functions-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
# /oreon:deps
%description
A library for generating high quality random numbers that follow
either a uniform or normal distribution.  The generated numbers are
suitable for use in statistical applications.

The uniform PRNG uses Marsaglia's MWC256 (also known as MWC8222)
multiply-with-carry generator, which has a period of 2^8222 and fares well in
tests of randomness. It is also extremely fast, between 2 and 3 times faster
than the Mersenne Twister.

Compared to the mersenne-random package, this package has a more
convenient API, is faster, and supports more statistical distributions.

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

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-mwc-random-devel -f %{oreon_filedir}/ghc-mwc-random-devel.list
%files -n ghc-mwc-random-doc -f %{oreon_filedir}/ghc-mwc-random-doc.list
%files -n ghc-mwc-random-prof -f %{oreon_filedir}/ghc-mwc-random-prof.list

%changelog

%autochangelog
