%global source1_hash 415ae0463233b7a73027a7f7409bc12208a72946ebf22eda584ac9454f3c0b67
%global source0_hash 67199e97d398403b433be8490440e1ed4c1dc3f03f9de737c512bad1ca9f9e59
%{?haskell_setup}
%global happylib_ver 2.2.1
%global happylib happy-lib-%{happylib_ver}
%global subpkgs %{happylib}
%bcond tests 0
Name:           happy
Version:        2.2.1
Release:        1%{?dist}
Summary:        Parser Generator for Haskell
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/happy
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{happylib}/%{happylib}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
%if %{with ghc_prof}
%endif
Requires:       ghc-happy-lib-common
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  libxml2
BuildRequires:  libxslt
BuildRequires:  make
# /oreon:deps
%description
Happy is a parser generator for Haskell. Given a grammar specification in BNF,
Happy generates Haskell code to parse the grammar. Happy works in a similar way
to the 'yacc' tool for C.

%global main_version %{version}

%package -n ghc-happy-lib-common
Version: %{happylib_ver}
Summary: Common data files for happy-lib
BuildArch: noarch
License: BSD-2-Clause
%description -n ghc-happy-lib-common
This package provides the data files for the happy-lib library.

%if %{defined ghclibdir}
%ghc_lib_subpackage -l BSD-2-Clause -c ghc-happy-lib-common %{happylib}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -a1
# End cabal-rpm setup

%build

%ghc_libs_build %{subpkgs}
%ghc_bin_build
%install
%ghc_libs_install %{subpkgs}
%ghc_bin_install
%oreon_autofiles ghc-happy-lib-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
PATH=%{buildroot}%{_bindir}:$PATH
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-happy-lib-common -f %{oreon_filedir}/ghc-happy-lib-common.list

%changelog

%autochangelog
