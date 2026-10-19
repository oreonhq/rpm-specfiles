%global source0_hash 7ccfc6abd01ed67c1a0924b353e526f1b766b21f42d4562ee635a8ebfc5bb38c
%global username    saslauth
%global _plugindir2 %{_libdir}/sasl2
%global bootstrap_cyrus_sasl 0
%global bdb_migration %[!(0%{?rhel} >= 10)]
%global gdbm_db_file /etc/sasl2/sasldb2
Summary:        The Cyrus SASL library
Name: cyrus-sasl
Version: 2.1.28
Release:        1%{?dist}
License: BSD-Attribution-HPND-disclaimer
URL: https://www.cyrusimap.org/sasl/
Source0:        https://github.com/cyrusimap/cyrus-sasl/releases/download/cyrus-sasl-2.1.28/cyrus-sasl-2.1.28.tar.gz
Source3: saslauth.sysusers
Source5: saslauthd.service
Source7: sasl-mechlist.c
Source9: saslauthd.sysconfig
Source10: make-no-dlcompatorsrp-tarball.sh
Source11: autogen.sh
Requires: %{name}-lib%{?_isa} = %{version}-%{release}
Patch11: cyrus-sasl-2.1.25-no_rpath.patch
Patch15: cyrus-sasl-2.1.20-saslauthd.conf-path.patch
Patch23: cyrus-sasl-2.1.23-man.patch
Patch24: cyrus-sasl-2.1.21-sizes.patch
Patch49: cyrus-sasl-2.1.26-md5global.patch
Patch101: cyrus-sasl-2.1.27-Add-basic-test-infrastructure.patch
Patch102: cyrus-sasl-2.1.27-Add-Channel-Binding-support-for-GSSAPI-GSS-SPNEGO.patch
Patch106: cyrus-sasl-2.1.27-nostrncpy.patch
Patch107: cyrus-sasl-2.1.27-more-tests.patch
Patch108: cyrus-sasl-2.1.27-Add-support-for-setting-max-ssf-0-to-GSS-SPNEGO.patch
Patch109: cyrus-sasl-2.1.27-Migration-from-BerkeleyDB.patch
Patch500: cyrus-sasl-2.1.27-coverity.patch
Patch501: cyrus-sasl-2.1.27-cumulative-digestmd5.patch
Patch502: cyrus-sasl-2.1.27-cumulative-ossl3.patch
Patch503: cyrus-sasl-2.1.28-SAST.patch
Patch599: cyrus-sasl-2.1.28-fedora-c99.patch
Patch600: cyrus-sasl-2.1.28-gcc15.patch
%if ! %{bootstrap_cyrus_sasl}
%endif
%if %{bdb_migration}
%endif
Requires: /sbin/nologin
Provides: user(%username)
Provides: group(%username)
%if "%{_sbindir}" == "%{_bindir}"
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/saslauthd
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gdbm-devel
BuildRequires:  groff
BuildRequires:  krb5-devel
BuildRequires:  krb5-server
BuildRequires:  libdb-devel-static
BuildRequires:  libpq-devel
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  nss_wrapper
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  socket_wrapper
BuildRequires:  zlib-devel
# /oreon:deps
%description
The %{name} package contains the Cyrus implementation of SASL.
SASL is the Simple Authentication and Security Layer, a method for
adding authentication support to connection-based protocols.

%package lib
Summary: Shared libraries needed by applications which use Cyrus SASL
%description lib
The %{name}-lib package contains shared libraries which are needed by
applications which use the Cyrus SASL library.

%package devel
Requires: %{name}-lib%{?_isa} = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Summary: Files needed for developing applications with Cyrus SASL
%description devel
The %{name}-devel package contains files needed for developing and
compiling applications which use the Cyrus SASL library.

%package gssapi
Requires: %{name}-lib%{?_isa} = %{version}-%{release}
Summary: GSSAPI authentication support for Cyrus SASL
%description gssapi
The %{name}-gssapi package contains the Cyrus SASL plugins which
support GSSAPI authentication. GSSAPI is commonly used for Kerberos
authentication.

%package plain
Requires: %{name}-lib%{?_isa} = %{version}-%{release}
Summary: PLAIN and LOGIN authentication support for Cyrus SASL
%description plain
The %{name}-plain package contains the Cyrus SASL plugins which support
PLAIN and LOGIN authentication schemes.

%package md5
Requires: %{name}-lib%{?_isa} = %{version}-%{release}
Summary: CRAM-MD5 and DIGEST-MD5 authentication support for Cyrus SASL
%description md5
The %{name}-md5 package contains the Cyrus SASL plugins which support
CRAM-MD5 and DIGEST-MD5 authentication schemes.

