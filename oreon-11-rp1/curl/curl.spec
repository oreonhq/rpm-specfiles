%global source0_hash 8dadd7d2536a314f982ad05a651b713f426bf7d02cc2c76cffb9796f2218e6c5
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: curl
Version: 8.23.0
Release: 5%{?dist}
Summary: HTTP client and library
License: curl
URL: https://curl.se/
Source0: https://curl.se/download/curl-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: pkgconf
BuildRequires: openssl-devel
BuildRequires: libnghttp2-devel
BuildRequires: zlib-devel
BuildRequires: python3
BuildRequires: libzstd-devel
BuildRequires: pkgconfig(libpsl)
BuildRequires: pkgconfig(libssh)
BuildRequires: pkgconfig(libbrotlidec)
BuildRequires: pkgconfig(libnghttp3)
BuildRequires: pkgconfig(libngtcp2)
BuildRequires: pkgconfig(libngtcp2_crypto_ossl)
BuildRequires: pkgconfig(libidn2)
BuildRequires: patchelf
Requires: libcurl%{?_isa} = %{version}-%{release}

%description
curl is a command line tool for transferring data with URL syntax.

%package -n libcurl
Summary: Library for transferring data with URL syntax
Requires: ca-certificates

%description -n libcurl
libcurl is a client-side URL transfer library.

%package -n libcurl-devel
Summary: Development files for libcurl
Requires: libcurl%{?_isa} = %{version}-%{release}
Requires: pkgconf
Obsoletes: curl-devel < 8.23.0-5

%description -n libcurl-devel
Headers, pkg-config file, and documentation for developing with libcurl.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure \
  --disable-static \
  --with-openssl \
  --with-ca-bundle=%{_sysconfdir}/pki/tls/certs/ca-bundle.crt \
  --with-ca-fallback \
  --with-nghttp2 \
  --with-zlib \
  --with-zstd \
  --disable-ldap \
  --disable-ldaps \
  --disable-manual \
  --with-libpsl \
  --without-libssh2 \
  --with-libssh \
  --with-brotli \
  --with-libidn2 \
  --with-ngtcp2 \
  --with-nghttp3
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.a
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
find %{buildroot} -name '*.la' -delete

%ldconfig_scriptlets -n libcurl

%files
%license COPYING
%{_bindir}/curl
%{_bindir}/wcurl
%{_mandir}/man1/curl.1*
%{_mandir}/man1/wcurl.1*

%files -n libcurl
%license COPYING
%{_libdir}/libcurl.so.4
%{_libdir}/libcurl.so.4.*

%files -n libcurl-devel
%{_bindir}/curl-config
%{_includedir}/curl/
%{_libdir}/libcurl.so
%{_libdir}/pkgconfig/libcurl.pc
%{_datadir}/aclocal/libcurl.m4
%{_mandir}/man1/curl-config.1*
%{_mandir}/man3/*
