%global source0_hash e30ce4b071ad4b48e7eb0c34c66324a32c2548cfc067900941a90f017dc174e3
Summary:        High-performance and highly configurable free RADIUS server
Name: freeradius
Version: 3.2.10
Release:        1%{?dist}
License: GPL-2.0-or-later AND LGPL-2.0-or-later
URL: http://www.freeradius.org/
%global HAVE_EC_CRYPTO 0
%global dist_base freeradius-server-%{version}
Source0:        https://www.%{name}.org/ftp/pub/%{name}/%{dist_base}.tar.bz2
Source100: radiusd.service
Source102: freeradius-logrotate
Source103: freeradius-pam-conf
Source104: freeradius-tmpfiles.conf
Source105: freeradius.sysusers
Patch1: freeradius-Adjust-configuration-to-fit-Red-Hat-specifics.patch
Patch2: freeradius-Use-system-crypto-policy-by-default.patch
Patch3: freeradius-bootstrap-create-only.patch
Patch4: freeradius-no-buildtime-cert-gen.patch
Patch5: freeradius-bootstrap-make-permissions.patch
Patch6: freeradius-ldap-infinite-timeout-on-starttls.patch
Patch7: freeradius-ease-openssl-version-check.patch
Patch8: freeradius-configure-c99.patch
Patch9: freeradius-openssl-no-engine.patch
Patch10: freeradius-no-sqlippool-tool.patch
%global docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
Requires: openssl >= %(rpm -q --queryformat '%%{EPOCH}:%%{VERSION}' openssl)
Requires(pre): glibc-common
Requires(post): systemd-sysv
Requires(post): systemd-units
Requires: make
Requires(preun): systemd-units
Requires(postun): systemd-units
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  chrpath
BuildRequires:  gcc
BuildRequires:  gdbm-devel
BuildRequires:  json-c-devel
BuildRequires:  krb5-devel
BuildRequires:  libcurl-devel
BuildRequires:  libpcap-devel
BuildRequires:  libpq-devel
BuildRequires:  librdkafka-devel
BuildRequires:  libtalloc-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  net-snmp-devel
BuildRequires:  net-snmp-utils
BuildRequires:  openldap-devel
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  sqlite-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemd-units
BuildRequires:  unixODBC-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The FreeRADIUS Server Project is a high performance and highly configurable
GPL'd free RADIUS server. The server is similar in some respects to
Livingston's 2.0 server.  While FreeRADIUS started as a variant of the
Cistron RADIUS server, they don't share a lot in common any more. It now has
many more features than Cistron or Livingston, and is much more configurable.

FreeRADIUS is an Internet authentication daemon, which implements the RADIUS
protocol, as defined in RFC 2865 (and others). It allows Network Access
Servers (NAS boxes) to perform authentication for dial-up users. There are
also RADIUS clients available for Web servers, firewalls, Unix logins, and
more.  Using RADIUS allows authentication and authorization for a network to
be centralized, and minimizes the amount of re-configuration which has to be
done when adding or deleting new users.

%package doc
Summary: FreeRADIUS documentation
%description doc
All documentation supplied by the FreeRADIUS project is included
in this package.

%package utils
Summary: FreeRADIUS utilities
Requires: %{name} = %{version}-%{release}
Requires: libpcap >= 0.9.4
%description utils
The FreeRADIUS server has a number of features found in other servers,
and additional features not found in any other server. Rather than
doing a feature by feature comparison, we will simply list the features
of the server, and let you decide if they satisfy your needs.

Support for RFC and VSA Attributes Additional server configuration
attributes Selecting a particular configuration Authentication methods

%package devel
Summary: FreeRADIUS development files
Requires: %{name} = %{version}-%{release}
%description devel
Development headers and libraries for FreeRADIUS.

%package ldap
Summary: LDAP support for freeradius
Requires: %{name} = %{version}-%{release}
BuildRequires: openldap-devel
%description ldap
This plugin provides the LDAP support for the FreeRADIUS server project.

%package krb5
Summary: Kerberos 5 support for freeradius
Requires: %{name} = %{version}-%{release}
BuildRequires: krb5-devel
%description krb5
This plugin provides the Kerberos 5 support for the FreeRADIUS server project.

%package perl
Summary: Perl support for freeradius
Requires: %{name} = %{version}-%{release}
%{?fedora:BuildRequires: perl-devel}
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::Embed)
%description perl
This plugin provides the Perl support for the FreeRADIUS server project.

%package -n python3-freeradius
Summary: Python 3 support for freeradius
Requires: %{name} = %{version}-%{release}
BuildRequires: python3-devel
%{?python_provide:%python_provide python3-freeradius}
%description -n python3-freeradius
This plugin provides the Python 3 support for the FreeRADIUS server project.

