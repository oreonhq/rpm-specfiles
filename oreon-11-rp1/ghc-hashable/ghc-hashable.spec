%global source0_hash ed0b7c10ce92c9ffe45420dadc38c6d39db486ff3633ff13567cc9f75f79b112
%global pkg_name hashable
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%ifnarch s390x
%bcond tests 1
%endif
Name:           ghc-%{pkg_name}
Version:        1.5.1.0
Release:        8%{?dist}
Summary:        A class for types that can be converted to a hash value
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/hashable
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-os-string-devel
BuildRequires:  ghc-os-string-prof
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
# /oreon:deps
%description
This package defines a class, 'Hashable', for types that can be converted to a
hash value. This class exists for the benefit of hashing-based data structures.
The package provides instances for basic types and a way to combine hash
values.

'Hashable' is intended exclusively for use in in-memory data structures.

'Hashable' does /not/ have a fixed standard. This allows it to improve over
time.

Because it does not have a fixed standard, different computers or computers on
different versions of the code will observe different hash values. As such,
'hashable' is not recommended for use other than in-memory datastructures.
Specifically, 'hashable' is not intended for network use or in applications
which persist hashed values. For stable hashing use named hashes: sha256,
crc32, xxhash etc.

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

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-hashable-devel -f %{oreon_filedir}/ghc-hashable-devel.list
%files -n ghc-hashable-doc -f %{oreon_filedir}/ghc-hashable-doc.list
%files -n ghc-hashable-prof -f %{oreon_filedir}/ghc-hashable-prof.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.1.0-8
- Prepare for Oreon 11 (RP1)
