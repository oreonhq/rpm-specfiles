%global source0_hash 2d1c07e6aa509c017516c08307b0b707cd165a17275ab5f1caff9aaa0e3b6c7d

%bcond CHECK 1

Name:           ngtcp2
Version:        1.21.0
Release:        %autorelease
Summary:        Implementation of RFC 9000 QUIC protocol

License:        MIT
URL:            https://github.com/ngtcp2/ngtcp2
Source0:        https://github.com/ngtcp2/ngtcp2/releases/download/v1.21.0/ngtcp2-1.21.0.tar.xz
Source1:        https://github.com/ngtcp2/ngtcp2/releases/download/v1.21.0/ngtcp2-1.21.0.tar.xz.asc
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xf4f3b91474d1eb29889bd0ef7e8403d5d673c366#/tatsuhiro-t.asc
# Release does not contain all parts to build documentation
# https://github.com/ngtcp2/ngtcp2/pull/1404
Source3:        https://github.com/ngtcp2/ngtcp2/raw/refs/tags/v1.21.0/doc/mkapiref.py
Source4:        https://github.com/ngtcp2/ngtcp2/raw/refs/tags/v1.21.0/doc/source/index.rst
Source5:        https://github.com/ngtcp2/ngtcp2/raw/refs/tags/v1.21.0/doc/source/programmers-guide.rst

BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  libev-devel
BuildRequires:  python3-sphinx
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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
install -p -m 755 %{SOURCE3} doc/
install -p -m 644 %{SOURCE4} doc/source/
install -p -m 644 %{SOURCE5} doc/source/


%build
autoreconf -fsi
%configure --with-gnutls --with-openssl --with-libev --disable-static --enable-werror
%make_build
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


%changelog
%autochangelog
