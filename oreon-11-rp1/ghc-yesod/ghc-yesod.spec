%global source0_hash e5359450328be1c00c54d46c320041877d2d6febfa427a0c027516a8ca74670b
%global pkg_name yesod
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        1.6.2.3
Release:        1%{?dist}
Summary:        Creation of type-safe, RESTful web applications
License:        MIT
URL:            https://hackage.haskell.org/package/yesod
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-data-default-class-devel
BuildRequires:  ghc-data-default-class-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-fast-logger-devel
BuildRequires:  ghc-fast-logger-prof
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-file-embed-prof
BuildRequires:  ghc-monad-logger-devel
BuildRequires:  ghc-monad-logger-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-shakespeare-devel
BuildRequires:  ghc-shakespeare-prof
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-streaming-commons-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-wai-extra-devel
BuildRequires:  ghc-wai-extra-prof
BuildRequires:  ghc-wai-logger-devel
BuildRequires:  ghc-wai-logger-prof
BuildRequires:  ghc-wai-prof
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-warp-prof
BuildRequires:  ghc-yaml-devel
BuildRequires:  ghc-yaml-prof
BuildRequires:  ghc-yesod-core-devel
BuildRequires:  ghc-yesod-core-prof
BuildRequires:  ghc-yesod-form-devel
BuildRequires:  ghc-yesod-form-prof
BuildRequires:  ghc-yesod-persistent-devel
BuildRequires:  ghc-yesod-persistent-prof
# /oreon:deps
%description
The yesod package groups together the various Yesod related packages
into one cohesive whole.

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
%files -n ghc-yesod-devel -f %{oreon_filedir}/ghc-yesod-devel.list
%files -n ghc-yesod-doc -f %{oreon_filedir}/ghc-yesod-doc.list
%files -n ghc-yesod-prof -f %{oreon_filedir}/ghc-yesod-prof.list

%changelog

%autochangelog
