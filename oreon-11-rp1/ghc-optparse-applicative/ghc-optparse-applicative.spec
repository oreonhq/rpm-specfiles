%global source1_hash 4c1dcbdbf2498f7cdd88826e876403db7f8d81931962060ec4c3a57a186c6cc3
%global source0_hash cf16aeefd821730c7738447fa7c6b7ada7ca1c9cc25400d64ef283294d345871
%global pkg_name optparse-applicative
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 0
Name:           ghc-%{pkg_name}
Version:        0.19.0.0
Release:        1%{?dist}
Summary:        Utilities and combinators for parsing command line options
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/optparse-applicative
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-prettyprinter-ansi-terminal-devel
BuildRequires:  ghc-prettyprinter-ansi-terminal-prof
BuildRequires:  ghc-prettyprinter-devel
BuildRequires:  ghc-prettyprinter-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-compat-devel
BuildRequires:  ghc-transformers-compat-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
# /oreon:deps
%description
Optparse-applicative is a haskell library for parsing options on the command
line, and providing a powerful applicative interface for composing them.

optparse-applicative takes care of reading and validating the arguments passed
to the command line, handling and reporting errors, generating a usage line, a
comprehensive help screen, and enabling context-sensitive bash, zsh, and fish
completions.

See the included README for detailed instructions and examples, which is also
available on github <https://github.com/pcapriotti/optparse-applicative>.

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
dos2unix -k -n %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup
cabal-tweak-remove-upperbound QuickCheck

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
%files -n ghc-optparse-applicative-devel -f %{oreon_filedir}/ghc-optparse-applicative-devel.list
%files -n ghc-optparse-applicative-doc -f %{oreon_filedir}/ghc-optparse-applicative-doc.list
%files -n ghc-optparse-applicative-prof -f %{oreon_filedir}/ghc-optparse-applicative-prof.list

%changelog

%autochangelog
