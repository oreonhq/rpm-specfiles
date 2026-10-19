%global source1_hash 3886299908d1a2f9cb53c2bc26cb9944f8e746192794a2f40e57f8ea8e2e13e3
%global source0_hash 445dda4f2771f53b13e771b9889718d750dae06026085a25a66d473da821cd4f
%global pkg_name explicit-exception
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.2.0.2
Release:        1%{?dist}
Summary:        Exceptions which are explicit in the type signature
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/explicit-exception
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-semigroups-devel
BuildRequires:  ghc-semigroups-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
# /oreon:deps
%description
Synchronous and Asynchronous exceptions which are explicit in the type
signature. The first ones are very similar to 'Either' and
'Control.Monad.Error.ErrorT'. The second ones are used for 'System.IO.readFile'
and 'System.IO.hGetContents'. This package is a proposal for improved exception
handling in Haskell. It strictly separates between handling of exceptional
situations (file not found, invalid user input, see
<http://wiki.haskell.org/Exception>) and (programming) errors (division by
zero, index out of range, see <http://wiki.haskell.org/Error>).
Handling of the first one is called "exception handling", whereas handling of
errors is better known as "debugging".

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

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
cp -bp %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-explicit-exception-devel -f %{oreon_filedir}/ghc-explicit-exception-devel.list
%files -n ghc-explicit-exception-doc -f %{oreon_filedir}/ghc-explicit-exception-doc.list
%files -n ghc-explicit-exception-prof -f %{oreon_filedir}/ghc-explicit-exception-prof.list

%changelog

%autochangelog
