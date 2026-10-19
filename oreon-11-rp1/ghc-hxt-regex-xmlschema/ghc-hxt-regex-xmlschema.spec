%global source0_hash b9b6bcfc7d8c5e9a0be87dc56b13a237a51ca2c19c6665a51378a9538b71d97a
%global pkg_name hxt-regex-xmlschema
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 0
Name:           ghc-%{pkg_name}
Version:        9.2.0.7
Release:        1%{?dist}
Summary:        A regular expression library for W3C XML Schema regular expressions
License:        MIT
URL:            https://hackage.haskell.org/package/hxt-regex-xmlschema
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-hxt-charproperties-devel
BuildRequires:  ghc-hxt-charproperties-prof
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
# /oreon:deps
%description
This library supports full W3C XML Schema regular expressions inclusive all
Unicode character sets and blocks. The complete grammar can be found under
<http://www.w3.org/TR/xmlschema11-2/#regexs>. It is implemented by the
technique of derivations of regular expressions.

The W3C syntax is extended to support not only union of regular sets, but also
intersection, set difference, exor. Matching of subexpressions is also
supported.

The library can be used for constricting lightweight scanners and tokenizers.
It is a standalone library, no external regex libraries are used.

Extensions in 9.2: The library does nor only support String's, but also
ByteString's and Text in strict and lazy variants.

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
%files -n ghc-hxt-regex-xmlschema-devel -f %{oreon_filedir}/ghc-hxt-regex-xmlschema-devel.list
%files -n ghc-hxt-regex-xmlschema-doc -f %{oreon_filedir}/ghc-hxt-regex-xmlschema-doc.list
%files -n ghc-hxt-regex-xmlschema-prof -f %{oreon_filedir}/ghc-hxt-regex-xmlschema-prof.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.2.0.7-1
- Prepare for Oreon 11 (RP1)
