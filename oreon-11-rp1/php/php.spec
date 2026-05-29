%global source0_hash none

%global source20_key_fpr 1198C0117593497A5EC5C199286AF1F9897469DC

# Fedora spec file for php
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

# Option to build as php8.5 with same provides
# php-common is the pivot package required by all
# Only used by RHEL
%bcond_with         rename

# API/ABI check
%global apiver      20250925
%global zendver     20250925
%global pdover      20240423

# we don't want -z defs linker flag
%undefine _strict_symbol_defs_build

# Adds -z now to the linker flags
%global _hardened_build 1

# version used for php embedded library soname
%global major_version 8.5

%global mysql_sock %(mysql_config --socket 2>/dev/null || echo /var/lib/mysql/mysql.sock)

# Regression tests take a long time, you can skip 'em with this
#global runselftest 0
%{!?runselftest: %global runselftest 1}

# Use the arch-specific mysql_config binary to avoid mismatch with the
# arch detection heuristic used by bindir/mysql_config.
%global mysql_config %{_libdir}/mysql/mysql_config

# needed at srpm build time, when httpd-devel not yet installed
%{!?_httpd_mmn:        %{expand: %%global _httpd_mmn        %%(cat %{_includedir}/httpd/.mmn 2>/dev/null || echo 0-0)}}

%if 0%{?fedora}
# Enabled by default on Fedora
%ifarch s390x
# https://bugzilla.redhat.com/show_bug.cgi?id=1969393
# firebird have ExcludeArch: s390x
%bcond_with      firebird
%else
%bcond_without   firebird
%endif
%bcond_without   freetds
%bcond_without   sodium
%bcond_without   tidy
%bcond_without   db4
%bcond_without   qdbm
%else
# Disabled by default on RHEL
%bcond_with      firebird
%bcond_with      freetds
%bcond_with      sodium
%bcond_with      tidy
%bcond_with      db4
%bcond_with      qdbm
%endif
%bcond_with      zts
%bcond_with      modphp
%bcond_without   lmdb

# liburiparser version 1.0.0 required
%global liburiparser_ver 1.0.0
%if 0%{?fedora}
# use system liburiparser when available
%bcond_without       liburiparser
%else
# use bundled library instead for now
%bcond_with          liburiparser
%endif

%global upver        8.5.4
#global rcver        RC1

Summary: PHP scripting language for creating dynamic web sites
%if %{with rename}
Name: php%{major_version}
%else
Name: php
%endif
Version: %{upver}%{?rcver:~%{rcver}}
Release: 1%{?dist}
# All files licensed under PHP version 3.01, except
# Zend is licensed under Zend
# TSRM is licensed under BSD
# main/snprintf.c, main/spprintf.c and main/rfc1867.c are ASL 1.0
# ext/date/lib is MIT
# Zend/zend_sort is NCSA
# Zend/asm is Boost
License: PHP-3.01 AND Zend-2.0 AND BSD-2-Clause AND MIT AND Apache-1.0 AND NCSA AND BSL-1.0
URL: http://www.php.net/

Source0:        https://www.php.net/distributions/php-8.5.4%{?rcver}.tar.xz
Source1: php.conf
Source2: php.ini
Source3: macros.php
Source4: php-fpm.conf
Source5: php-fpm-www.conf
Source6: php-fpm.service
Source7: php-fpm.logrotate
Source9: php.modconf
Source12: php-fpm.wants
Source13: nginx-fpm.conf
Source14: nginx-php.conf
Source15: php.tmpfiles
# See https://secure.php.net/gpg-keys.php
Source20:        https://www.php.net/distributions/php-keyring.gpg
Source21:        https://www.php.net/distributions/php-8.5.4%{?rcver}.tar.xz.asc
# Configuration files for some extensions
Source50: 10-opcache.ini
Source51: opcache-default.blacklist
Source53: 20-ffi.ini

# Build fixes
Patch1: php-8.4.0-httpd.patch
Patch5: php-8.5.0-includedir.patch
Patch6: php-8.5.0-embed.patch
Patch8: php-8.4.0-libdb.patch

# Functional changes
# Use system nikic/php-parser
Patch41: php-8.5.0-parser.patch
# use system tzdata
Patch42: php-8.5.0-systzdata-v24.patch
# See http://bugs.php.net/53436
# + display PHP version backported from 8.4
Patch43: php-8.4.0-phpize.patch
# Use -lldap_r for OpenLDAP
Patch45: php-8.5.0-ldap_r.patch
# drop "Configure command" from phpinfo output
# and only use gcc (instead of full version)
Patch47: php-8.4.0-phpinfo.patch
# Always warn about missing curve_name
# Both Fedora and RHEL do not support arbitrary EC parameters
Patch48: php-8.5.0-openssl-ec-param.patch

# Upstream fixes (100+)

# Security fixes (200+)

# Fixes for tests (300+)
# Factory is droped from system tzdata
Patch300: php-7.4.0-datetests.patch

ExcludeArch:   %{ix86}

BuildRequires: gnupg2
BuildRequires: bzip2-devel
BuildRequires: pkgconfig(libcurl)  >= 7.29.0
BuildRequires: httpd-devel >= 2.0.46-1
BuildRequires: pam-devel
# to ensure we are using httpd with filesystem feature (see #1081453)
BuildRequires: httpd-filesystem
# to ensure we are using nginx with filesystem feature (see #1142298)
BuildRequires: nginx-filesystem
BuildRequires: libstdc++-devel
# no pkgconfig to avoid compat-openssl10
BuildRequires: openssl-devel >= 1.0.2
BuildRequires: pkgconfig(sqlite3) >= 3.7.4
BuildRequires: pkgconfig(zlib) >= 1.2.0.4
BuildRequires: smtpdaemon
BuildRequires: pkgconfig(libedit)
BuildRequires: pkgconfig(libpcre2-8) >= 10.30
BuildRequires: pkgconfig(capstone) >= 3.0
BuildRequires: pkgconfig(libxcrypt)
BuildRequires: libxcrypt-devel
BuildRequires: bzip2
BuildRequires: perl-interpreter
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: libtool-ltdl-devel
BuildRequires: systemtap-sdt-devel
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
BuildRequires: systemtap-sdt-dtrace
%endif
%if %{with liburiparser}
BuildRequires: pkgconfig(liburiparser) >= %{liburiparser_ver}
%else
Provides:      bundled(liburiparser) = %{liburiparser_ver}
%endif
# used for tests
BuildRequires: %{_bindir}/ps
BuildRequires: tzdata

%if %{with zts}
Provides: php-zts = %{version}-%{release}
Provides: php-zts%{?_isa} = %{version}-%{release}
%endif

%if %{with modphp}
Requires: httpd-mmn = %{_httpd_mmn}
Provides: mod_php                = %{version}-%{release}
# To ensure correct /var/lib/php/session ownership:
Requires(pre): httpd-filesystem
# php engine for Apache httpd webserver
Provides: php(httpd)
# mod_php is deprecated, no package should requires php or mod_php
# all packages must requires used SAPI (cli, fpm, embded..)
# and used extrensions (mysqli, mbstring, xmlwriter...)
Provides: deprecated()
%else
# preserve old behavior
Recommends: httpd
%endif
Requires:   %{name}-common%{?_isa}   = %{version}-%{release}
# For backwards-compatibility, pull the "php" command
Recommends: %{name}-cli%{?_isa}      = %{version}-%{release}
# httpd have threaded MPM by default
Recommends: %{name}-fpm%{?_isa}      = %{version}-%{release}
# as "php" is now mostly a meta-package, commonly used extensions
# reduce diff with "dnf module install php"
Recommends: %{name}-mbstring%{?_isa} = %{version}-%{release}
Recommends: %{name}-pdo%{?_isa}      = %{version}-%{release}
%if %{with sodium}
Recommends: %{name}-sodium%{?_isa}   = %{version}-%{release}
%endif
Recommends: %{name}-xml%{?_isa}      = %{version}-%{release}
%if %{with rename}
Conflicts:  php         < %{major_version}
Provides:   php         = %{version}-%{release}
Provides:   php%{?_isa} = %{version}-%{release}
%endif


