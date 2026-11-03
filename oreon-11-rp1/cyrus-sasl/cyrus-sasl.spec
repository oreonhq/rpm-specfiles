%global source0_hash 7ccfc6abd01ed67c1a0924b353e526f1b766b21f42d4562ee635a8ebfc5bb38c

Name: cyrus-sasl
Version: 2.1.28
Release: 38%{?dist}
Summary: Cyrus SASL authentication library
License: BSD-3-Clause
URL: https://www.cyrusimap.org/sasl/
Source0: https://github.com/cyrusimap/cyrus-sasl/releases/download/cyrus-sasl-%{version}/cyrus-sasl-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconf
BuildRequires: openssl-devel
BuildRequires: krb5-devel
BuildRequires: oreon-rpm-macros
Requires: cyrus-sasl-lib%{?_isa} = %{version}-%{release}

%description
The SASL library and the plugins OpenLDAP and other clients load.

%package devel
Summary: Development files for Cyrus SASL
Requires: cyrus-sasl-lib%{?_isa} = %{version}-%{release}

%description devel
Headers and the pkgconfig file for Cyrus SASL.

%package lib
Summary: Shared libraries for Cyrus SASL
Obsoletes: cyrus-sasl < 2.1.28-38

%description lib
The Cyrus SASL library and the ANONYMOUS plugin.

%package gs2
Summary: GS2 SASL plugin
Requires: cyrus-sasl-lib%{?_isa} = %{version}-%{release}

%description gs2
GS2 SASL plugin for Cyrus SASL.

%package gssapi
Summary: GSSAPI SASL plugin
Requires: cyrus-sasl-lib%{?_isa} = %{version}-%{release}

%description gssapi
GSSAPI SASL plugin for Cyrus SASL.

%package md5
Summary: CRAM-MD5 and DIGEST-MD5 SASL plugins
Requires: cyrus-sasl-lib%{?_isa} = %{version}-%{release}

%description md5
CRAM-MD5 and DIGEST-MD5 SASL plugins for Cyrus SASL.

%package plain
Summary: PLAIN and LOGIN SASL plugins
Requires: cyrus-sasl-lib%{?_isa} = %{version}-%{release}

%description plain
PLAIN and LOGIN SASL plugins for Cyrus SASL.

%package scram
Summary: SCRAM SASL plugin
Requires: cyrus-sasl-lib%{?_isa} = %{version}-%{release}

%description scram
SCRAM SASL plugin for Cyrus SASL.

%prep
%autosetup -n cyrus-sasl-%{version} -p1
%oreon_sha256

%build
%global _oreon_cflags %{_oreon_cflags} -std=gnu17 -include time.h
%oreon_configure --disable-static --with-openssl --enable-gssapi --disable-otp --enable-login
%oreon_make

%install
%oreon_make_install
find %{buildroot} -name '*.la' -delete

%files
%license COPYING
%{_bindir}/pluginviewer
%{_bindir}/saslauthd
%{_bindir}/testsaslauthd
%{_mandir}/man8/saslauthd.8*
%{_mandir}/man8/testsaslauthd.8*

%ldconfig_scriptlets lib

%files lib
%license COPYING
%{_libdir}/libsasl2.so.3
%{_libdir}/libsasl2.so.3.*
%dir %{_libdir}/sasl2
%{_libdir}/sasl2/libanonymous.so*

%files gs2
%{_libdir}/sasl2/libgs2.so*

%files gssapi
%{_libdir}/sasl2/libgssapiv2.so*

%files md5
%{_libdir}/sasl2/libcrammd5.so*
%{_libdir}/sasl2/libdigestmd5.so*

%files plain
%{_libdir}/sasl2/libplain.so*
%{_libdir}/sasl2/liblogin.so*

%files scram
%{_libdir}/sasl2/libscram.so*

%files devel
%{_includedir}/sasl/
%{_libdir}/libsasl2.so
%{_libdir}/pkgconfig/libsasl2.pc
%{_mandir}/man3/*.3*
