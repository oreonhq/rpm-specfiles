%global source0_hash 2d83efa441110d35d02ddc286c04f7661d94c18e167a815ef7a2578b2a636a4d
%global pkg_name xmonad-contrib
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        0.18.2
Release:        1%{?dist}
Summary:        Community-maintained extensions for xmonad
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/xmonad-contrib
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Patch0:         xmonad-contrib-use_xft-flag.patch
Patch1:         xmonad-contrib-ewmh-set-NET_WM_STATE.patch
Patch2:         xmonad-contrib-0.17.0-PositionStore-dont-rescale-with-screen.patch
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-X11-devel
BuildRequires:  ghc-X11-prof
BuildRequires:  ghc-X11-xft-devel
BuildRequires:  ghc-X11-xft-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-utf8-string-prof
BuildRequires:  ghc-xmonad-devel
BuildRequires:  ghc-xmonad-prof
# /oreon:deps
%description
Community-maintained tiling algorithms and extension modules for xmonad, an X11
tiling window manager.

For an introduction to building, configuring and using xmonad extensions, see
"XMonad.Doc". In particular:

"XMonad.Doc.Configuring", a guide to configuring xmonad
"XMonad.Doc.Extending", using the contributed extensions library
"XMonad.Doc.Developing", introduction to xmonad internals and writing your own
extensions.

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
%autopatch -p1
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-xmonad-contrib-devel -f %{oreon_filedir}/ghc-xmonad-contrib-devel.list
%files -n ghc-xmonad-contrib-doc -f %{oreon_filedir}/ghc-xmonad-contrib-doc.list
%files -n ghc-xmonad-contrib-prof -f %{oreon_filedir}/ghc-xmonad-contrib-prof.list

%changelog

%autochangelog