%description
PHP is an HTML-embedded scripting language. PHP attempts to make it
easy for developers to write dynamically generated web pages. PHP also
offers built-in database integration for several commercial and
non-commercial database management systems, so writing a
database-enabled webpage with PHP is fairly simple. The most common
use of PHP coding is probably as a replacement for CGI scripts.
%if %{with modphp}
The %{name} package contains the module (often referred to as mod_php)
which adds support for the PHP language to Apache HTTP Server when
running in prefork mode. This module is deprecated.
%endif

%package cli
Summary: Command-line interface for PHP
# sapi/cli/ps_title.c is PostgreSQL
License: PHP-3.01 AND Zend-2.0 AND BSD-2-Clause AND MIT AND Apache-1.0 AND NCSA AND PostgreSQL
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Provides: php-cgi = %{version}-%{release}, php-cgi%{?_isa} = %{version}-%{release}
Provides: php-pcntl, php-pcntl%{?_isa}
Provides: php-readline, php-readline%{?_isa}
%if %{with rename}
Conflicts:  php-cli         < %{major_version}
Provides:   php-cli         = %{version}-%{release}
Provides:   php-cli%{?_isa} = %{version}-%{release}
%endif

%description cli
The %{name}-cli package contains the command-line interface
executing PHP scripts, /usr/bin/php, and the CGI interface.


%package dbg
Summary: The interactive PHP debugger
Requires: %{name}-common%{?_isa} = %{version}-%{release}
%if %{with rename}
Conflicts:  php-dbg         < %{major_version}
Provides:   php-dbg         = %{version}-%{release}
Provides:   php-dbg%{?_isa} = %{version}-%{release}
%endif

%description dbg
The %{name}-dbg package contains the interactive PHP debugger.


%package fpm
Summary: PHP FastCGI Process Manager
BuildRequires: libacl-devel
BuildRequires: pkgconfig(libsystemd) >= 209
BuildRequires: pkgconfig(libselinux)
Requires: %{name}-common%{?_isa} = %{version}-%{release}
%{?systemd_requires}
# To ensure correct /var/lib/php/session ownership:
Requires(pre): httpd-filesystem
# For php.conf in /etc/httpd/conf.d
# and version 2.4.10 for proxy support in SetHandler
Requires: httpd-filesystem >= 2.4.10
# php engine for Apache httpd webserver
Provides: php(httpd)
# for /etc/nginx ownership
Requires: nginx-filesystem
%if %{with rename}
Conflicts:  php-fpm         < %{major_version}
Provides:   php-fpm         = %{version}-%{release}
Provides:   php-fpm%{?_isa} = %{version}-%{release}
%endif

%description fpm
PHP-FPM (FastCGI Process Manager) is an alternative PHP FastCGI
implementation with some additional features useful for sites of
any size, especially busier sites.

%package common
Summary: Common files for PHP
# All files licensed under PHP version 3.01, except
# fileinfo is licensed under PHP version 3.0
# regex, libmagic are licensed under BSD
License: PHP-3.01 AND BSD-2-Clause
Requires: tzdata
# ABI/API check - Arch specific
Provides: php(api) = %{apiver}-%{__isa_bits}
Provides: php(zend-abi) = %{zendver}-%{__isa_bits}
Provides: php(language) = %{version}, php(language)%{?_isa} = %{version}
# Provides for all builtin/shared modules:
Provides: php-bz2, php-bz2%{?_isa}
Provides: php-calendar, php-calendar%{?_isa}
Provides: php-core = %{version}, php-core%{?_isa} = %{version}
Provides: php-ctype, php-ctype%{?_isa}
Provides: php-curl, php-curl%{?_isa}
Provides: php-date, php-date%{?_isa}
Provides: bundled(timelib)
Provides: php-exif, php-exif%{?_isa}
Provides: php-fileinfo, php-fileinfo%{?_isa}
Provides: bundled(libmagic) = 5.43
Provides: php-filter, php-filter%{?_isa}
Provides: php-ftp, php-ftp%{?_isa}
Provides: php-gettext, php-gettext%{?_isa}
Provides: php-hash, php-hash%{?_isa}
Provides: php-lexbor, php-lexbor%{?_isa}
Provides: php-mhash = %{version}, php-mhash%{?_isa} = %{version}
Provides: php-iconv, php-iconv%{?_isa}
Obsoletes: php-json < 8
Provides: php-json = %{version}, php-json%{?_isa} = %{version}
Provides: php-libxml, php-libxml%{?_isa}
Obsoletes: php-opcache < 8.5.0
Provides: php-opcache = %{version}, php-opcache%{?_isa} = %{version}
Provides: php-openssl, php-openssl%{?_isa}
Provides: php-phar, php-phar%{?_isa}
Provides: php-pcre, php-pcre%{?_isa}
Provides: php-random, php-random%{?_isa}
Provides: php-reflection, php-reflection%{?_isa}
Provides: php-session, php-session%{?_isa}
Provides: php-sockets, php-sockets%{?_isa}
Provides: php-spl, php-spl%{?_isa}
Provides: php-standard = %{version}, php-standard%{?_isa} = %{version}
Provides: php-tokenizer, php-tokenizer%{?_isa}
Provides: php-uri, php-uri%{?_isa}
Provides: php-zlib, php-zlib%{?_isa}
%if %{with rename}
Conflicts:  php-common         < %{major_version}
Provides:   php-common         = %{version}-%{release}
Provides:   php-common%{?_isa} = %{version}-%{release}
%endif

%description common
The %{name}-common package contains files used by both the %{name}
package and the %{name}-cli package.

%package devel
Summary: Files needed for building PHP extensions
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Requires: %{name}-cli%{?_isa} = %{version}-%{release}
# always needed to build extension
Requires: autoconf
Requires: automake
Requires: make
Requires: gcc
Requires: gcc-c++
Requires: libtool
# see "php-config --libs"
Requires: krb5-devel%{?_isa}
Requires: libxml2-devel%{?_isa}
Requires: openssl-devel%{?_isa} >= 1.0.2
Requires: pcre2-devel%{?_isa}
Requires: zlib-devel%{?_isa}
%if %{with zts}
Provides: php-zts-devel = %{version}-%{release}
Provides: php-zts-devel%{?_isa} = %{version}-%{release}
%endif
%if %{with rename}
Conflicts:  php-devel         < %{major_version}
Provides:   php-devel         = %{version}-%{release}
Provides:   php-devel%{?_isa} = %{version}-%{release}
%endif
Recommends: php-nikic-php-parser5 >= 5.6.1
Conflicts:  php-nikic-php-parser5 <  5.6.1


%description devel
The %{name}-devel package contains the files needed for building PHP
extensions. If you need to compile your own PHP extensions, you will
need to install this package.

%package ldap
Summary: A module for PHP applications that use LDAP
# All files licensed under PHP version 3.01
License:  PHP-3.01
Requires: %{name}-common%{?_isa} = %{version}-%{release}
BuildRequires: pkgconfig(libsasl2)
BuildRequires: openldap-devel
BuildRequires: openssl-devel >= 1.0.2
%if %{with rename}
Conflicts:  php-ldap         < %{major_version}
Provides:   php-ldap         = %{version}-%{release}
Provides:   php-ldap%{?_isa} = %{version}-%{release}
%endif

