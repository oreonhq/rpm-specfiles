%global source0_hash 7fa78ae9a2a1d1c69179238e8849340ad26be6496b763a489bf2e0eb5b7c4c19
%global pkg_name cpphs
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           %{pkg_name}
Version:        1.20.10
Release:        1%{?dist}
Summary:        A liberalised C pre-processor for Haskell
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/cpphs
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-polyparse-devel
BuildRequires:  ghc-polyparse-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
# /oreon:deps
%description
Cpphs is a re-implementation of the C pre-processor that is both more
compatible with Haskell, and itself written in Haskell so that it can be
distributed with compilers.

This version of the C pre-processor is pretty-much feature-complete and
compatible with traditional (K&R) pre-processors. Additional features include:
a plain-text mode; an option to unlit literate code files; and an option to
turn off macro-expansion.

%package -n ghc-%{name}
Summary:        Haskell %{name} library
License:        LGPL-2.1-or-later
%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.

%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
License:        LGPL-2.1-or-later
Provides:       ghc-%{name}-static = %{version}-%{release}
Provides:       ghc-%{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       ghc-%{name}%{?_isa} = %{version}-%{release}
%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.

%if %{with haddock}
%package -n ghc-%{name}-doc
Summary:        Haskell %{name} library documentation
License:        LGPL-2.1-or-later
BuildArch:      noarch
Requires:       ghc-filesystem
%description -n ghc-%{name}-doc
This package provides the Haskell %{name} library documentation.
%endif

%if %{with ghc_prof}
%package -n ghc-%{name}-prof
Summary:        Haskell %{name} profiling library
License:        LGPL-2.1-or-later
Requires:       ghc-%{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (ghc-%{name}-devel and ghc-prof)
%description -n ghc-%{name}-prof
This package provides the Haskell %{name} profiling library.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 644 -p -t %{buildroot}%{_mandir}/man1/ ./docs/cpphs.1
rm %{buildroot}%{_defaultlicensedir}/%{name}/LICENCE-LGPL
%oreon_autofiles ghc-cpphs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ghc-cpphs-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ghc-cpphs-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ghc-cpphs-prof usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-cpphs -f %{oreon_filedir}/ghc-cpphs.list
%files -n ghc-cpphs-devel -f %{oreon_filedir}/ghc-cpphs-devel.list
%files -n ghc-cpphs-doc -f %{oreon_filedir}/ghc-cpphs-doc.list
%files -n ghc-cpphs-prof -f %{oreon_filedir}/ghc-cpphs-prof.list

%changelog

%autochangelog
