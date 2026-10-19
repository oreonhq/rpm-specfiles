%global source1_hash 1b61e76b974e217b33c9c676e950ea15df7ad900dedb54756276bb65d88b7f7d
%global source0_hash f7eeb82e55882b4d87bb5080694901381153cc70e53a6bb03f5b5518a3634595
%global pkg_name servant-foreign
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 0
Name:           ghc-%{pkg_name}
Version:        0.16.1
Release:        1%{?dist}
Summary:        Helpers for generating clients for servant APIs in any programming language
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/servant-foreign
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-base-compat-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-discover-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-lens-devel
BuildRequires:  ghc-lens-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-servant-devel
BuildRequires:  ghc-servant-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
# /oreon:deps
%description
Helper types and functions for generating client functions for servant APIs in
any programming language

This package provides types and functions that collect all the data needed to
generate client functions in the programming language of your choice.
This effectively means you only have to write the code that "pretty-prints"
this data as some code in your target language.

See the servant-js package for an example

<https://github.com/haskell-servant/servant/blob/master/servant-foreign/CHANGELOG.md
CHANGELOG>.

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
%files -n ghc-servant-foreign-devel -f %{oreon_filedir}/ghc-servant-foreign-devel.list
%files -n ghc-servant-foreign-doc -f %{oreon_filedir}/ghc-servant-foreign-doc.list
%files -n ghc-servant-foreign-prof -f %{oreon_filedir}/ghc-servant-foreign-prof.list

%changelog

%autochangelog