%description ldap
The %{name}-ldap adds Lightweight Directory Access Protocol (LDAP)
support to PHP. LDAP is a set of protocols for accessing directory
services over the Internet. PHP is an HTML-embedded scripting
language.

%package pdo
Summary: A database access abstraction module for PHP applications
# All files licensed under PHP version 3.01
License:  PHP-3.01
Requires: %{name}-common%{?_isa} = %{version}-%{release}
# ABI/API check - Arch specific
Provides: php-pdo-abi  = %{pdover}-%{__isa_bits}
Provides: php(pdo-abi) = %{pdover}-%{__isa_bits}
Provides: php-sqlite3, php-sqlite3%{?_isa}
Provides: php-pdo_sqlite, php-pdo_sqlite%{?_isa}
%if %{with rename}
Conflicts:  php-pdo         < %{major_version}
Provides:   php-pdo         = %{version}-%{release}
Provides:   php-pdo%{?_isa} = %{version}-%{release}
%endif

%description pdo
The %{name}-pdo package contains a dynamic shared object that will add
a database access abstraction layer to PHP.  This module provides
a common interface for accessing MySQL, PostgreSQL or other
databases.

%package mysqlnd
Summary: A module for PHP applications that use MySQL databases
# All files licensed under PHP version 3.01
License:  PHP-3.01
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Requires: %{name}-pdo%{?_isa} = %{version}-%{release}
Provides: php_database
Provides: php-mysqli = %{version}-%{release}
Provides: php-mysqli%{?_isa} = %{version}-%{release}
Provides: php-pdo_mysql, php-pdo_mysql%{?_isa}
%if %{with rename}
Conflicts:  php-mysqlnd         < %{major_version}
Provides:   php-mysqlnd         = %{version}-%{release}
Provides:   php-mysqlnd%{?_isa} = %{version}-%{release}
%endif

%description mysqlnd
The %{name}-mysqlnd package contains a dynamic shared object that will add
MySQL database support to PHP. MySQL is an object-relational database
management system. PHP is an HTML-embeddable scripting language. If
you need MySQL support for PHP applications, you will need to install
this package and the php package.

This package use the MySQL Native Driver

%package pgsql
Summary: A PostgreSQL database module for PHP
# All files licensed under PHP version 3.01
License:  PHP-3.01
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Requires: %{name}-pdo%{?_isa} = %{version}-%{release}
Provides: php_database
Provides: php-pdo_pgsql, php-pdo_pgsql%{?_isa}
BuildRequires: krb5-devel
BuildRequires: openssl-devel >= 1.0.2
BuildRequires: libpq-devel
%if %{with rename}
Conflicts:  php-pgsql         < %{major_version}
Provides:   php-pgsql         = %{version}-%{release}
Provides:   php-pgsql%{?_isa} = %{version}-%{release}
%endif

%description pgsql
The %{name}-pgsql package add PostgreSQL database support to PHP.
PostgreSQL is an object-relational database management
system that supports almost all SQL constructs. PHP is an
HTML-embedded scripting language. If you need back-end support for
PostgreSQL, you should install this package in addition to the main
php package.

%package process
Summary: Modules for PHP script using system process interfaces
# All files licensed under PHP version 3.01
License:  PHP-3.01
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Provides: php-posix, php-posix%{?_isa}
Provides: php-shmop, php-shmop%{?_isa}
Provides: php-sysvsem, php-sysvsem%{?_isa}
Provides: php-sysvshm, php-sysvshm%{?_isa}
Provides: php-sysvmsg, php-sysvmsg%{?_isa}
%if %{with rename}
Conflicts:  php-process         < %{major_version}
Provides:   php-process         = %{version}-%{release}
Provides:   php-process%{?_isa} = %{version}-%{release}
%endif

%description process
The %{name}-process package contains dynamic shared objects which add
support to PHP using system interfaces for inter-process
communication.

%package odbc
Summary: A module for PHP applications that use ODBC databases
# All files licensed under PHP version 3.01, except
# pdo_odbc is licensed under PHP version 3.0
License:  PHP-3.01
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Requires: %{name}-pdo%{?_isa} = %{version}-%{release}
Provides: php_database
Provides: php-pdo_odbc, php-pdo_odbc%{?_isa}
BuildRequires: unixODBC-devel
%if %{with rename}
Conflicts:  php-odbc         < %{major_version}
Provides:   php-odbc         = %{version}-%{release}
Provides:   php-odbc%{?_isa} = %{version}-%{release}
%endif

%description odbc
The %{name}-odbc package contains a dynamic shared object that will add
database support through ODBC to PHP. ODBC is an open specification
which provides a consistent API for developers to use for accessing
data sources (which are often, but not always, databases). PHP is an
HTML-embeddable scripting language. If you need ODBC support for PHP
applications, you will need to install this package and the php
package.

%package soap
Summary: A module for PHP applications that use the SOAP protocol
# All files licensed under PHP version 3.01
License:  PHP-3.01
Requires: %{name}-common%{?_isa} = %{version}-%{release}
BuildRequires: pkgconfig(libxml-2.0)
%if %{with rename}
Conflicts:  php-soap         < %{major_version}
Provides:   php-soap         = %{version}-%{release}
Provides:   php-soap%{?_isa} = %{version}-%{release}
%endif

%description soap
The %{name}-soap package contains a dynamic shared object that will add
support to PHP for using the SOAP web services protocol.

%if %{with firebird}
%package pdo-firebird
Summary: PDO driver for Interbase/Firebird databases
# All files licensed under PHP version 3.01
License:  PHP-3.01
# for fb_config command
BuildRequires:  firebird-devel
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Requires: %{name}-pdo%{?_isa} = %{version}-%{release}
Provides: php_database
Provides: php-pdo_firebird, php-pdo_firebird%{?_isa}
%if %{with rename}
Conflicts:  php-pdo-firebird         < %{major_version}
Provides:   php-pdo-firebird         = %{version}-%{release}
Provides:   php-pdo-firebird%{?_isa} = %{version}-%{release}
%endif

%description pdo-firebird
The %{name}-pdo-firebird package contains the PDO driver for
Interbase/Firebird databases.
%endif

%package snmp
Summary: A module for PHP applications that query SNMP-managed devices
# All files licensed under PHP version 3.01
License:  PHP-3.01
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Requires: net-snmp
BuildRequires: net-snmp-devel
%if %{with rename}
Conflicts:  php-snmp         < %{major_version}
Provides:   php-snmp         = %{version}-%{release}
Provides:   php-snmp%{?_isa} = %{version}-%{release}
%endif

%description snmp
The %{name}-snmp package contains a dynamic shared object that will add
support for querying SNMP devices to PHP.  PHP is an HTML-embeddable
scripting language. If you need SNMP support for PHP applications, you
will need to install this package and the php package.

%package xml
Summary: A module for PHP applications which use XML
# All files licensed under PHP version 3.01
License:  PHP-3.01
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Provides: php-dom, php-dom%{?_isa}
Provides: php-domxml, php-domxml%{?_isa}
Provides: php-simplexml, php-simplexml%{?_isa}
Provides: php-xmlreader, php-xmlreader%{?_isa}
Provides: php-xmlwriter, php-xmlwriter%{?_isa}
Provides: php-xsl, php-xsl%{?_isa}
BuildRequires: pkgconfig(libxslt)  >= 1.1
BuildRequires: pkgconfig(libexslt)
BuildRequires: pkgconfig(libxml-2.0)  >= 2.7.6
%if %{with rename}
Conflicts:  php-xml         < %{major_version}
Provides:   php-xml         = %{version}-%{release}
Provides:   php-xml%{?_isa} = %{version}-%{release}
%endif

%description xml
The %{name}-xml package contains dynamic shared objects which add support
to PHP for manipulating XML documents using the DOM tree,
and performing XSL transformations on XML documents.

