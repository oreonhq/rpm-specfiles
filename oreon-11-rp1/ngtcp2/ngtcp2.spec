%global source0_hash 2a34d2484ba17847a5d11965704e9dd0fac4c6d8efc75ffe1ec7de66d8c6b6fb
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: ngtcp2
Version: 1.25.0
Release: 4%{?dist}
Summary: QUIC protocol library
License: MIT
URL: https://github.com/ngtcp2/ngtcp2
Source0: https://github.com/ngtcp2/ngtcp2/releases/download/v%{version}/ngtcp2-%{version}.tar.xz
Source1: ngtcp2-%{version}.tar.xz.asc
Source2: ngtcp2-key.asc

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: patchelf
BuildRequires: pkgconf
BuildRequires: openssl-devel
BuildRequires: gnutls-devel

%description
ngtcp2 implements the QUIC protocol (RFC 9000). This build ships the
library and the OpenSSL and GnuTLS crypto helper libraries.

%package -n libngtcp2
Summary: ngtcp2 library
Obsoletes: ngtcp2 < 1.25.0-3

%description -n libngtcp2
Shared ngtcp2 library.

%package -n libngtcp2-devel
Summary: Development files for libngtcp2
Requires: libngtcp2%{?_isa} = %{version}-%{release}
Obsoletes: ngtcp2-devel < 1.25.0-3

%description -n libngtcp2-devel
Headers and development library for libngtcp2.

%package -n libngtcp2-crypto-ossl
Summary: ngtcp2 ossl crypto helper
Requires: libngtcp2%{?_isa} = %{version}-%{release}
Obsoletes: ngtcp2-crypto-ossl < 1.25.0-3

%description -n libngtcp2-crypto-ossl
ngtcp2 crypto helper library for ossl.

%package -n libngtcp2-crypto-ossl-devel
Summary: Development files for libngtcp2-crypto-ossl
Requires: libngtcp2-crypto-ossl%{?_isa} = %{version}-%{release}
Requires: libngtcp2-devel%{?_isa} = %{version}-%{release}
Obsoletes: ngtcp2-crypto-ossl-devel < 1.25.0-3

%description -n libngtcp2-crypto-ossl-devel
Headers and development library for libngtcp2-crypto-ossl.

%package -n libngtcp2-crypto-gnutls
Summary: ngtcp2 gnutls crypto helper
Requires: libngtcp2%{?_isa} = %{version}-%{release}
Obsoletes: ngtcp2-crypto-gnutls < 1.25.0-3

%description -n libngtcp2-crypto-gnutls
ngtcp2 crypto helper library for gnutls.

%package -n libngtcp2-crypto-gnutls-devel
Summary: Development files for libngtcp2-crypto-gnutls
Requires: libngtcp2-crypto-gnutls%{?_isa} = %{version}-%{release}
Requires: libngtcp2-devel%{?_isa} = %{version}-%{release}
Obsoletes: ngtcp2-crypto-gnutls-devel < 1.25.0-3

%description -n libngtcp2-crypto-gnutls-devel
Headers and development library for libngtcp2-crypto-gnutls.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n ngtcp2-%{version} -p1

%build
%oreon_configure --disable-static --enable-lib-only --with-openssl --with-gnutls
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%ldconfig_scriptlets -n libngtcp2
%ldconfig_scriptlets -n libngtcp2-crypto-ossl
%ldconfig_scriptlets -n libngtcp2-crypto-gnutls

%files -n libngtcp2
%license COPYING
%{_docdir}/ngtcp2/
%{_libdir}/libngtcp2.so.*

%files -n libngtcp2-devel
%dir %{_includedir}/ngtcp2
%{_includedir}/ngtcp2/ngtcp2.h
%{_includedir}/ngtcp2/ngtcp2_crypto.h
%{_includedir}/ngtcp2/version.h
%{_libdir}/libngtcp2.so
%{_libdir}/pkgconfig/libngtcp2.pc

%files -n libngtcp2-crypto-ossl
%{_libdir}/libngtcp2_crypto_ossl.so.*

%files -n libngtcp2-crypto-ossl-devel
%{_includedir}/ngtcp2/ngtcp2_crypto_ossl.h
%{_libdir}/libngtcp2_crypto_ossl.so
%{_libdir}/pkgconfig/libngtcp2_crypto_ossl.pc

%files -n libngtcp2-crypto-gnutls
%{_libdir}/libngtcp2_crypto_gnutls.so.*

%files -n libngtcp2-crypto-gnutls-devel
%{_includedir}/ngtcp2/ngtcp2_crypto_gnutls.h
%{_libdir}/libngtcp2_crypto_gnutls.so
%{_libdir}/pkgconfig/libngtcp2_crypto_gnutls.pc
