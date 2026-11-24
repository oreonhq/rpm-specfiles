# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 53675e98fa83b48201d24f7bfbcaeaa1b51496b8b19ff969785856bdeb196af3
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond openssl 1
%define openssl_ver 3.0.13
%bcond nss 1
%define nss_ver 3.91
%define nspr_ver 4.34.1
%bcond gcrypt 0
%define gcrypt_ver 1.4.0
%bcond gnutls 1
%define gnutls_ver 3.8.3

Summary: Library providing support for "XML Signature" and "XML Encryption" standards
Name: xmlsec1
Version: 1.3.11
Release:        %{autorelease}
Epoch: 1
License: MIT
Source0: https://github.com/lsh123/xmlsec/releases/download/%{version}/xmlsec1-%{version}.tar.gz
URL: http://www.aleksey.com/xmlsec/

Patch0: 0000-so-name.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: make
BuildRequires: pkgconfig(libxml-2.0) >= 2.9.13
BuildRequires: pkgconfig(libxslt) >= 1.1.35
%if %{with openssl}
BuildRequires: pkgconfig(openssl) >= %{openssl_ver}
%endif
%if %{with nss}
BuildRequires: pkgconfig(nss) >= %{nss_ver}
BuildRequires: pkgconfig(nspr) >= %{nspr_ver}
%endif
%if %{with gcrypt}
BuildRequires: libgcrypt-devel >= %{gcrypt_ver}
%endif
%if %{with gnutls}
BuildRequires: pkgconfig(gnutls) >= %{gnutls_ver}
%endif
BuildRequires: libtool-ltdl-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gettext-devel
BuildRequires: libtool

%description
XML Security Library is a C library based on LibXML2  and OpenSSL.
The library was created with a goal to support major XML security
standards "XML Digital Signature" and "XML Encryption".

%package devel
Summary: Libraries, includes, etc. to develop applications with XML Digital Signatures and XML Encryption support.
Requires: xmlsec1%{?_isa} = 1:%{version}-%{release}

%description devel
Libraries, includes, etc. you can use to develop applications with XML Digital
Signatures and XML Encryption support.

%if %{with openssl}
%package openssl
Summary: OpenSSL crypto plugin for XML Security Library
Requires: xmlsec1%{?_isa} = 1:%{version}-%{release}

%description openssl
OpenSSL plugin for XML Security Library provides OpenSSL based crypto services
for the xmlsec library.

%package openssl-devel
Summary: OpenSSL crypto plugin for XML Security Library
Requires: xmlsec1-devel%{?_isa} = 1:%{version}-%{release}
Requires: xmlsec1-openssl%{?_isa} = 1:%{version}-%{release}
Requires: openssl-devel%{?_isa} >= 1:%{openssl_ver}

%description openssl-devel
Libraries, includes, etc. for developing XML Security applications with OpenSSL
%endif

%if %{with gcrypt}
%package gcrypt
Summary: GCrypt crypto plugin for XML Security Library
Requires: xmlsec1%{?_isa} = 1:%{version}-%{release}
Provides: deprecated()

%description gcrypt
GCrypt plugin for XML Security Library provides GCrypt based crypto services
for the xmlsec library.

%package gcrypt-devel
Summary: GCrypt crypto plugin for XML Security Library
Requires: xmlsec1-devel%{?_isa} = 1:%{version}-%{release}
Requires: xmlsec1-gcrypt%{?_isa} = 1:%{version}-%{release}
Requires: libgcrypt-devel%{?_isa} >= %{gcrypt_ver}
Provides: deprecated()

%description gcrypt-devel
Libraries, includes, etc. for developing XML Security applications with GCrypt.
%endif

%if %{with gnutls}
%package gnutls
Summary: GNUTls crypto plugin for XML Security Library
Requires: xmlsec1%{?_isa} = 1:%{version}-%{release}

%description gnutls
GNUTls plugin for XML Security Library provides GNUTls based crypto services
for the xmlsec library.

