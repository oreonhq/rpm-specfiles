%global source0_hash efde5f6f19896f0200bb5245e3866035667271c7b1e84626d26095f24a6fbb42
%global srcname zabbix
%global with_selinux 1
%global selinuxtype targeted
%bcond_with go
%bcond_with java
Name:           zabbix
Epoch:          1
Version:        7.4.14
Release:        1%{?dist}
Summary:        Open-source monitoring solution for your IT infrastructure
License:        AGPL-3.0-only AND MIT AND GPL-2.0-or-later AND Zlib AND BSD-3-Clause AND BSD-2-Clause AND ISC
URL:            https://www.zabbix.com
Source0:        https://cdn.zabbix.com/zabbix/sources/stable/7.4/zabbix-%{version}.tar.gz
Source1:        %{srcname}-web.conf
Source2:        %{srcname}-php-fpm.conf
Source5:        %{srcname}-logrotate.in
Source9:        %{srcname}-tmpfiles-zabbix.conf
Source10:       %{srcname}-agent.service
Source11:       %{srcname}-proxy-mysql.service
Source12:       %{srcname}-proxy-pgsql.service
Source13:       %{srcname}-proxy-sqlite3.service
Source14:       %{srcname}-server-mysql.service
Source15:       %{srcname}-server-pgsql.service
Source16:       %{srcname}-fedora-epel.README
Source17:       %{srcname}-tmpfiles-zabbixsrv.conf
Source18:       %{srcname}.te
Source19:       %{srcname}.if
Source20:       %{srcname}.fc
Patch0:         %{srcname}-config.patch
Patch1:         %{srcname}-out-of-tree.patch
Patch2:         %{srcname}-crypto-policy.patch
Patch3:         %{srcname}-configure-sscanf.patch
%if %{with go}
%endif
Requires:        logrotate
%if 0%{?with_selinux}
Requires:        (%{srcname}-selinux if selinux-policy-%{selinuxtype})
%endif
Provides:        bundled(md5-deutsch)
%if "x%{?srcname}" != "x%{name}"
Provides:        %{srcname} = %{version}-%{release}
Conflicts:       %{srcname} < 6.0
%endif
# oreon:deps
BuildRequires:  OpenIPMI-devel
BuildRequires:  curl-devel
BuildRequires:  dejavu-sans-fonts
BuildRequires:  gcc
BuildRequires:  gnutls-devel
BuildRequires:  java-devel
BuildRequires:  libevent-devel
BuildRequires:  libpq-devel
BuildRequires:  libssh2-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  net-snmp-devel
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  osgi(logback)
BuildRequires:  osgi(org.junit)
BuildRequires:  osgi(slf4j.api)
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig(systemd)
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  sqlite-devel
BuildRequires:  systemd
BuildRequires:  unixODBC-devel
# /oreon:deps
%description
Zabbix is software that monitors numerous parameters of a network and the
health and integrity of servers. Zabbix uses a flexible notification mechanism
that allows users to configure e-mail based alerts for virtually any event.
This allows a fast reaction to server problems. Zabbix offers excellent
reporting and data visualization features based on the stored data.
This makes Zabbix ideal for capacity planning.

Zabbix supports both polling and trapping. All Zabbix reports and statistics,
as well as configuration parameters are accessed through a web-based front end.
A web-based front end ensures that the status of your network and the health of
your servers can be assessed from any location. Properly configured, Zabbix can
play an important role in monitoring IT infrastructure. This is equally true
for small organizations with a few servers and for large companies with a
multitude of servers.

%package dbfiles-mysql
Summary:             Zabbix database schemas, images, data and patches
BuildArch:           noarch
%description dbfiles-mysql
Zabbix database schemas, images, data and patches necessary for creating
and/or updating MySQL databases

%package dbfiles-pgsql
Summary:             Zabbix database schemas, images, data and patches
BuildArch:           noarch
%description dbfiles-pgsql
Zabbix database schemas, images, data and patches necessary for creating
and/or updating PostgreSQL databases

%package dbfiles-sqlite3
Summary:             Zabbix database schemas and patches
BuildArch:           noarch
%description dbfiles-sqlite3
Zabbix database schemas and patches necessary for creating
and/or updating SQLite databases