%package mysql
Summary: MySQL support for freeradius
Requires: %{name} = %{version}-%{release}
BuildRequires: mariadb-connector-c-devel
%description mysql
This plugin provides the MySQL support for the FreeRADIUS server project.

%package postgresql
Summary: Postgresql support for freeradius
Requires: %{name} = %{version}-%{release}
BuildRequires: libpq-devel
%description postgresql
This plugin provides the postgresql support for the FreeRADIUS server project.

%package sqlite
Summary: SQLite support for freeradius
Requires: %{name} = %{version}-%{release}
BuildRequires: sqlite-devel
%description sqlite
This plugin provides the SQLite support for the FreeRADIUS server project.

%package unixODBC
Summary: Unix ODBC support for freeradius
Requires: %{name} = %{version}-%{release}
BuildRequires: unixODBC-devel
%description unixODBC
This plugin provides the unixODBC support for the FreeRADIUS server project.

%package rest
Summary: REST support for freeradius
Requires: %{name} = %{version}-%{release}
BuildRequires: libcurl-devel
BuildRequires: json-c-devel
%description rest
This plugin provides the REST support for the FreeRADIUS server project.

%package kafka
Summary: Kafka producer support for FreeRADIUS
Requires: %{name} = %{version}-%{release}
Requires: librdkafka
BuildRequires: librdkafka-devel
%description kafka
This plugin provides Kafka producer support for the FreeRADIUS server project.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{dist_base}
# Note: We explicitly do not make patch backup files because 'make install'
# mistakenly includes the backup files, especially problematic for raddb config files.
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1

%build

%global _hardened_build 1
%global build_ldflags %{build_ldflags} $(python3-config --embed --libs)
export PY3_LIB_DIR="$(python3-config --configdir)"
export PY3_INC_DIR="$(python3 -c 'import sysconfig; print(sysconfig.get_config_var("INCLUDEPY"))')"
%configure \
        --libdir=%{_libdir}/freeradius \
        --enable-reproducible-builds \
        --disable-openssl-version-check \
        --with-openssl \
        --with-udpfromto \
        --with-threads \
        --with-docdir=%{docdir} \
        --with-rlm-sql_postgresql-include-dir=/usr/include/pgsql \
        --with-rlm-sql-postgresql-lib-dir=%{_libdir} \
        --with-rlm-sql_mysql-include-dir=/usr/include/mysql \
        --with-mysql-lib-dir=%{_libdir}/mariadb \
        --with-unixodbc-lib-dir=%{_libdir} \
        --with-rlm-dbm-lib-dir=%{_libdir} \
        --with-rlm-krb5-include-dir=/usr/kerberos/include \
        --with-rlm_python3 \
        --with-rlm-python3-lib-dir=$PY3_LIB_DIR \
        --with-rlm-python3-include-dir=$PY3_INC_DIR \
        --without-rlm_python \
        --without-rlm_eap_ikev2 \
        --without-rlm_eap_tnc \
        --without-rlm_sql_iodbc \
        --without-rlm_sql_firebird \
        --without-rlm_sql_db2 \
        --without-rlm_sql_oracle \
        --without-rlm_unbound \
        --without-rlm_redis \
        --without-rlm_rediswho \
        --without-rlm_cache_memcached