%package mbstring
Summary: A module for PHP applications which need multi-byte string handling
# All files licensed under PHP version 3.01, except
# libmbfl is licensed under LGPLv2
# ucgendat is licensed under OpenLDAP
License: PHP-3.01 AND LGPL-2.1-only AND OLDAP-2.8
BuildRequires: pkgconfig(oniguruma) >= 6.8
Provides: bundled(libmbfl) = 1.3.2
Requires: %{name}-common%{?_isa} = %{version}-%{release}
%if %{with rename}
Conflicts:  php-mbstring         < %{major_version}
Provides:   php-mbstring         = %{version}-%{release}
Provides:   php-mbstring%{?_isa} = %{version}-%{release}
%endif

%description mbstring
The %{name}-mbstring package contains a dynamic shared object that will add
support for multi-byte string handling to PHP.

%package gd
Summary: A module for PHP applications for using the gd graphics library
# All files licensed under PHP version 3.01
License:  PHP-3.01
Requires: %{name}-common%{?_isa} = %{version}-%{release}
BuildRequires: pkgconfig(gdlib) >= 2.1.1
%if %{with rename}
Conflicts:  php-gd         < %{major_version}
Provides:   php-gd         = %{version}-%{release}
Provides:   php-gd%{?_isa} = %{version}-%{release}
%endif

%description gd
The %{name}-gd package contains a dynamic shared object that will add
support for using the gd graphics library to PHP.

%package bcmath
Summary: A module for PHP applications for using the bcmath library
# All files licensed under PHP version 3.01, except
# libbcmath is licensed under LGPLv2+
License:  PHP-3.01 AND LGPL-2.1-or-later
Requires: %{name}-common%{?_isa} = %{version}-%{release}
%if %{with rename}
Conflicts:  php-bcmath         < %{major_version}
Provides:   php-bcmath         = %{version}-%{release}
Provides:   php-bcmath%{?_isa} = %{version}-%{release}
%endif

%description bcmath
The %{name}-bcmath package contains a dynamic shared object that will add
support for using the bcmath library to PHP.

%package gmp
Summary: A module for PHP applications for using the GNU MP library
# All files licensed under PHP version 3.01
License:  PHP-3.01
BuildRequires: gmp-devel
Requires: %{name}-common%{?_isa} = %{version}-%{release}
%if %{with rename}
Conflicts:  php-gmp         < %{major_version}
Provides:   php-gmp         = %{version}-%{release}
Provides:   php-gmp%{?_isa} = %{version}-%{release}
%endif

%description gmp
These functions allow you to work with arbitrary-length integers
using the GNU MP library.

%package dba
Summary: A database abstraction layer module for PHP applications
# All files licensed under PHP version 3.01
License:  PHP-3.01
%if %{with db4}
BuildRequires: libdb-devel
%endif
BuildRequires: tokyocabinet-devel
%if %{with lmdb}
BuildRequires: lmdb-devel
%endif
%if %{with qdbm}
BuildRequires: qdbm-devel
%endif
Requires: %{name}-common%{?_isa} = %{version}-%{release}
%if %{with rename}
Conflicts:  php-dba         < %{major_version}
Provides:   php-dba         = %{version}-%{release}
Provides:   php-dba%{?_isa} = %{version}-%{release}
%endif

%description dba
The %{name}-dba package contains a dynamic shared object that will add
support for using the DBA database abstraction layer to PHP.

%if %{with tidy}
%package tidy
Summary: Standard PHP module provides tidy library support
# All files licensed under PHP version 3.01
License:  PHP-3.01
Requires: %{name}-common%{?_isa} = %{version}-%{release}
BuildRequires: libtidy-devel
%if %{with rename}
Conflicts:  php-tidy         < %{major_version}
Provides:   php-tidy         = %{version}-%{release}
Provides:   php-tidy%{?_isa} = %{version}-%{release}
%endif

%description tidy
The %{name}-tidy package contains a dynamic shared object that will add
support for using the tidy library to PHP.
%endif

%if %{with freetds}
%package pdo-dblib
Summary: PDO driver for Microsoft SQL Server and Sybase databases
# All files licensed under PHP version 3.01
License:  PHP-3.01
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Requires: %{name}-pdo%{?_isa} = %{version}-%{release}
BuildRequires: freetds-devel
Provides: php-pdo_dblib, php-pdo_dblib%{?_isa}
%if %{with rename}
Conflicts:  php-pdo-dblib         < %{major_version}
Provides:   php-pdo-dblib         = %{version}-%{release}
Provides:   php-pdo-dblib%{?_isa} = %{version}-%{release}
%endif

%description pdo-dblib
The %{name}-pdo-dblib package contains a dynamic shared object
that implements the PHP Data Objects (PDO) interface to enable access from
PHP to Microsoft SQL Server and Sybase databases through the FreeTDS library.
%endif

%package embedded
Summary: PHP library for embedding in applications
Requires: %{name}-common%{?_isa} = %{version}-%{release}
# doing a real -devel package for just the .so symlink is a bit overkill
Provides: php-embedded-devel = %{version}-%{release}
Provides: php-embedded-devel%{?_isa} = %{version}-%{release}
%if %{with rename}
Conflicts:  php-embedded         < %{major_version}
Provides:   php-embedded         = %{version}-%{release}
Provides:   php-embedded%{?_isa} = %{version}-%{release}
%endif

%description embedded
The %{name}-embedded package contains a library which can be embedded
into applications to provide PHP scripting language support.

%package intl
Summary: Internationalization extension for PHP applications
# All files licensed under PHP version 3.01
License:  PHP-3.01
Requires: %{name}-common%{?_isa} = %{version}-%{release}
BuildRequires: pkgconfig(icu-i18n) >= 50.1
BuildRequires: pkgconfig(icu-io)   >= 50.1
BuildRequires: pkgconfig(icu-uc)   >= 50.1
%if %{with rename}
Conflicts:  php-intl         < %{major_version}
Provides:   php-intl         = %{version}-%{release}
Provides:   php-intl%{?_isa} = %{version}-%{release}
%endif

%description intl
The %{name}-intl package contains a dynamic shared object that will add
support for using the ICU library to PHP.

%package enchant
Summary: Enchant spelling extension for PHP applications
# All files licensed under PHP version 3.0
License:  PHP-3.01
Requires: %{name}-common%{?_isa} = %{version}-%{release}
BuildRequires: pkgconfig(enchant-2)
%if %{with rename}
Conflicts:  php-enchant         < %{major_version}
Provides:   php-enchant         = %{version}-%{release}
Provides:   php-enchant%{?_isa} = %{version}-%{release}
%endif

%description enchant
The %{name}-enchant package contains a dynamic shared object that will add
support for using the enchant library to PHP.

%if %{with sodium}
%package sodium
Summary: Wrapper for the Sodium cryptographic library
# All files licensed under PHP version 3.0.1
License:  PHP-3.01
BuildRequires:  pkgconfig(libsodium) >= 1.0.9

Requires: %{name}-common%{?_isa} = %{version}-%{release}
Obsoletes: php-pecl-libsodium2 < 3
Provides:  php-pecl(libsodium)         = %{version}
Provides:  php-pecl(libsodium)%{?_isa} = %{version}
%if %{with rename}
Conflicts: php-sodium         < %{major_version}
Provides:  php-sodium         = %{version}-%{release}
Provides:  php-sodium%{?_isa} = %{version}-%{release}
%endif

%description sodium
The %{name}-sodium package provides a simple,
low-level PHP extension for the libsodium cryptographic library.
%endif


%package ffi
Summary: Foreign Function Interface
# All files licensed under PHP version 3.0.1
License:  PHP-3.01
BuildRequires:  pkgconfig(libffi)
Requires: %{name}-common%{?_isa} = %{version}-%{release}
%if %{with rename}
Conflicts: php-ffi         < %{major_version}
Provides:  php-ffi         = %{version}-%{release}
Provides:  php-ffi%{?_isa} = %{version}-%{release}
%endif