%package server
Summary:             Zabbix server common files
BuildArch:           noarch
Requires:            %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:            %{name}-server-implementation = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:            fping
Requires:            traceroute
Requires(post):      systemd
Requires(preun):     systemd
Requires(postun):    systemd
Provides:            user(zabbixsrv)
Provides:            group(zabbixsrv)
%description server
Zabbix server common files

%package server-mysql
Summary:             Zabbix server compiled to use MySQL
Requires:            %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:            %{name}-dbfiles-mysql
Requires:            %{name}-server = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(post):      %{_sbindir}/update-alternatives
Requires(postun):    %{_sbindir}/update-alternatives
Provides:            %{name}-server-implementation = %{?epoch:%{epoch}:}%{version}-%{release}
%description server-mysql
Zabbix server compiled to use MySQL

%package server-pgsql
Summary:             Zabbix server compiled to use PostgreSQL
Requires:            %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:            %{name}-server = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:            %{name}-dbfiles-pgsql
Requires(post):      %{_sbindir}/update-alternatives
Requires(postun):    %{_sbindir}/update-alternatives
Provides:            %{name}-server-implementation = %{?epoch:%{epoch}:}%{version}-%{release}
%description server-pgsql
Zabbix server compiled to use PostgreSQL

%package agent
Summary:             Zabbix agent
Requires:            %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(post):      systemd
Requires(preun):     systemd
Requires(postun):    systemd
%description agent
Zabbix agent, to be installed on monitored systems

%package proxy
Summary:             Zabbix proxy common files
BuildArch:           noarch
Requires:            %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:            %{name}-proxy-implementation = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(post):      systemd
Requires(preun):     systemd
Requires(postun):    systemd
Requires:            fping
%description proxy
Zabbix proxy commmon files

%package proxy-mysql
Summary:             Zabbix proxy compiled to use MySQL
Requires:            %{name}-proxy = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:            %{name}-dbfiles-mysql
Provides:            %{name}-proxy-implementation = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(post):      %{_sbindir}/update-alternatives
Requires(postun):    %{_sbindir}/update-alternatives
%description proxy-mysql
Zabbix proxy compiled to use MySQL

%package proxy-pgsql
Summary:             Zabbix proxy compiled to use PostgreSQL
Requires:            %{name}-proxy = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:            %{name}-dbfiles-pgsql
Provides:            %{name}-proxy-implementation = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(post):      %{_sbindir}/update-alternatives
Requires(postun):    %{_sbindir}/update-alternatives
%description proxy-pgsql
Zabbix proxy compiled to use PostgreSQL

%package proxy-sqlite3
Summary:             Zabbix proxy compiled to use SQLite
Requires:            %{name}-proxy = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:            %{name}-dbfiles-sqlite3
Provides:            %{name}-proxy-implementation = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(post):      %{_sbindir}/update-alternatives
Requires(postun):    %{_sbindir}/update-alternatives
%description proxy-sqlite3
Zabbix proxy compiled to use SQLite

%package web
Summary:         Zabbix Web Frontend
BuildArch:       noarch
Requires:        php-bcmath
Requires:        php-fpm
Requires:        php-gd
Requires:        php-gettext
Requires:        php-json
Requires:        php-ldap
Requires:        php-mbstring
Requires:        php-xml
Requires:        js-jquery >= 3.6.0
Provides:        bundled(js-jquery-ui) = 1.13.2
Requires:        dejavu-sans-fonts
Requires:        %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:        %{name}-web-database = %{?epoch:%{epoch}:}%{version}-%{release}
%description web
The php frontend to display the Zabbix web interface.

%package web-mysql
Summary:         Zabbix web frontend for MySQL
BuildArch:       noarch
Requires:        %{name}-web = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:        php-mysqli
Provides:        %{name}-web-database = %{?epoch:%{epoch}:}%{version}-%{release}
%description web-mysql
Zabbix web frontend for MySQL

%package web-pgsql
Summary:         Zabbix web frontend for PostgreSQL
BuildArch:       noarch
Requires:        %{name}-web = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:        php-pgsql
Provides:        %{name}-web-database = %{?epoch:%{epoch}:}%{version}-%{release}
%description web-pgsql
Zabbix web frontend for PostgreSQL

