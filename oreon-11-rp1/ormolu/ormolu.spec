%global source5_hash 2c1d251f4d5cfb08d3826ccabca1afa8699c8531612283ec8f7e6a8edc2416ed
%global source4_hash fc01b166df6ba45f6ce157165eb786da208dbab41252fd81134f8ba02cf3f505
%global source3_hash d38b18581fe4da33bcfcc5d368c48a88f27e9801035e4ace59776e14c7787b5a
%global source2_hash f97c12b64cee6bbb8273ee7946d37a6d5dcd3bc1c3599a66f8bbfd6dc54190c6
%global source1_hash b17c31a4502f14dd32e892358efb0343f21bd6b54d18684bfe9422aa562c2c25
%global source0_hash da96cd7c8265390f0cc2cb9dbf0b3b4298803c37ccddecea5718ef46d991c980
%global pkg_name ormolu
%global pkgver %{pkg_name}-%{version}
%haskell_setup -h -p
%global choice choice-0.2.4.1
%global ghclibparser ghc-lib-parser-9.10.3.20250912
%global markdownunlit markdown-unlit-0.6.0
%global thenv th-env-0.1.1
%global subpkgs %{choice} %{markdownunlit} %{thenv} %{ghclibparser}
%bcond tests 0
Name:           %{pkg_name}
Version:        0.7.7.0
Release:        1%{?dist}
Summary:        A formatter for Haskell source code
License:        BSD-3-Clause AND MIT
URL:            https://hackage.haskell.org/package/ormolu
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{choice}/%{choice}.tar.gz
Source2:        https://hackage.haskell.org/package/%{ghclibparser}/%{ghclibparser}.tar.gz
Source3:        https://hackage.haskell.org/package/%{markdownunlit}/%{markdownunlit}.tar.gz
Source4:        https://hackage.haskell.org/package/%{thenv}/%{thenv}.tar.gz
Source5:        https://hackage.haskell.org/package/%{pkgver}/%{name}.cabal#/%{pkgver}.cabal
%if %{with tests}
%endif
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  alex
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Cabal-syntax-devel
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-MemoTrie-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-discover-devel
BuildRequires:  ghc-hspec-megaparsec-devel
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-path-devel
BuildRequires:  ghc-path-io-devel
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-th-compat-devel
BuildRequires:  happy
BuildRequires:  help2man
# /oreon:deps
%description
Ormolu is a formatter for Haskell source code.
The project was created with the following goals in mind:

- Using GHC's own parser to avoid parsing problems caused by haskell-src-exts.

- Let some whitespace be programmable. The layout of the input
  influences the layout choices in the output. This means that the
  choices between single-line/multi-line layouts in each particular
  situation are made by the user, not by an algorithm. This makes the
  implementation simpler and leaves some control to the user while
  still guaranteeing that the formatted code is stylistically
  consistent.

- Writing code in such a way so it's easy to modify and maintain.

- Implementing one “true” formatting style which admits no configuration.

- That formatting style aims to result in minimal diffs while still
  remaining very close to “conventional” Haskell formatting people
  use.

- Choose a style compatible with modern dialects of Haskell. As new
  Haskell extensions enter broad use, we may change the style to
  accommodate them.

- Idempotence: formatting already formatted code doesn't change it.

- Be well-tested and robust to the point that it can be used in large
  projects without exposing unfortunate, disappointing bugs here and
  there.

%package -n ghc-%{name}
Summary:        Haskell %{name} library
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

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -a1 -a2 -a3 -a4
dos2unix -k -n %{SOURCE5} %{name}.cabal
# End cabal-rpm setup

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
set noclobber
mkdir -p %{buildroot}%{bash_completions_dir}
mkdir -p %{buildroot}%{fish_completions_dir}
mkdir -p %{buildroot}%{zsh_completions_dir}
%{buildroot}%{_bindir}/%{name} --bash-completion-script %{name} | sed s/filenames/default/ > %{buildroot}%{bash_completions_dir}/%{name}
%{buildroot}%{_bindir}/%{name} --fish-completion-script %{name} > %{buildroot}%{fish_completions_dir}/%{name}
%{buildroot}%{_bindir}/%{name} --zsh-completion-script %{name} | sed s/filenames/default/ > %{buildroot}%{zsh_completions_dir}/_%{name}
mkdir -p %{buildroot}%{_mandir}/man1/
help2man --no-info %{buildroot}%{_bindir}/%{name} > %{buildroot}%{_mandir}/man1/%{name}.1
rm -r %{buildroot}%{ghclibdir}/lib
rm -r %{buildroot}%{_datadir}/%{ghclibparser}
mkdir licenses
mv %{buildroot}%{_licensedir}/{ghc-ghc-lib-parser,ghc-markdown-unlit,ghc-th-env} licenses
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if %{with tests}
PATH=%{buildroot}%{_bindir}:$PATH
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-ormolu -f %{oreon_filedir}/ghc-ormolu.list
%files -n ghc-ormolu-devel -f %{oreon_filedir}/ghc-ormolu-devel.list

%changelog

%autochangelog
