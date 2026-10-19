%global source0_hash c9fe1bf2904825a65b667251ec644f197b71dc5c209d2d254be5de3d496b0e43
%global pkg_name echo
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.1.4
Release:        1%{?dist}
Summary:        A cross-platform, cross-console way to handle echoing terminal input
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/echo
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
The 'base' library exposes the 'hGetEcho' and 'hSetEcho' functions for querying
and setting echo status, but unfortunately, neither function works with MinTTY
consoles on Windows. This is a serious issue, since 'hGetEcho' and 'hSetEcho'
are often used to disable input echoing when a program prompts for a password,
so many programs will reveal your password as you type it on MinTTY!

This library provides an alternative interface which works with both MinTTY and
other consoles. An example is included which demonstrates how one might prompt
for a password using this library. To build it, make sure to configure with the
'-fexample' flag.

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
%files -n ghc-echo-devel -f %{oreon_filedir}/ghc-echo-devel.list
%files -n ghc-echo-doc -f %{oreon_filedir}/ghc-echo-doc.list
%files -n ghc-echo-prof -f %{oreon_filedir}/ghc-echo-prof.list

%changelog

%autochangelog