%package gnutls-devel
Summary: GNUTls crypto plugin for XML Security Library
Requires: xmlsec1-devel%{?_isa} = 1:%{version}-%{release}
Requires: xmlsec1-gnutls%{?_isa} = 1:%{version}-%{release}
Requires: gnutls-devel%{?_isa} >= %{gnutls_ver}

%description gnutls-devel
Libraries, includes, etc. for developing XML Security applications with GNUTls.
%endif

%if %{with nss}
%package nss
Summary: NSS crypto plugin for XML Security Library
Requires: xmlsec1%{?_isa} = 1:%{version}-%{release}

%description nss
NSS plugin for XML Security Library provides NSS based crypto services
for the xmlsec library

%package nss-devel
Summary: NSS crypto plugin for XML Security Library
Requires: xmlsec1-devel%{?_isa} = 1:%{version}-%{release}
Requires: xmlsec1-nss%{?_isa} = 1:%{version}-%{release}
Requires: nspr-devel%{?_isa} >= %{nspr_ver}
Requires: nss-devel%{?_isa} >= %{nss_ver}

%description nss-devel
Libraries, includes, etc. for developing XML Security applications with NSS.
%endif

%prep
%oreon_sha256
%autosetup -p1

%build
autoreconf -vfi
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build V=1

sed 's+/lib64+/$archlib+g' < xmlsec1-config | sed 's+/lib+/$archlib+g' | sed 's+ -DXMLSEC_NO_SIZE_T++' > xmlsec1-config.$$ && mv xmlsec1-config.$$ xmlsec1-config

%install
%make_install
rm -vf %{buildroot}%{_libdir}/*.la

rm -rf __tmp_doc ; mkdir __tmp_doc
mv %{buildroot}%{_docdir}/xmlsec1/* __tmp_doc

%files
%doc AUTHORS.md ChangeLog NEWS Copyright
%{_mandir}/man1/xmlsec1.1*
%{_libdir}/libxmlsec1.so.*
%{_bindir}/xmlsec1

%files devel
%{_bindir}/xmlsec1-config
%dir %{_includedir}/xmlsec1
%dir %{_includedir}/xmlsec1/xmlsec
%{_includedir}/xmlsec1/xmlsec/*.h
%{_libdir}/libxmlsec1.so
%{_libdir}/pkgconfig/xmlsec1.pc
%{_libdir}/xmlsec1Conf.sh
%{_datadir}/aclocal/xmlsec1.m4
%{_mandir}/man1/xmlsec1-config.1*
%doc HACKING __tmp_doc/*

%if %{with openssl}
%files openssl
%{_libdir}/libxmlsec1-openssl.so.*
%{_libdir}/libxmlsec1-openssl.so

%files openssl-devel
%{_includedir}/xmlsec1/xmlsec/openssl/
%{_libdir}/pkgconfig/xmlsec1-openssl.pc
%endif

%if %{with gcrypt}
%files gcrypt
%{_libdir}/libxmlsec1-gcrypt.so.*
%{_libdir}/libxmlsec1-gcrypt.so

%files gcrypt-devel
%{_includedir}/xmlsec1/xmlsec/gcrypt/
%{_libdir}/pkgconfig/xmlsec1-gcrypt.pc
%endif

%if %{with gnutls}
%files gnutls
%{_libdir}/libxmlsec1-gnutls.so.*
%{_libdir}/libxmlsec1-gnutls.so

%files gnutls-devel
%{_includedir}/xmlsec1/xmlsec/gnutls/
%{_libdir}/pkgconfig/xmlsec1-gnutls.pc
%endif

%if %{with nss}
%files nss
%{_libdir}/libxmlsec1-nss.so.*
%{_libdir}/libxmlsec1-nss.so

%files nss-devel
%{_includedir}/xmlsec1/xmlsec/nss/
%{_libdir}/pkgconfig/xmlsec1-nss.pc
%endif

%changelog
%autochangelog
