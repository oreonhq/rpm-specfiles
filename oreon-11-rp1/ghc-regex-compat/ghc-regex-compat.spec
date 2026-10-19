%global source0_hash e27ed1d8c3616a7bd471c66950c7dd3bbdfe435da8319d647bfea12031bb301c
%global pkg_name regex-compat
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.95.2.2
Release:        1%{?dist}
Summary:        Replaces/enhances "Text.Regex"
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/regex-compat
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-regex-base-devel
BuildRequires:  ghc-regex-base-prof
BuildRequires:  ghc-regex-posix-devel
BuildRequires:  ghc-regex-posix-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
One module compat layer over <//hackage.haskell.org/package/regex-posix
regex-posix> to replace "Text.Regex".

See also <https://wiki.haskell.org/Regular_expressions> for more information.

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
%files -n ghc-regex-compat-devel -f %{oreon_filedir}/ghc-regex-compat-devel.list
%files -n ghc-regex-compat-doc -f %{oreon_filedir}/ghc-regex-compat-doc.list
%files -n ghc-regex-compat-prof -f %{oreon_filedir}/ghc-regex-compat-prof.list

%changelog

%autochangelog
