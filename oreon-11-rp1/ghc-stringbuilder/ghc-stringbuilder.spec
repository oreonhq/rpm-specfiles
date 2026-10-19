%global source0_hash d878bdc4da806dbce5ab684ef13d2634c17c15b991d0ed3bb25a331eba6603ba
%global pkg_name stringbuilder
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        0.5.1
Release:        1%{?dist}
Summary:        A writer monad for multi-line string literals
License:        MIT
URL:            https://hackage.haskell.org/package/stringbuilder
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
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
A string builder can be used to construct multi-line string literals in a
monadic way. This is primarily meant for test suites that use a lot of
multi-line string literals, and when it really matters that the syntax is as
easy on the eyes as it can get.

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
%files -n ghc-stringbuilder-devel -f %{oreon_filedir}/ghc-stringbuilder-devel.list
%files -n ghc-stringbuilder-doc -f %{oreon_filedir}/ghc-stringbuilder-doc.list
%files -n ghc-stringbuilder-prof -f %{oreon_filedir}/ghc-stringbuilder-prof.list

%changelog

%autochangelog
