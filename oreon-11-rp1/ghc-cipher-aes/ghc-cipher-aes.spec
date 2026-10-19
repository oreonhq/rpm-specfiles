%global source0_hash d3b171895698c73da24d7ce97543f725d26637f038de670c0fd4012ca7f95015
%global pkg_name cipher-aes
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.2.11
Release:        1%{?dist}
Summary:        Fast AES cipher implementation with advanced mode of operations
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/cipher-aes
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-byteable-devel
BuildRequires:  ghc-byteable-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-crypto-cipher-types-devel
BuildRequires:  ghc-crypto-cipher-types-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-securemem-devel
BuildRequires:  ghc-securemem-prof
# /oreon:deps
%description
Fast AES cipher implementation with advanced mode of operations.

The modes of operations available are ECB (Electronic code book), CBC (Cipher
block chaining), CTR (Counter), XTS (XEX with ciphertext stealing), GCM (Galois
Counter Mode).

The AES implementation uses AES-NI when available (on x86 and x86-64
architecture), but fallback gracefully to a software C implementation.

The software implementation uses S-Boxes, which might suffer for cache timing
issues. However do notes that most other known software implementations,
including very popular one (openssl, gnutls) also uses similar implementation.
If it matters for your case, you should make sure you have AES-NI available, or
you'll need to use a different implementation.

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
%files -n ghc-cipher-aes-devel -f %{oreon_filedir}/ghc-cipher-aes-devel.list
%files -n ghc-cipher-aes-doc -f %{oreon_filedir}/ghc-cipher-aes-doc.list
%files -n ghc-cipher-aes-prof -f %{oreon_filedir}/ghc-cipher-aes-prof.list

%changelog

%autochangelog
