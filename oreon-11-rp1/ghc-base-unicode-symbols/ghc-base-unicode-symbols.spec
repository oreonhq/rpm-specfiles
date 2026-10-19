%global source0_hash 4364d6c403616e9ec0c240c4cb450c66af43ea8483d73c315e96f4ba3cb97062
%global pkg_name base-unicode-symbols
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.2.4.2
Release:        1%{?dist}
Summary:        Unicode alternatives for common functions and operators
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/base-unicode-symbols
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
This package defines new symbols for a number of functions, operators and types
in the base package. All symbols are documented with their actual definition
and information regarding their Unicode code point. They should be completely
interchangeable with their definitions.

For more Unicode goodness you can enable the UnicodeSyntax language extension.
This extension enables Unicode characters to be used to stand for certain ASCII
character sequences, i.e. → instead of ->, ∀ instead of forall and many others.

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
%files -n ghc-base-unicode-symbols-devel -f %{oreon_filedir}/ghc-base-unicode-symbols-devel.list
%files -n ghc-base-unicode-symbols-doc -f %{oreon_filedir}/ghc-base-unicode-symbols-doc.list
%files -n ghc-base-unicode-symbols-prof -f %{oreon_filedir}/ghc-base-unicode-symbols-prof.list

%changelog

%autochangelog