%if %{with java}
%package -n java-%{srcname}
Summary:         Zabbix Java connector
BuildArch:       noarch
BuildRequires:   java-devel
BuildRequires:   osgi(org.junit)
BuildRequires:   osgi(slf4j.api)
BuildRequires:   osgi(logback)
%description -n java-%{srcname}
Zabbix Java connector.
%endif

%if 0%{?with_selinux}
# SELinux subpackage
%package selinux
Summary:             Zabbix SELinux policy
BuildArch:           noarch
Requires:            selinux-policy-%{selinuxtype}
Requires(post):      selinux-policy-%{selinuxtype}
BuildRequires:       selinux-policy-devel
%{?selinux_requires}
%description selinux
Custom SELinux policy module
%endif

%prep

%autosetup -p1
autoreconf

# Remove bundled java libs
find -name \*.jar -delete

# Remove prebuilt Windows binaries
rm -rf bin

# Override creation of statically named directory for alertscripts and externalscripts
# https://support.zabbix.com/browse/ZBX-6159
sed -i '/CURL_SSL_.*_LOCATION\|SCRIPTS_PATH/s|\${datadir}/zabbix|/var/lib/zabbixsrv|' \
    configure

# Kill off .htaccess files, options set in SOURCE1
find -name .htaccess -delete

# Fix path to traceroute utility (on all Linux targets)
find database -name 'data.sql' -exec sed -i 's|/usr/bin/traceroute|/bin/traceroute|' {} \;

# Common
# Settings with hard-coded defaults that are not suitable for Fedora
# are explicitly set, leaving the comment with the default value in place.
# Settings without hard-coded defaults are simply replaced -- be they
# comments or explicit settings!

# Also replace the datadir placeholder that is not expanded, but effective
sed -i \
    -e '\|^# LogFileSize=.*|a LogFileSize=0' \
    -e 's|^DBUser=root|DBUser=zabbix|' \
    -e 's|^# DBSocket=.*|DBSocket=%{_sharedstatedir}/mysql/mysql.sock|' \
    -e '\|^# ExternalScripts=|a ExternalScripts=%{_sharedstatedir}/zabbixsrv/externalscripts' \
    -e '\|^# AlertScriptsPath=|a AlertScriptsPath=%{_sharedstatedir}/zabbixsrv/alertscripts' \
    -e '\|^# TmpDir=\/tmp|a TmpDir=%{_sharedstatedir}/zabbixsrv/tmp' \
    -e 's|/usr/local||' \
    -e 's|\${datadir}|/usr/share|' \
    conf/zabbix_agentd.conf conf/zabbix_proxy.conf conf/zabbix_server.conf

# Specific
sed -i \
    -e '\|^# PidFile=.*|a PidFile=%{_rundir}/zabbix/zabbix_agentd.pid' \
    -e 's|^LogFile=.*|LogFile=%{_localstatedir}/log/zabbix/zabbix_agentd.log|' \
    conf/zabbix_agentd.conf

sed -i \
    -e '\|^# PidFile=.*|a PidFile=%{_rundir}/zabbixsrv/zabbix_proxy.pid' \
    -e 's|^LogFile=.*|LogFile=%{_localstatedir}/log/zabbixsrv/zabbix_proxy.log|' \
    conf/zabbix_proxy.conf

sed -i \
    -e '\|^# PidFile=.*|a PidFile=%{_rundir}/zabbixsrv/zabbix_server.pid' \
    -e 's|^LogFile=.*|LogFile=%{_localstatedir}/log/zabbixsrv/zabbix_server.log|' \
    conf/zabbix_server.conf

# Install README file
install -m 0644 -p %{SOURCE16} .

# Create a sysusers.d config file
cat >zabbix.sysusers.conf <<EOF
u zabbix - 'Zabbix Monitoring System' %{_sharedstatedir}/zabbix -
EOF

%build

common_flags="
    --enable-dependency-tracking
    --enable-proxy
    --enable-ipv6
    --with-net-snmp
    --with-ldap
    --with-libcurl
    --with-openipmi
    --with-unixodbc
    --with-ssh2
    --with-libxml2
    --with-libevent
    --with-libpcre2
    --with-openssl
