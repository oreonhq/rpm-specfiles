%global source1_hash 88838540b080308174d4fa51f20f15f46ed928bf1cf664f533f9bda5ae1e0b8e
%global source0_hash 82b1afd9e2f0bf50afd190de4401132e879c031e06800c161e64eebbd1f2631b
%global pkg_name fsnotify
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global stringinterpolate string-interpolate-0.3.4.0
%global subpkgs %{stringinterpolate}
Name:           ghc-%{pkg_name}
Version:        0.4.4.0
Release:        13%{?dist}
Summary:        Cross platform library for file change notification
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/fsnotify
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{stringinterpolate}/%{stringinterpolate}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-haskell-src-exts-devel
BuildRequires:  ghc-haskell-src-exts-prof
BuildRequires:  ghc-haskell-src-meta-devel
BuildRequires:  ghc-haskell-src-meta-prof
BuildRequires:  ghc-hinotify-devel
BuildRequires:  ghc-hinotify-prof
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-monad-control-prof
BuildRequires:  ghc-monad-logger-devel
BuildRequires:  ghc-monad-logger-prof
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-retry-devel
BuildRequires:  ghc-retry-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-safe-exceptions-devel
BuildRequires:  ghc-safe-exceptions-prof
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-temporary-prof
BuildRequires:  ghc-text-conversions-devel
BuildRequires:  ghc-text-conversions-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unix-compat-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-unliftio-devel
BuildRequires:  ghc-unliftio-prof
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-utf8-string-prof
# /oreon:deps
%description
Cross platform library for file creation, modification, and deletion
notification. This library builds upon existing libraries for platform-specific
Windows, Mac, and Linux filesystem event notification.

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
%ghc_lib_subpackage -l BSD-3-Clause %{stringinterpolate}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
# End cabal-rpm setup
( cd %{stringinterpolate}
  cabal-tweak-dep-ver template-haskell '<2.22' '<2.23'
)

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
rm %{buildroot}%{_bindir}/example
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-fsnotify-devel -f %{oreon_filedir}/ghc-fsnotify-devel.list
%files -n ghc-fsnotify-doc -f %{oreon_filedir}/ghc-fsnotify-doc.list
%files -n ghc-fsnotify-prof -f %{oreon_filedir}/ghc-fsnotify-prof.list

%changelog

%autochangelog
