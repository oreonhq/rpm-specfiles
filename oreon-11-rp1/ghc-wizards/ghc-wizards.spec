%global source1_hash cb7798895ee35e06c00a69eb1cd8a3c45921e3c5fb76ffcf11a76a15fbda4365
%global source0_hash 05650d7bf6dd0e6b87d0d7da6fb003601ce5d7b1f3d69571127ec3c9425b9bb2
%global pkg_name wizards
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        1.0.3
Release:        1%{?dist}
Summary:        High level, generic library for interrogative user interfaces
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/wizards
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-control-monad-free-devel
BuildRequires:  ghc-control-monad-free-prof
BuildRequires:  ghc-haskeline-devel
BuildRequires:  ghc-haskeline-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
# /oreon:deps
%description
'wizards' is a package designed for the quick and painless development of
/interrogative/ programs, which revolve around a "dialogue" with the user, who
is asked a series of questions in a sequence much like an installation wizard.

Everything from interactive system scripts, to installation wizards, to
full-blown shells can be implemented with the support of 'wizards'.

It is developed transparently on top of a free monad, which separates out the
semantics of the program from any particular interface. A variety of backends
exist, including console-based "System.Console.Wizard.Haskeline" and
"System.Console.Wizard.BasicIO", and the pure "System.Console.Wizard.Pure".
It is also possible to write your own backends, or extend existing back-ends
with new features. While both built-in IO backends operate on a console, there
is no reason why 'wizards' cannot also be used for making GUI wizard
interfaces.

See the github page for examples on usage:

<http://www.github.com/liamoc/wizards>

For creating backends, the module "System.Console.Wizard.Internal" has a brief
tutorial.

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
%files -n ghc-wizards-devel -f %{oreon_filedir}/ghc-wizards-devel.list
%files -n ghc-wizards-doc -f %{oreon_filedir}/ghc-wizards-doc.list
%files -n ghc-wizards-prof -f %{oreon_filedir}/ghc-wizards-prof.list

%changelog

%autochangelog
