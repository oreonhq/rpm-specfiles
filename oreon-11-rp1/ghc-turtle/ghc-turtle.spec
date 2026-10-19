%global source1_hash 75710c60388e572bc17cbb08a81cbb4537f2207f8dcf187e9b1928d1e0b023a6
%global source0_hash 1a0166b11566e956bcec6f37cfcfc4d0647d4540479545d4858d2ff8c43a5b2d
%global pkg_name turtle
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        1.6.2
Release:        1%{?dist}
Summary:        Shell programming, Haskell-style
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/turtle
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-ansi-wl-pprint-devel
BuildRequires:  ghc-ansi-wl-pprint-prof
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-clock-devel
BuildRequires:  ghc-clock-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-doctest-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-foldl-devel
BuildRequires:  ghc-foldl-prof
BuildRequires:  ghc-hostname-devel
BuildRequires:  ghc-hostname-prof
BuildRequires:  ghc-managed-devel
BuildRequires:  ghc-managed-prof
BuildRequires:  ghc-optional-args-devel
BuildRequires:  ghc-optional-args-prof
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-optparse-applicative-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-streaming-commons-prof
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-temporary-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unix-compat-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
# /oreon:deps
%description
'turtle' is a reimplementation of the Unix command line environment in Haskell
so that you can use Haskell as both a shell and a scripting language.

Features include:

* Batteries included: Command an extended suite of predefined utilities

* Interoperability: You can still run external shell commands

* Portability: Works on Windows, OS X, and Linux

* Exception safety: Safely acquire and release resources

* Streaming: Transform or fold command output in constant space

* Patterns: Use typed regular expressions that can parse structured values

* Formatting: Type-safe 'printf'-style text formatting

* Modern: Supports 'text'

Read "Turtle.Tutorial" for a detailed tutorial or "Turtle.Prelude" for a
quick-start guide

'turtle' is designed to be beginner-friendly, but as a result lacks certain
features, like tracing commands. If you feel comfortable using 'turtle' then
you should also check out the 'Shelly' library which provides similar
functionality.

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
Obsoletes:      %{name}-devel-doc < %{version}-%{release}
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

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-turtle-devel -f %{oreon_filedir}/ghc-turtle-devel.list
%files -n ghc-turtle-doc -f %{oreon_filedir}/ghc-turtle-doc.list
%files -n ghc-turtle-prof -f %{oreon_filedir}/ghc-turtle-prof.list

%changelog

%autochangelog
