%global source0_hash d3e4a55f94995f85987bd25232bf9000c0ca27c86a9cd073304be62591f84f07
%global pkg_name brainfuck
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           %{pkg_name}
Version:        0.1.0.4
Release:        1%{?dist}
Summary:        Brainfuck interpreter
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/brainfuck
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
# /oreon:deps
%description
This is an interpreter of the brainf*ck language, written in the pure, lazy,
functional language Haskell.

%package -n ghc-%{name}
Summary:        Haskell %{name} library
%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.

%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
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
BuildArch:      noarch
Requires:       ghc-filesystem
%description -n ghc-%{name}-doc
This package provides the Haskell %{name} library documentation.
%endif

%if %{with ghc_prof}
%package -n ghc-%{name}-prof
Summary:        Haskell %{name} profiling library
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
%oreon_autofiles ghc-brainfuck usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ghc-brainfuck-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ghc-brainfuck-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ghc-brainfuck-prof usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-brainfuck -f %{oreon_filedir}/ghc-brainfuck.list
%files -n ghc-brainfuck-devel -f %{oreon_filedir}/ghc-brainfuck-devel.list
%files -n ghc-brainfuck-doc -f %{oreon_filedir}/ghc-brainfuck-doc.list
%files -n ghc-brainfuck-prof -f %{oreon_filedir}/ghc-brainfuck-prof.list

%changelog

%autochangelog
