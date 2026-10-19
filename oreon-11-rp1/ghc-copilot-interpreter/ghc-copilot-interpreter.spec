%global source0_hash 0ec88836b8f0df92441506017c5382717955fda3f99b58c38a2713f948cc5ec9
%global pkg_name copilot-interpreter
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        4.8.1
Release:        1%{?dist}
Summary:        Interpreter for Copilot
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/copilot-interpreter
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-copilot-core-devel
BuildRequires:  ghc-copilot-core-prof
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
Interpreter for Copilot.

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

%files -f %{oreon_filedir}/main.list
%files -n ghc-copilot-interpreter-devel -f %{oreon_filedir}/ghc-copilot-interpreter-devel.list
%files -n ghc-copilot-interpreter-doc -f %{oreon_filedir}/ghc-copilot-interpreter-doc.list
%files -n ghc-copilot-interpreter-prof -f %{oreon_filedir}/ghc-copilot-interpreter-prof.list

%changelog

%autochangelog
