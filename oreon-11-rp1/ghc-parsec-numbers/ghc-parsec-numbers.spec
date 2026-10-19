%global source0_hash 77019a4817712f6bfc61c9d148b680579955eb40d286f7766f7b0a90c726febf
%global pkg_name parsec-numbers
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.1.0
Release:        1%{?dist}
Summary:        Utilities for parsing numbers from strings
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/parsec-numbers
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Patch0:         parsec-numbers-0.1.0-license-file.patch
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
Parsec-numbers provides the number parsers without the need to use a large (and
unportable) token parser.

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
%autopatch -p1
# End cabal-rpm setup
# empty file
rm LICENSE

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-parsec-numbers-devel -f %{oreon_filedir}/ghc-parsec-numbers-devel.list
%files -n ghc-parsec-numbers-doc -f %{oreon_filedir}/ghc-parsec-numbers-doc.list
%files -n ghc-parsec-numbers-prof -f %{oreon_filedir}/ghc-parsec-numbers-prof.list

%changelog

%autochangelog
