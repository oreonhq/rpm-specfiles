%global source0_hash 58b6b1650918e7289b1882e39a99392a2b20d5c342f857cd49422db5e6086d92
%global pkg_name copilot
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        4.8.1
Release:        1%{?dist}
Summary:        A stream DSL for writing embedded C programs
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/copilot
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-copilot-c99-devel
BuildRequires:  ghc-copilot-c99-prof
BuildRequires:  ghc-copilot-core-devel
BuildRequires:  ghc-copilot-core-prof
BuildRequires:  ghc-copilot-language-devel
BuildRequires:  ghc-copilot-language-prof
BuildRequires:  ghc-copilot-libraries-devel
BuildRequires:  ghc-copilot-libraries-prof
BuildRequires:  ghc-copilot-prettyprinter-devel
BuildRequires:  ghc-copilot-prettyprinter-prof
BuildRequires:  ghc-copilot-theorem-devel
BuildRequires:  ghc-copilot-theorem-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-optparse-applicative-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
Copilot is a stream-based runtime verification framework implemented as an
embedded domain-specific language (EDSL) in Haskell. Programs can be
interpreted for testing, or translated into C99 code to be incorporated in a
project, or as a standalone application. The C99 backend output is constant in
memory and time, making it suitable for systems with hard realtime
requirements.

This package is the main entry-point for using Copilot.

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
%files -n ghc-copilot-devel -f %{oreon_filedir}/ghc-copilot-devel.list
%files -n ghc-copilot-doc -f %{oreon_filedir}/ghc-copilot-doc.list
%files -n ghc-copilot-prof -f %{oreon_filedir}/ghc-copilot-prof.list

%changelog

%autochangelog
