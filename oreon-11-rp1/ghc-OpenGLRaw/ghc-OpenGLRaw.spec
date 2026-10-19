%global source1_hash 01b745fbd269fc96d982c3c915c5559793457ff02f9f6cce3ee259aed97378f1
%global source0_hash 121abdea149ac74514efb2c1c1c319466757242d1b72a8bdf99d49535f06d31e
%global pkg_name OpenGLRaw
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        3.3.4.1
Release:        1%{?dist}
Summary:        A raw binding for the OpenGL graphics system
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/OpenGLRaw
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-fixed-devel
BuildRequires:  ghc-fixed-prof
BuildRequires:  ghc-half-devel
BuildRequires:  ghc-half-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  libglvnd-devel
# /oreon:deps
%description
OpenGLRaw is a raw Haskell binding for the OpenGL 4.6 graphics system and lots
of OpenGL extensions. It is basically a 1:1 mapping of OpenGL's C API, intended
as a basis for a nicer interface. OpenGLRaw offers access to all necessary
functions, tokens and types plus a general facility for loading extension
entries. The module hierarchy closely mirrors the naming structure of the
OpenGL extensions, making it easy to find the right module to import.
All API entries are loaded dynamically, so no special C header files are needed
for building this package. If an API entry is not found at runtime, a userError
is thrown.

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
Requires:       libglvnd-devel%{?_isa}
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
dos2unix -k -n %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-OpenGLRaw-devel -f %{oreon_filedir}/ghc-OpenGLRaw-devel.list
%files -n ghc-OpenGLRaw-doc -f %{oreon_filedir}/ghc-OpenGLRaw-doc.list
%files -n ghc-OpenGLRaw-prof -f %{oreon_filedir}/ghc-OpenGLRaw-prof.list

%changelog

%autochangelog
