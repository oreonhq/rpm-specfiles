%global source1_hash 8672b9388f5ddfa8ece691e59b4272fa807a2ddf0698970cd73af9bebb98058d
%global source0_hash 958cfb3bd54b1bfa9e1e2d9cd1748e76c10d2b30a3cceeab3f6a852205c1a869
%global pkg_name cmark-gfm
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global cmarkgfm_release 0.29.0.gfm.13
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        0.2.6
Release:        1%{?dist}
Summary:        Fast, accurate GitHub Flavored Markdown parser and renderer
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/cmark-gfm
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
Provides:       bundled(cmark-gfm) = %{cmarkgfm_release}
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
# /oreon:deps
%description
This package provides Haskell bindings for <https://github.com/github/cmark-gfm
libcmark-gfm>, the reference parser for <https://github.github.com/gfm/ GitHub
Flavored Markdown>, a fully specified variant of Markdown. It includes sources
for libcmark-gfm (%{cmarkgfm_release}) and does not require prior installation
of the C library.

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

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
dos2unix -k -n %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup
cabal-tweak-dep-ver bytestring 0.11.5 0.10

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
%files -n ghc-cmark-gfm-devel -f %{oreon_filedir}/ghc-cmark-gfm-devel.list
%files -n ghc-cmark-gfm-doc -f %{oreon_filedir}/ghc-cmark-gfm-doc.list
%files -n ghc-cmark-gfm-prof -f %{oreon_filedir}/ghc-cmark-gfm-prof.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.6-1
- Prepare for Oreon 11 (RP1)
