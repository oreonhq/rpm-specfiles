%global source0_hash b8e7f7b6a123ff22488f77a771cbd2cc285ef41299747662797abe9741778a6f
%global pkg_name fgl-visualize
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.1.0.1
Release:        1%{?dist}
Summary:        Convert FGL graphs to dot (graphviz) files
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/fgl-visualize
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-dotgen-devel
BuildRequires:  ghc-dotgen-prof
BuildRequires:  ghc-fgl-devel
BuildRequires:  ghc-fgl-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
Convert FGL graphs to dot files for easy visualization using the 'dot' tool.
Other visualizations might follow but there are no immediate plans (patches
welcome).

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
%files -n ghc-fgl-visualize-devel -f %{oreon_filedir}/ghc-fgl-visualize-devel.list
%files -n ghc-fgl-visualize-doc -f %{oreon_filedir}/ghc-fgl-visualize-doc.list
%files -n ghc-fgl-visualize-prof -f %{oreon_filedir}/ghc-fgl-visualize-prof.list

%changelog

%autochangelog
