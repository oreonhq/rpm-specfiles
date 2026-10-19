%global source0_hash 971d360428ac97af9a4e55e4f2c23649f6cedc0ce5d6e94d520e663f33ea5113
%global pkg_name blaze-builder
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.4.4.1
Release:        1%{?dist}
Summary:        Efficient buffered output
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/blaze-builder
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
# /oreon:deps
%description
This library allows to efficiently serialize Haskell values to lazy bytestrings
with a large average chunk size. The large average chunk size allows to make
good use of cache prefetching in later processing steps (e.g.
compression) and reduces the system call overhead when writing the resulting
lazy bytestring to a file or sending it over the network.

This library was inspired by the module Data.Binary.Builder provided by the
binary package. It was originally developed with the specific needs of the
blaze-html package in mind. Since then it has been restructured to serve as a
drop-in replacement for Data.Binary.Builder, which it improves upon both in
speed as well as expressivity.

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
%files -n ghc-blaze-builder-devel -f %{oreon_filedir}/ghc-blaze-builder-devel.list
%files -n ghc-blaze-builder-doc -f %{oreon_filedir}/ghc-blaze-builder-doc.list
%files -n ghc-blaze-builder-prof -f %{oreon_filedir}/ghc-blaze-builder-prof.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.4.1-1
- Prepare for Oreon 11 (RP1)
