%global source0_hash df481dc960e2c59a30395f7335031fd4ef8773b8a42894a4f2320e00ff474418
%bcond tests 1
Name:           alex
Version:        3.5.4.2
Release:        1%{?dist}
Summary:        Tool for generating lexical analysers in Haskell
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/alex
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  docbook-style-xsl
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  libxslt
BuildRequires:  make
# /oreon:deps
%description
Alex is a tool for generating lexical analysers in Haskell. It takes a
description of tokens based on regular expressions and generates a Haskell
module containing code for scanning text efficiently. It is similar to the tool
lex or flex for C/C++.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q
# End cabal-rpm setup

%build

%ghc_bin_build
%install
%ghc_bin_install
%oreon_autofiles main

%check

%if %{with tests}
PATH=%{buildroot}%{_bindir}:$PATH
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
