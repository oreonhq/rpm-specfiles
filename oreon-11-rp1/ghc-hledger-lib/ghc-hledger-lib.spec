%global source4_hash a14df4e578db371e5c609f0784209144545f9cae90026d24a3398042f7c591ea
%global source3_hash bbe62357e944549ce7f45c8f998e82b4d90c5aff6462446fb01cf32cddb744f4
%global source2_hash 2fb6ce7fba65414a5fc389cd9a6236c40d34339b5341238358ac88b6e5a6cc1d
%global source1_hash 4631963337675db145c2bf9752bf27b4bae68b7c48ffcac60b428f557b63e786
%global source0_hash c709c4b7f0c1882e22ec47c1f31e5c5746bf2126cb998f6036a09937fb1be6cd
%global pkg_name hledger-lib
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global cassavamegaparsec cassava-megaparsec-2.1.1
%global encoding encoding-0.10.2
%global lucid lucid-2.11.20250303
%global timeit timeit-2.0
%global subpkgs %{cassavamegaparsec} %{encoding} %{lucid} %{timeit}
%bcond tests 0
Name:           ghc-%{pkg_name}
Version:        1.52.4
Release:        1%{?dist}
Summary:        A library providing the core functionality of hledger
License:        GPL-3.0-or-later
URL:            https://hackage.haskell.org/package/hledger-lib
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{cassavamegaparsec}/%{cassavamegaparsec}.tar.gz
Source2:        https://hackage.haskell.org/package/%{encoding}/%{encoding}.tar.gz
Source3:        https://hackage.haskell.org/package/%{lucid}/%{lucid}.tar.gz
Source4:        https://hackage.haskell.org/package/%{timeit}/%{timeit}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Decimal-devel
BuildRequires:  ghc-Decimal-prof
BuildRequires:  ghc-Glob-devel
BuildRequires:  ghc-Glob-prof
BuildRequires:  ghc-OneTuple-devel
BuildRequires:  ghc-OneTuple-prof
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-aeson-pretty-prof
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-ansi-terminal-prof
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-blaze-builder-prof
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-blaze-markup-devel
BuildRequires:  ghc-blaze-markup-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-call-stack-devel
BuildRequires:  ghc-call-stack-prof
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-cassava-devel
BuildRequires:  ghc-cassava-prof
BuildRequires:  ghc-cmdargs-devel
BuildRequires:  ghc-cmdargs-prof
BuildRequires:  ghc-colour-devel
BuildRequires:  ghc-colour-prof
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-conduit-extra-prof
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-data-fix-devel
BuildRequires:  ghc-data-fix-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-doclayout-devel
BuildRequires:  ghc-doclayout-prof
BuildRequires:  ghc-doctest-devel
BuildRequires:  ghc-extensible-exceptions-devel
BuildRequires:  ghc-extensible-exceptions-prof
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-extra-prof
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-file-embed-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-foldl-devel
BuildRequires:  ghc-foldl-prof
BuildRequires:  ghc-ghc-bignum-devel
BuildRequires:  ghc-ghc-bignum-prof
BuildRequires:  ghc-ghc-devel
BuildRequires:  ghc-ghc-prof
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-hashtables-devel
BuildRequires:  ghc-hashtables-prof
BuildRequires:  ghc-haskeline-devel
BuildRequires:  ghc-haskeline-prof
BuildRequires:  ghc-integer-logarithms-devel
BuildRequires:  ghc-integer-logarithms-prof
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-megaparsec-prof
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-microlens-prof
BuildRequires:  ghc-microlens-th-devel
BuildRequires:  ghc-microlens-th-prof
BuildRequires:  ghc-mmorph-devel
BuildRequires:  ghc-mmorph-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-old-time-devel
BuildRequires:  ghc-old-time-prof
BuildRequires:  ghc-parser-combinators-devel
BuildRequires:  ghc-parser-combinators-prof
BuildRequires:  ghc-pretty-simple-devel
BuildRequires:  ghc-pretty-simple-prof
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-profunctors-devel
BuildRequires:  ghc-profunctors-prof
BuildRequires:  ghc-regex-compat-devel
BuildRequires:  ghc-regex-compat-prof
BuildRequires:  ghc-regex-tdfa-devel
BuildRequires:  ghc-regex-tdfa-prof
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-splitmix-devel
BuildRequires:  ghc-splitmix-prof
BuildRequires:  ghc-strict-devel
BuildRequires:  ghc-strict-prof
BuildRequires:  ghc-tabular-devel
BuildRequires:  ghc-tabular-prof
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-hunit-prof
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-terminal-size-devel
BuildRequires:  ghc-terminal-size-prof
BuildRequires:  ghc-terminfo-devel
BuildRequires:  ghc-terminfo-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-text-short-devel
BuildRequires:  ghc-text-short-prof
BuildRequires:  ghc-these-devel
BuildRequires:  ghc-these-prof
BuildRequires:  ghc-time-compat-devel
BuildRequires:  ghc-time-compat-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-uglymemo-devel
BuildRequires:  ghc-uglymemo-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-utf8-string-prof
BuildRequires:  ghc-uuid-types-devel
BuildRequires:  ghc-uuid-types-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
# /oreon:deps
%description
This library contains hledger's core functionality. It is used by most hledger*
packages so that they support the same command line options, file formats,
reports, etc.

hledger is a robust, cross-platform set of tools for tracking money, time, or
any other commodity, using double-entry accounting and a simple, editable file
format, with command-line, terminal and web interfaces. It is a Haskell rewrite
of Ledger, and one of the leading implementations of Plain Text Accounting.
Read more at: <https://hledger.org>.

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

%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l MIT %{cassavamegaparsec}
%ghc_lib_subpackage -l BSD-3-Clause %{encoding}
%ghc_lib_subpackage -l BSD-3-Clause %{lucid}
%ghc_lib_subpackage -l BSD-3-Clause %{timeit}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1 -a2 -a3 -a4
# End cabal-rpm setup

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-hledger-lib-devel -f %{oreon_filedir}/ghc-hledger-lib-devel.list
%files -n ghc-hledger-lib-doc -f %{oreon_filedir}/ghc-hledger-lib-doc.list
%files -n ghc-hledger-lib-prof -f %{oreon_filedir}/ghc-hledger-lib-prof.list

%changelog

%autochangelog