%description ffi
FFI is one of the features that made Python and LuaJIT very useful for fast
prototyping. It allows calling C functions and using C data types from pure
scripting language and therefore develop “system code” more productively.

For PHP, FFI opens a way to write PHP extensions and bindings to C libraries
in pure PHP.


%prep
%(test -z "%{source20_key_fpr}" || { f="%{SOURCE20}"; test -f "$f" || { echo "oreon: missing Source20 key $f" >&2; exit 1; }; fpr=$(gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source20_key_fpr}" || { echo "oreon: Source20 key fingerprint mismatch" >&2; exit 1; }; })
%{?gpgverify:%{gpgverify} --keyring='%{SOURCE20}' --signature='%{SOURCE21}' --data='%{SOURCE0}'}

%setup -q -n php-%{upver}%{?rcver}

%patch -P1 -p1 -b .mpmcheck
%patch -P5 -p1 -b .includedir
%patch -P6 -p1 -b .embed
%patch -P8 -p1 -b .libdb

%patch -P41 -p1 -b .syslib
%patch -P42 -p1 -b .systzdata
%patch -P43 -p1 -b .headers
%patch -P45 -p1 -b .ldap_r
%patch -P47 -p1 -b .phpinfo
%patch -P48 -p1 -b .ec-param

# upstream patches

# security patches

# Fixes for tests
%patch -P300 -p1 -b .datetests


# Prevent %%doc confusion over LICENSE files
cp Zend/LICENSE ZEND_LICENSE
cp TSRM/LICENSE TSRM_LICENSE
cp Zend/asm/LICENSE BOOST_LICENSE
cp sapi/fpm/LICENSE fpm_LICENSE
cp ext/mbstring/libmbfl/LICENSE libmbfl_LICENSE
cp ext/fileinfo/libmagic/LICENSE libmagic_LICENSE
cp ext/bcmath/libbcmath/LICENSE libbcmath_LICENSE
cp ext/date/lib/LICENSE.rst timelib_LICENSE

# Multiple builds for multiple SAPIs
# mod_php (apache2handler) and libphp (embed) can not be built from same tree
mkdir \
    build-cgi \
%if %{with modphp}
    build-apache \
%endif
%if %{with zts}
    build-zts build-ztscli \
%endif
    build-fpm

# ----- Manage known as failed test -------
# affected by systzdata patch
rm ext/date/tests/timezone_location_get.phpt
rm ext/date/tests/timezone_version_get.phpt
rm ext/date/tests/timezone_version_get_basic1.phpt
# fails sometime
rm ext/sockets/tests/mcast_ipv?_recv.phpt
# Both Fedora and RHEL do not support arbitrary EC parameters
# https://bugzilla.redhat.com/2223953
rm ext/openssl/tests/ecc_custom_params.phpt
# Failing when build with PHP installed
rm ext/opcache/tests/zzz_basic_logging.phpt

# Safety check for API version change.
pver=$(sed -n '/#define PHP_VERSION /{s/.* "//;s/".*$//;p}' main/php_version.h)
if test "x${pver}" != "x%{upver}%{?rcver}"; then
   : Error: Upstream PHP version is now ${pver}, expecting %{upver}%{?rcver}.
   : Update the version/rcver macros and rebuild.
   exit 1
fi

vapi=`sed -n '/#define PHP_API_VERSION/{s/.* //;p}' main/php.h`
if test "x${vapi}" != "x%{apiver}"; then
   : Error: Upstream API version is now ${vapi}, expecting %{apiver}.
   : Update the apiver macro and rebuild.
   exit 1
fi

vzend=`sed -n '/#define ZEND_MODULE_API_NO/{s/^[^0-9]*//;p;}' Zend/zend_modules.h`
if test "x${vzend}" != "x%{zendver}"; then
   : Error: Upstream Zend ABI version is now ${vzend}, expecting %{zendver}.
   : Update the zendver macro and rebuild.
   exit 1
fi

# Safety check for PDO ABI version change
vpdo=`sed -n '/#define PDO_DRIVER_API/{s/.*[ 	]//;p}' ext/pdo/php_pdo_driver.h`
if test "x${vpdo}" != "x%{pdover}"; then
   : Error: Upstream PDO ABI version is now ${vpdo}, expecting %{pdover}.
   : Update the pdover macro and rebuild.
   exit 1
fi

# https://bugs.php.net/63362 - Not needed but installed headers.
# Drop some Windows specific headers to avoid installation,
# before build to ensure they are really not needed.
rm -f TSRM/tsrm_win32.h \
      TSRM/tsrm_config.w32.h \
      Zend/zend_config.w32.h \
      ext/mysqlnd/config-win.h \
      ext/standard/winver.h \
      main/win32_internal_function_disabled.h \
      main/win95nt.h

# Fix some bogus permissions
find . -name \*.[ch] -exec chmod 644 {} \;
chmod 644 README.*

# Some extensions have their own configuration file
cp %{SOURCE50} %{SOURCE51} %{SOURCE53} .


%build
# This package fails to build with LTO due to undefined symbols.  LTO
# was disabled in OpenSuSE as well, but with no real explanation why
# beyond the undefined symbols.  It really shold be investigated further.
# Disable LTO
%define _lto_cflags %{nil}

# Set build date from https://reproducible-builds.org/specs/source-date-epoch/
export SOURCE_DATE_EPOCH=$(date +%s -r NEWS)
export PHP_UNAME=$(uname)
export PHP_BUILD_SYSTEM=$(cat /etc/redhat-release | sed -e 's/ Beta//')
%if 0%{?vendor:1}
export PHP_BUILD_PROVIDER="%{vendor}"
%endif
export PHP_BUILD_COMPILER="$(gcc --version | head -n1)"
export PHP_BUILD_ARCH="%{_arch}"

# Force use of system libtool:
libtoolize --force --copy
cat `aclocal --print-ac-dir`/{libtool,ltoptions,ltsugar,ltversion,lt~obsolete}.m4 >build/libtool.m4

# Regenerate configure scripts (patches change config.m4's)
touch configure.ac
./buildconf --force

CFLAGS=$(echo $RPM_OPT_FLAGS -fno-strict-aliasing -Wno-pointer-sign | sed 's/-mstackrealign//')
export CFLAGS

# Install extension modules in %%{_libdir}/php/modules.
EXTENSION_DIR=%{_libdir}/php/modules; export EXTENSION_DIR

# Set PEAR_INSTALLDIR to ensure that the hard-coded include_path
# includes the PEAR directory even though pear is packaged
# separately.
PEAR_INSTALLDIR=%{_datadir}/pear; export PEAR_INSTALLDIR

# Shell function to configure and build a PHP tree.
build() {
# Old/recent bison version seems to produce a broken parser;
# upstream uses GNU Bison 2.3. Workaround:
mkdir Zend && cp ../Zend/zend_{language,ini}_{parser,scanner}.[ch] Zend

# Always static:
# date, ereg, filter, libxml, reflection, spl: not supported
# hash: for PHAR_SIG_SHA256 and PHAR_SIG_SHA512
# session: dep on hash, used by soap
# sockets: heavily used by FPM test suite
# pcre: used by filter, zip
# pcntl, readline: only used by CLI sapi
# openssl: for PHAR_SIG_OPENSSL
# zlib: used by image

ln -sf ../configure
%configure \
    --enable-rtld-now \
    --cache-file=../config.cache \
    --with-libdir=%{_lib} \
    --with-config-file-path=%{_sysconfdir} \
    --with-config-file-scan-dir=%{_sysconfdir}/php.d \
    --disable-debug \
    --with-pic \
    --disable-rpath \
    --without-pear \
    --with-exec-dir=%{_bindir} \
    --without-gdbm \
    --enable-opcache-file \
    --with-openssl \
    --with-openssl-argon2 \
    --with-system-ciphers \
    --with-external-pcre \
    --with-external-libcrypt \
%if %{with liburiparser}
    --with-external-uriparser \
%endif
%ifarch s390 s390x sparc64 sparcv9 riscv64
    --without-pcre-jit \
%endif
    --with-zlib \
    --with-layout=GNU \
    --with-libxml \
    --with-system-tzdata \
    --with-mhash \
    --without-password-argon2 \
    --enable-dtrace \
    --enable-sockets \
    $*
if test $? != 0; then
  tail -500 config.log
  : configure failed
  exit 1
fi

%make_build
}

# Build cli and cgi SAPI, and most shared extensions
pushd build-cgi

build --enable-pcntl \
      --with-capstone \
      --enable-phpdbg --enable-phpdbg-readline \
      --enable-mbstring=shared \
      --enable-mbregex \
      --enable-gd=shared \
      --with-external-gd \
      --with-gmp=shared \
      --enable-calendar=shared \
      --enable-bcmath=shared \
      --with-bz2=shared \
      --enable-ctype=shared \
      --enable-dba=shared \
%if %{with db4}
                          --with-db4=%{_prefix} \
%endif
                          --with-tcadb=%{_prefix} \
%if %{with lmdb}
                          --with-lmdb=%{_prefix} \
%endif
%if %{with qdbm}
                          --with-qdbm=%{_prefix} \
%endif
      --enable-exif=shared \
      --enable-ftp=shared \
      --with-gettext=shared \
      --with-iconv=shared \
      --enable-tokenizer=shared \
      --with-ldap=shared --with-ldap-sasl \
      --enable-mysqlnd=shared \
      --with-mysqli=shared,mysqlnd \
      --with-mysql-sock=%{mysql_sock} \
%if %{with firebird}
      --with-pdo-firebird=shared \
%endif
      --enable-dom=shared \
      --with-pgsql=shared \
      --enable-simplexml=shared \
      --enable-xml=shared \
      --with-snmp=shared,%{_prefix} \
      --enable-soap=shared \
      --with-xsl=shared,%{_prefix} \
      --enable-xmlreader=shared --enable-xmlwriter=shared \
      --with-curl=shared \
      --enable-pdo=shared \
      --with-pdo-odbc=shared,unixODBC,%{_prefix} \
      --with-pdo-mysql=shared,mysqlnd \
      --with-pdo-pgsql=shared,%{_prefix} \
      --with-pdo-sqlite=shared \
%if %{with freetds}
      --with-pdo-dblib=shared,%{_prefix} \
%endif
      --with-sqlite3=shared \
      --without-readline \
      --with-libedit \
      --enable-phar=shared \
%if %{with tidy}
      --with-tidy=shared,%{_prefix} \
%endif
      --enable-sysvmsg=shared --enable-sysvshm=shared --enable-sysvsem=shared \
      --enable-shmop=shared \
      --enable-posix=shared \
      --with-unixODBC=shared,%{_prefix} \
      --enable-fileinfo=shared \
      --with-ffi=shared \
%if %{with sodium}
      --with-sodium=shared \
%else
      --without-sodium \
%endif
      --enable-intl=shared \
      --with-enchant=shared
popd

without_shared="--without-gd \
      --disable-dom --disable-dba --without-unixODBC \
      --without-mysqli \
      --disable-pdo \
      --disable-phpdbg \
      --without-ffi \
      --disable-xmlreader --disable-xmlwriter \
      --without-sodium \
      --without-sqlite3 --disable-phar --disable-fileinfo \
      --without-curl --disable-posix --disable-xml \
      --disable-simplexml --disable-exif --without-gettext \
      --without-iconv --disable-ftp --without-bz2 --disable-ctype \
      --disable-shmop --disable-tokenizer \
      --disable-sysvmsg --disable-sysvshm --disable-sysvsem"

%if %{with modphp}
# Build Apache module
# use separate build to avoid libedit, libncurses...
pushd build-apache
build --with-apxs2=%{_httpd_apxs} \
      ${without_shared}
popd
%endif

# Build php-fpm and embed
pushd build-fpm
build --enable-fpm \
      --with-fpm-acl \
      --with-fpm-systemd \
      --with-fpm-selinux \
      --enable-embed \
      ${without_shared}
popd

%if %{with zts}
# Build a special thread-safe (mainly for modules)
pushd build-ztscli

EXTENSION_DIR=%{_libdir}/php-zts/modules
build --includedir=%{_includedir}/php-zts \
      --libdir=%{_libdir}/php-zts \
      --enable-zts \
      --program-prefix=zts- \
      --disable-cgi \
      --with-config-file-scan-dir=%{_sysconfdir}/php-zts.d \
      --enable-pcntl \
      --with-capstone \
      --enable-mbstring=shared \
      --enable-mbregex \
      --enable-gd=shared \
      --with-external-gd \
      --with-gmp=shared \
      --enable-calendar=shared \
      --enable-bcmath=shared \
      --with-bz2=shared \
      --enable-ctype=shared \
      --enable-dba=shared \
%if %{with db4}
                          --with-db4=%{_prefix} \
%endif
                          --with-tcadb=%{_prefix} \
%if %{with lmdb}
                          --with-lmdb=%{_prefix} \
%endif
%if %{with qdbm}
                          --with-qdbm=%{_prefix} \
%endif
      --with-gettext=shared \
      --with-iconv=shared \
      --enable-tokenizer=shared \
      --enable-exif=shared \
      --enable-ftp=shared \
      --with-ldap=shared --with-ldap-sasl \
      --enable-mysqlnd=shared \
      --with-mysqli=shared,mysqlnd \
      --with-mysql-sock=%{mysql_sock} \
      --enable-mysqlnd-threading \
%if %{with firebird}
      --with-pdo-firebird=shared \
%endif
      --enable-dom=shared \
      --with-pgsql=shared \
      --enable-simplexml=shared \
      --enable-xml=shared \
      --with-snmp=shared,%{_prefix} \
      --enable-soap=shared \
      --with-xsl=shared,%{_prefix} \
      --enable-xmlreader=shared --enable-xmlwriter=shared \
      --with-curl=shared \
      --enable-pdo=shared \
      --with-pdo-odbc=shared,unixODBC,%{_prefix} \
      --with-pdo-mysql=shared,mysqlnd \
      --with-pdo-pgsql=shared,%{_prefix} \
      --with-pdo-sqlite=shared \
%if %{with freetds}
      --with-pdo-dblib=shared,%{_prefix} \
%endif
      --with-sqlite3=shared \
      --without-readline \
      --with-libedit \
      --enable-phar=shared \
%if %{with tidy}
      --with-tidy=shared,%{_prefix} \
%endif
      --enable-sysvmsg=shared --enable-sysvshm=shared --enable-sysvsem=shared \
      --enable-shmop=shared \
      --enable-posix=shared \
      --with-unixODBC=shared,%{_prefix} \
      --enable-fileinfo=shared \
      --with-ffi=shared \
%if %{with sodium}
      --with-sodium=shared \
%else
      --without-sodium \
%endif
      --enable-intl=shared \
      --with-enchant=shared
popd

### NOTE!!! EXTENSION_DIR was changed for the -zts build, so it must remain
### the last SAPI to be built.
%endif


%check
: Ensure proper NTS/ZTS build
$RPM_BUILD_ROOT%{_bindir}/php     -n -v | grep NTS
%if %{with zts}
$RPM_BUILD_ROOT%{_bindir}/zts-php -n -v | grep ZTS
%endif

%if %runselftest
cd build-fpm

# Run tests, using the CLI SAPI
export NO_INTERACTION=1 REPORT_EXIT_STATUS=1 MALLOC_CHECK_=2
export SKIP_ONLINE_TESTS=1
export SKIP_IO_CAPTURE_TESTS=1
unset TZ LANG LC_ALL
if ! make test TESTS=%{?_smp_mflags}; then
  set +x
  for f in $(find .. -name \*.diff -type f -print); do
    if ! grep -q XFAIL "${f/.diff/.phpt}"
    then
      echo "TEST FAILURE: $f --"
      cat "$f"
      echo -e "\n-- $f result ends."
    fi
  done
  set -x
  #exit 1
fi
unset NO_INTERACTION REPORT_EXIT_STATUS MALLOC_CHECK_
%endif

%install
%if %{with zts}
# Install the extensions for the ZTS version
make -C build-ztscli install \
     INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

# Install the version for embedded script language in applications + php_embed.h
make -C build-fpm install-sapi install-headers \
     INSTALL_ROOT=$RPM_BUILD_ROOT

# Install the php-fpm binary
make -C build-fpm install-fpm \
     INSTALL_ROOT=$RPM_BUILD_ROOT

# Install everything from the CGI SAPI build
make -C build-cgi install \
     INSTALL_ROOT=$RPM_BUILD_ROOT

# Use php-config from embed SAPI to reduce used libs
install -m 755 build-fpm/scripts/php-config $RPM_BUILD_ROOT%{_bindir}/php-config

# Install the default configuration file
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/php.ini

# For third-party packaging:
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/php/preload

# Install tmpfiles.d file
install -p -D -m 0644 %{SOURCE15} %{buildroot}%{_tmpfilesdir}/php.conf

%if %{with modphp}
# install the DSO
install -m 755 -d $RPM_BUILD_ROOT%{_httpd_moddir}
install -m 755 build-apache/libs/libphp.so $RPM_BUILD_ROOT%{_httpd_moddir}
%endif

# Apache config fragment
# Dual config file with httpd >= 2.4 (fedora >= 18)
%if %{with modphp}
install -D -m 644 %{SOURCE9} $RPM_BUILD_ROOT%{_httpd_modconfdir}/20-php.conf
%endif
install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_httpd_confdir}/php.conf

install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php.d
%if %{with zts}
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php-zts.d
%endif
install -m 755 -d $RPM_BUILD_ROOT%{_sharedstatedir}/php
install -m 755 -d $RPM_BUILD_ROOT%{_sharedstatedir}/php/peclxml
install -m 700 -d $RPM_BUILD_ROOT%{_sharedstatedir}/php/session
install -m 700 -d $RPM_BUILD_ROOT%{_sharedstatedir}/php/wsdlcache
install -m 700 -d $RPM_BUILD_ROOT%{_sharedstatedir}/php/opcache

install -m 755 -d $RPM_BUILD_ROOT%{_docdir}/pecl
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/tests/pecl

# PHP-FPM stuff
# Log
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/log/php-fpm
install -m 755 -d $RPM_BUILD_ROOT/run/php-fpm
# Config
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.d
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.conf
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.d/www.conf
mv $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.conf.default .
mv $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.d/www.conf.default .
# install systemd unit files and scripts for handling server startup
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/systemd/system/php-fpm.service.d
install -Dm 644 %{SOURCE6}  $RPM_BUILD_ROOT%{_unitdir}/php-fpm.service
install -Dm 644 %{SOURCE12} $RPM_BUILD_ROOT%{_unitdir}/httpd.service.d/php-fpm.conf
install -Dm 644 %{SOURCE12} $RPM_BUILD_ROOT%{_unitdir}/nginx.service.d/php-fpm.conf
# LogRotate
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/php-fpm
# Nginx configuration
install -D -m 644 %{SOURCE13} $RPM_BUILD_ROOT%{_sysconfdir}/nginx/conf.d/php-fpm.conf
install -D -m 644 %{SOURCE14} $RPM_BUILD_ROOT%{_sysconfdir}/nginx/default.d/php.conf

TESTCMD="$RPM_BUILD_ROOT%{_bindir}/php --no-php-ini"
# Ensure all provided extensions are really there
for mod in core date filter hash json lexbor libxml openssl pcntl pcre random readline reflection session spl standard uri zlib
do
     $TESTCMD --modules | grep -qi $mod
done

TESTCMD="$TESTCMD --define extension_dir=$RPM_BUILD_ROOT%{_libdir}/php/modules"

# Generate files lists and stub .ini files for each subpackage
for mod in pgsql odbc ldap snmp \
    mysqlnd mysqli \
    mbstring gd dom xsl soap bcmath dba \
    simplexml bz2 calendar ctype exif ftp gettext gmp iconv \
    tokenizer opcache \
    sqlite3 \
    enchant phar fileinfo intl \
    ffi \
%if %{with tidy}
    tidy \
%endif
    curl \
%if %{with sodium}
    sodium \
%endif
    posix shmop sysvshm sysvsem sysvmsg xml \
    pdo pdo_mysql pdo pdo_pgsql pdo_odbc pdo_sqlite \
%if %{with firebird}
    pdo_firebird \
%endif
%if %{with freetds}
    pdo_dblib \
%endif
    xmlreader xmlwriter
do
    case $mod in
      opcache)
        # static extension
        ini=10-${mod}.ini;;
      pdo_*|mysqli|xmlreader)
        # Extensions with dependencies on 20-*
        TESTCMD="$TESTCMD --define extension=$mod"
        ini=30-${mod}.ini;;
      *)
        # Extensions with no dependency
        TESTCMD="$TESTCMD --define extension=$mod"
        ini=20-${mod}.ini;;
    esac

    $TESTCMD --modules | grep -qi $mod

    # some extensions have their own config file
    if [ -f ${ini} ]; then
      cp -p ${ini} $RPM_BUILD_ROOT%{_sysconfdir}/php.d/${ini}