"
%global _configure ../configure
%if %{with java}
export CLASSPATH=$(build-classpath junit slf4j-api logback-core logback-classic android-json)
%endif
mkdir -p build-frontend
cd build-frontend
%configure $common_flags --enable-agent --with-sqlite3 %{?with_go:--enable-agent2} %{?with_java:--enable-java}
%make_build
cd -
mkdir -p build-server-mysql
cd build-server-mysql
%configure $common_flags --with-mysql --enable-server
%make_build
cd -
mkdir -p build-server-postgresql
cd build-server-postgresql
%configure $common_flags --with-postgresql --enable-server
%make_build
cd -
%if 0%{?with_selinux}
mkdir selinux
cp -p %{SOURCE18} selinux/
cp -p %{SOURCE19} selinux/
cp -p %{SOURCE20} selinux/
make -f %{_datadir}/selinux/devel/Makefile %{srcname}.pp
bzip2 -9 %{srcname}.pp
%endif
%install
%make_install -C build-frontend
mv $RPM_BUILD_ROOT%{_sbindir}/zabbix_proxy{,_sqlite3}
%make_install -C build-server-mysql
mv $RPM_BUILD_ROOT%{_sbindir}/zabbix_proxy{,_mysql}
mv $RPM_BUILD_ROOT%{_sbindir}/zabbix_server{,_mysql}
%make_install -C build-server-postgresql
mv $RPM_BUILD_ROOT%{_sbindir}/zabbix_proxy{,_pgsql}
mv $RPM_BUILD_ROOT%{_sbindir}/zabbix_server{,_pgsql}
touch $RPM_BUILD_ROOT%{_sbindir}/zabbix_{proxy,server}
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/zabbix
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/zabbix
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/zabbixsrv
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d
install -m 0644 -p %{SOURCE9} $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/zabbix.conf
install -m 0644 -p %{SOURCE17} $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/zabbixsrv.conf
mkdir -p $RPM_BUILD_ROOT%{_rundir}
install -d -m 0755 $RPM_BUILD_ROOT%{_rundir}/zabbix/
install -d -m 0755 $RPM_BUILD_ROOT%{_rundir}/zabbixsrv/
find ui -name '*.orig' -delete
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{srcname}
cp -a ui/* $RPM_BUILD_ROOT%{_datadir}/%{srcname}/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{srcname}/web
touch $RPM_BUILD_ROOT%{_sysconfdir}/%{srcname}/web/zabbix.conf.php
[ -d %{_fontbasedir}/dejavu ] &&
  ln -sf ../../../fonts/dejavu/DejaVuSans.ttf $RPM_BUILD_ROOT%{_datadir}/%{srcname}/assets/fonts/
[ -d %{_fontbasedir}/dejavu-sans-fonts ] &&
  ln -sf ../../../fonts/dejavu-sans-fonts/DejaVuSans.ttf $RPM_BUILD_ROOT%{_datadir}/%{srcname}/assets/fonts/
ln -sf ../../../javascript/jquery/3/jquery.min.js $RPM_BUILD_ROOT%{_datadir}/%{srcname}/js/vendors/jquery.js
mv $RPM_BUILD_ROOT%{_datadir}/%{srcname}/conf/maintenance.inc.php $RPM_BUILD_ROOT%{_sysconfdir}/%{srcname}/web/maintenance.inc.php || :
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/%{srcname}.conf
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.d
install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.d/%{srcname}.conf
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
sed -e 's|COMPONENT|agentd|g; s|USER|zabbix|g' %{SOURCE5} > \
     $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-agent
sed -e 's|COMPONENT|server|g; s|USER|zabbixsrv|g' %{SOURCE5} > \
     $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-server
sed -e 's|COMPONENT|proxy|g; s|USER|zabbixsrv|g' %{SOURCE5} > \
     $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-proxy
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -m 0644 -p %{SOURCE10} $RPM_BUILD_ROOT%{_unitdir}/zabbix-agent.service
install -m 0644 -p %{SOURCE11} $RPM_BUILD_ROOT%{_unitdir}/zabbix-proxy-mysql.service
install -m 0644 -p %{SOURCE12} $RPM_BUILD_ROOT%{_unitdir}/zabbix-proxy-pgsql.service
install -m 0644 -p %{SOURCE13} $RPM_BUILD_ROOT%{_unitdir}/zabbix-proxy-sqlite3.service
install -m 0644 -p %{SOURCE14} $RPM_BUILD_ROOT%{_unitdir}/zabbix-server-mysql.service
install -m 0644 -p %{SOURCE15} $RPM_BUILD_ROOT%{_unitdir}/zabbix-server-pgsql.service
touch $RPM_BUILD_ROOT%{_unitdir}/zabbix-server.service
touch $RPM_BUILD_ROOT%{_unitdir}/zabbix-proxy.service
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/zabbixsrv/tmp
for db in postgresql mysql; do
    mkdir $RPM_BUILD_ROOT%{_datadir}/%{srcname}-$db
    cp -p database/$db/*.sql $RPM_BUILD_ROOT%{_datadir}/%{srcname}-$db
done
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{srcname}-sqlite3
cp -p database/sqlite3/schema.sql $RPM_BUILD_ROOT%{_datadir}/%{srcname}-sqlite3
%if 0%{?with_selinux}
install -D -m 0644 %{name}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
install -D -p -m 0644 selinux/%{name}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{name}.if
%endif
install -m0644 -D zabbix.sysusers.conf %{buildroot}%{_sysusersdir}/zabbix.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post server

%systemd_post zabbix-server.service
if [ $1 -gt 1 ] ; then
  chmod 0640 %{_sysconfdir}/zabbix_server.conf
  chown root:zabbixsrv %{_sysconfdir}/zabbix_server.conf
fi
:
%post server-mysql

%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_server \
    %{srcname}-server %{_sbindir}/%{srcname}_server_mysql 10 \
        --slave %{_unitdir}/zabbix-server.service %{srcname}-server.service \
            %{_unitdir}/zabbix-server-mysql.service
%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_server \
    %{srcname}-server %{_sbindir}/%{srcname}_server_mysql 10 \
        --slave %{_unitdir}/zabbix-server.service %{srcname}-server.service \
            %{_unitdir}/zabbix-server-mysql.service
%post server-pgsql

%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_server \
    %{srcname}-server %{_sbindir}/%{srcname}_server_pgsql 10 \
        --slave %{_unitdir}/zabbix-server.service %{srcname}-server.service \
            %{_unitdir}/zabbix-server-pgsql.service
%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_server \
    %{srcname}-server %{_sbindir}/%{srcname}_server_pgsql 10 \
        --slave %{_unitdir}/zabbix-server.service %{srcname}-server.service \
            %{_unitdir}/zabbix-server-pgsql.service
%post proxy

%systemd_post zabbix-proxy.service
if [ $1 -gt 1 ] ; then
  chmod 0640 %{_sysconfdir}/zabbix_proxy.conf
  chown root:zabbixsrv %{_sysconfdir}/zabbix_proxy.conf
fi
:
%post proxy-mysql

%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_proxy \
    %{srcname}-proxy %{_sbindir}/%{srcname}_proxy_mysql 10 \
        --slave %{_unitdir}/zabbix-proxy.service %{srcname}-proxy.service \
            %{_unitdir}/zabbix-proxy-mysql.service
%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_proxy \
    %{srcname}-proxy %{_sbindir}/%{srcname}_proxy_mysql 10 \
        --slave %{_unitdir}/zabbix-proxy.service %{srcname}-proxy.service \
            %{_unitdir}/zabbix-proxy-mysql.service
%post proxy-pgsql

%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_proxy \
    %{srcname}-proxy %{_sbindir}/%{srcname}_proxy_pgsql 10 \
        --slave %{_unitdir}/zabbix-proxy.service %{srcname}-proxy.service \
            %{_unitdir}/zabbix-proxy-pgsql.service
%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_proxy \
    %{srcname}-proxy %{_sbindir}/%{srcname}_proxy_pgsql 10 \
        --slave %{_unitdir}/zabbix-proxy.service %{srcname}-proxy.service \
            %{_unitdir}/zabbix-proxy-pgsql.service
%post proxy-sqlite3

%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_proxy \
    %{srcname}-proxy %{_sbindir}/%{srcname}_proxy_sqlite3 10 \
        --slave %{_unitdir}/zabbix-proxy.service %{srcname}-proxy.service \
            %{_unitdir}/zabbix-proxy-sqlite3.service
%{_sbindir}/update-alternatives --install %{_sbindir}/%{srcname}_proxy \
    %{srcname}-proxy %{_sbindir}/%{srcname}_proxy_sqlite3 10 \
        --slave %{_unitdir}/zabbix-proxy.service %{srcname}-proxy.service \
            %{_unitdir}/zabbix-proxy-sqlite3.service
%if 0%{?with_selinux}
%pre selinux

%selinux_relabel_pre -s %{selinuxtype}
%post selinux

%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%postun selinux

if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}
fi
%posttrans selinux

%selinux_relabel_post -s %{selinuxtype}
%endif
%post agent

%systemd_post zabbix-agent.service
%pre server

getent group zabbixsrv > /dev/null || groupadd -r zabbixsrv
if getent passwd zabbixsrv > /dev/null; then
    if [[ $(id -gn zabbixsrv) == "zabbix" ]]; then
        usermod -c "Zabbix Monitoring System -- Proxy or server" -g zabbixsrv zabbixsrv
    fi
else
    useradd -r -g zabbixsrv -d %{_sharedstatedir}/zabbixsrv -s /sbin/nologin \
    -c "Zabbix Monitoring System -- Proxy or server" zabbixsrv
fi
:
%preun server

  %systemd_preun zabbix-server.service
%pre proxy

getent group zabbixsrv > /dev/null || groupadd -r zabbixsrv
if getent passwd zabbixsrv > /dev/null; then
    if [[ $(id -gn zabbixsrv) == "zabbix" ]]; then
        usermod -c "Zabbix Monitoring System -- Proxy or server" -g zabbixsrv zabbixsrv
    fi
else
    useradd -r -g zabbixsrv -d %{_sharedstatedir}/zabbixsrv -s /sbin/nologin \
    -c "Zabbix Monitoring System -- Proxy or server" zabbixsrv
fi
:
%preun proxy

%systemd_preun zabbix-proxy.service
%preun agent

%systemd_preun zabbix-agent.service
%postun server

%systemd_postun_with_restart zabbix-server.service
%postun server-mysql

if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{srcname}-server %{_sbindir}/%{srcname}_server_mysql
fi
%postun server-pgsql

if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{srcname}-server %{_sbindir}/%{srcname}_server_pgsql
fi
%postun proxy

%systemd_postun_with_restart zabbix-proxy.service
%postun proxy-mysql

if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{srcname}-proxy %{_sbindir}/%{srcname}_proxy_mysql
fi
%postun proxy-pgsql

if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{srcname}-proxy %{_sbindir}/%{srcname}_proxy_pgsql
fi
%postun proxy-sqlite3

if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{srcname}-proxy %{_sbindir}/%{srcname}_proxy_sqlite3
fi
%postun agent

%systemd_postun_with_restart zabbix-agent.service
%files -f %{oreon_filedir}/main.list
%files -n zabbix-dbfiles-mysql -f %{oreon_filedir}/zabbix-dbfiles-mysql.list
%files -n zabbix-dbfiles-pgsql -f %{oreon_filedir}/zabbix-dbfiles-pgsql.list
%files -n zabbix-dbfiles-sqlite3 -f %{oreon_filedir}/zabbix-dbfiles-sqlite3.list
%files -n zabbix-server -f %{oreon_filedir}/zabbix-server.list
%files -n zabbix-server-mysql -f %{oreon_filedir}/zabbix-server-mysql.list
%files -n zabbix-server-pgsql -f %{oreon_filedir}/zabbix-server-pgsql.list
%files -n zabbix-agent -f %{oreon_filedir}/zabbix-agent.list
%files -n zabbix-proxy -f %{oreon_filedir}/zabbix-proxy.list
%files -n zabbix-proxy-mysql -f %{oreon_filedir}/zabbix-proxy-mysql.list
%files -n zabbix-proxy-pgsql -f %{oreon_filedir}/zabbix-proxy-pgsql.list
%files -n zabbix-proxy-sqlite3 -f %{oreon_filedir}/zabbix-proxy-sqlite3.list
%files -n zabbix-web -f %{oreon_filedir}/zabbix-web.list
%files -n zabbix-web-mysql -f %{oreon_filedir}/zabbix-web-mysql.list
%files -n zabbix-web-pgsql -f %{oreon_filedir}/zabbix-web-pgsql.list
%files -n java-zabbix -f %{oreon_filedir}/java-zabbix.list
%files -n zabbix-selinux -f %{oreon_filedir}/zabbix-selinux.list

%changelog

%autochangelog
