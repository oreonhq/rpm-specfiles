%global source1_hash 195b368dddc1fcc5dc4cc642f476cfd32625b7009bc8bb15256276f83a92a84a
%global source0_hash d365d5051696c15414ebe23749fc67475a532234b7c7d77060323d149a8fc4fe
%global pkg_name io-streams
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        1.5.2.2
Release:        1%{?dist}
Summary:        Simple, composable, and easy-to-use stream I/O
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/io-streams
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-zlib-bindings-devel
BuildRequires:  ghc-zlib-bindings-prof
# /oreon:deps
%description
The io-streams library contains simple and easy-to-use primitives for I/O using
streams. Most users will want to import the top-level convenience module
"System.IO.Streams", which re-exports most of the library:

For first-time users, 'io-streams' comes with an included tutorial, which can
be found in the "System.IO.Streams.Tutorial" module.

'io-streams' comes with:
* functions to use files, handles, concurrent channels, sockets, lists,
vectors, and more as streams.
* a variety of combinators for wrapping and transforming streams, including
compression and decompression using zlib, controlling precisely how many bytes
are read from or written to a stream, buffering output using bytestring
builders, folds, maps, filters, zips, etc.
* support for parsing from streams using 'attoparsec'.
* support for spawning processes and communicating with them using streams.

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
%files -n ghc-io-streams-devel -f %{oreon_filedir}/ghc-io-streams-devel.list
%files -n ghc-io-streams-doc -f %{oreon_filedir}/ghc-io-streams-doc.list
%files -n ghc-io-streams-prof -f %{oreon_filedir}/ghc-io-streams-prof.list

%changelog

%autochangelog
