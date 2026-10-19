%global source0_hash 63c830bd2af23e372ebfee628d9f538a32d8368cf74f897370d839bf8e7b4bc1
%global pkg_name control-monad-free
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.6.2
Release:        1%{?dist}
Summary:        Free monads and monad transformers
License:        LicenseRef-Fedora-Public-Domain
URL:            https://hackage.haskell.org/package/control-monad-free
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
# /oreon:deps
%description
This package provides datatypes to construct Free monads, Free monad
transformers, and useful instances. In addition it provides the constructs to
avoid quadratic complexity of left associative bind, as explained in:

Janis Voigtlander, Asymptotic Improvement of Computations over Free Monads,
MPC'08/. http://www.janis-voigtlaender.eu/Voi08d.html

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

%files -f %{oreon_filedir}/main.list
%files -n ghc-control-monad-free-devel -f %{oreon_filedir}/ghc-control-monad-free-devel.list
%files -n ghc-control-monad-free-doc -f %{oreon_filedir}/ghc-control-monad-free-doc.list
%files -n ghc-control-monad-free-prof -f %{oreon_filedir}/ghc-control-monad-free-prof.list

%changelog

%autochangelog
