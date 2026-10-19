%global source0_hash a589de48cfebe2d928266e6556a1997b6ecf2383e57d3a619aa40465b0075e6f
%global pkg_name select-rpms
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.3.1
Release:        1%{?dist}
Summary:        Select a subset of RPM packages
License:        MIT
URL:            https://hackage.haskell.org/package/select-rpms
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Glob-devel
BuildRequires:  ghc-Glob-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-extra-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-rpm-nvr-devel
BuildRequires:  ghc-rpm-nvr-prof
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-simple-cmd-args-devel
BuildRequires:  ghc-simple-cmd-args-prof
BuildRequires:  ghc-simple-cmd-devel
BuildRequires:  ghc-simple-cmd-prof
BuildRequires:  ghc-simple-prompt-devel
BuildRequires:  ghc-simple-prompt-prof
# /oreon:deps
%description
A library for selecting a subset of RPM (sub)packages.

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
%files -n ghc-select-rpms-devel -f %{oreon_filedir}/ghc-select-rpms-devel.list
%files -n ghc-select-rpms-doc -f %{oreon_filedir}/ghc-select-rpms-doc.list
%files -n ghc-select-rpms-prof -f %{oreon_filedir}/ghc-select-rpms-prof.list

%changelog

%autochangelog
