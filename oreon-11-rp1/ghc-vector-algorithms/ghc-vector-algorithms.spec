%global source1_hash 83d27cee5be1d5342ddbf39999d0c8ea54cb433d0891eea5471fbfaa29f8dec5
%global source0_hash d2b674676802670d8a682b357da6b6b5741b4a33b191f0ffe5f2b2bc40558eb2
%global pkg_name vector-algorithms
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global bitvec bitvec-1.1.5.0
%global subpkgs %{bitvec}
%bcond tests 0
Name:           ghc-%{pkg_name}
Version:        0.9.1.0
Release:        7%{?dist}
Summary:        Efficient algorithms for vector arrays
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/vector-algorithms
Source0:        https://hackage.haskell.org/package/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{bitvec}/%{bitvec}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-ghc-bignum-devel
BuildRequires:  ghc-ghc-bignum-prof
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
# /oreon:deps
%description
Efficient algorithms for sorting vector arrays. At some stage other vector
algorithms may be added.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides the Haskell %{pkg_name} library development
files.

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
%ghc_lib_subpackage -l BSD-3-Clause %{bitvec}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
# End cabal-rpm setup
cabal-tweak-remove-upperbound QuickCheck

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-vector-algorithms-devel -f %{oreon_filedir}/ghc-vector-algorithms-devel.list
%files -n ghc-vector-algorithms-doc -f %{oreon_filedir}/ghc-vector-algorithms-doc.list
%files -n ghc-vector-algorithms-prof -f %{oreon_filedir}/ghc-vector-algorithms-prof.list

%changelog

%autochangelog
