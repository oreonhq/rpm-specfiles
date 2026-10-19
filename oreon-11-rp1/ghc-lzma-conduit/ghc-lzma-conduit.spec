%global source1_hash 80a5278291a2ce114f0395733ee3a0cfbe106aa748e3e4b19b07982392eadcf1
%global source0_hash 3f980a11565128aac6f5f433bfd81999756a0c00bd2032bd5849909721abbbde
%global pkg_name lzma-conduit
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global lzma lzma-0.0.1.1
%global subpkgs %{lzma}
Name:           ghc-%{pkg_name}
Version:        1.2.3
Release:        27%{?dist}
Summary:        Conduit interface for lzma/xz compression
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/lzma-conduit
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{lzma}/%{lzma}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  xz-devel
# /oreon:deps
%description
This package provides an Conduit interface for the LZMA compression algorithm
used in the .xz file format.

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

%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l BSD-3-Clause -c xz-devel %{lzma}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
# End cabal-rpm setup
cabal-tweak-dep-ver bytestring '< 0.12' '< 0.13'
cabal-tweak-dep-ver resourcet '< 1.3' '< 1.4'
cabal-tweak-dep-ver transformers '< 0.6' '< 0.7'

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-lzma-conduit-devel -f %{oreon_filedir}/ghc-lzma-conduit-devel.list
%files -n ghc-lzma-conduit-doc -f %{oreon_filedir}/ghc-lzma-conduit-doc.list
%files -n ghc-lzma-conduit-prof -f %{oreon_filedir}/ghc-lzma-conduit-prof.list

%changelog

%autochangelog
