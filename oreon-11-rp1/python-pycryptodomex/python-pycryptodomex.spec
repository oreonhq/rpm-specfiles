%global source0_hash none

%global srcname pycryptodomex
%global _description %{expand:PyCryptodome is a self-contained Python package of low-level cryptographic
primitives. It's a fork of PyCrypto. It brings several enhancements with respect
to the last official version of PyCrypto (2.6.1), for instance:

  * Authenticated encryption modes (GCM, CCM, EAX, SIV, OCB)
  * Accelerated AES on Intel platforms via AES-NI
  * Elliptic curves cryptography (NIST P-256 curve only)
  * Better and more compact API (nonce and iv attributes for ciphers, automatic
    generation of random nonces and IVs, simplified CTR cipher mode, and more)
  * SHA-3 (including SHAKE XOFs) and BLAKE2 hash algorithms
  * Salsa20 and ChaCha20 stream ciphers
  * scrypt and HKDF
  * Deterministic (EC)DSA
  * Password-protected PKCS#8 key containers
  * Shamir's Secret Sharing scheme
  * Random numbers get sourced directly from the OS (and not from a CSPRNG in
    userspace)
  * Cleaner RSA and DSA key generation (largely based on FIPS 186-4)
  * Major clean ups and simplification of the code base

PyCryptodome is not a wrapper to a separate C library like OpenSSL. To the
largest possible extent, algorithms are implemented in pure Python. Only the
pieces that are extremely critical to performance (e.g. block ciphers) are
implemented as C extensions.

Note: all modules are installed under the Cryptodome package to avoid conflicts
with the PyCrypto library.}

Name:           python-%{srcname}
Version:        3.23.0
Release:        5%{?dist}
Summary:        A self-contained cryptographic library for Python

# PyCrypto-based code is public domain, further PyCryptodome contributions are
# BSD
License:        BSD-2-Clause AND LicenseRef-Fedora-Public-Domain
URL:            http://www.pycryptodome.org/
Source0:        https://github.com/Legrandin/pycryptodome/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Use external libtomcrypt library
Patch0:         %{name}-3.15.0-use_external_libtomcrypt.patch

BuildRequires:  gcc
BuildRequires:  libtomcrypt-devel
BuildRequires:  make
BuildRequires:  python3-devel
# Needed for documentation
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-autodoc-typehints}
BuildRequires:  %{py3_dist sphinx-rtd-theme}

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
# GMP library is dl-opened
Requires:       gmp%{?_isa}

%description -n python3-%{srcname}
%{_description}

%package -n python3-%{srcname}-selftest
Summary:        PyCryptodome test suite module
Requires:       python3-%{srcname}%{?_isa}

%description -n python3-%{srcname}-selftest
%{_description}

This package provides the PyCryptodome test suite module (Cryptodome.SelfTest).

%prep
%autosetup -n pycryptodome-%{version} -p0

# Drop bundled libraries
rm -r src/libtom/

# Remove shebang
sed '1{\@^#! /usr/bin/env python@d}' lib/Crypto/SelfTest/__main__.py >lib/Crypto/SelfTest/__main__.py.new && \
touch -r lib/Crypto/SelfTest/__main__.py lib/Crypto/SelfTest/__main__.py.new && \
mv lib/Crypto/SelfTest/__main__.py.new lib/Crypto/SelfTest/__main__.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
touch .separate_namespace
%pyproject_wheel

# Build man pages
%make_build -C Doc/ man SPHINXBUILD=sphinx-build

%install
%pyproject_install
%pyproject_save_files Cryptodome

# Install man pages
install -Dpm 0644 Doc/_build/man/pycryptodome.1 $RPM_BUILD_ROOT%{_mandir}/man1/pycryptodome.1

%check
PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitearch}/ %{__python3} %{py_setup} test

%files -n python3-%{srcname} -f %{pyproject_files}
%doc AUTHORS.rst Changelog.rst README.rst
%license LICENSE.rst
%exclude %{python3_sitearch}/Cryptodome/SelfTest/
%{_mandir}/man1/pycryptodome.1*

%files -n python3-%{srcname}-selftest
%{python3_sitearch}/Cryptodome/SelfTest/

%changelog
%autochangelog
