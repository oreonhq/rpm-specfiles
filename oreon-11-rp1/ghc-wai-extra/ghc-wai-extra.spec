%global source0_hash ee63740b8dd478b01196f8968603b1bc0ee00aa5502d17edae579abfd0f150f7
%global pkg_name wai-extra
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 0
Name:           ghc-%{pkg_name}
Version:        3.1.18
Release:        1%{?dist}
Summary:        Basic WAI handlers and middleware
License:        MIT
URL:            https://hackage.haskell.org/package/wai-extra
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-HUnit-prof
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-ansi-terminal-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-call-stack-devel
BuildRequires:  ghc-call-stack-prof
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-cookie-devel
BuildRequires:  ghc-cookie-prof
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-fast-logger-devel
BuildRequires:  ghc-fast-logger-prof
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-discover-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-iproute-devel
BuildRequires:  ghc-iproute-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-streaming-commons-prof
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-vault-devel
BuildRequires:  ghc-vault-prof
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-wai-logger-devel
BuildRequires:  ghc-wai-logger-prof
BuildRequires:  ghc-wai-prof
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-warp-prof
BuildRequires:  ghc-word8-devel
BuildRequires:  ghc-word8-prof
BuildRequires:  ghc-zlib-devel
# /oreon:deps
%description
Provides basic WAI handler and middleware functionality:

* WAI Testing Framework
Hspec testing facilities and helpers for WAI.

* Event Source/Event Stream
Send server events to the client. Compatible with the JavaScript EventSource
API.

* Accept Override
Override the Accept header in a request. Special handling for the _accept query
parameter (which is used throughout WAI override the Accept header).

* Add Headers
WAI Middleware for adding arbitrary headers to an HTTP request.

* Clean Path
Clean a request path to a canonical form.

* Combine Headers
Combine duplicate headers into one.

* GZip Compression
Negotiate HTTP payload gzip compression.

* Health check endpoint
Add an empty health check endpoint.

* HTTP Basic Authentication
WAI Basic Authentication Middleware which uses Authorization header.

* JSONP
"JSON with Padding" middleware. Automatic wrapping of JSON responses to convert
into JSONP.

* Method Override / Post
Allows overriding of the HTTP request method via the _method query string
parameter.

* Request Logging
Request logging middleware for development and production environments

* Request Rewrite
Rewrite request path info based on a custom conversion rules.

* Select

Dynamically choose between Middlewares.

* Stream Files
Convert ResponseFile type responses into ResponseStream type.

* Virtual Host
Redirect incoming requests to a new host based on custom rules.

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
%files -n ghc-wai-extra-devel -f %{oreon_filedir}/ghc-wai-extra-devel.list
%files -n ghc-wai-extra-doc -f %{oreon_filedir}/ghc-wai-extra-doc.list
%files -n ghc-wai-extra-prof -f %{oreon_filedir}/ghc-wai-extra-prof.list

%changelog

%autochangelog
