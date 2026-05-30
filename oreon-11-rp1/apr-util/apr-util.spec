%global source0_hash a41076e3710746326c3945042994ad9a4fcac0ce0277dd8fea076fec3c9772b5

%define aprver 1

%if 0%{?fedora} < 39 && 0%{?rhel} <= 9
%global with_lmdb 0
%else
%global with_lmdb 1
%endif

%if %{with_lmdb}
%define dbdep lmdb-devel
%else
%if 0%{?fedora} < 18 && 0%{?rhel} < 7
%define dbdep db4-devel
%else
%define dbdep libdb-devel
%endif
%endif

%if 0%{?fedora} < 27 && 0%{?rhel} <= 7
%global with_nss 1
%else
%global with_nss 0
%endif

%if 0%{?fedora} < 36 && 0%{?rhel} <= 9
%global ldaplib ldap_r
%else
%global ldaplib ldap
%endif

# Disable .la file removal since the .la file is exported via apu-config.
%global __brp_remove_la_files %nil

%define apuver 1

Summary: Apache Portable Runtime Utility library
Name: apr-util
Version: 1.6.3
Release: 27%{?dist}
# Apache-2.0:  everything
# RSA-MD:      https://gitlab.com/fedora/legal/fedora-legal-docs/-/merge_requests/187
#              include\apr_md5.h, passwd\apr_md5.c, crypto\apr_md4.c, include\apr_md4.h
#
# LicenseRef-Fedora-Public-Domain: crypto\crypt_blowfish.c, crypto\crypt_blowfish.h
# Beerware:                        passwd\apr_md5.c
# OLDAP-2.7 AND BSD-4.3RENO:       ldap/apr_ldap_url.c
License: Apache-2.0 AND (Beerware AND LicenseRef-Fedora-Public-Domain AND OLDAP-2.7 AND BSD-4.3RENO)
URL: https://apr.apache.org/
Source0:        https://www.apache.org/dist/apr/%{name}-%{version}.tar.bz2
Patch1: apr-util-1.2.7-pkgconf.patch
Patch2: apr-util-1.4.1-private.patch
Patch3: apr-util-1.6.3-allow-ipv6.patch
Patch4: apr-util-configure-c99.patch
Patch5: apr-util-1.6.3-lmdb-support.patch
Patch6: apr-util-1.6.3-r1908586.patch
Patch7: apr-util-1.6.3-r1908584.patch
Patch8: apr-util-1.6.3-r1908585.patch
Patch9: apr-util-1.6.3-drop-engine-headers.patch
Patch10: apr-util-1.6.3-r1928729.patch
BuildRequires: gcc
BuildRequires: autoconf, apr-devel >= 1.3.0
BuildRequires: %{dbdep}, expat-devel, libuuid-devel
BuildRequires: libxcrypt-devel
Recommends: apr-util-openssl%{_isa} = %{version}-%{release}
%if %{with_lmdb}
Recommends: apr-util-lmdb%{_isa} = %{version}-%{release}
%else
%if 0%{?fedora} < 27
Requires: apr-util-bdb%{?_isa} = %{version}-%{release}
%else
Recommends: apr-util-bdb%{_isa} = %{version}-%{release}
%endif
%endif

%description
The mission of the Apache Portable Runtime (APR) is to provide a
free library of C data structures and routines.  This library
contains additional utility interfaces for APR; including support
for XML, LDAP, database interfaces, URI parsing and more.

%package devel
Summary: APR utility library development kit
Requires: apr-util%{?_isa} = %{version}-%{release}, apr-devel%{?_isa}, pkgconfig
Requires: expat-devel%{?_isa}, openldap-devel%{?_isa}

%description devel
This package provides the support files which can be used to 
build applications using the APR utility library.  The mission 
of the Apache Portable Runtime (APR) is to provide a free 
library of C data structures and routines.

%package pgsql
Summary: APR utility library PostgreSQL DBD driver
BuildRequires: libpq-devel
Requires: apr-util%{?_isa} = %{version}-%{release}

%description pgsql
This package provides the PostgreSQL driver for the apr-util
DBD (database abstraction) interface.

%if %{with_lmdb}
%package lmdb
Summary: APR utility library LMDB driver
Requires: apr-util%{?_isa} = %{version}-%{release}
# Remove libdb dependency from apr-util
# https://bugzilla.redhat.com/show_bug.cgi?id=1779267
Obsoletes: apr-util-bdb < 1.6.3-13
Provides: apr-util-%{aprver}(dbm)%{?_isa} = %{version}-%{release}

%description lmdb
This package provides the LMDB driver for the apr-util
DBM (database abstraction) interface.
%else
%package bdb
Summary: APR utility library Berkeley DB driver
Requires: apr-util%{?_isa} = %{version}-%{release}
Provides: apr-util-%{aprver}(dbm)%{?_isa} = %{version}-%{release}

%description bdb
This package provides the Berkeley DB driver for the apr-util
DBM (database abstraction) interface.
%endif

%package mysql
Summary: APR utility library MySQL DBD driver
BuildRequires: mariadb-connector-c-devel
Requires: apr-util%{?_isa} = %{version}-%{release}

