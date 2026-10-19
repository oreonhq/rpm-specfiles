%global source0_hash 96de1dd6f6a0476d2d2e7964926d8c1ddc3bb0e210e1b1812d3ba5a454a392e2
%define aprver 1
%if 0%{?fedora} < 39 && 0%{?rhel} <= 9 && 0%{?oreon} < 11
%global with_lmdb 0
%else
%global with_lmdb 1
%endif
%define dbdep lmdb-devel
%if 0%{?fedora} < 18 && 0%{?rhel} < 7 && 0%{?oreon} < 11
%endif
%if 0%{?fedora} < 27 && 0%{?rhel} <= 7 && 0%{?oreon} < 11
%global with_nss 1
%else
%global with_nss 0
%endif
%if 0%{?fedora} < 36 && 0%{?rhel} <= 9 && 0%{?oreon} < 11
%global ldaplib ldap_r
%else
%global ldaplib ldap
%endif
%global __brp_remove_la_files %nil
%define apuver 1
Summary:        Apache Portable Runtime Utility library
Name: apr-util
Version: 1.6.5
Release:        1%{?dist}
License: Apache-2.0 AND (Beerware AND LicenseRef-Fedora-Public-Domain AND OLDAP-2.7 AND BSD-4.3RENO)
URL: https://apr.apache.org/
Source0:        https://www.apache.org/dist/apr/%{name}-%{version}.tar.bz2
Patch1: apr-util-1.2.7-pkgconf.patch
Patch2: apr-util-1.4.1-private.patch
Patch5: apr-util-1.6.3-lmdb-support.patch
Patch9: apr-util-1.6.3-drop-engine-headers.patch
Patch10: apr-util-1.6.3-r1928729.patch
Recommends: apr-util-openssl%{_isa} = %{version}-%{release}
Recommends: apr-util-lmdb%{_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  apr-devel
BuildRequires:  autoconf
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  libpq-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  lmdb-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  sqlite-devel
BuildRequires:  unixODBC-devel
# /oreon:deps
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

%package lmdb
Summary: APR utility library LMDB driver
Requires: apr-util%{?_isa} = %{version}-%{release}
Obsoletes: apr-util-bdb < 1.6.5-13
Provides: apr-util-%{aprver}(dbm)%{?_isa} = %{version}-%{release}
%description lmdb
This package provides the LMDB driver for the apr-util
DBM (database abstraction) interface.

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

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

: Configured for LDAP library: %{ldaplib}
: Configured for DBM library: %{dbdep}

%build

autoheader && autoconf
export ac_cv_ldap_set_rebind_proc_style=three
%configure --with-apr=%{_prefix} \
        --includedir=%{_includedir}/apr-%{apuver} \
        --with-ldap=%{ldaplib} --without-gdbm \
        --with-sqlite3 --with-pgsql --with-mysql --with-odbc \
        --with-dbm=lmdb --with-lmdb \
        --without-sqlite2 \
        --with-crypto --with-openssl \
        --without-nss \
   || { cat config.log; exit 1; }
%{make_build}
%install
rm -rf $RPM_BUILD_ROOT
%{make_install}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/aclocal
install -m 644 build/find_apu.m4 $RPM_BUILD_ROOT/%{_datadir}/aclocal
rm -f $RPM_BUILD_ROOT%{_libdir}/aprutil.exp \
      $RPM_BUILD_ROOT%{_libdir}/libapr*.a
sed -i '/^old_library/s,libapr.*\.a,,' \
      $RPM_BUILD_ROOT%{_libdir}/libapr*.la
sed -ri '/^dependency_libs/{s,-l(pq|sqlite[0-9]|rt|dl|uuid) ,,g}' \
      $RPM_BUILD_ROOT%{_libdir}/libapr*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/apr-util-%{apuver}/*.*a
%oreon_autofiles apr-util-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles apr-util-pgsql usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles apr-util-lmdb usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles apr-util-mysql usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles apr-util-sqlite usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles apr-util-odbc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles apr-util-ldap usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles apr-util-openssl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export MALLOC_CHECK_=2 MALLOC_PERTURB_=$(($RANDOM % 255 + 1))
cd test
%{make_build} testall
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}/apr-util-%{apuver}
./testall -v -q
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n apr-util-devel -f %{oreon_filedir}/apr-util-devel.list
%files -n apr-util-pgsql -f %{oreon_filedir}/apr-util-pgsql.list
%files -n apr-util-lmdb -f %{oreon_filedir}/apr-util-lmdb.list
%files -n apr-util-mysql -f %{oreon_filedir}/apr-util-mysql.list
%files -n apr-util-sqlite -f %{oreon_filedir}/apr-util-sqlite.list
%files -n apr-util-odbc -f %{oreon_filedir}/apr-util-odbc.list
%files -n apr-util-ldap -f %{oreon_filedir}/apr-util-ldap.list
%files -n apr-util-openssl -f %{oreon_filedir}/apr-util-openssl.list

%changelog

%autochangelog
