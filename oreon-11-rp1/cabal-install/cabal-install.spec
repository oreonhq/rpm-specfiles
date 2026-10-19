%global source3_hash f491b7323a85c03eb1d750c795e971ed397c339f622bded4f34a41f88bcaf83c
%global source2_hash deff01d066a027bfb609522465e8e0580d8b56004cebb5b1f3e0f05f79cbf85d
%global source1_hash 71dba1d353e9039834573291eaefdb10d7cbc62ee0d81e7a53e9e8cf55225e7a
%global source0_hash 7e5c3f5e53f7c91f9ff8f0fb075574e772562d0eeb400c402c7d9277558f0821
%global pkg_name cabal-install
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global cabalinstallsolver cabal-install-solver-3.12.1.0
%global openbrowser open-browser-0.4.0.0
%global subpkgs %{cabalinstallsolver} %{openbrowser}
Name:           %{pkg_name}
Version:        3.18.1.0
Release:        1%{?dist}
Summary:        The command-line interface for Cabal and Hackage
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/cabal-install
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{cabalinstallsolver}/%{cabalinstallsolver}.tar.gz
Source2:        https://hackage.haskell.org/package/%{openbrowser}/%{openbrowser}.tar.gz
Source3:        https://hackage.haskell.org/package/%{pkgver}/%{name}.cabal#/%{pkgver}.cabal
Source10:       cabal-install.sh
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
Requires:       filesystem
Requires:       bind-utils
Requires:       setup
Recommends:     ghc
Recommends:     zlib-devel
Obsoletes:      %{name}-common < %{version}-%{release}
Obsoletes:      %{name}-static < %{version}-%{release}
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Cabal-prof
BuildRequires:  ghc-Cabal-syntax-devel
BuildRequires:  ghc-Cabal-syntax-prof
BuildRequires:  ghc-HTTP-devel
BuildRequires:  ghc-HTTP-prof
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-base16-bytestring-prof
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-cryptohash-sha256-devel
BuildRequires:  ghc-cryptohash-sha256-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-echo-devel
BuildRequires:  ghc-echo-prof
BuildRequires:  ghc-edit-distance-devel
BuildRequires:  ghc-edit-distance-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-hackage-security-devel
BuildRequires:  ghc-hackage-security-prof
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-lukko-devel
BuildRequires:  ghc-lukko-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-regex-base-devel
BuildRequires:  ghc-regex-base-prof
BuildRequires:  ghc-regex-posix-devel
BuildRequires:  ghc-regex-posix-prof
BuildRequires:  ghc-resolv-devel
BuildRequires:  ghc-resolv-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-safe-exceptions-devel
BuildRequires:  ghc-safe-exceptions-prof
BuildRequires:  ghc-semaphore-compat-devel
BuildRequires:  ghc-semaphore-compat-prof
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-tar-devel
BuildRequires:  ghc-tar-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-zlib-devel
BuildRequires:  ghc-zlib-prof
# /oreon:deps
%description
The 'cabal' command-line program simplifies the process of managing Haskell
software by automating the fetching, configuration, compilation and
installation of Haskell libraries and programs.

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

%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l BSD-3-Clause %{cabalinstallsolver}
%ghc_lib_subpackage -l BSD-3-Clause %{openbrowser}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -a1 -a2
dos2unix -k -n %{SOURCE3} %{name}.cabal
# End cabal-rpm setup

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
install -pm 644 -D -t %{buildroot}%{bash_completions_dir} bash-completion/cabal
install -pm 644 -D -t %{buildroot}%{_sysconfdir}/profile.d/ %{SOURCE10}
%oreon_autofiles ghc-cabal-install usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ghc-cabal-install-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ghc-cabal-install-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ghc-cabal-install-prof usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-cabal-install -f %{oreon_filedir}/ghc-cabal-install.list
%files -n ghc-cabal-install-devel -f %{oreon_filedir}/ghc-cabal-install-devel.list
%files -n ghc-cabal-install-doc -f %{oreon_filedir}/ghc-cabal-install-doc.list
%files -n ghc-cabal-install-prof -f %{oreon_filedir}/ghc-cabal-install-prof.list

%changelog

%autochangelog
