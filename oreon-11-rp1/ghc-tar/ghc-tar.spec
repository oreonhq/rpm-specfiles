%global source4_hash 389f7bfe97982486db9950d0f570795c975ecf3ee478fe732b79231b1f2fe731
%global source3_hash 310a19e4c792de4d30c912bc71ff3becb40818d7c796b9999bcd0979dab87d5b
%global source2_hash 1ade8fbee13db15e8d22a1ecdca54794617cabc69911b51d46a65e12f4554ef7
%global source1_hash b101e8dedc66da051a16022287d9b05c2dcb2f54f973fb09298b3486cd63ec2f
%global source0_hash d84e77b028024eacf4324e805aa2eff4478a6249c7d9f2588c97273f41b88d5e
%global pkg_name tar
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global atomiccounter atomic-counter-0.1.2.4
%global directoryospathstreaming directory-ospath-streaming-0.2.2
%global fileio file-io-0.1.5
%global subpkgs %{atomiccounter} %{directoryospathstreaming} %{fileio}
%bcond tests 0
Name:           ghc-%{pkg_name}
Version:        0.7.2.0
Release:        1%{?dist}
Summary:        Reading, writing and manipulating ".tar" archive files
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/tar
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.%{pkg_name}.gz
Source1:        https://hackage.haskell.org/package/%{atomiccounter}/%{atomiccounter}.tar.gz
Source2:        https://hackage.haskell.org/package/%{directoryospathstreaming}/%{directoryospathstreaming}.tar.gz
Source3:        https://hackage.haskell.org/package/%{fileio}/%{fileio}.tar.gz
Source4:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-os-string-devel
BuildRequires:  ghc-os-string-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
# /oreon:deps
%description
This library is for working with "'.tar'" archive files. It can read and write
a range of common variations of archive format including V7, POSIX USTAR and
GNU formats.

It provides support for packing and unpacking portable archives. This makes it
suitable for distribution but not backup because details like file ownership
and exact permissions are not preserved.

It also provides features for random access to archive content using an index.

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
%ghc_lib_subpackage -l Apache-2.0 %{atomiccounter}
%ghc_lib_subpackage -l Apache-2.0 %{directoryospathstreaming}
%ghc_lib_subpackage -l BSD-3-Clause %{fileio}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1 -a2 -a3
dos2unix -k -n %{SOURCE4} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-tar-devel -f %{oreon_filedir}/ghc-tar-devel.list
%files -n ghc-tar-doc -f %{oreon_filedir}/ghc-tar-doc.list
%files -n ghc-tar-prof -f %{oreon_filedir}/ghc-tar-prof.list

%changelog

%autochangelog
