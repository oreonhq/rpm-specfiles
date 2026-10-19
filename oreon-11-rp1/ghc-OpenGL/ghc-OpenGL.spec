%global source1_hash bcd8a08d9e2679b28faffffa71e3c7cc101bb72d7518ead85155dd3a194a2988
%global source0_hash 5a05ffc752dfc7dd16818d7b3c7c59a27639e246cdfa1963fa02e3ce247a2e19
%global pkg_name OpenGL
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        3.0.3.0
Release:        1%{?dist}
Summary:        A binding for the OpenGL graphics system
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/OpenGL
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-GLURaw-devel
BuildRequires:  ghc-GLURaw-prof
BuildRequires:  ghc-ObjectName-devel
BuildRequires:  ghc-ObjectName-prof
BuildRequires:  ghc-OpenGLRaw-devel
BuildRequires:  ghc-OpenGLRaw-prof
BuildRequires:  ghc-StateVar-devel
BuildRequires:  ghc-StateVar-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
# /oreon:deps
%description
A Haskell binding for the OpenGL graphics system (GL, version 4.6) and its
accompanying utility library (GLU, version 1.3).

OpenGL is the industry's most widely used and supported 2D and 3D graphics
application programming interface (API), incorporating a broad set of
rendering, texture mapping, special effects, and other powerful visualization
functions. For more information about OpenGL and its various extensions, please
see <http://www.opengl.org/> and <http://www.opengl.org/registry/>.

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
%files -n ghc-OpenGL-devel -f %{oreon_filedir}/ghc-OpenGL-devel.list
%files -n ghc-OpenGL-doc -f %{oreon_filedir}/ghc-OpenGL-doc.list
%files -n ghc-OpenGL-prof -f %{oreon_filedir}/ghc-OpenGL-prof.list

%changelog

%autochangelog
