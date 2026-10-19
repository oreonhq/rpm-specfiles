%global source1_hash eca91c02ccdc050cd335224af22a31a7d03f9f799a95227f0b8117be43311e1d
%global source0_hash 72d86f8aa625b461f4397f737346f78a1700a7ffbff55cf6375c5e18916e986d
%global pkg_name lukko
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.1.2
Release:        1%{?dist}
Summary:        File locking
License:        GPL-2.0-or-later AND BSD-3-Clause
URL:            https://hackage.haskell.org/package/lukko
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
This package provides access to platform dependent file locking APIs:

*
<https://www.gnu.org/software/libc/manual/html_node/Open-File-Description-Locks.html
Open file descriptor locking> on Linux ("Lukko.OFD") * BSD-style 'flock(2)'
locks on UNIX platforms ("Lukko.FLock") * Windows locking via
<https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-lockfilee
LockFileEx> ("Lukko.Windows") * No-op locking, which throws exceptions
("Lukko.NoOp") * "Lukko" module exports the best option for the target platform
with uniform API.

There are alternative file locking packages:

* "GHC.IO.Handle.Lock" in 'base >= 4.10' is good enough for most use cases.
However, uses only 'Handle's so these locks cannot be used for intra-process
locking. (You should use e.g. 'MVar' in addition).

* <https://hackage.haskell.org/package/filelock filelock> doesn't support OFD
locking.

/Lukko/ means lock in Finnish.

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
%files -n ghc-lukko-devel -f %{oreon_filedir}/ghc-lukko-devel.list
%files -n ghc-lukko-doc -f %{oreon_filedir}/ghc-lukko-doc.list
%files -n ghc-lukko-prof -f %{oreon_filedir}/ghc-lukko-prof.list

%changelog

%autochangelog
