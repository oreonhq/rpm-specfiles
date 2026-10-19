%global source13_hash b09e6dca2cee09dfa4a0516df4c96410393711d11059226588a4e9dbc8c15cfd
%global source12_hash 33910f79ff3c17b6f3cc1068fdc4f94dafad87b0e079c4157eeba8686fdeaeb1
%global source11_hash c902dbaf0e9cf7056d786d44fbdea2781bc65524089639242c2624dae841ba1d
%global source10_hash 293e75f849254ce0ce0d7fa659681917e07a557c602505a2f9e20777467e984e
%global source9_hash 1bf88b8d2c4ac90dee3000684b6e0078502dc5a1030528b687aa143b3ecc1f02
%global source8_hash 939f728e5507c0d1427ef27ae8783ba082a79a10839f089ee02d6c9c6bf5de28
%global source7_hash e32d9efb7862507e76e3f6876c67c980da9a5b4d743e07d424159868ae471c67
%global source6_hash 09e5385852d02830152a4ef72a4928a7a3c9353a1fa6fc8510228d9215bfeab6
%global source5_hash 71aa17132bff71814d653caed8f9da55c27e3c3425eb4db404fa65b3ca296dfe
%global source4_hash f27e0a28459755f6c301eb9661f15230ccc6cf94f699d9aafb34ce659138dab5
%global source3_hash 2dbdc1850e6768fd5f4e4c45d011ef6796d8b2d639ec200da7f4407ae02d09a6
%global source2_hash 820613b12ce759c8c8a254c78a0e4c474b2cd4cfd08fc0c1d4d5584c58ff2288
%global source1_hash 3bc7e503c204990b47cf977b9ffa498c564086165fba4700512afc6b5e3c69c4
%global source0_hash a4f57af0da1c3fb05dc3b9c50c86ce3932614776d3b32b2ffcbbfa38e3eab8c5
%global pkg_name Agda
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global ListLike ListLike-4.7.8.4
%global apnormalize ap-normalize-0.1.0.1
%global fmlist fmlist-0.9.4
%global genericdata generic-data-1.1.0.2
%global murmurhash murmur-hash-0.1.0.11
%global nonemptycontainers nonempty-containers-0.3.5.0
%global nonemptyvector nonempty-vector-0.2.4
%global peano peano-0.1.1.0
%global pqueue pqueue-1.5.0.0
%global processextras process-extras-0.7.4
%global showcombinators show-combinators-0.2.0.0
%global vectorhashtables vector-hashtables-0.1.2.1
%global subpkgs %{apnormalize} %{fmlist} %{ListLike} %{murmurhash} %{nonemptyvector} %{nonemptycontainers} %{peano} %{pqueue} %{processextras} %{showcombinators} %{genericdata} %{vectorhashtables}
Name:           %{pkg_name}
Version:        2.8.0.2
Release:        1%{?dist}
Summary:        A dependently typed functional programming language and proof assistant
License:        MIT AND BSD-3-Clause
URL:            https://hackage.haskell.org/package/Agda
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{ListLike}/%{ListLike}.tar.gz
Source2:        https://hackage.haskell.org/package/%{apnormalize}/%{apnormalize}.tar.gz
Source3:        https://hackage.haskell.org/package/%{fmlist}/%{fmlist}.tar.gz
Source4:        https://hackage.haskell.org/package/%{genericdata}/%{genericdata}.tar.gz
Source5:        https://hackage.haskell.org/package/%{murmurhash}/%{murmurhash}.tar.gz
Source6:        https://hackage.haskell.org/package/%{nonemptycontainers}/%{nonemptycontainers}.tar.gz
Source7:        https://hackage.haskell.org/package/%{nonemptyvector}/%{nonemptyvector}.tar.gz
Source8:        https://hackage.haskell.org/package/%{peano}/%{peano}.tar.gz
Source9:        https://hackage.haskell.org/package/%{pqueue}/%{pqueue}.tar.gz
Source10:       https://hackage.haskell.org/package/%{processextras}/%{processextras}.tar.gz
Source11:       https://hackage.haskell.org/package/%{showcombinators}/%{showcombinators}.tar.gz
Source12:       https://hackage.haskell.org/package/%{vectorhashtables}/%{vectorhashtables}.tar.gz
Source13:       https://hackage.haskell.org/package/%{pkgver}/%{name}.cabal#/%{pkgver}.cabal
Source20:       agda-mode-init.el
ExcludeArch:    %{ix86} armv7hl
%if %{with clustercounting}
%endif
%if %{with ghc_prof}
%if %{with clustercounting}
%endif
%endif
Provides:       agda = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}
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
Provides:       emacs-agda = %{version}-%{release}
# oreon:deps
BuildRequires:  alex
BuildRequires:  emacs(bin)
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-STMonadTrans-devel
BuildRequires:  ghc-STMonadTrans-prof
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-ansi-terminal-prof
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-orphans-devel
BuildRequires:  ghc-base-orphans-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-boxes-devel
BuildRequires:  ghc-boxes-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-comonad-devel
BuildRequires:  ghc-comonad-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-data-hash-devel
BuildRequires:  ghc-data-hash-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-dlist-prof
BuildRequires:  ghc-edit-distance-devel
BuildRequires:  ghc-edit-distance-prof
BuildRequires:  ghc-enummapset-devel
BuildRequires:  ghc-enummapset-prof
BuildRequires:  ghc-equivalence-devel
BuildRequires:  ghc-equivalence-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-filelock-devel
BuildRequires:  ghc-filelock-prof
BuildRequires:  ghc-filemanip-devel
BuildRequires:  ghc-filemanip-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-generic-deriving-devel
BuildRequires:  ghc-generic-deriving-prof
BuildRequires:  ghc-ghc-boot-th-devel
BuildRequires:  ghc-ghc-boot-th-prof
BuildRequires:  ghc-ghc-compact-devel
BuildRequires:  ghc-ghc-compact-prof
BuildRequires:  ghc-gitrev-devel
BuildRequires:  ghc-gitrev-prof
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-haskeline-devel
BuildRequires:  ghc-haskeline-prof
BuildRequires:  ghc-indexed-traversable-devel
BuildRequires:  ghc-indexed-traversable-prof
BuildRequires:  ghc-invariant-devel
BuildRequires:  ghc-invariant-prof
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-monad-control-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-parallel-devel
BuildRequires:  ghc-parallel-prof
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-regex-tdfa-devel
BuildRequires:  ghc-regex-tdfa-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-semigroupoids-devel
BuildRequires:  ghc-semigroupoids-prof
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-strict-devel
BuildRequires:  ghc-strict-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-these-devel
BuildRequires:  ghc-these-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-uri-encode-devel
BuildRequires:  ghc-uri-encode-prof
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-utf8-string-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-zlib-devel
BuildRequires:  ghc-zlib-prof
BuildRequires:  happy
# /oreon:deps
%description
Agda is a dependently typed functional programming language: It has
inductive families, which are similar to Haskell's GADTs, but they can
be indexed by values and not just types. It also has parameterized
modules, mixfix operators, Unicode characters, and an interactive
Emacs interface (the type checker can assist in the development of your code).

