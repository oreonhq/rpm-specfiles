%global source1_hash e823948a5c0633eceda80260200040769b608b062f3297d095d33ac735605ee1
%global source0_hash 1920adf31b15d167f60374fbfd0a53a1fbe7820fd7fd459beacf6eb00d03f183
%global pkg_name http-media
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 0
Name:           ghc-%{pkg_name}
Version:        0.8.1.1
Release:        1%{?dist}
Summary:        Processing HTTP Content-Type and Accept headers
License:        MIT
URL:            https://hackage.haskell.org/package/http-media
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-utf8-string-prof
# /oreon:deps
%description
This library is intended to be a comprehensive solution to parsing and
selecting quality-indexed values in HTTP headers. It is capable of parsing both
media types and language parameters from the Accept and Content header
families, and can be extended to match against other accept headers as well.
Selecting the appropriate header value is achieved by comparing a list of
server options against the quality-indexed values supplied by the client.

In the following example, the Accept header is parsed and then matched against
a list of server options to serve the appropriate media using 'mapAcceptMedia':

> getHeader >>= maybe send406Error sendResourceWith . mapAcceptMedia > [
("text/html", asHtml) > , ("application/json", asJson) > ]

Similarly, the Content-Type header can be used to produce a parser for request
bodies based on the given content type with 'mapContentMedia':

> getContentType >>= maybe send415Error readRequestBodyWith .
mapContentMedia > [ ("application/json", parseJson) > , ("text/plain",
parseText) > ]

The API is agnostic to your choice of server.

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
cp -bp %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup
cabal-tweak-remove-upperbound QuickCheck

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
%files -n ghc-http-media-devel -f %{oreon_filedir}/ghc-http-media-devel.list
%files -n ghc-http-media-doc -f %{oreon_filedir}/ghc-http-media-doc.list
%files -n ghc-http-media-prof -f %{oreon_filedir}/ghc-http-media-prof.list

%changelog

%autochangelog
