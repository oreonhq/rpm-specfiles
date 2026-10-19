%global source0_hash 118ada3837b80c6327b11449bdab50d620043731be2b2494eadcd8e854bff83f
%global pkg_name xml-conduit
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 0
Name:           ghc-%{pkg_name}
Version:        1.10.1.0
Release:        1%{?dist}
Summary:        XML parsing and rendering with conduit
License:        MIT
URL:            https://hackage.haskell.org/package/xml-conduit
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-blaze-markup-devel
BuildRequires:  ghc-blaze-markup-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-cabal-doctest-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-conduit-extra-prof
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-doctest-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-xml-types-devel
BuildRequires:  ghc-xml-types-prof
# /oreon:deps
%description
This package provides parsing and rendering functions for XML. It is
based on the datatypes found in the xml-types package. This package is
broken up into the following modules:

* Text.XML: DOM-based parsing and rendering.
  This is the most commonly used module.

* Text.XML.Cursor: A wrapper around Text.XML which allows bidirectional
  traversing of the DOM, similar to XPath. (Note: Text.XML.Cursor.Generic
  is the same concept, but will work with any node representation.)

* Text.XML.Unresolved: A slight modification  to Text.XML which does not
  require  all entities  to be  resolved at  parsing. The  datatypes are
  slightly  more complicated  here, and  therefore this  module is  only
  recommended when you need to deal directly with raw entities.

* Text.XML.Stream.Parse: Streaming parser, including some streaming
  parser combinators.

* Text.XML.Stream.Render: Streaming renderer.

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
%files -n ghc-xml-conduit-devel -f %{oreon_filedir}/ghc-xml-conduit-devel.list
%files -n ghc-xml-conduit-doc -f %{oreon_filedir}/ghc-xml-conduit-doc.list
%files -n ghc-xml-conduit-prof -f %{oreon_filedir}/ghc-xml-conduit-prof.list

%changelog

%autochangelog