%if %{with zts}
      cp -p ${ini} $RPM_BUILD_ROOT%{_sysconfdir}/php-zts.d/${ini}
%endif
    else
      cat > $RPM_BUILD_ROOT%{_sysconfdir}/php.d/${ini} <<EOF
; Enable ${mod} extension module
extension=${mod}
EOF
%if %{with zts}
      cat > $RPM_BUILD_ROOT%{_sysconfdir}/php-zts.d/${ini} <<EOF
; Enable ${mod} extension module
extension=${mod}
EOF
%endif
    fi
    cat > files.${mod} <<EOF
%{_libdir}/php/modules/${mod}.so
%config(noreplace) %{_sysconfdir}/php.d/${ini}
%if %{with zts}
%{_libdir}/php-zts/modules/${mod}.so
%config(noreplace) %{_sysconfdir}/php-zts.d/${ini}
%endif
EOF
done

# The dom, xsl and xml* modules are all packaged in php-xml
cat files.dom files.xsl files.xml{reader,writer} \
    files.simplexml >> files.xml

# mysqlnd
cat files.mysqli \
    files.pdo_mysql \
    >> files.mysqlnd

# Split out the PDO modules
cat files.pdo_pgsql >> files.pgsql
cat files.pdo_odbc >> files.odbc

