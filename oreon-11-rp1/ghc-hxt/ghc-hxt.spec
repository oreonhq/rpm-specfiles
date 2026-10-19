%global source0_hash ef602fe674225527750574dd555dbdf402ab77d054af75d41ca21b42dbb23ad9
%global pkg_name hxt
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        9.3.1.22
Release:        1%{?dist}
Summary:        A collection of tools for processing XML with Haskell
License:        MIT
URL:            https://hackage.haskell.org/package/hxt
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-hxt-charproperties-devel
BuildRequires:  ghc-hxt-charproperties-prof
BuildRequires:  ghc-hxt-regex-xmlschema-devel
BuildRequires:  ghc-hxt-regex-xmlschema-prof
BuildRequires:  ghc-hxt-unicode-devel
BuildRequires:  ghc-hxt-unicode-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
The Haskell XML Toolbox bases on the ideas of HaXml and HXML, but introduces a
more general approach for processing XML with Haskell. The Haskell XML Toolbox
uses a generic data model for representing XML documents, including the DTD
subset and the document subset, in Haskell. It contains a validating XML
parser, a HTML parser, namespace support, an XPath expression evaluator, an
XSLT library, a RelaxNG schema validator and funtions for serialization and
deserialization of user defined data. The library makes extensive use of the
arrow approach for processing XML. Since version 9 the toolbox is partitioned
into various (sub-)packages. This package contains the core functionality,
hxt-curl, hxt-tagsoup, hxt-relaxng, hxt-xpath, hxt-xslt, hxt-regex-xmlschema
contain the extensions. hxt-unicode contains encoding and decoding functions,
hxt-charproperties char properties for unicode and XML. Changes from 9.3.1.21:
ghc-9.0 compatibility

Changes from 9.3.1.20: ghc 8.10 and 9.0 compatibility, tuple picker up to
24-tuples, Either instance for xpickle

Changes from 9.3.1.19: ghc-8.8.2 compatibility

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
%files -n ghc-hxt-devel -f %{oreon_filedir}/ghc-hxt-devel.list
%files -n ghc-hxt-doc -f %{oreon_filedir}/ghc-hxt-doc.list
%files -n ghc-hxt-prof -f %{oreon_filedir}/ghc-hxt-prof.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.3.1.22-1
- Prepare for Oreon 11 (RP1)
