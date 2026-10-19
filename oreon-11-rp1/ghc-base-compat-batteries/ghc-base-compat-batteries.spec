%global source0_hash 4c166cccd33a82714153839a9a2b31f1d4e0a91c00a4a9277c29364b80a94ab8
%global pkg_name base-compat-batteries
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        0.15.0
Release:        1%{?dist}
Summary:        Base-compat with extra batteries
License:        MIT
URL:            https://hackage.haskell.org/package/base-compat-batteries
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-base-compat-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-discover-devel
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
Provides functions available in later versions of 'base' to a wider range of
compilers, without requiring you to use CPP pragmas in your code.
the suffix '.Repl.Batteries', which are distinct from anything in

depends on compatibility packages (such as 'semigroups') to offer a wider
support window than 'base-compat', which has no dependencies. Most of the

See
'<https://github.com/haskell-compat/base-compat/blob/master/base-compat/README.markdown#dependencies
here>' for a more comprehensive list of differences between 'base-compat' and
'base-compat-batteries'.

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
This package provides the Haskell %{pkg_name} library
documentation.
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
%files -n ghc-base-compat-batteries-devel -f %{oreon_filedir}/ghc-base-compat-batteries-devel.list
%files -n ghc-base-compat-batteries-doc -f %{oreon_filedir}/ghc-base-compat-batteries-doc.list
%files -n ghc-base-compat-batteries-prof -f %{oreon_filedir}/ghc-base-compat-batteries-prof.list

%changelog

%autochangelog
