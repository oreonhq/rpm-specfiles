%global source0_hash 98dca11044640c26ddd976ce6f3c7b3da52a967d5fd8a9c223f9a96e12ea9958
%global pkg_name filepath-bytestring
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 0
Name:           ghc-%{pkg_name}
Version:        1.5.2.0.5
Release:        1%{?dist}
Summary:        Library for manipulating RawFilePaths in a cross platform way
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/filepath-bytestring
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
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
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
# /oreon:deps
%description
This package provides functionality for manipulating 'RawFilePath' values.
It can be used as a drop in replacement for the filepath library to get the
benefits of using ByteStrings. It provides three modules:

* "System.FilePath.Posix.ByteString" manipulates POSIX/Linux style
'RawFilePath' values (with '/' as the path separator).

* "System.FilePath.Windows.ByteString" manipulates Windows style 'RawFilePath'
values (with either '\' or '/' as the path separator, and deals with drives).

* "System.FilePath.ByteString" is an alias for the module appropriate to your
platform.

All three modules provide the same API, and the same documentation (calling out
differences in the different variants).

This package is now deprecated, since filepath 1.4.100.0 provides an OsPath
type that is based on a bytestring. See
https://hasufell.github.io/posts/2022-06-29-fixing-haskell-filepaths.html.

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
This package provides the Haskell %{pkg_name} library
documentation.
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
%files -n ghc-filepath-bytestring-devel -f %{oreon_filedir}/ghc-filepath-bytestring-devel.list
%files -n ghc-filepath-bytestring-doc -f %{oreon_filedir}/ghc-filepath-bytestring-doc.list
%files -n ghc-filepath-bytestring-prof -f %{oreon_filedir}/ghc-filepath-bytestring-prof.list

%changelog

%autochangelog
