%global source0_hash e8ca2dee598c790dd1c1c4359bdd1e495d9b881f5aa1f539c22f0dd5563747bf
%global pkg_name regex-base
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.94.0.3
Release:        1%{?dist}
Summary:        Common "Text.Regex.*" API for Regex matching
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/regex-base
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
# /oreon:deps
%description
This package does not provide the ability to do regular expression matching.
Instead, it provides the type classes that constitute the abstract API that is
implemented by 'regex-*' backends such as:

* <https://hackage.haskell.org/package/regex-posix regex-posix>

* <https://hackage.haskell.org/package/regex-parsec regex-parsec>

* <https://hackage.haskell.org/package/regex-dfa regex-dfa>

* <https://hackage.haskell.org/package/regex-tdfa regex-tdfa>

* <https://hackage.haskell.org/package/regex-pcre regex-pcre>

See also <https://wiki.haskell.org/Regular_expressions> for more information.

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
%files -n ghc-regex-base-devel -f %{oreon_filedir}/ghc-regex-base-devel.list
%files -n ghc-regex-base-doc -f %{oreon_filedir}/ghc-regex-base-doc.list
%files -n ghc-regex-base-prof -f %{oreon_filedir}/ghc-regex-base-prof.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.94.0.3-1
- Prepare for Oreon 11 (RP1)