Agda is also a proof assistant: It is an interactive system for writing and
checking proofs. Agda is based on intuitionistic type theory, a foundational
system for constructive mathematics developed by the Swedish logician Per
Martin-Löf. It has many similarities with other proof assistants based on
dependent types, such as Rocq (formerly known as Coq), Idris, Lean and NuPRL.

This package includes both a command-line program (agda) and an Emacs mode.

%package common
Summary:        %{name} common files
License:        MIT AND BSD-3-Clause AND BSD-2-Clause
BuildArch:      noarch
%description common
This package provides the %{name} core libraries and runtime related files.

%package -n ghc-%{name}
Summary:        Haskell %{name} library
Requires:       %{name}-common = %{version}-%{release}
%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.

%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Provides:       ghc-%{name}-static = %{version}-%{release}
Provides:       ghc-%{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       ghc-%{name}%{?_isa} = %{version}-%{release}
%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.

%if %{with haddock}
%package -n ghc-%{name}-doc
Summary:        Haskell %{name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem
%description -n ghc-%{name}-doc
This package provides the Haskell %{name} library documentation.
%endif

%if %{with ghc_prof}
%package -n ghc-%{name}-prof
Summary:        Haskell %{name} profiling library
Requires:       ghc-%{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (ghc-%{name}-devel and ghc-prof)
%description -n ghc-%{name}-prof
This package provides the Haskell %{name} profiling library.
%endif

%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l BSD-3-Clause %{ListLike}
%ghc_lib_subpackage -l MIT %{apnormalize}
%ghc_lib_subpackage -l BSD-3-Clause %{fmlist}
%ghc_lib_subpackage -l MIT %{genericdata}
%ghc_lib_subpackage -l BSD-3-Clause %{murmurhash}
%ghc_lib_subpackage -l BSD-3-Clause %{nonemptycontainers}
%ghc_lib_subpackage -l BSD-3-Clause %{nonemptyvector}
%ghc_lib_subpackage -l BSD-3-Clause %{peano}
%ghc_lib_subpackage -l BSD-3-Clause %{pqueue}
%ghc_lib_subpackage -l MIT %{processextras}
%ghc_lib_subpackage -l MIT %{showcombinators}
%ghc_lib_subpackage -l BSD-3-Clause %{vectorhashtables}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12
cp -bp %{SOURCE13} %{name}.cabal
# End cabal-rpm setup
%if %{with clustercounting}
#cabal-tweak-flag enable-cluster-counting True
%endif
(
    cd %{pqueue}
    cabal-tweak-dep-ver base '< 4.19' '< 4.21'
    cabal-tweak-dep-ver deepseq '< 1.5' '< 1.6'
)
(
    cd %{showcombinators}
    cabal-tweak-dep-ver base '< 4.14' '< 4.21'
)

# check the Agda version in the emacs mode
if ! grep -q \"%{version}\" src/data/emacs-mode/agda2-mode.el; then
  echo "agda2-version in src/data/emacs-mode/agda2-mode.el out of sync!"
  exit 1
fi

%build

%define elisp_files eri.el agda-input.el annotation.el agda2-highlight.el agda2-abbrevs.el agda2-queue.el agda2-mode.el agda2-mode-pkg.el agda2.el
(
cd src/data/emacs-mode
for i in *.el; do
  if ! echo %{elisp_files} | grep -q $i; then
     echo "$i missing from %%elisp_files - aborting!"
     exit 1
  fi
done
)
%ghc_libs_build %{subpkgs}
%ghc_lib_build
(
cd src/data/emacs-mode
for i in %elisp_files; do
  %{_emacs_bytecompile} $i
done
)
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
mv %{buildroot}%{_ghcdocdir}{,-common}
for i in $(find %{buildroot}%{_datadir}/%{pkgver} -name "*.agda"); do
  Agda_datadir=%{buildroot}%{_datadir}/%{pkgver} LD_LIBRARY_PATH=%{buildroot}%{_ghcdynlibdir} %{buildroot}%{_bindir}/agda $i
done
mkdir -p %{buildroot}%{_emacs_sitelispdir}/agda
for i in src/data/emacs-mode/*; do
  install -p -m 0644 $i %{buildroot}%{_emacs_sitelispdir}/agda
done
mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -p -m 0644 %SOURCE20 %{buildroot}%{_emacs_sitestartdir}
rm %{buildroot}%{_bindir}/agda-mode
rm -r %{buildroot}%{_datadir}/%{pkgver}/emacs-mode
%oreon_autofiles Agda-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ghc-Agda usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ghc-Agda-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ghc-Agda-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ghc-Agda-prof usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n Agda-common -f %{oreon_filedir}/Agda-common.list
%files -n ghc-Agda -f %{oreon_filedir}/ghc-Agda.list
%files -n ghc-Agda-devel -f %{oreon_filedir}/ghc-Agda-devel.list
%files -n ghc-Agda-doc -f %{oreon_filedir}/ghc-Agda-doc.list
%files -n ghc-Agda-prof -f %{oreon_filedir}/ghc-Agda-prof.list

%changelog

%autochangelog
