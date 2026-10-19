%global source0_hash 9f28d0a67ac3d956d2dd78eb19ea922c0a9192bbbeeeead20d39f561636828a3
%global pkg_name simple-sendfile
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 0
Name:           ghc-%{pkg_name}
Version:        0.2.32
Release:        1%{?dist}
Summary:        Cross-platform sendfile system call
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/simple-sendfile
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
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-easy-file-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-discover-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
# /oreon:deps
%description
A Haskell cross-platform library for the sendfile system call.
This library tries to minimize system calls,
since they are a bottleneck for web servers.

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
%files -n ghc-simple-sendfile-devel -f %{oreon_filedir}/ghc-simple-sendfile-devel.list
%files -n ghc-simple-sendfile-doc -f %{oreon_filedir}/ghc-simple-sendfile-doc.list
%files -n ghc-simple-sendfile-prof -f %{oreon_filedir}/ghc-simple-sendfile-prof.list

%changelog

%autochangelog
