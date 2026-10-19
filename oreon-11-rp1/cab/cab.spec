%global source0_hash 422034ac06d60e150038fcbbf93bd30b2d944876e8bf628e5f7393fe16c6c9c5
%global pkg_name cab
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           %{pkg_name}
Version:        0.2.22
Release:        1%{?dist}
Summary:        Maintenance command for Haskell cabal packages
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/cab
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
Requires:       cabal-install
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Cabal-prof
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-conduit-extra-prof
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
Cab provides a maintenance command for Haskell cabal packages.
It is partly a wrapper of ghc-pkg and cabal.
If you get confused by the differences between the two commands,
need a way to check all outdated packages, or
to remove outdated packages recursively, this command will help.

%package -n ghc-%{name}
Summary:        Haskell %{name} library
%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.

%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Provides:       ghc-%{name}-static = %{version}-%{release}
Provides:       ghc-%{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       ghc-%{name}%{?_isa} = %{version}-%{release}
%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.

%if %{with haddock}
%package -n ghc-%{name}-doc
Summary:        Haskell %{name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem
%description -n ghc-%{name}-doc
This package provides the Haskell %{name} library documentation.
%endif

%if %{with ghc_prof}
%package -n ghc-%{name}-prof
Summary:        Haskell %{name} profiling library
Requires:       ghc-%{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (ghc-%{name}-devel and ghc-prof)
%description -n ghc-%{name}-prof
This package provides the Haskell %{name} profiling library.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles ghc-cab usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ghc-cab-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ghc-cab-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ghc-cab-prof usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-cab -f %{oreon_filedir}/ghc-cab.list
%files -n ghc-cab-devel -f %{oreon_filedir}/ghc-cab-devel.list
%files -n ghc-cab-doc -f %{oreon_filedir}/ghc-cab-doc.list
%files -n ghc-cab-prof -f %{oreon_filedir}/ghc-cab-prof.list

%changelog

%autochangelog
