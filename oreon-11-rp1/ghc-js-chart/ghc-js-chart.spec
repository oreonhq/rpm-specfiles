%global source0_hash 0a08efdd35bd1b8f293f9163f59305f31835304b74c3e3a1a840fc94bbc9bd0e
%global pkg_name js-chart
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        2.9.4.1
Release:        13%{?dist}
Summary:        Obtain minified chart.js code
License:        MIT
URL:            https://hackage.haskell.org/package/js-chart
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
Requires:       ghc-%{pkg_name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
This package bundles the minified <http://www.chartjs.org/ chart.js> code into
a Haskell package, so it can be depended upon by Cabal packages. The first
three components of the version number match the upstream chart.js version.
The package is designed to meet the redistribution requirements of downstream
users (e.g. Debian). This package is a fork of
<https://hackage.haskell.org/package/js-flot js-flot> using chart.js instead of
flot.

%package data
Summary:        Haskell %{pkg_name} library data files
BuildArch:      noarch
%description data
This package provides the Haskell %{pkg_name} library data files.

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
echo "%{_datadir}/%{pkgver}" >> ghc-js-chart-data.files
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-js-chart-data -f %{oreon_filedir}/ghc-js-chart-data.list
%files -n ghc-js-chart-devel -f %{oreon_filedir}/ghc-js-chart-devel.list
%files -n ghc-js-chart-doc -f %{oreon_filedir}/ghc-js-chart-doc.list
%files -n ghc-js-chart-prof -f %{oreon_filedir}/ghc-js-chart-prof.list

%changelog

%autochangelog
