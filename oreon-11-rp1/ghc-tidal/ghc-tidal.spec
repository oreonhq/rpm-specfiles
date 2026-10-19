%global source2_hash 5b6feadab19bd66a15645b8520f066770ae6e43d624c3269160aa2ef54ab5897
%global source1_hash 326d7110d2f9fd5653f6bb906506aad00bb61c41594f99eb97c0155e6175fff1
%global source0_hash 5da17198327675b22edc1170bb45b91e4754088abb46092dc602eb99173a5046
%global pkg_name tidal
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global tidalcore tidal-core-1.10.1
%global tidallink tidal-link-1.2.0
%global subpkgs %{tidalcore} %{tidallink}
%ifnarch s390x %{ix86}
%bcond tests 1
%endif
Name:           ghc-%{pkg_name}
Version:        1.10.3
Release:        1%{?dist}
Summary:        Pattern language for improvised music
License:        GPL-3.0-or-later
URL:            https://hackage.haskell.org/package/tidal
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{tidalcore}/%{tidalcore}.tar.gz
Source2:        https://hackage.haskell.org/package/%{tidallink}/%{tidallink}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-clock-devel
BuildRequires:  ghc-clock-prof
BuildRequires:  ghc-colour-devel
BuildRequires:  ghc-colour-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-hosc-devel
BuildRequires:  ghc-hosc-prof
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
# /oreon:deps
%description
Tidal is a domain specific language for live coding patterns.

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

%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l GPL-3.0-or-later %{tidalcore}
%ghc_lib_subpackage -l GPL-3.0-or-later %{tidallink}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1 -a2
# End cabal-rpm setup

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
echo %{_bindir}/tidal-linktest >> %{tidallink}/ghc-tidal-link-devel.files
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-tidal-devel -f %{oreon_filedir}/ghc-tidal-devel.list
%files -n ghc-tidal-doc -f %{oreon_filedir}/ghc-tidal-doc.list
%files -n ghc-tidal-prof -f %{oreon_filedir}/ghc-tidal-prof.list

%changelog

%autochangelog
