%global source0_hash ab9e02357faaa04a3bb000279ca54cca550ecd51505b6f6e846de669a7884fdc
%global pkg_name happstack-server
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        7.9.3
Release:        1%{?dist}
Summary:        Web related tools and services
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/happstack-server
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-extensible-exceptions-devel
BuildRequires:  ghc-extensible-exceptions-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-hslogger-devel
BuildRequires:  ghc-hslogger-prof
BuildRequires:  ghc-html-devel
BuildRequires:  ghc-html-prof
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-monad-control-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-sendfile-devel
BuildRequires:  ghc-sendfile-prof
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-syb-prof
BuildRequires:  ghc-system-filepath-devel
BuildRequires:  ghc-system-filepath-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-threads-devel
BuildRequires:  ghc-threads-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-base-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-utf8-string-prof
BuildRequires:  ghc-xhtml-devel
BuildRequires:  ghc-xhtml-prof
BuildRequires:  ghc-zlib-devel
BuildRequires:  ghc-zlib-prof
# /oreon:deps
%description
Happstack Server provides an HTTP server and a rich set of functions for
routing requests, handling query parameters, generating responses, working with
cookies, serving files, and more. For in-depth documentation see the Happstack
Crash Course <http://happstack.com/docs/crashcourse/index.html>.

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
%files -n ghc-happstack-server-devel -f %{oreon_filedir}/ghc-happstack-server-devel.list
%files -n ghc-happstack-server-doc -f %{oreon_filedir}/ghc-happstack-server-doc.list
%files -n ghc-happstack-server-prof -f %{oreon_filedir}/ghc-happstack-server-prof.list

%changelog

%autochangelog