# This would more appropriately be named cyrus-sasl-auxprop-sql.
%package sql
Requires: %{name}-lib%{?_isa} = %{version}-%{release}
Summary: SQL auxprop support for Cyrus SASL
%description sql
The %{name}-sql package contains the Cyrus SASL plugin which supports
using a RDBMS for storing shared secrets.

%if ! %{bootstrap_cyrus_sasl}
# This was *almost* named cyrus-sasl-auxprop-ldapdb, but that's a lot of typing.
%package ldap
Requires: %{name}-lib%{?_isa} = %{version}-%{release}
Summary: LDAP auxprop support for Cyrus SASL
%description ldap
The %{name}-ldap package contains the Cyrus SASL plugin which supports using
a directory server, accessed using LDAP, for storing shared secrets.
%endif

%package scram
Requires: %{name}-lib%{?_isa} = %{version}-%{release}
Summary: SCRAM auxprop support for Cyrus SASL
%description scram
The %{name}-scram package contains the Cyrus SASL plugin which supports
the SCRAM authentication scheme.

%package gs2
Requires: %{name}-lib%{?_isa} = %{version}-%{release}
Summary: GS2 support for Cyrus SASL
%description gs2
The %{name}-gs2 package contains the Cyrus SASL plugin which supports
the GS2 authentication scheme.

###

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n cyrus-sasl-%{version}
rm -rf dlcompat* 2>/dev/null || :
rm -rf plugins/srp* 2>/dev/null || :
%patch -P11 -p1 -b .no_rpath
%patch -P15 -p1 -b .path
%patch -P23 -p1 -b .man
%patch -P24 -p1 -b .sizes
%patch -P49 -p1 -b .md5global.h
%patch -P101 -p1 -b .tests
%patch -P102 -p1 -b .gssapi_cbs
%patch -P106 -p1 -b .nostrncpy
%patch -P107 -p1 -b .moretests
%patch -P108 -p1 -b .maxssf0
%if %{bdb_migration}
%patch -P109 -p1 -b .frombdb
%endif
%patch -P500 -p1 -b .coverity
%patch -P501 -p1 -b .digestmd5
%patch -P502 -p1 -b .ossl3
%patch -P503 -p1 -b .sast
%patch -P599 -p1 -b .c99
%patch -P600 -p1 -b .gcc15

%build

cp %{SOURCE11} ./
rm configure aclocal.m4 config/ltmain.sh Makefile.in
export NOCONFIGURE=yes
sh autogen.sh
%set_build_flags
krb5_prefix=`krb5-config --prefix`
if test x$krb5_prefix = x%{_prefix} ; then
        krb5_prefix=
else
        CPPFLAGS="-I${krb5_prefix}/include $CPPFLAGS"; export CPPFLAGS
        LDFLAGS="-L${krb5_prefix}/%{_lib} $LDFLAGS"; export LDFLAGS
fi
LIBS="-lcrypt"; export LIBS
if pkg-config openssl ; then
        CPPFLAGS="`pkg-config --cflags-only-I openssl` $CPPFLAGS"; export CPPFLAGS
        LDFLAGS="`pkg-config --libs-only-L openssl` $LDFLAGS"; export LDFLAGS
fi
INC_DIR="`mysql_config --include`"
if test x"$INC_DIR" != "x-I%{_includedir}"; then
        CPPFLAGS="$INC_DIR $CPPFLAGS"; export CPPFLAGS
fi
LIB_DIR="`mysql_config --libs | sed -e 's,-[^L][^ ]*,,g' -e 's,^ *,,' -e 's, *$,,' -e 's,  *, ,g'`"
if test x"$LIB_DIR" != "x-L%{_libdir}"; then
        LDFLAGS="$LIB_DIR $LDFLAGS"; export LDFLAGS
fi
INC_DIR="-I`pg_config --includedir`"
if test x"$INC_DIR" != "x-I%{_includedir}"; then
        CPPFLAGS="$INC_DIR $CPPFLAGS"; export CPPFLAGS
fi
LIB_DIR="-L`pg_config --libdir`"
if test x"$LIB_DIR" != "x-L%{_libdir}"; then
        LDFLAGS="$LIB_DIR $LDFLAGS"; export LDFLAGS
fi
LDFLAGS="-Wl,--enable-new-dtags $LDFLAGS"; export LDFLAGS
echo "$CFLAGS"
echo "$CPPFLAGS"
echo "$LDFLAGS"
%configure \
        --enable-shared --disable-static \
        --disable-java \
        --with-plugindir=%{_plugindir2} \
        --with-configdir=%{_plugindir2}:%{_sysconfdir}/sasl2 \
        --disable-krb4 \
        --enable-gssapi${krb5_prefix:+=${krb5_prefix}} \
        --with-gss_impl=mit \
        --with-rc4 \
        --with-dblib=gdbm \
        --with-dbpath=%{gdbm_db_file} \
        --with-saslauthd=/run/saslauthd --without-pwcheck \
