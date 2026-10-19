%global source0_hash cc445d439ea2f65cac7604d3578aa2c3a62e5a91dc989f4ce5b3390db9e59636
%global pkg_name filepattern
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        0.1.3
Release:        1%{?dist}
Summary:        File path glob-like matching
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/filepattern
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
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-extra-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
A library for matching files using patterns such as '"src/**/*.png"' for all
'.png' files recursively under the 'src' directory. Features:

* All matching is /O(n)/. Most functions precompute some information given only
one argument.

* See "System.FilePattern" and '?==' simple matching and semantics.

* Use 'match' and 'substitute' to extract suitable strings from the '*' and
'**' matches, and substitute them back into other patterns.

* Use 'step' and 'matchMany' to perform bulk matching of many patterns against
many paths simultaneously.

* Use "System.FilePattern.Directory" to perform optimised directory traverals
using patterns.

Originally taken from the <https://hackage.haskell.org/package/shake Shake
library>.

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
%files -n ghc-filepattern-devel -f %{oreon_filedir}/ghc-filepattern-devel.list
%files -n ghc-filepattern-doc -f %{oreon_filedir}/ghc-filepattern-doc.list
%files -n ghc-filepattern-prof -f %{oreon_filedir}/ghc-filepattern-prof.list

%changelog

%autochangelog