# sysv* and posix in packaged in php-process
cat files.shmop files.sysv* files.posix > files.process

# Package sqlite3 and pdo_sqlite with pdo; isolating the sqlite dependency
# isn't useful at this time since rpm itself requires sqlite.
cat files.pdo_sqlite >> files.pdo
cat files.sqlite3 >> files.pdo

# Package curl, phar and fileinfo in -common.
cat files.curl files.phar files.fileinfo \
    files.exif files.gettext files.iconv files.calendar \
    files.ftp files.bz2 files.ctype \
    files.tokenizer > files.common

# The default Zend OPcache blacklist file
rm files.opcache
install -m 644 %{SOURCE51} $RPM_BUILD_ROOT%{_sysconfdir}/php.d/opcache-default.blacklist
%if %{with zts}
install -m 644 %{SOURCE51} $RPM_BUILD_ROOT%{_sysconfdir}/php-zts.d/opcache-default.blacklist
sed -e '/blacklist_filename/s/php.d/php-zts.d/' \
    -i $RPM_BUILD_ROOT%{_sysconfdir}/php-zts.d/10-opcache.ini
%endif

# Install the macros file:
sed -e "s/@PHP_APIVER@/%{apiver}-%{__isa_bits}/" \
    -e "s/@PHP_ZENDVER@/%{zendver}-%{__isa_bits}/" \
    -e "s/@PHP_PDOVER@/%{pdover}-%{__isa_bits}/" \
    -e "s/@PHP_VERSION@/%{upver}/" \
