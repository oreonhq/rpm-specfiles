%global source0_hash 13a2adae4edf4394e15af0a3b825d8cee44b85dce55c21768468aae38bbe1dee
%global source1_hash 2f7398262895ba298c1f43aa055f509021ebec82593b7e745d80832c4e4f42ed
%global pkg_name texmath
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global typstsymbols typst-symbols-0.1.8.1
%global subpkgs %{typstsymbols}
Name:           ghc-%{pkg_name}
Version:        0.13.3
Release:        1%{?dist}
Summary:        Conversion between math formats
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/texmath
Source0:        https://hackage.haskell.org/package/texmath-%{version}/texmath-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/typst-symbols-0.1.8.1/typst-symbols-0.1.8.1.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-pandoc-types-devel
BuildRequires:  ghc-pandoc-types-prof
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-syb-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-xml-devel
BuildRequires:  ghc-xml-prof
# /oreon:deps
%description
The texmath library provides functions to read and write TeX math, presentation
MathML, and OMML (Office Math Markup Language, used in Microsoft Office).
Support is also included for converting math formats to Gnu eqn, typst, and
pandoc's native format (allowing conversion, via pandoc, to a variety of
different markup formats). The TeX reader supports basic LaTeX and AMS
extensions, and it can parse and apply LaTeX macros. (See
<https://johnmacfarlane.net/texmath here> for a live demo of bidirectional
conversion between LaTeX and MathML.)

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
%ghc_lib_subpackage -l MIT %{typstsymbols}
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
%files -n ghc-texmath-devel -f %{oreon_filedir}/ghc-texmath-devel.list
%files -n ghc-texmath-doc -f %{oreon_filedir}/ghc-texmath-doc.list
%files -n ghc-texmath-prof -f %{oreon_filedir}/ghc-texmath-prof.list

%changelog

%autochangelog
