%global source0_hash 27c44a81677633021411ca564e93092b0d412d4a4de7e0cfda57ab26d79a3b8c
%global pkg_name copilot-c99
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        4.8.1
Release:        1%{?dist}
Summary:        A compiler for Copilot targeting C99
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/copilot-c99
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-copilot-core-devel
BuildRequires:  ghc-copilot-core-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-language-c99-devel
BuildRequires:  ghc-language-c99-prof
BuildRequires:  ghc-language-c99-simple-devel
BuildRequires:  ghc-language-c99-simple-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
This package is a back-end from Copilot to C.

Copilot is a stream (i.e., infinite lists) domain-specific language (DSL) in
Haskell that compiles into embedded C. Copilot contains an interpreter,
multiple back-end compilers, and other verification tools.

A tutorial, examples, and other information are available at
<https://copilot-language.github.io>.

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
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-copilot-c99-devel -f %{oreon_filedir}/ghc-copilot-c99-devel.list
%files -n ghc-copilot-c99-doc -f %{oreon_filedir}/ghc-copilot-c99-doc.list
%files -n ghc-copilot-c99-prof -f %{oreon_filedir}/ghc-copilot-c99-prof.list

%changelog

%autochangelog