%if ! %{with zts}
    -e "/zts/d" \
%endif
    < %{SOURCE3} > macros.php
install -m 644 -D macros.php \
           $RPM_BUILD_ROOT%{_rpmmacrodir}/macros.php

# Remove unpackaged files
rm -rf $RPM_BUILD_ROOT%{_libdir}/php/modules/*.a \
       $RPM_BUILD_ROOT%{_libdir}/php-zts/modules/*.a \
       $RPM_BUILD_ROOT%{_bindir}/{phptar} \
       $RPM_BUILD_ROOT%{_datadir}/pear \
       $RPM_BUILD_ROOT%{_bindir}/zts-phar* \
       $RPM_BUILD_ROOT%{_mandir}/man1/zts-phar* \
       $RPM_BUILD_ROOT%{_libdir}/libphp.a \
       $RPM_BUILD_ROOT%{_libdir}/libphp.la

# Remove irrelevant docs
rm -f README.{Zeus,QNX,CVS-RULES}


%post fpm
%systemd_post php-fpm.service

%preun fpm
%systemd_preun php-fpm.service

# Raised by new pool installation or new extension installation
%transfiletriggerin fpm -- %{_sysconfdir}/php-fpm.d %{_sysconfdir}/php.d
systemctl try-restart php-fpm.service >/dev/null 2>&1 || :


%files
%if %{with modphp}
%{_httpd_moddir}/libphp.so
%config(noreplace) %{_httpd_modconfdir}/20-php.conf
%attr(0770,root,apache) %dir %{_sharedstatedir}/php/session
%attr(0770,root,apache) %dir %{_sharedstatedir}/php/wsdlcache
%attr(0770,root,apache) %dir %{_sharedstatedir}/php/opcache
%config(noreplace) %{_httpd_confdir}/php.conf
%{_tmpfilesdir}/php.conf
%endif

%files common -f files.common
%doc EXTENSIONS NEWS UPGRADING* README.REDIST.BINS *md docs
%license LICENSE TSRM_LICENSE ZEND_LICENSE BOOST_LICENSE
%license libmagic_LICENSE
%license timelib_LICENSE
%doc php.ini-*
%config(noreplace) %{_sysconfdir}/php.ini
%config(noreplace) %{_sysconfdir}/php.d/10-opcache.ini
%config(noreplace) %{_sysconfdir}/php.d/opcache-default.blacklist
%dir %{_sysconfdir}/php.d
%dir %{_libdir}/php
%dir %{_libdir}/php/modules
%if %{with zts}
%config(noreplace) %{_sysconfdir}/php-zts.d/opcache-default.blacklist
%dir %{_sysconfdir}/php-zts.d
%dir %{_libdir}/php-zts
%dir %{_libdir}/php-zts/modules
%endif
%dir %{_sharedstatedir}/php
%dir %{_sharedstatedir}/php/peclxml
%dir %{_datadir}/php
%dir %{_docdir}/pecl
%dir %{_datadir}/tests
%dir %{_datadir}/tests/pecl

%files cli
%{_bindir}/php
%if %{with zts}
%{_bindir}/zts-php
%{_mandir}/man1/zts-php.1*
%endif
%{_bindir}/php-cgi
%{_bindir}/phar.phar
%{_bindir}/phar
# provides phpize here (not in -devel) for pecl command
%{_bindir}/phpize
%{_mandir}/man1/php.1*
%{_mandir}/man1/php-cgi.1*
%{_mandir}/man1/phar.1*
%{_mandir}/man1/phar.phar.1*
%{_mandir}/man1/phpize.1*

%files dbg
%doc sapi/phpdbg/CREDITS
%{_bindir}/phpdbg
%{_mandir}/man1/phpdbg.1*
%if %{with zts}
%{_bindir}/zts-phpdbg
%{_mandir}/man1/zts-phpdbg.1*
%endif

%files fpm
%doc php-fpm.conf.default www.conf.default
%license fpm_LICENSE
%attr(0770,root,apache) %dir %{_sharedstatedir}/php/session
%attr(0770,root,apache) %dir %{_sharedstatedir}/php/wsdlcache
%attr(0770,root,apache) %dir %{_sharedstatedir}/php/opcache
%config(noreplace) %{_httpd_confdir}/php.conf
%config(noreplace) %{_sysconfdir}/php-fpm.conf
%config(noreplace) %{_sysconfdir}/php-fpm.d/www.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/php-fpm
%config(noreplace) %{_sysconfdir}/nginx/conf.d/php-fpm.conf
%config(noreplace) %{_sysconfdir}/nginx/default.d/php.conf
%{_unitdir}/php-fpm.service
%{_unitdir}/httpd.service.d/php-fpm.conf
%{_unitdir}/nginx.service.d/php-fpm.conf
%{_sbindir}/php-fpm
%dir %{_sysconfdir}/systemd/system/php-fpm.service.d
%dir %{_sysconfdir}/php-fpm.d
# log owned by apache for log
%attr(770,apache,root) %dir %{_localstatedir}/log/php-fpm
%dir %ghost /run/php-fpm
%{_mandir}/man8/php-fpm.8*
%dir %{_datadir}/php/fpm
%{_datadir}/php/fpm/status.html
%{_tmpfilesdir}/php.conf

%files devel
%{_bindir}/php-config
%{_includedir}/php
%{_libdir}/php/build
%if %{with zts}
%{_bindir}/zts-php-config
%{_bindir}/zts-phpize
%{_includedir}/php-zts
%{_libdir}/php-zts/build
%{_mandir}/man1/zts-php-config.1*
%{_mandir}/man1/zts-phpize.1*
%endif
%{_mandir}/man1/php-config.1*
%{_rpmmacrodir}/macros.php

%files embedded
%{_libdir}/libphp.so
%{_libdir}/libphp-%{major_version}.so

%files pgsql -f files.pgsql
%files odbc -f files.odbc
%files ldap -f files.ldap
%files snmp -f files.snmp
%files xml -f files.xml
%files mbstring -f files.mbstring
%license libmbfl_LICENSE
%files gd -f files.gd
%files soap -f files.soap
%files bcmath -f files.bcmath
%license libbcmath_LICENSE
%files gmp -f files.gmp
%files dba -f files.dba
%files pdo -f files.pdo
%if %{with tidy}
%files tidy -f files.tidy
%endif
%if %{with freetds}
%files pdo-dblib -f files.pdo_dblib
%endif
%files intl -f files.intl
%files process -f files.process
%if %{with firebird}
%files pdo-firebird -f files.pdo_firebird
%endif
%files enchant -f files.enchant
%files mysqlnd -f files.mysqlnd
%if %{with sodium}
%files sodium -f files.sodium
%endif
%files ffi -f files.ffi
%dir %{_datadir}/php/preload


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{upver}%{?rcver:~%{rcver}}-1
- Prepare for Oreon 11 (RP1)
