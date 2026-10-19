%global source1_hash eaf28dc9884718a306ed1e0c215a24b36c68b8aa3be425617f66d886d43fe1e0
%global source0_hash c6a7d5e41ad0ee1a05c660acf4fd34b21f38330eec165d246b7fffb398e59fb3
%global pkg_name reflection
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        2.1.9
Release:        1%{?dist}
Summary:        Reifies arbitrary terms into types that can be reflected back into terms
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/reflection
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-discover-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
# /oreon:deps
%description
This package addresses the "configuration problem" which is propagating
configurations that are available at run-time, allowing multiple configurations
to coexist without resorting to mutable global variables or
'System.IO.Unsafe.unsafePerformIO'.

That package is an implementation of the ideas presented in the paper
"Functional Pearl: Implicit Configurations" by Oleg Kiselyov and Chung-chieh
Shan (<http://okmij.org/ftp/Haskell/tr-15-04.pdf original paper>).
However, the API has been streamlined to improve performance.

There are a handful of tutorials on how to use this library:

* Austin Seipp's tutorial
<https://www.schoolofhaskell.com/user/thoughtpolice/using-reflection Reflecting
values to types and back> provides a summary of the approach taken by this
library, along with more motivating examples.

* Arnaud Spiwack's tutorial
<https://www.tweag.io/posts/2017-12-21-reflection-tutorial.html All about
reflection> explains how to use this library.

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
%files -n ghc-reflection-devel -f %{oreon_filedir}/ghc-reflection-devel.list
%files -n ghc-reflection-doc -f %{oreon_filedir}/ghc-reflection-doc.list
%files -n ghc-reflection-prof -f %{oreon_filedir}/ghc-reflection-prof.list

%changelog

%autochangelog
