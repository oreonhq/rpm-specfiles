%global source0_hash 7b5823f3bd94b57022d9d84ab3555303653c5121eaaef2ee1fd4918f3c434466
%global pkg_name hxt-unicode
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        9.0.2.4
Release:        1%{?dist}
Summary:        Unicode en-/decoding functions for utf8, iso-latin-* and other encodings
License:        MIT AND BSD-3-Clause
URL:            https://hackage.haskell.org/package/hxt-unicode
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-hxt-charproperties-devel
BuildRequires:  ghc-hxt-charproperties-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
Unicode encoding and decoding functions for utf8, iso-latin-* and somes other
encodings, used in the Haskell XML Toolbox. ISO Latin 1 - 16, utf8, utf16,
ASCII are supported. Decoding is done with lazy functions, errors may be
detected or ignored.

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
%files -n ghc-hxt-unicode-devel -f %{oreon_filedir}/ghc-hxt-unicode-devel.list
%files -n ghc-hxt-unicode-doc -f %{oreon_filedir}/ghc-hxt-unicode-doc.list
%files -n ghc-hxt-unicode-prof -f %{oreon_filedir}/ghc-hxt-unicode-prof.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.0.2.4-1
- Prepare for Oreon 11 (RP1)
