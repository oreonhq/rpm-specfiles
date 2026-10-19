%global source1_hash a694e88f9ec9fc79f0b03f233d3fea592b68f70a34aac2ddb5bcaecb6562e2fd
%global source0_hash 1d5a91143ef0e22157536093ec8e59d226a68220ec89378d5dcaeea86472c784
%global pkg_name base16-bytestring
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        1.0.2.0
Release:        1%{?dist}
Summary:        RFC 4648-compliant Base16 encodings for ByteStrings
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/base16-bytestring
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
This package provides support for encoding and decoding binary data according
to 'base16' (see also <https://tools.ietf.org/html/rfc4648 RFC 4648>) for
strict (see "Data.ByteString.Base16") and lazy 'ByteString's (see
"Data.ByteString.Base16.Lazy").

See the <https://hackage.haskell.org/package/base16 base16> package which
provides superior encoding and decoding performance as well as support for
lazy, short, and strict variants of 'Text' and 'ByteString' values.
Additionally, see the <https://hackage.haskell.org/package/base-encoding
base-encoding> package which provides an uniform API providing conversion paths
between more binary and textual types.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides the Haskell %{pkg_name} library development
files.

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
cp -bp %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-base16-bytestring-devel -f %{oreon_filedir}/ghc-base16-bytestring-devel.list
%files -n ghc-base16-bytestring-doc -f %{oreon_filedir}/ghc-base16-bytestring-doc.list
%files -n ghc-base16-bytestring-prof -f %{oreon_filedir}/ghc-base16-bytestring-prof.list

%changelog

%autochangelog
