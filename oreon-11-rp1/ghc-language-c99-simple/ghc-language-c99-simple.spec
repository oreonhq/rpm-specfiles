%global source0_hash 7275797bd2cfd4799ae0094ecd9da4e9333d12defd396277ac403343e542e06e
%global pkg_name language-c99-simple
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.3.0
Release:        1%{?dist}
Summary:        C-like AST to simplify writing C99 programs
License:        MIT
URL:            https://hackage.haskell.org/package/language-c99-simple
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-language-c99-devel
BuildRequires:  ghc-language-c99-prof
BuildRequires:  ghc-language-c99-util-devel
BuildRequires:  ghc-language-c99-util-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
This package is a wrapper on top of 'language-c99'. It provides a simpler
interface more suited for writing C99 programs. It achieves this by
implementing its own C-like AST, supporting the most used C features.
In turn, this AST is translated into actual C99 one, showing that it is an
actual subset.

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

%files -f %{oreon_filedir}/main.list
%files -n ghc-language-c99-simple-devel -f %{oreon_filedir}/ghc-language-c99-simple-devel.list
%files -n ghc-language-c99-simple-doc -f %{oreon_filedir}/ghc-language-c99-simple-doc.list
%files -n ghc-language-c99-simple-prof -f %{oreon_filedir}/ghc-language-c99-simple-prof.list

%changelog

%autochangelog
