%global source1_hash cc7867f81c6eb3f1924bbb1029757af6e3b67a3c224c1faa329be3ea70ad729c
%global source0_hash d94961ca15c42c798d19cde540ec12b25cc43435fb95e682399d6c1a02022d4e
%global pkg_name network-bsd
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        2.8.1.0
Release:        1%{?dist}
Summary:        POSIX network database (<netdb.h>) API
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/network-bsd
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
This package provides Haskell bindings to the the [POSIX network database
(<netdb.h>)
API](http://pubs.opengroup.org/onlinepubs/009696699/basedefs/netdb.h.html).

=== Relationship to the 'network' package

The 'network' package version 2.* series provides "Network.BSD" but it is
removed starting with 'network' version 3.0.

This package provides the "Network.BSD" module split off from the
<https://hackage.haskell.org/package/network network package>.

If in addition to the 'network''s modules also "Network.BSD" is necessary, add
'network-bsd' to your dependencies like so:

> library > build-depends: network >= 2.7 && < 3.1 > , network-bsd >= 2.7 && <
2.9

I.e. you can control the version of the 'network' package independently.

__NOTE__: Starting with 'network-bsd-2.8.1.0' the APIs of 'network' and
'network-bsd' evolve differently, and consequently the versioning doesn't match
up anymore! Moreover, also starting with version 'network-bsd-2.8.1.0' this
package requires 'network >= 3' in order to avoid module name clashes with
'network < 3''s "Network.BSD" module.

However, 'network-bsd-2.7.0.0' and 'network-bsd-2.8.0.0' passes thru the
"Network.BSD" module from 'network-2.7.*' and 'network-2.8.*' respectively in a
non-clashing way via Cabal's
<https://www.haskell.org/cabal/users-guide/developing-packages.html#pkg-field-library-reexported-modules
reexported-modules> feature while ensuring a well-defined
<https://pvp.haskell.org/ API versioning> of the observable API of
'network-bsd'. This is why the example above supporting a wide range of
'network' versions works by including version 2.7.0.0 in the required version
range of 'network-bsd'.

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

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-network-bsd-devel -f %{oreon_filedir}/ghc-network-bsd-devel.list
%files -n ghc-network-bsd-doc -f %{oreon_filedir}/ghc-network-bsd-doc.list
%files -n ghc-network-bsd-prof -f %{oreon_filedir}/ghc-network-bsd-prof.list

%changelog

%autochangelog
