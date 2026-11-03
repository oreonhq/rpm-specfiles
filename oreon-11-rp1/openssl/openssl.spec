%global source0_hash 50c17baf54cb008f6ce42d50deb4b28050a1aad711636cabd4b241c7e90cc2fd
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: openssl
Epoch: 1
Version: 4.1.0
Release: 2%{?dist}
Summary: OpenSSL TLS library
License: Apache-2.0
URL: https://www.openssl.org/
Source0: https://github.com/openssl/openssl/releases/download/openssl-%{version}/openssl-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: perl
BuildRequires: zlib-devel
BuildRequires: patchelf
BuildRequires: file

Requires: openssl-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description
OpenSSL command line tool for TLS and cryptography.

%package libs
Summary: OpenSSL TLS and crypto libraries

%description libs
Shared libraries, providers, and configuration for OpenSSL.

%package devel
Summary: Development files for OpenSSL
Requires: openssl-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
Header files, pkg-config, and CMake files for developing with OpenSSL.

%package perl
Summary: Perl helper scripts for OpenSSL
Requires: openssl%{?_isa} = %{epoch}:%{version}-%{release}
Requires: perl

%description perl
CA.pl and tsget scripts for OpenSSL.

%prep
%oreon_sha256
%autosetup -p1

%build
CFLAGS='%{build_cflags}' CXXFLAGS='%{build_cxxflags}' LDFLAGS='%{build_ldflags}' \
./Configure \
  --prefix=%{_prefix} \
  --libdir=%{_lib} \
  --openssldir=%{_sysconfdir}/pki/tls \
  shared \
  zlib \
  no-docs \
  -Wl,-z,relro,-z,now
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install_sw install_ssldirs
rm -f %{buildroot}%{_libdir}/*.a
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done

%ldconfig_scriptlets libs

%files
%license LICENSE.txt
%{_bindir}/openssl

%files libs
%license LICENSE.txt
%{_libdir}/libcrypto.so.4
%{_libdir}/libssl.so.4
%dir %{_libdir}/ossl-modules
%{_libdir}/ossl-modules/legacy.so
%dir %{_sysconfdir}/pki/tls
%dir %{_sysconfdir}/pki/tls/certs
%dir %{_sysconfdir}/pki/tls/private
%config(noreplace) %{_sysconfdir}/pki/tls/openssl.cnf
%config(noreplace) %{_sysconfdir}/pki/tls/ct_log_list.cnf
%{_sysconfdir}/pki/tls/openssl.cnf.dist
%{_sysconfdir}/pki/tls/ct_log_list.cnf.dist

%files devel
%{_includedir}/openssl/
%{_libdir}/libcrypto.so
%{_libdir}/libssl.so
%{_libdir}/pkgconfig/libcrypto.pc
%{_libdir}/pkgconfig/libssl.pc
%{_libdir}/pkgconfig/openssl.pc
%dir %{_libdir}/cmake/OpenSSL
%{_libdir}/cmake/OpenSSL/OpenSSLConfig.cmake
%{_libdir}/cmake/OpenSSL/OpenSSLConfigVersion.cmake

%files perl
%dir %{_sysconfdir}/pki/tls/misc
%{_sysconfdir}/pki/tls/misc/CA.pl
%{_sysconfdir}/pki/tls/misc/tsget.pl
%{_sysconfdir}/pki/tls/misc/tsget
