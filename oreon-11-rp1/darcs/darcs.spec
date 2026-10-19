%global source2_hash 218e8746098c246a5cf497e96eac6b4305495de18dc5f281598d79b54e8decbb
%global source1_hash 6f6c1e7a9a9155ad78ca78cb9abd6f7e2e1c78b3e549b179dc0874e6428f490d
%global source0_hash e310692989e313191824f532a26c5eae712217444214266503d5eb5867f951ab
%global pkg_name darcs
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global dataordlist data-ordlist-0.4.7.0
%global strictidentity strict-identity-0.1.0.0
%global subpkgs %{dataordlist} %{strictidentity}
Name:           %{pkg_name}
Version:        2.18.5
Release:        1%{?dist}
Summary:        A distributed, interactive, smart revision control system
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/darcs
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{dataordlist}/%{dataordlist}.tar.gz
Source2:        https://hackage.haskell.org/package/%{strictidentity}/%{strictidentity}.tar.gz
Patch0:         darcs-Cabal-3.12.patch
%if %{with ghc_prof}
%endif
Obsoletes:      darcs-server < 2.2.1-6
Obsoletes:      darcs-common < %{version}-%{release}
Obsoletes:      darcs-static < %{version}-%{release}
# oreon:deps
BuildRequires:  bash-completion
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-base16-bytestring-prof
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-constraints-devel
BuildRequires:  ghc-constraints-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-crypton-connection-devel
BuildRequires:  ghc-crypton-connection-prof
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-cryptonite-prof
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-fgl-devel
BuildRequires:  ghc-fgl-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-haskeline-devel
BuildRequires:  ghc-haskeline-prof
BuildRequires:  ghc-html-devel
BuildRequires:  ghc-html-prof
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-client-tls-prof
BuildRequires:  ghc-http-conduit-devel
BuildRequires:  ghc-http-conduit-prof
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-memory-prof
BuildRequires:  ghc-mmap-devel
BuildRequires:  ghc-mmap-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-old-time-devel
BuildRequires:  ghc-old-time-prof
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-regex-applicative-devel
BuildRequires:  ghc-regex-applicative-prof
BuildRequires:  ghc-regex-base-devel
BuildRequires:  ghc-regex-base-prof
BuildRequires:  ghc-regex-tdfa-devel
BuildRequires:  ghc-regex-tdfa-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-tar-devel
BuildRequires:  ghc-tar-prof
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-temporary-prof
BuildRequires:  ghc-terminal-size-devel
BuildRequires:  ghc-terminal-size-prof
BuildRequires:  ghc-terminfo-devel
BuildRequires:  ghc-terminfo-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-tls-devel
BuildRequires:  ghc-tls-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unix-compat-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-utf8-string-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-zip-archive-devel
BuildRequires:  ghc-zip-archive-prof
BuildRequires:  ghc-zlib-devel
BuildRequires:  ghc-zlib-prof
# /oreon:deps
%description
Darcs is a distributed, interactive, smart revision control system.
Darcs is easy to learn and efficient to use because it asks you questions
in response to simple commands, giving you choices in your workflow.
You can choose to record one change in a file, while ignoring another.
You can review each patch as you update from upstream.
Originally developed by physicist David Roundy,
darcs is based on a unique algebra of patches.

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
%ghc_lib_subpackage -l BSD-3-Clause %{dataordlist}
%ghc_lib_subpackage -l BSD-3-Clause %{strictidentity}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -a1 -a2
%autopatch -p1
# End cabal-rpm setup
cabal-tweak-dep-ver base '< 4.20' '< 4.21'
cabal-tweak-dep-ver hashable '< 1.5' '< 1.6'
(
cd %{strictidentity}
cabal-tweak-dep-ver base '<4.8' '<4.21'
)

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
install -Dpm 644 contrib/darcs_completion %{buildroot}%{_datadir}/bash-completion/completions/darcs
%oreon_autofiles ghc-darcs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ghc-darcs-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ghc-darcs-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ghc-darcs-prof usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-darcs -f %{oreon_filedir}/ghc-darcs.list
%files -n ghc-darcs-devel -f %{oreon_filedir}/ghc-darcs-devel.list
%files -n ghc-darcs-doc -f %{oreon_filedir}/ghc-darcs-doc.list
%files -n ghc-darcs-prof -f %{oreon_filedir}/ghc-darcs-prof.list

%changelog

%autochangelog
