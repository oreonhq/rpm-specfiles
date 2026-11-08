# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2a34d2484ba17847a5d11965704e9dd0fac4c6d8efc75ffe1ec7de66d8c6b6fb
%global source3_hash daa20426ead1f0061c74a967ac566787c723411a7d726f5dec75faa2e2ee926e
%global source4_hash 7b399eee49aea00d96c0dda004de62eb2b5e9058097da08474f66c3efae951cb
%global source5_hash 06a15976b2a76a4e507580540881d6a89df6de79ba38f533586c3f68bdcea314

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global upstream_sources 0 1
%global pgp_signature_sources 1

%bcond CHECK 1

Name:           ngtcp2
Version:        1.25.0
Release:        1%{?dist}
Summary:        Implementation of RFC 9000 QUIC protocol

License:        MIT
URL:            https://github.com/ngtcp2/ngtcp2
VCS:            git:%{url}.git
Source0:        https://github.com/ngtcp2/ngtcp2/releases/download/v%{version}/ngtcp2-%{version}.tar.xz
Patch0:         ngtcp2-addr-memcpy.patch
Source1:        ngtcp2-1.25.0.tar.xz.asc
Source2:        tatsuhiro-t.asc
# Release does not contain all parts to build documentation
# https://github.com/ngtcp2/ngtcp2/pull/1404
Source3:        https://github.com/ngtcp2/ngtcp2/raw/refs/tags/v%{version}/doc/mkapiref.py
Source4:        https://github.com/ngtcp2/ngtcp2/raw/refs/tags/v%{version}/doc/source/index.rst
Source5:        https://github.com/ngtcp2/ngtcp2/raw/refs/tags/v%{version}/doc/source/programmers-guide.rst
Source10:       https://files.pythonhosted.org/packages/source/m/markupsafe/markupsafe-3.0.4.tar.gz

BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  gdb
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  libev-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-markupsafe
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  gnupg2

%description
"Call it TCP/2. One More Time."

ngtcp2 project is an effort to implement RFC9000 QUIC protocol.

%package devel
Summary:        The ngtcp2 development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Suggests:       %{name}-crypto-any-devel%{?_isa} = %{version}-%{release}

%description devel
"Call it TCP/2. One More Time."

ngtcp2 project is an effort to implement RFC9000 QUIC protocol.

Development headers and libraries.

%package crypto-gnutls
Summary:        The ngtcp2 GnuTLS crypto provider
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description crypto-gnutls
"Call it TCP/2. One More Time." RFC9000 QUIC protocol.

GnuTLS library provider.

%package crypto-gnutls-devel
Summary:        The ngtcp2 GnuTLS crypto provider headers
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-crypto-gnutls%{?_isa} = %{version}-%{release}
BuildRequires:  gnutls-devel >= 3.7.5
Requires:       gnutls-devel >= 3.7.5
Provides:       %{name}-crypto-any-devel = %{version}-%{release}

%description crypto-gnutls-devel
"Call it TCP/2. One More Time." RFC9000 QUIC protocol.

GnuTLS library provider headers.

%package crypto-ossl
Summary:        The ngtcp2 dependency for OpenSSL
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description crypto-ossl
"Call it TCP/2. One More Time." RFC9000 QUIC protocol.

OpenSSL library provider.

%package crypto-ossl-devel
Summary:        The ngtcp2 dependency for OpenSSL headers
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-crypto-ossl%{?_isa} = %{version}-%{release}
BuildRequires:  openssl-devel >= 3.5.0
BuildRequires:  oreon-rpm-macros
Requires:       openssl-devel >= 3.5.0
Provides:       %{name}-crypto-any-devel = %{version}-%{release}

%description crypto-ossl-devel
"Call it TCP/2. One More Time." RFC9000 QUIC protocol.

OpenSSL library provider headers.

%package doc
Summary:        The ngtcp2 API documentation
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
"Call it TCP/2. One More Time." RFC9000 QUIC protocol.

Development API documentation.

%prep
%oreon_sha256
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
echo '%{source4_hash}  %{SOURCE4}' | sha256sum -c -
echo '%{source5_hash}  %{SOURCE5}' | sha256sum -c -

%autosetup -p1
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
install -p -m 755 %{SOURCE3} doc/
install -p -m 644 %{SOURCE4} doc/source/
install -p -m 644 %{SOURCE5} doc/source/


%build
autoreconf -fsi
%configure --with-gnutls --with-openssl --with-libev --disable-static --enable-werror
%make_build
echo '2e9ad7dd851bf45fab9f75cbff4cb493fee9979e8d8c7c9c3ee119022518edd6  %{SOURCE10}' | sha256sum -c -
tar -xzf %{SOURCE10} -C %{_builddir}
export PYTHONPATH="%{_builddir}/markupsafe-3.0.4/src${PYTHONPATH:+:$PYTHONPATH}"
%make_build html

rm -f doc/build/html/.buildinfo


%install
%make_install
# Required on epel9
rm -f ${RPM_BUILD_ROOT}%{_libdir}/lib%{name}*.la

%check
%make_build check

%files
%license COPYING
%doc README.rst
#doc SECURITY.md
%doc AUTHORS
%{_libdir}/libngtcp2.so.16*


%files crypto-gnutls
%{_libdir}/libngtcp2_crypto_gnutls.so.8*


%files crypto-ossl
%{_libdir}/libngtcp2_crypto_ossl.so.0*


%files devel
%doc ChangeLog
%{_libdir}/libngtcp2.so
%{_libdir}/pkgconfig/libngtcp2.pc
%{_includedir}/%{name}/
%exclude %{_includedir}/%{name}/ngtcp2_crypto_*.h


%files crypto-gnutls-devel
%{_libdir}/libngtcp2_crypto_gnutls.so
%{_libdir}/pkgconfig/libngtcp2_crypto_gnutls.pc
%{_includedir}/%{name}/ngtcp2_crypto_gnutls.h


%files crypto-ossl-devel
%{_libdir}/libngtcp2_crypto_ossl.so
%{_libdir}/pkgconfig/libngtcp2_crypto_ossl.pc
%{_includedir}/%{name}/ngtcp2_crypto_ossl.h


%files doc
%doc doc/build/html/


