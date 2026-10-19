%global source2_hash ef0fa6639a972869445fb2c92dafa09bca5628b8ba03d52f17673745e73261c0
%global source1_hash b74eca9290fe838a0e3be857a38b62cf6fb7478acee400eac19e47471a2c96b5
%global source0_hash a47457fd746db202711b6a6b34a8575daa291a01a99cd0900e639aadc06fca7e
%global pkg_name snap-server
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global iostreamshaproxy io-streams-haproxy-1.0.1.0
%global subpkgs %{iostreamshaproxy}
Name:           ghc-%{pkg_name}
Version:        1.1.2.1
Release:        32%{?dist}
Summary:        A web server for the Snap Framework
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/snap-server
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{iostreamshaproxy}/%{iostreamshaproxy}.tar.gz
Source2:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-blaze-builder-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-clock-devel
BuildRequires:  ghc-clock-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-io-streams-devel
BuildRequires:  ghc-io-streams-prof
BuildRequires:  ghc-lifted-base-devel
BuildRequires:  ghc-lifted-base-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-old-locale-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-snap-core-devel
BuildRequires:  ghc-snap-core-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unix-compat-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
# /oreon:deps
%description
Snap is a simple and fast web development framework and server written in
Haskell. For more information or to download the latest version, you can visit
the Snap project website at <http://snapframework.com/>.

The Snap HTTP server is a high performance web server library written in
Haskell. Together with the 'snap-core' library upon which it depends, it
provides a clean and efficient Haskell programming interface to the HTTP
protocol.

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
%ghc_lib_subpackage -l BSD-3-Clause %{iostreamshaproxy}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
dos2unix -k -n %{SOURCE2} %{pkg_name}.cabal
# End cabal-rpm setup
cabal-tweak-drop-dep bytestring-builder,

(
cd %{iostreamshaproxy}
cabal-tweak-dep-ver attoparsec '< 0.14' '< 0.15'
cabal-tweak-dep-ver base '< 4.13' '< 4.21'
cabal-tweak-dep-ver bytestring '< 0.11' '< 0.13'
cabal-tweak-dep-ver network '< 3.1' '< 3.3'
cabal-tweak-dep-ver transformers '< 0.6' '< 0.7'
)

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-snap-server-devel -f %{oreon_filedir}/ghc-snap-server-devel.list
%files -n ghc-snap-server-doc -f %{oreon_filedir}/ghc-snap-server-doc.list
%files -n ghc-snap-server-prof -f %{oreon_filedir}/ghc-snap-server-prof.list

%changelog

%autochangelog
