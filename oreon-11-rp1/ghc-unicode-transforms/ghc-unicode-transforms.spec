%global source2_hash b9162641de63cfe4eda8ad3ab4b483f6197173736751c7b3246c62b2b7107168
%global source1_hash b28733168535a23c068c2554a118f0ba544561f93f37a1c4e8556e3e4d029947
%global source0_hash 3278e1e1d648da4bcd7368658ae091a89080e88a2f44db9df5136711e99649fc
%global pkg_name unicode-transforms
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global unicodedata unicode-data-0.6.0
%global subpkgs %{unicodedata}
Name:           ghc-%{pkg_name}
Version:        0.4.0.1
Release:        14%{?dist}
Summary:        Unicode normalization
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/unicode-transforms
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{unicodedata}/%{unicodedata}.tar.gz
Source2:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
# /oreon:deps
%description
Fast Unicode 14.0.0 normalization in Haskell (NFC, NFKC, NFD, NFKD).

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

%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l Apache-2.0 %{unicodedata}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
dos2unix -k -n %{SOURCE2} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-unicode-transforms-devel -f %{oreon_filedir}/ghc-unicode-transforms-devel.list
%files -n ghc-unicode-transforms-doc -f %{oreon_filedir}/ghc-unicode-transforms-doc.list
%files -n ghc-unicode-transforms-prof -f %{oreon_filedir}/ghc-unicode-transforms-prof.list

%changelog

%autochangelog
