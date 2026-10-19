%global source1_hash b81733e9b429f9ecb351fe806b2edc10bac8199273b7d7932ffa3653596f0053
%global source0_hash 928260b9db16e216d38793aba776743399ba977308dd88877a3fdf834ea3bd30
%global pkg_name zip-archive
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        0.5
Release:        1%{?dist}
Summary:        Library for creating and modifying zip archives
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/zip-archive
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-digest-devel
BuildRequires:  ghc-digest-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-zlib-devel
BuildRequires:  ghc-zlib-prof
BuildRequires:  unzip
# /oreon:deps
%description
The zip-archive library provides functions for creating, modifying, and
extracting files from zip archives. The zip archive format is documented in
<http://www.pkware.com/documents/casestudies/APPNOTE.TXT>.

Certain simplifying assumptions are made about the zip archives: in particular,
there is no support for strong encryption, zip files that span multiple disks,
ZIP64, OS-specific file attributes, or compression methods other than Deflate.
However, the library should be able to read the most common zip archives, and
the archives it produces should be readable by all standard unzip programs.

Archives are built and extracted in memory, so manipulating large zip files
will consume a lot of memory. If you work with large zip files or need features
not supported by this library, a better choice may be
<http://hackage.haskell.org/package/zip zip>, which uses a memory-efficient
streaming approach. However, zip can only read and write archives inside
instances of MonadIO, so zip-archive is a better choice if you want to
manipulate zip archives in "pure" contexts.

As an example of the use of the library, a standalone zip archiver and
extracter is provided in the source distribution.

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

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-zip-archive-devel -f %{oreon_filedir}/ghc-zip-archive-devel.list
%files -n ghc-zip-archive-doc -f %{oreon_filedir}/ghc-zip-archive-doc.list
%files -n ghc-zip-archive-prof -f %{oreon_filedir}/ghc-zip-archive-prof.list

%changelog

%autochangelog
