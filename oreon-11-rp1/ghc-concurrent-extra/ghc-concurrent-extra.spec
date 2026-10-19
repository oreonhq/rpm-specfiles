%global source0_hash 040e6db9e0147de9929661759930f1566a7250add4c7f65b04dc6e070c991df9
%global pkg_name concurrent-extra
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.7.0.12
Release:        1%{?dist}
Summary:        Extra concurrency primitives
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/concurrent-extra
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-unbounded-delays-devel
BuildRequires:  ghc-unbounded-delays-prof
# /oreon:deps
%description
The 'concurrent-extra' package offers among other things the following
selection of synchronisation primitives:

* 'Broadcast': Wake multiple threads by broadcasting a value.

* 'Event': Wake multiple threads by signaling an event.

* 'Lock': Enforce exclusive access to a resource. Also known as a binary
semaphore or mutex. The package additionally provides an alternative that works
in the 'STM' monad.

* 'RLock': A lock which can be acquired multiple times by the same thread.
Also known as a reentrant mutex.

* 'ReadWriteLock': Multiple-reader, single-writer locks. Used to protect shared
resources which may be concurrently read, but only sequentially written.

* 'ReadWriteVar': Concurrent read, sequential write variables.

Please consult the API documentation of the individual modules for more
detailed information.

This package was inspired by the concurrency libraries of Java and Python.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides the Haskell %{pkg_name} library development
files.

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
%files -n ghc-concurrent-extra-devel -f %{oreon_filedir}/ghc-concurrent-extra-devel.list
%files -n ghc-concurrent-extra-doc -f %{oreon_filedir}/ghc-concurrent-extra-doc.list
%files -n ghc-concurrent-extra-prof -f %{oreon_filedir}/ghc-concurrent-extra-prof.list

%changelog

%autochangelog
