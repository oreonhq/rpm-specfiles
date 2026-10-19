%global source4_hash 5bf2c1fa251be664743bf742ca41ff03eed25f53c9f9895c4f82a949c8429703
%global source3_hash c2ab67e09edc4bade04e269adc059320e83f68b31e428d11a69b20c4f161ddc1
%global source2_hash 35e5433512b883e83aa8bb8c3475221174445a87e51f162b2ce07f9cf1eb3c1a
%global source1_hash b0b44b0f2eaceb83f46dfa3d1747e080c45204c64d18bb9e63747299266f0c95
%global source0_hash 558758f29d9edfc6b64433c417c93c3c0ac164410bee72aadf59888fa608bed4
%global pkg_name brick
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global bimap bimap-0.5.0
%global vtycrossplatform vty-crossplatform-0.4.0.0
%global vtyunix vty-unix-0.2.0.0
%global subpkgs %{bimap} %{vtyunix} %{vtycrossplatform}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        3.0
Release:        1%{?dist}
Summary:        A declarative terminal user interface library
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/brick
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{bimap}/%{bimap}.tar.gz
Source2:        https://hackage.haskell.org/package/%{vtycrossplatform}/%{vtycrossplatform}.tar.gz
Source3:        https://hackage.haskell.org/package/%{vtyunix}/%{vtyunix}.tar.gz
Source4:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-ansi-terminal-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-blaze-builder-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-config-ini-devel
BuildRequires:  ghc-config-ini-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-clist-devel
BuildRequires:  ghc-data-clist-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-microlens-mtl-devel
BuildRequires:  ghc-microlens-mtl-prof
BuildRequires:  ghc-microlens-prof
BuildRequires:  ghc-microlens-th-devel
BuildRequires:  ghc-microlens-th-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-terminfo-devel
BuildRequires:  ghc-terminfo-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-text-zipper-devel
BuildRequires:  ghc-text-zipper-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unix-compat-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-utf8-string-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-vty-devel
BuildRequires:  ghc-vty-prof
BuildRequires:  ghc-word-wrap-devel
BuildRequires:  ghc-word-wrap-prof
# /oreon:deps
%description
Write terminal user interfaces (TUIs) painlessly with 'brick'!
You write an event handler and a drawing function and
the library does the rest.

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
%ghc_lib_subpackage -l BSD-3-Clause %{bimap}
%ghc_lib_subpackage -l BSD-3-Clause %{vtycrossplatform}
%ghc_lib_subpackage -l BSD-3-Clause %{vtyunix}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1 -a2 -a3
dos2unix -k -n %{SOURCE4} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
echo %{_bindir}/vty-unix-build-width-table >> %{vtyunix}/ghc-vty-unix.files
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-brick-devel -f %{oreon_filedir}/ghc-brick-devel.list
%files -n ghc-brick-doc -f %{oreon_filedir}/ghc-brick-doc.list
%files -n ghc-brick-prof -f %{oreon_filedir}/ghc-brick-prof.list

%changelog

%autochangelog
