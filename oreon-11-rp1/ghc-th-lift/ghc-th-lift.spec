%global source0_hash dd157c626cb0b0fa71adac3690305aeafccf503583fce387628b210fadc69806
%global pkg_name th-lift
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 0
Name:           ghc-%{pkg_name}
Version:        0.8.7
Release:        1%{?dist}
Summary:        Derive Template Haskell's Lift class for datatypes
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/th-lift
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-th-abstraction-devel
BuildRequires:  ghc-th-abstraction-prof
# /oreon:deps
%description
Derive Template Haskell's 'Lift' class for datatypes using 'TemplateHaskell'.
The functionality in this package has largely been subsumed by the 'DeriveLift'
language extension, which is available in GHC 8.0 and later versions.
As such, this package is only useful as a way to backport bugfixes to
'DeriveLift' in later GHC versions back to older GHCs.

The following libraries are related:

* The <https://hackage.haskell.org/package/th-orphans th-orphans> package
provides instances for 'template-haskell' syntax types.

* The <http://hackage.haskell.org/package/th-lift-instances th-lift-instances>
package provides 'Lift' instances for types in 'base', 'text', 'bytestring',
'vector', etc. Some of these instances are only provided for old versions of
their respective libraries, as the same 'Lift' instances are also present
upstream on newer versions.

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
%files -n ghc-th-lift-devel -f %{oreon_filedir}/ghc-th-lift-devel.list
%files -n ghc-th-lift-doc -f %{oreon_filedir}/ghc-th-lift-doc.list
%files -n ghc-th-lift-prof -f %{oreon_filedir}/ghc-th-lift-prof.list

%changelog

%autochangelog
