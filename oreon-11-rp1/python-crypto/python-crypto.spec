%global source0_hash f2ce1e989b272cfcb677616763e0a2e7ec659effa67a88aa92b3a65528f60a3c

Summary:	Unmaintained cryptography library for Python
Name:		python-crypto
Version:	2.6.1
Release:	60%{?dist}
# Mostly LicenseRef-Fedora-Public-Domain apart from parts of HMAC.py and setup.py, which are PSF-2.0
License:	LicenseRef-Fedora-Public-Domain AND PSF-2.0
URL:		http://www.pycrypto.org/
Source0:	http://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/pycrypto-%{version}.tar.gz
Patch0:		python-crypto-2.4-optflags.patch
Patch1:		python-crypto-2.4-fix-pubkey-size-divisions.patch
Patch2:		pycrypto-2.6.1-CVE-2013-7459.patch
Patch3:		pycrypto-2.6.1-unbundle-libtomcrypt.patch
Patch4:		python-crypto-2.6.1-link.patch
Patch5:		pycrypto-2.6.1-CVE-2018-6594.patch
Patch6:		pycrypto-2.6.1-use-os-random.patch
Patch7:		pycrypto-2.6.1-drop-py2.1-support.patch
Patch8:		python-crypto-2.6.1-python3.10.patch
Patch9:		python-crypto-2.6.1-python3.11.patch
Patch10:	python-crypto-2.6.1-python3only.patch
Patch11:	python-crypto-2.6.1-no-distutils.patch
Patch12:	python-crypto-2.6.1-SyntaxWarning.patch
Patch13:	python-crypto-2.6.1-python3.12.patch
Patch14:	python-crypto-2.6.1-python3.13.patch
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	gmp-devel >= 4.1
BuildRequires:	libtomcrypt-devel >= 1.16
BuildRequires:	python3-devel

%description
PyCrypto is a collection of both secure hash functions (such as MD5 and
SHA), and various encryption algorithms (AES, DES, RSA, ElGamal, etc.).

This software is no longer maintained upstream. Please use the Cryptography
or PyCryptodome software instead.

%package -n python3-crypto
Summary:	Unmaintained cryptography library for Python

%description -n python3-crypto
PyCrypto is a collection of both secure hash functions (such as MD5 and
SHA), and various encryption algorithms (AES, DES, RSA, ElGamal, etc.).

This software is no longer maintained upstream. Please use the Cryptography
or PyCryptodome software instead.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n pycrypto-%{version} -q

# Use distribution compiler flags rather than upstream's
%patch -P 0 -p1

# Fix divisions within benchmarking suite:
%patch -P 1 -p1

# AES.new with invalid parameter crashes python
# https://github.com/dlitz/pycrypto/issues/176
# CVE-2013-7459
%patch -P 2 -p1

# Unbundle libtomcrypt (#1087557)
rm -rf src/libtom
%patch -P 3

# log() not available in libgmp, need libm too
%patch -P 4

# When creating ElGamal keys, the generator wasn't a square residue: ElGamal
# encryption done with those keys cannot be secure under the DDH assumption
# https://bugzilla.redhat.com/show_bug.cgi?id=1542313 (CVE-2018-6594)
# https://github.com/TElgamal/attack-on-pycrypto-elgamal
# https://github.com/Legrandin/pycryptodome/issues/90
# https://github.com/dlitz/pycrypto/issues/253
# Patch based on this commit from cryptodome:
# https://github.com/Legrandin/pycryptodome/commit/99c27a3b
# Converted to pull request for pycrypto:
# https://github.com/dlitz/pycrypto/pull/256
%patch -P 5

# Replace the user-space RNG with a thin wrapper to os.urandom
# Based on https://github.com/Legrandin/pycryptodome/commit/afd6328f
# Fixes compatibility with Python 3.8 (#1718332)
%patch -P 6

# We already require Python 2.4 or later, so drop support for Python 2.1
# in the code
%patch -P 7

# Fix Python 3.10 compatibility
# https://bugzilla.redhat.com/show_bug.cgi?id=1897544
%patch -P 8

# Fix Python 3.11 compatibility
# https://bugzilla.redhat.com/show_bug.cgi?id=2021808
%patch -P 9

# Convert all code to Python 3 before the ability to use 2to3 goes away
%patch -P 10

# Drop use of deprecated distutils, going away in Python 3.12
%patch -P 11

# Get rid of a SyntaxWarning in test_random.py
%patch -P 12

# Fix Python 3.12 compatibility
%patch -P 13

# Fix Python 3.13 compatibility
%patch -P 14

%generate_buildrequires
%pyproject_buildrequires

%build
%global optflags %{optflags} -fno-strict-aliasing
%pyproject_wheel

%install
%pyproject_install

# Remove group write permissions on shared objects
find %{buildroot}%{python3_sitearch} -name '*.so' -exec chmod -c g-w {} \;

%check
# Main test suite
%{py3_test_envvars} %{python3} lib/Crypto/SelfTest/__init__.py

# Benchmark
%{py3_test_envvars} %{python3} pct-speedtest.py

%files -n python3-crypto
%license COPYRIGHT LEGAL/
%doc README TODO ACKS ChangeLog Doc/
%{python3_sitearch}/Crypto/
%{python3_sitearch}/pycrypto-%{version}.dist-info/

%changelog
%autochangelog
