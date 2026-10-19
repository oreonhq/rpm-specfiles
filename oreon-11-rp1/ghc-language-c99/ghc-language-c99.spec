%global source0_hash 7062d0fb381308316f777b52a889ef6b4ed88c23804a1cf7b4653cac8b7bcc09
%global pkg_name language-c99
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.2.0
Release:        1%{?dist}
Summary:        An implementation of the C99 AST that strictly follows the standard
License:        MIT
URL:            https://hackage.haskell.org/package/language-c99
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
This package contains an implementation of the C99 AST as described in
<http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf>. Sticking closely
to this standard assures us that the program we deal with is a valid C99
program.

Additionally the library comes with a pretty printer.

The package does not come with handy wrapper and utility functions to write a
C99 program, it just contains the bare AST. It is highly recommended to use the
wrapper provided by 'language-c99-simple' and 'language-c99-util' for writing
programs.

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
%files -n ghc-language-c99-devel -f %{oreon_filedir}/ghc-language-c99-devel.list
%files -n ghc-language-c99-doc -f %{oreon_filedir}/ghc-language-c99-doc.list
%files -n ghc-language-c99-prof -f %{oreon_filedir}/ghc-language-c99-prof.list

%changelog

%autochangelog
