%global source0_hash a087fa01a1c52f5386d43f5355f64841c5a4b56b53720090d66b5aa00bfeb106
%global pkg_name js-jquery
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 0
Name:           ghc-%{pkg_name}
Version:        3.7.1
Release:        1%{?dist}
Summary:        Obtain minified jQuery code
License:        MIT
URL:            https://hackage.haskell.org/package/js-jquery
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
Provides: bundled(jquery) = %{version}
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HTTP-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
This package bundles the minified <http://jquery.com/ jQuery> code into a
Haskell package, so it can be depended upon by Cabal packages. The first three
components of the version number match the upstream jQuery version.
The package is designed to meet the redistribution requirements of downstream
users (e.g. Debian).

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

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-js-jquery-devel -f %{oreon_filedir}/ghc-js-jquery-devel.list
%files -n ghc-js-jquery-doc -f %{oreon_filedir}/ghc-js-jquery-doc.list
%files -n ghc-js-jquery-prof -f %{oreon_filedir}/ghc-js-jquery-prof.list

%changelog

%autochangelog
