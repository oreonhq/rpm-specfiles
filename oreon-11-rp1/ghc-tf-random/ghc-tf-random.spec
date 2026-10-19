%global source0_hash 2e30cec027b313c9e1794d326635d8fc5f79b6bf6e7580ab4b00186dadc88510
%global pkg_name tf-random
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.5
Release:        1%{?dist}
Summary:        High-quality splittable pseudorandom number generator
License:        BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL:            https://hackage.haskell.org/package/tf-random
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
# /oreon:deps
%description
This package contains an implementation of a high-quality splittable
pseudorandom number generator. The generator is based on a cryptographic hash
function built on top of the ThreeFish block cipher. See the paper /Splittable
Pseudorandom Number Generators Using Cryptographic Hashing/ by Claessen, Pałka
for details and the rationale of the design.

The package provides the following:

* A splittable PRNG that implements the standard 'System.Random.RandomGen'
class.

* The generator also implements an alternative version of the
'System.Random.TF.Gen.RandomGen' class (exported from "System.Random.TF.Gen"),
which requires the generator to return pseudorandom integers from the full
32-bit range, and contains an n-way split function.

* An alternative version of the 'Random' class is provided, which is linked to
the new 'RandomGen' class, together with 'Random' instances for some integral
types.

* Two functions for initialising the generator with a non-deterministic seed:
one using the system time, and one using the '/dev/urandom' UNIX special file.

The package uses an adapted version of the reference C implementation of
ThreeFish from the reference package of the Skein hash function
(<https://www.schneier.com/skein.html>), originally written by Doug Whiting.

Please note that even though the generator provides very high-quality
pseudorandom numbers, it has not been designed with cryptographic applications
in mind.

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
%files -n ghc-tf-random-devel -f %{oreon_filedir}/ghc-tf-random-devel.list
%files -n ghc-tf-random-doc -f %{oreon_filedir}/ghc-tf-random-doc.list
%files -n ghc-tf-random-prof -f %{oreon_filedir}/ghc-tf-random-prof.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5-1
- Prepare for Oreon 11 (RP1)
