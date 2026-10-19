%global source1_hash bf5797222c7f3580b84b43cef84a51237b30d6be00a010d94ede59deeda19e06
%global source0_hash 3e44ac5d3e684b65e9efaf60ca9a907a86edc879dfcf63f86eebc721e542864d
%global pkg_name JuicyPixels
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        3.3.9
Release:        1%{?dist}
Summary:        Picture loading and serialization
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/JuicyPixels
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-zlib-devel
BuildRequires:  ghc-zlib-prof
# /oreon:deps
%description
This library can load and store images in PNG, Bitmap, Jpeg, Radiance, Tiff and
Gif images.

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
sed -i 's/\r$//' LICENSE

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-JuicyPixels-devel -f %{oreon_filedir}/ghc-JuicyPixels-devel.list
%files -n ghc-JuicyPixels-doc -f %{oreon_filedir}/ghc-JuicyPixels-doc.list
%files -n ghc-JuicyPixels-prof -f %{oreon_filedir}/ghc-JuicyPixels-prof.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.9-1
- Prepare for Oreon 11 (RP1)
