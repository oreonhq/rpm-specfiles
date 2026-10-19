%global source1_hash 142f695ab8a38c476ba0189ff8b8d81686ea9cdd5f68a1afede9240cb21dc8dc
%global source0_hash 442eba38d8e4c9ae2575a40288c8277599649cf13bf114543fa0de2da83aeddb
%global pkg_name text-icu
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.8.0.5
Release:        1%{?dist}
Summary:        Bindings to the ICU library
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/text-icu
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  libicu-devel
BuildRequires:  pkgconfig(icu-i18n)
# /oreon:deps
%description
Haskell bindings to the International Components for Unicode (ICU) libraries.
These libraries provide robust and full-featured Unicode services on a wide
variety of platforms.

Features include:

* Both pure and impure bindings, to allow for fine control over efficiency and
ease of use.

* Breaking of strings on character, word, sentence, and line boundaries.

* Access to the Unicode Character Database (UCD) of character metadata.

* String collation functions, for locales where the conventions for
lexicographic ordering differ from the simple numeric ordering of character
codes.

* Character set conversion functions, allowing conversion between Unicode and
over 220 character encodings.

* Unicode normalization. (When implementations keep strings in a normalized
form, they can be assured that equivalent strings have a unique binary
representation.)

* Regular expression search and replace.

* Security checks for visually confusable (spoofable) strings.

* Bidirectional Unicode algorithm

* Calendar objects holding dates and times.

* Number and calendar formatting.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libicu-devel%{?_isa}
Requires:       pkgconfig(icu-i18n)
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
dos2unix -k -n %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-text-icu-devel -f %{oreon_filedir}/ghc-text-icu-devel.list
%files -n ghc-text-icu-doc -f %{oreon_filedir}/ghc-text-icu-doc.list
%files -n ghc-text-icu-prof -f %{oreon_filedir}/ghc-text-icu-prof.list

%changelog

%autochangelog
