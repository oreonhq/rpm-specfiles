%global source0_hash 7e570460c35c5deec54d1ba46305ddb4679c7d4aae84f631dd0c61daaeaa8150
%global pkg_name regex-posix
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.96.0.2
Release:        1%{?dist}
Summary:        POSIX Backend for "Text.Regex" (regex-base)
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/regex-posix
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-regex-base-devel
BuildRequires:  ghc-regex-base-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
The POSIX regex backend for <//hackage.haskell.org/package/regex-base
regex-base>.

The main appeal of this backend is that it's very lightweight due to its
reliance on the ubiquitous
<https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/regex.h.html POSIX.2
regex> facility that is provided by the standard C library on most POSIX
platforms.

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
%files -n ghc-regex-posix-devel -f %{oreon_filedir}/ghc-regex-posix-devel.list
%files -n ghc-regex-posix-doc -f %{oreon_filedir}/ghc-regex-posix-doc.list
%files -n ghc-regex-posix-prof -f %{oreon_filedir}/ghc-regex-posix-prof.list

%changelog

%autochangelog
