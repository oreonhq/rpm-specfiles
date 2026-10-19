%global source1_hash eaf0ec6b390c6ef6627534e897b733151aae75c9b441b28754011359cfffa75b
%global source0_hash 9af814f76451b0adbcceb2c46cae463f63c5de50b2b6be66f4ef4d15ce2a49b5
%global pkg_name websockets
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.13.0.0
Release:        1%{?dist}
Summary:        A sensible and clean way to write WebSocket-capable servers in Haskell
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/websockets
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-SHA-devel
BuildRequires:  ghc-SHA-prof
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-entropy-devel
BuildRequires:  ghc-entropy-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-streaming-commons-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
# /oreon:deps
%description
This library allows you to write WebSocket-capable servers.

An example server:
<https://github.com/jaspervdj/websockets/blob/master/example/server.lhs>

An example client:
<https://github.com/jaspervdj/websockets/blob/master/example/client.hs>

This package only supports insecure ('ws://...') WebSockets. If you need secure
('wss://...') websockets, consider using Wuss:
<https://hackage.haskell.org/package/wuss>

See also:

* The specification of the WebSocket protocol:
<http://www.whatwg.org/specs/web-socket-protocol/>

* The JavaScript API for dealing with WebSockets:
<http://www.w3.org/TR/websockets/>.

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
cabal-tweak-drop-dep bytestring-builder

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-websockets-devel -f %{oreon_filedir}/ghc-websockets-devel.list
%files -n ghc-websockets-doc -f %{oreon_filedir}/ghc-websockets-doc.list
%files -n ghc-websockets-prof -f %{oreon_filedir}/ghc-websockets-prof.list

%changelog

%autochangelog
