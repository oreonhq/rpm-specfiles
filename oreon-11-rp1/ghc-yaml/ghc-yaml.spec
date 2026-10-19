%global source2_hash 6f0a1859e0fb3068e50dbc7fe9bf9a26847741bc24344e35e16a03711a18f88d
%global source0_hash ee74923ee5b0fef74413c58aaa20ea59baf5d29d256a62fb47cc279570d9dc2f
%global source1_hash d6297ec9b1ebb4e4b580a4357d840d08a6f53e13a10c0c53ee74b973bba6fa13
%global pkg_name yaml
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global libyaml libyaml-0.1.4
%global subpkgs %{libyaml}
Name:           ghc-%{pkg_name}
Version:        0.11.11.2
Release:        26%{?dist}
Summary:        Support for parsing and rendering YAML documents
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/yaml
Source0:        https://hackage.haskell.org/package/yaml-%{version}/yaml-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/libyaml-0.1.4/libyaml-0.1.4.tar.gz
Source2:        https://hackage.haskell.org/package/yaml-%{version}/yaml.cabal#/yaml-%{version}.cabal
Patch0:         system-libyaml.patch
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
BuildRequires:  libyaml-devel
# /oreon:deps
%description
Provides support for parsing and emitting Yaml documents.

The package is broken down into two modules. "Data.Yaml" provides a high-level
interface based around the JSON datatypes provided by the 'aeson' package.
"Text.Libyaml" provides a lower-level, streaming interface. For most users,
"Data.Yaml" is recommended.

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
%ghc_lib_subpackage -l BSD-3-Clause -c libyaml-devel%{?_isa} %{libyaml}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
dos2unix -k -n %{SOURCE2} %{pkg_name}.cabal
# End cabal-rpm setup
(
cd %{libyaml}
%patch -P0 -p1 -b .orig
)

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-yaml-devel -f %{oreon_filedir}/ghc-yaml-devel.list
%files -n ghc-yaml-doc -f %{oreon_filedir}/ghc-yaml-doc.list
%files -n ghc-yaml-prof -f %{oreon_filedir}/ghc-yaml-prof.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.11.11.2-26
- Prepare for Oreon 11 (RP1)
