%global source0_hash 9dd4dfb590c77e4f6aff68296602de58422eed5e7148fc29190d875a4e7d0f53
%global pkg_name lazysmallcheck
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.6
Release:        1%{?dist}
Summary:        A library for demand-driven testing of Haskell programs
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/lazysmallcheck
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
Lazy SmallCheck is a library for exhaustive, demand-driven testing of Haskell
programs. It is based on the idea that if a property holds for a
partially-defined input then it must also hold for all fully-defined
refinements of the that input. Compared to ``eager'' input generation as in
SmallCheck, Lazy SmallCheck may require significantly fewer test-cases to
verify a property for all inputs up to a given depth.

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

%files -f %{oreon_filedir}/main.list
%files -n ghc-lazysmallcheck-devel -f %{oreon_filedir}/ghc-lazysmallcheck-devel.list
%files -n ghc-lazysmallcheck-doc -f %{oreon_filedir}/ghc-lazysmallcheck-doc.list
%files -n ghc-lazysmallcheck-prof -f %{oreon_filedir}/ghc-lazysmallcheck-prof.list

%changelog

%autochangelog