%description mysql
This package provides the MySQL driver for the apr-util DBD
(database abstraction) interface.

%package sqlite
Summary: APR utility library SQLite DBD driver
BuildRequires: sqlite-devel >= 3.0.0
Requires: apr-util%{?_isa} = %{version}-%{release}

%description sqlite
This package provides the SQLite driver for the apr-util DBD
(database abstraction) interface.

%package odbc
Summary: APR utility library ODBC DBD driver
BuildRequires: unixODBC-devel
Requires: apr-util%{?_isa} = %{version}-%{release}

%description odbc
This package provides the ODBC driver for the apr-util DBD
(database abstraction) interface.

%package ldap
Summary: APR utility library LDAP support
BuildRequires: openldap-devel
Requires: apr-util%{?_isa} = %{version}-%{release}

%description ldap
This package provides the LDAP support for the apr-util.

%package openssl
Summary: APR utility library OpenSSL crypto support
BuildRequires: openssl-devel
Requires: apr-util%{?_isa} = %{version}-%{release}

%description openssl
This package provides the OpenSSL crypto support for the apr-util.

%if %{with_nss}
%package nss
Summary: APR utility library NSS crypto support
BuildRequires: nss-devel
BuildRequires: make
Requires: apr-util%{?_isa} = %{version}-%{release}

%description nss
This package provides the NSS crypto support for the apr-util.
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

: Configured for LDAP library: %{ldaplib}
: Configured for DBM library: %{dbdep}

%build
autoheader && autoconf
# A fragile autoconf test which fails if the code trips
# any other warning; force correct result for OpenLDAP:
export ac_cv_ldap_set_rebind_proc_style=three
%configure --with-apr=%{_prefix} \
        --includedir=%{_includedir}/apr-%{apuver} \
        --with-ldap=%{ldaplib} --without-gdbm \
        --with-sqlite3 --with-pgsql --with-mysql --with-odbc \
%if %{with_lmdb}
        --with-dbm=lmdb --with-lmdb \
%else
        --with-dbm=db5 --with-berkeley-db \
%endif
        --without-sqlite2 \
        --with-crypto --with-openssl \
%if %{with_nss}
        --with-nss \
%else
        --without-nss \
%endif
   || { cat config.log; exit 1; }
%{make_build}

%install
rm -rf $RPM_BUILD_ROOT
%{make_install}

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/aclocal
install -m 644 build/find_apu.m4 $RPM_BUILD_ROOT/%{_datadir}/aclocal

# Unpackaged files; remove the static libaprutil
rm -f $RPM_BUILD_ROOT%{_libdir}/aprutil.exp \
      $RPM_BUILD_ROOT%{_libdir}/libapr*.a

# And remove the reference to the static libaprutil from the .la
# file.
sed -i '/^old_library/s,libapr.*\.a,,' \
      $RPM_BUILD_ROOT%{_libdir}/libapr*.la

# Remove unnecessary exports from dependency_libs
sed -ri '/^dependency_libs/{s,-l(pq|sqlite[0-9]|rt|dl|uuid) ,,g}' \
      $RPM_BUILD_ROOT%{_libdir}/libapr*.la

# Trim libtool DSO cruft
rm -f $RPM_BUILD_ROOT%{_libdir}/apr-util-%{apuver}/*.*a

%check
# Run the less verbose test suites
export MALLOC_CHECK_=2 MALLOC_PERTURB_=$(($RANDOM % 255 + 1))
cd test
%{make_build} testall
# testall breaks with DBD DSO; ignore
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}/apr-util-%{apuver}
./testall -v -q

%ldconfig_scriptlets

%files
%doc CHANGES LICENSE NOTICE
%{_libdir}/libaprutil-%{apuver}.so.*
%dir %{_libdir}/apr-util-%{apuver}

%if %{with_lmdb}
%files lmdb
%{_libdir}/apr-util-%{apuver}/apr_dbm_lmdb*
%else
%files bdb
%{_libdir}/apr-util-%{apuver}/apr_dbm_db*
%endif

%files pgsql
%{_libdir}/apr-util-%{apuver}/apr_dbd_pgsql*

%files mysql
%{_libdir}/apr-util-%{apuver}/apr_dbd_mysql*

%files sqlite
%{_libdir}/apr-util-%{apuver}/apr_dbd_sqlite*

%files odbc
%{_libdir}/apr-util-%{apuver}/apr_dbd_odbc*

%files ldap
%{_libdir}/apr-util-%{apuver}/apr_ldap*

%files openssl
%{_libdir}/apr-util-%{apuver}/apr_crypto_openssl*

%if %{with_nss}
%files nss
%{_libdir}/apr-util-%{apuver}/apr_crypto_nss*
%endif

%files devel
%{_bindir}/apu-%{apuver}-config
%{_libdir}/libaprutil-%{apuver}.la
%{_libdir}/libaprutil-%{apuver}.so
%{_includedir}/apr-%{apuver}/*.h
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.3-27
- Prepare for Oreon 11 (RP1)
