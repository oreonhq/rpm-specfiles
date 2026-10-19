%global source0_hash ab78c945590aa7705a75dbee0cc602c23f46b0087ed04168261cff452d09c2d9
%global pkg_name crypton
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%ifnarch ppc64le s390x riscv64
%bcond tests 1
%endif
Name:           ghc-%{pkg_name}
Version:        2.1.3
Release:        1%{?dist}
Summary:        Cryptography Primitives sink
License:        BSD-3-Clause AND (CC0-1.0 OR Apache-2.0) AND (CC0-1.0 OR Apache-2.0 OR OpenSSL)
URL:            https://hackage.haskell.org/package/crypton
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-basement-devel
BuildRequires:  ghc-basement-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-memory-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-kat-devel
BuildRequires:  ghc-tasty-quickcheck-devel
# /oreon:deps
%description
A repository of cryptographic primitives.

* Symmetric ciphers: AES, DES, 3DES, CAST5, Blowfish, Twofish, Camellia, RC4,
Salsa, XSalsa, ChaCha.

* Hash: SHA1, SHA2, SHA3, SHAKE, MD2, MD4, MD5, Keccak, Skein, Ripemd, Tiger,
Whirlpool, Blake2

* MAC: HMAC, KMAC, Poly1305

* Asymmetric crypto: DSA, RSA, DH, ECDH, ECDSA, ECC, Curve25519, Curve448,
Ed25519, Ed448

* Key Derivation Function: PBKDF2, Scrypt, HKDF, Argon2, BCrypt, BCryptPBKDF

* Cryptographic Random generation: System Entropy, Deterministic Random
Generator

* Data related: Anti-Forensic Information Splitter (AFIS)

If anything cryptographic related is missing from here, submit a pull request
to have it added. This package strives to be a cryptographic kitchen sink that
provides cryptography for everyone.

Evaluate the security related to your requirements before using.

Read "Crypto.Tutorial" for a quick start guide.

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
%files -n ghc-crypton-devel -f %{oreon_filedir}/ghc-crypton-devel.list
%files -n ghc-crypton-doc -f %{oreon_filedir}/ghc-crypton-doc.list
%files -n ghc-crypton-prof -f %{oreon_filedir}/ghc-crypton-prof.list

%changelog

%autochangelog
