%global source0_hash 9cf083cef2e2ba88a425f132c8a82bfa931eb4b0c38232b2017f8fcea2e23073
%global source1_hash 9fc9ce2157f1889bd99a4d22c9f1c64589590be0f797c3efe71c8fa17a11a689
%global pkg_name ansi-terminal
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global ansiterminaltypes ansi-terminal-types-1.1.3
%global subpkgs %{ansiterminaltypes}
Name:           ghc-%{pkg_name}
Version:        1.1.5
Release:        1%{?dist}
Summary:        Simple ANSI terminal support
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/ansi-terminal
Source0:        https://hackage.haskell.org/package/ansi-terminal-%{version}/ansi-terminal-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/ansi-terminal-types-1.1.3/ansi-terminal-types-1.1.3.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-colour-devel
BuildRequires:  ghc-colour-prof
BuildRequires:  ghc-rpm-macros-extra
# /oreon:deps
%description
ANSI terminal support for Haskell: allows cursor movement, screen clearing,
color output, showing or hiding the cursor, and changing the title.
Works on UNIX and Windows.

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

%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l BSD-3-Clause %{ansiterminaltypes}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
# End cabal-rpm setup

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-ansi-terminal-devel -f %{oreon_filedir}/ghc-ansi-terminal-devel.list
%files -n ghc-ansi-terminal-doc -f %{oreon_filedir}/ghc-ansi-terminal-doc.list
%files -n ghc-ansi-terminal-prof -f %{oreon_filedir}/ghc-ansi-terminal-prof.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.5-1
- Prepare for Oreon 11 (RP1)
