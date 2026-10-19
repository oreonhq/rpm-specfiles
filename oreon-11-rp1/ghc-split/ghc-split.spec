%global source0_hash 18adb60f7f12d08601c382d47c2bacbbd4de4b9233f09683889d15b64b6420d6
%global pkg_name split
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 0
Name:           ghc-%{pkg_name}
Version:        0.2.5.1
Release:        1%{?dist}
Summary:        Combinator library for splitting lists
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/split
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
A collection of various methods for splitting lists into parts, akin to the
"split" function found in several mainstream languages. Here is its tale:

Once upon a time the standard "Data.List" module held no function for splitting
a list into parts according to a delimiter. Many a brave lambda-knight strove
to add such a function, but their striving was in vain, for Lo, the Supreme
Council fell to bickering amongst themselves what was to be the essential
nature of the One True Function which could cleave a list in twain (or thrain,
or any required number of parts).

And thus came to pass the split package, comprising divers functions for
splitting a list asunder, each according to its nature. And the Supreme Council
had no longer any grounds for argument, for the favored method of each was
contained therein.

To get started, see the "Data.List.Split" module.

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
%files -n ghc-split-devel -f %{oreon_filedir}/ghc-split-devel.list
%files -n ghc-split-doc -f %{oreon_filedir}/ghc-split-doc.list
%files -n ghc-split-prof -f %{oreon_filedir}/ghc-split-prof.list

%changelog

%autochangelog