make %{?_smp_mflags} || make -j1
%install
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/lib/radiusd
make install R=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/log/radius/radacct
touch $RPM_BUILD_ROOT/var/log/radius/{radutmp,radius.log}
install -D -m 644 %{SOURCE100} $RPM_BUILD_ROOT/%{_unitdir}/radiusd.service
install -D -m 644 %{SOURCE102} $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d/radiusd
install -D -m 644 %{SOURCE103} $RPM_BUILD_ROOT/%{_sysconfdir}/pam.d/radiusd
mkdir -p %{buildroot}%{_tmpfilesdir}
mkdir -p %{buildroot}%{_localstatedir}/run/
install -d -m 0710 %{buildroot}%{_localstatedir}/run/radiusd/
install -d -m 0700 %{buildroot}%{_localstatedir}/run/radiusd/tmp
install -m 0644 %{SOURCE104} %{buildroot}%{_tmpfilesdir}/radiusd.conf
install -p -D -m 0644 %{SOURCE105} %{buildroot}%{_sysusersdir}/freeradius.conf
mkdir -p $RPM_BUILD_ROOT%{_datadir}/snmp/mibs/
install -m 644 mibs/*RADIUS*.mib $RPM_BUILD_ROOT%{_datadir}/snmp/mibs/
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/freeradius/*.so
for f in $RPM_BUILD_ROOT/usr/sbin/*; do chrpath --delete $f || true; done
for f in $RPM_BUILD_ROOT/usr/bin/*; do chrpath --delete $f || true; done
mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/freeradius" > %{buildroot}/%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/certs/*.crt
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/certs/*.crl
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/certs/*.csr
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/certs/*.der
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/certs/*.key
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/certs/*.pem
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/certs/*.p12
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/certs/index.*
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/certs/serial*
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/certs/dh
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/certs/random
rm -f $RPM_BUILD_ROOT/usr/sbin/rc.radiusd
rm -f $RPM_BUILD_ROOT/usr/bin/rbmonkey
rm -rf $RPM_BUILD_ROOT/%{_libdir}/freeradius/*.a
rm -rf $RPM_BUILD_ROOT/%{_libdir}/freeradius/*.la
rm -rf $RPM_BUILD_ROOT/etc/raddb/mods-config/sql/main/mssql
rm -rf $RPM_BUILD_ROOT/etc/raddb/mods-config/sql/ippool/oracle
rm -rf $RPM_BUILD_ROOT/etc/raddb/mods-config/sql/ippool/mssql
rm -rf $RPM_BUILD_ROOT/etc/raddb/mods-config/sql/ippool-dhcp/oracle
rm -rf $RPM_BUILD_ROOT/etc/raddb/mods-config/sql/main/oracle
rm -r $RPM_BUILD_ROOT/etc/raddb/mods-config/sql/moonshot-targeted-ids
rm $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/mods-available/unbound
rm $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/mods-config/unbound/default.conf
rm $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/mods-available/couchbase
rm $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/mods-available/abfab*
rm $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/mods-available/moonshot-targeted-ids
rm $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/policy.d/abfab*
rm $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/policy.d/moonshot-targeted-ids
rm $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/sites-available/abfab*
rm $RPM_BUILD_ROOT/%{_libdir}/freeradius/rlm_test.so
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/experimental.conf
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/mods-config/sql/ippool/mongo/queries.conf
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/mods-config/sql/main/mongo/queries.conf
for f in COPYRIGHT CREDITS INSTALL.rst README.rst VERSION; do
    cp $f $RPM_BUILD_ROOT/%{docdir}
done
cp LICENSE $RPM_BUILD_ROOT/%{docdir}/LICENSE.gpl
cp src/lib/LICENSE $RPM_BUILD_ROOT/%{docdir}/LICENSE.lgpl
cp src/LICENSE.openssl $RPM_BUILD_ROOT/%{docdir}/LICENSE.openssl
cat >> $RPM_BUILD_ROOT/%{docdir}/REDHAT << EOF
Red Hat, RHEL, Fedora, and CentOS specific information can be found on the
FreeRADIUS Wiki in the Red Hat FAQ.
http://wiki.freeradius.org/guide/Red-Hat-FAQ
Please reference that document.
All documentation is in the freeradius-doc sub-package.
EOF
%oreon_autofiles python3-freeradius usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%preun

%systemd_preun radiusd.service
%post

if [ -x /usr/sbin/setsebool ]; then
    /usr/sbin/setsebool -P radius_use_jit on || :
fi
%postun

if [ $1 -eq 0 ]; then
    if [ -x /usr/sbin/setsebool ]; then
        /usr/sbin/setsebool -P radius_use_jit off || :
    fi
fi
%systemd_postun_with_restart radiusd.service
/bin/systemctl try-restart radiusd.service >/dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list
%files -n freeradius-doc -f %{oreon_filedir}/freeradius-doc.list
%files -n freeradius-utils -f %{oreon_filedir}/freeradius-utils.list
%files -n freeradius-devel -f %{oreon_filedir}/freeradius-devel.list
%files -n freeradius-ldap -f %{oreon_filedir}/freeradius-ldap.list
%files -n freeradius-krb5 -f %{oreon_filedir}/freeradius-krb5.list
%files -n freeradius-perl -f %{oreon_filedir}/freeradius-perl.list
%files -n python3-freeradius -f %{oreon_filedir}/python3-freeradius.list
%files -n freeradius-mysql -f %{oreon_filedir}/freeradius-mysql.list
%files -n freeradius-postgresql -f %{oreon_filedir}/freeradius-postgresql.list
%files -n freeradius-sqlite -f %{oreon_filedir}/freeradius-sqlite.list
%files -n freeradius-unixODBC -f %{oreon_filedir}/freeradius-unixODBC.list
%files -n freeradius-rest -f %{oreon_filedir}/freeradius-rest.list
%files -n freeradius-kafka -f %{oreon_filedir}/freeradius-kafka.list

%changelog

%autochangelog
