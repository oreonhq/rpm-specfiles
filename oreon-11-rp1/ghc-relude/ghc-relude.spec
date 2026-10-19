%global source1_hash 8cde8eb1dc75161ecc64922ce9944aeaeeea2775d8af967dcc12364c6a0f7dfd
%global source0_hash 91eda82d135af2f15fa9adf050f35e22bb01710192cdede9fb8ce8d8145dc5a0
%global pkg_name relude
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        1.2.2.2
Release:        1%{?dist}
Summary:        Safe, performant, user-friendly and lightweight Haskell Standard Library
License:        MIT
URL:            https://hackage.haskell.org/package/relude
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
# /oreon:deps
%description
'relude' is an alternative prelude library. If you find the default
'Prelude' unsatisfying, despite its advantages, consider using 'relude'
instead.

== Relude goals and design principles

* Productivity: You can be more productive with a "non-standard"
standard library, and 'relude' helps you with writing safer and more
efficient code faster.

* Total programming: Usage of partial functions can lead to unexpected
bugs and runtime exceptions in pure code. The types of partial
functions lie about their behavior. And even if it is not always
possible to rely only on total functions, 'relude' strives to
encourage best-practices and reduce the chances of introducing a bug.

* Type-safety: We use the "make invalid states unrepresentable" motto as
one of our guiding principles. If it is possible, we express this concept
through the types. Example: ' whenNotNull :: Applicative f => [a] ->
(NonEmpty a -> f ()) -> f () '

* Performance: We prefer 'Text' over 'String', use space-leaks-free
functions (e.g. our custom performant 'sum' and 'product'),
introduce 'INLINE' and 'SPECIALIZE' pragmas where appropriate,
and make efficient container types (e.g. 'Map', 'HashMap', 'Set') more
accessible.

* Minimalism (low number of dependencies): We do not force users of
'relude' to stick to any specific lens or text formatting or logging library.
Where possible, 'relude' depends only on boot libraries.

* Convenience: Despite minimalism, we want to bring commonly used types and
functions into scope, and make available functions easier to use.

* Excellent documentation:
1. Tutorial
2. Migration guide from 'Prelude'
3. Haddock for every function with examples tested by doctest
4. Documentation regarding internal module structure
5. 'relude'-specific HLint rules

* User-friendliness: Anyone should be able to quickly migrate to 'relude'.
Only some basic familiarity with the common libraries like 'text' and
'containers' should be enough (but not necessary).

* Exploration: We have space to experiment with new ideas and proposals
without introducing breaking changes. 'relude' uses the approach with 'Extra.*'
modules which are not exported by default. The chosen approach makes it quite
easy for us to provide new functionality without breaking anything and let the
users decide to use it or not.

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
dos2unix -k -n %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-relude-devel -f %{oreon_filedir}/ghc-relude-devel.list
%files -n ghc-relude-doc -f %{oreon_filedir}/ghc-relude-doc.list
%files -n ghc-relude-prof -f %{oreon_filedir}/ghc-relude-prof.list

%changelog

%autochangelog
