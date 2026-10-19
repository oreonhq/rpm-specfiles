%global source0_hash 9e26f12230d38ae56dcf94f8c139799dc3b7376f3434d35ce74847a0a24fd5ff
%global pkg_name th-compat
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%ifnarch armv7hl
%bcond tests 1
%endif
Name:           ghc-%{pkg_name}
Version:        0.1.7
Release:        1%{?dist}
Summary:        Backward- (and forward-)compatible Quote and Code types
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/th-compat
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-discover-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
# /oreon:deps
%description
This package defines a "Language.Haskell.TH.Syntax.Compat" module, which
backports the 'Quote' and 'Code' types to work across a wide range of
'template-haskell' versions. The 'makeRelativeToProject' utility is also
backported. On recent versions of 'template-haskell' (2.17.0.0 or later), this
module simply reexports definitions from "Language.Haskell.TH.Syntax".
Refer to the Haddocks for "Language.Haskell.TH.Syntax.Compat" for examples of
how to use this module.

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

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-th-compat-devel -f %{oreon_filedir}/ghc-th-compat-devel.list
%files -n ghc-th-compat-doc -f %{oreon_filedir}/ghc-th-compat-doc.list
%files -n ghc-th-compat-prof -f %{oreon_filedir}/ghc-th-compat-prof.list

%changelog

%autochangelog
