%global source0_hash c355407ca0c54bf02199358c7fa4ffd3174a59e951e1267b7db70810dfb0193a
%global pkg_name language-docker
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        16.0.0
Release:        1%{?dist}
Summary:        Dockerfile parser, pretty-printer and embedded DSL
License:        GPL-3.0-or-later
URL:            https://hackage.haskell.org/package/language-docker
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-default-class-devel
BuildRequires:  ghc-data-default-class-prof
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-discover-devel
BuildRequires:  ghc-hspec-megaparsec-devel
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-megaparsec-prof
BuildRequires:  ghc-prettyprinter-devel
BuildRequires:  ghc-prettyprinter-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
# /oreon:deps
%description
All functions for parsing and pretty-printing Dockerfiles are exported through
'Language.Docker'. For more fine-grained operations look for specific modules
that implement a certain functionality. See the
<https://github.com/hadolint/language-docker GitHub project> for the
source-code and examples.

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

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-language-docker-devel -f %{oreon_filedir}/ghc-language-docker-devel.list
%files -n ghc-language-docker-doc -f %{oreon_filedir}/ghc-language-docker-doc.list
%files -n ghc-language-docker-prof -f %{oreon_filedir}/ghc-language-docker-prof.list

%changelog

%autochangelog
