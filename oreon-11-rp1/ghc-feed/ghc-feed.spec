%global source1_hash 266d3066528b1c0a849c7be3d0c162f59a763d35faad96707fdfd5fa58332e79
%global source0_hash a8f54072edaaf7e978062b9de94733e8cc43e31b2dda3446f901bf57f1815955
%global pkg_name feed
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        1.3.2.1
Release:        1%{?dist}
Summary:        Interfacing with RSS (v 0.9x, 2.x, 1.0) + Atom feeds
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/feed
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-base-compat-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-old-locale-prof
BuildRequires:  ghc-old-time-devel
BuildRequires:  ghc-old-time-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-locale-compat-devel
BuildRequires:  ghc-time-locale-compat-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-utf8-string-prof
BuildRequires:  ghc-xml-conduit-devel
BuildRequires:  ghc-xml-conduit-prof
BuildRequires:  ghc-xml-types-devel
BuildRequires:  ghc-xml-types-prof
# /oreon:deps
%description
Interfacing with RSS (v 0.9x, 2.x, 1.0) + Atom feeds.

To help working with the multiple feed formats we've ended up with, this set of
modules provides parsers, pretty printers and some utility code for querying
and just generally working with a concrete representation of feeds in Haskell.

See here for an example of how to create an Atom feed:
<https://github.com/haskell-party/feed/blob/master/tests/Example/CreateAtom.hs>

For basic reading and editing of feeds, consult the documentation of the
Text.Feed.* hierarchy.

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
dos2unix -k -n %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-feed-devel -f %{oreon_filedir}/ghc-feed-devel.list
%files -n ghc-feed-doc -f %{oreon_filedir}/ghc-feed-doc.list
%files -n ghc-feed-prof -f %{oreon_filedir}/ghc-feed-prof.list

%changelog

%autochangelog
