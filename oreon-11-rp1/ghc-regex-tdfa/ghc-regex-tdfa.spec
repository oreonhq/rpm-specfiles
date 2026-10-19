%global source0_hash 331285935eb029bc048fad5031c8de31b038bb361c5b6cbbfc47c011cc2ee295
%global pkg_name regex-tdfa
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        1.3.2.6
Release:        1%{?dist}
Summary:        Pure Haskell Tagged DFA Backend for "Text.Regex" (regex-base)
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/regex-tdfa
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
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-regex-base-devel
BuildRequires:  ghc-regex-base-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
# /oreon:deps
%description
This package provides a pure Haskell "Tagged" DFA regex engine for
<//hackage.haskell.org/package/regex-base regex-base>. This implementation was
inspired by the algorithm (and Master's thesis) behind the regular expression
library known as <https://github.com/laurikari/tre/ TRE or libtre>.

Please consult the "Text.Regex.TDFA" module for API documentation including a
tutorial with usage examples; see also
<https://wiki.haskell.org/Regular_expressions> for general information about
regular expression support in Haskell.

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
%files -n ghc-regex-tdfa-devel -f %{oreon_filedir}/ghc-regex-tdfa-devel.list
%files -n ghc-regex-tdfa-doc -f %{oreon_filedir}/ghc-regex-tdfa-doc.list
%files -n ghc-regex-tdfa-prof -f %{oreon_filedir}/ghc-regex-tdfa-prof.list

%changelog

%autochangelog