%if ! %{bootstrap_cyrus_sasl}
        --with-ldap \
%endif
        --with-devrandom=/dev/urandom \
        --enable-anon \
        --enable-cram \
        --enable-digest \
        --disable-ntlm \
        --enable-plain \
        --enable-login \
        --enable-alwaystrue \
        --enable-httpform \
        --disable-otp \
%if ! %{bootstrap_cyrus_sasl}
        --enable-ldapdb \
%endif
        --enable-sql --with-mysql=yes --with-pgsql=yes \
        --without-sqlite \
        --enable-auth-sasldb \
        "$@"
make sasldir=%{_plugindir2}
make -C saslauthd testsaslauthd
make -C sample
pushd lib
../libtool --mode=link %{__cc} -o sasl2-shared-mechlist -I../include $CFLAGS %{SOURCE7} $LDFLAGS ./libsasl2.la
%install
test "$RPM_BUILD_ROOT" != "/" && rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT sasldir=%{_plugindir2}
make install DESTDIR=$RPM_BUILD_ROOT sasldir=%{_plugindir2} -C plugins
install -m755 -d $RPM_BUILD_ROOT%{_bindir}
./libtool --mode=install \
install -m755 sample/client $RPM_BUILD_ROOT%{_bindir}/sasl2-sample-client
./libtool --mode=install \
install -m755 sample/server $RPM_BUILD_ROOT%{_bindir}/sasl2-sample-server
%if %{bdb_migration} && "%{_sbindir}" != "%{_bindir}"
mv $RPM_BUILD_ROOT%{_sbindir}/cyrusbdb2current $RPM_BUILD_ROOT%{_bindir}/cyrusbdb2current
%endif
./libtool --mode=install \
install -m755 saslauthd/testsaslauthd $RPM_BUILD_ROOT%{_sbindir}/testsaslauthd
install -m755 -d $RPM_BUILD_ROOT%{_mandir}/man8/
install -m644 -p saslauthd/saslauthd.mdoc $RPM_BUILD_ROOT%{_mandir}/man8/saslauthd.8
install -m644 -p saslauthd/testsaslauthd.8 $RPM_BUILD_ROOT%{_mandir}/man8/testsaslauthd.8
install -d -m755 $RPM_BUILD_ROOT/%{_unitdir} $RPM_BUILD_ROOT/etc/sysconfig
install -m644 -p %{SOURCE5} $RPM_BUILD_ROOT/%{_unitdir}/saslauthd.service
install -m644 -p %{SOURCE9} $RPM_BUILD_ROOT/etc/sysconfig/saslauthd
install -m755 -d $RPM_BUILD_ROOT/%{_sysconfdir}/sasl2
install -m755 -d $RPM_BUILD_ROOT/%{_plugindir2}
./libtool --mode=install \
install -m755 lib/sasl2-shared-mechlist $RPM_BUILD_ROOT/%{_sbindir}/
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/cyrus-sasl.conf
rm -f $RPM_BUILD_ROOT%{_libdir}/sasl2/libotp.*
rm -f $RPM_BUILD_ROOT%{_libdir}/sasl2/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/sasl2/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_mandir}/cat8/saslauthd.8
%oreon_autofiles cyrus-sasl-lib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cyrus-sasl-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cyrus-sasl-gssapi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cyrus-sasl-plain usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cyrus-sasl-md5 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cyrus-sasl-sql usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cyrus-sasl-ldap usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cyrus-sasl-scram usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cyrus-sasl-gs2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check %{?_smp_mflags}
%post

%systemd_post saslauthd.service
%preun

%systemd_preun saslauthd.service
%postun

%systemd_postun_with_restart saslauthd.service
%ldconfig_scriptlets lib
%files -f %{oreon_filedir}/main.list
%files -n cyrus-sasl-lib -f %{oreon_filedir}/cyrus-sasl-lib.list
%files -n cyrus-sasl-devel -f %{oreon_filedir}/cyrus-sasl-devel.list
%files -n cyrus-sasl-gssapi -f %{oreon_filedir}/cyrus-sasl-gssapi.list
%files -n cyrus-sasl-plain -f %{oreon_filedir}/cyrus-sasl-plain.list
%files -n cyrus-sasl-md5 -f %{oreon_filedir}/cyrus-sasl-md5.list
%files -n cyrus-sasl-sql -f %{oreon_filedir}/cyrus-sasl-sql.list
%files -n cyrus-sasl-ldap -f %{oreon_filedir}/cyrus-sasl-ldap.list
%files -n cyrus-sasl-scram -f %{oreon_filedir}/cyrus-sasl-scram.list
%files -n cyrus-sasl-gs2 -f %{oreon_filedir}/cyrus-sasl-gs2.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.28-1
- Prepare for Oreon 11 (RP1)
