%global source1_hash 43f7e6f2d71a4f6b8b2b17c1790ba3a9f4f5bd781a2713d0343a9a491010957e
%global source0_hash 047fbf4499fe3a8b8b7e3e1ec0b1446181a03cd1dda4242b3db4d89f63899907
%global pkg_name gi-gdk
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        4.0.10
Release:        1%{?dist}
Summary:        Gdk bindings (compatibility layer)
License:        LGPL-2.1-or-later
URL:            https://hackage.haskell.org/package/gi-gdk
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-gi-gdk4-devel
BuildRequires:  ghc-gi-gdk4-prof
BuildRequires:  ghc-haskell-gi-devel
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
This package re-exports (for backward compatibility) the haskell-gi generated
bindings in the gi-gdk4 package.

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

# with dynamic Setup get:
# libHSgi-gio-2.0.25.so: error: undefined reference to 'g_tls_certificate_new_from_pkcs11_uris'
%define ghc_static_setup 1
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
dos2unix -k -n %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-gi-gdk-devel -f %{oreon_filedir}/ghc-gi-gdk-devel.list
%files -n ghc-gi-gdk-doc -f %{oreon_filedir}/ghc-gi-gdk-doc.list
%files -n ghc-gi-gdk-prof -f %{oreon_filedir}/ghc-gi-gdk-prof.list

%changelog

%autochangelog
