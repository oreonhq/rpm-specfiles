%define contentdir %{_datadir}/httpd
%define docroot /var/www
%define suexec_caller apache
%define mmn 20120211
%define mmnisa %{mmn}%{__isa_name}%{__isa_bits}
%define vstring %(source /etc/os-release; echo ${NAME})
%define bugurl %(source /etc/os-release; echo ${BUG_REPORT_URL})
%if 0%{?fedora} > 26 || 0%{?rhel} > 7
%global mpm event
%else
%global mpm prefork
%endif

%bcond pcre2 %[0%{?fedora} > 35 || 0%{?rhel} > 9]
%bcond pcre %{without pcre2}
%bcond engine %[0%{?fedora} < 41 && 0%{?rhel} < 10]
%bcond worker %[0%{?fedora} < 44 && 0%{?rhel} < 11]

%if %{with worker}
%global mpms event prefork worker
%else
%global mpms event prefork
%endif

# Similar issue to https://bugzilla.redhat.com/show_bug.cgi?id=2043092
%undefine _package_note_flags

Summary: Apache HTTP Server
Name: httpd
Version: 2.4.66
Release: 5%{?dist}
URL: https://httpd.apache.org/
Source0: https://www.apache.org/dist/httpd/httpd-%{version}.tar.bz2
Source1: https://www.apache.org/dist/httpd/httpd-%{version}.tar.bz2.asc
# gpg key file downloaded and verified by luhliarik
# https://httpd.apache.org/dev/verification.html
Source2: https://dist.apache.org/repos/dist/release/httpd/KEYS
Source3: httpd.logrotate
Source4: instance.conf
Source5: httpd-ssl-pass-dialog
Source6: httpd.tmpfiles
Source7: httpd.service
Source8: action-graceful.sh
Source9: action-configtest.sh
Source10: server-status.conf
Source11: httpd.conf
Source12: 00-base.conf
Source13: 00-mpm.conf
Source14: 00-lua.conf
Source15: 01-cgi.conf
Source16: 00-dav.conf
Source17: 00-proxy.conf
Source18: 00-ssl.conf
Source19: 01-ldap.conf
Source20: 00-proxyhtml.conf
Source21: userdir.conf
Source22: ssl.conf
Source23: welcome.conf
Source24: manual.conf
Source25: 00-systemd.conf
Source26: 01-session.conf
Source27: 10-listen443.conf
Source28: httpd.socket
Source29: 00-optional.conf
Source30: README.confd
Source31: README.confmod
Source32: httpd.service.xml
Source33: htcacheclean.service.xml
Source34: httpd.conf.xml
Source35: 00-brotli.conf
Source40: htcacheclean.service
Source41: htcacheclean.sysconf
Source42: httpd-init.service
Source43: httpd-ssl-gencerts
Source44: httpd@.service
Source45: config.layout
Source46: apachectl.sh
Source47: apachectl.xml
Source48: apache-poweredby.png
Source49: httpd.sysusers

# build/scripts patches
Patch2: httpd-2.4.43-apxs.patch
Patch3: httpd-2.4.43-deplibs.patch
# Needed for socket activation and mod_systemd patch
Patch19: httpd-2.4.53-detect-systemd.patch
# Features/functional changes
Patch20: httpd-2.4.48-r1842929+.patch
Patch21: httpd-2.4.64-mod_systemd.patch
Patch22: httpd-2.4.53-export.patch
Patch23: httpd-2.4.43-corelimit.patch
Patch24: httpd-2.4.66-autoindex.patch
Patch25: httpd-2.4.43-cachehardmax.patch
Patch26: httpd-2.4.43-sslciphdefault.patch
Patch27: httpd-2.4.64-sslprotdefault.patch
Patch28: httpd-2.4.43-logjournal.patch
Patch29: httpd-2.4.63-r1912477+.patch
Patch30: httpd-2.4.64-separate-systemd-fns.patch

# Bug fixes
# https://bugzilla.redhat.com/show_bug.cgi?id=1397243
Patch60: httpd-2.4.43-enable-sslv3.patch
Patch61: httpd-2.4.65-hcheck-stuck.patch

# Security fixes
# Patch200: ...

# Apache-2.0: everything
# BSD-3-Clause: util_pcre.c, ap_regex.h
# metamail AND HPND-sell-variant:: server/util_md5.c:
# Spencer-94: modules/metadata/mod_mime_magic.c
License: Apache-2.0 AND (BSD-3-Clause AND metamail AND HPND-sell-variant AND Spencer-94)

BuildRequires: gcc, autoconf, pkgconfig, findutils, xmlto
BuildRequires: perl-interpreter, perl-generators, systemd-devel
BuildRequires: zlib-devel, libselinux-devel, lua-devel, brotli-devel
BuildRequires: apr-devel >= 1.5.0, apr-util-devel >= 1.5.0
BuildRequires: openldap-devel
BuildRequires: systemd-rpm-macros
BuildRequires: libxcrypt-devel
%if %{with pcre2}
BuildRequires: pcre2-devel
%endif
%if %{with pcre}
BuildRequires: pcre-devel > 5.0
%endif
BuildRequires: gnupg2
Requires: system-logos(httpd-logo-ng)
Provides: webserver
Requires: httpd-core = 0:%{version}-%{release}
Recommends: mod_http2, mod_lua
%{?systemd_requires}

%description
The Apache HTTP Server is a powerful, efficient, and extensible
web server.

%package core
Summary: httpd minimal core
Provides: mod_dav = %{version}-%{release}, httpd-suexec = %{version}-%{release}
Provides: httpd-mmn = %{mmn}, httpd-mmn = %{mmnisa}
Provides: mod_proxy_uwsgi = %{version}-%{release}
Requires: /etc/mime.types
Requires: httpd-tools = %{version}-%{release}
Requires: httpd-filesystem = %{version}-%{release}
%if 0%{?fedora} > 39 || 0%{?rhel} > 9
Requires: apr-util-1(dbm)%{_isa}
%endif
Requires(pre): httpd-filesystem
Conflicts: apr < 1.5.0-1
Conflicts: httpd < 2.4.53-2
Obsoletes: mod_proxy_uwsgi < 2.0.17.1-2

# Compat symlinks for Requires in other packages.
%if "%{_sbindir}" == "%{_bindir}"
# We rely on filesystem to create the symlink for us.
Requires:           filesystem(unmerged-sbin-symlinks)
Provides:           /usr/sbin/apachectl
Provides:           /usr/sbin/httpd
%endif

%description core
The httpd-core package contains essential httpd binaries.

%package devel
Summary: Development interfaces for the Apache HTTP Server
Requires: apr-devel, apr-util-devel, pkgconfig, libtool
Requires: httpd-core = 0:%{version}-%{release}

%description devel
The httpd-devel package contains the APXS binary and other files
that you need to build Dynamic Shared Objects (DSOs) for the
Apache HTTP Server.

If you are installing the Apache HTTP Server and you want to be
able to compile or develop additional modules for Apache, you need
to install this package.

%package manual
Summary: Documentation for the Apache HTTP Server
Requires: httpd-core = 0:%{version}-%{release}
BuildArch: noarch

%description manual
The httpd-manual package contains the complete manual and
reference guide for the Apache HTTP Server. The information can
also be found at https://httpd.apache.org/docs/2.4/.

%package filesystem
Summary: The basic directory layout for the Apache HTTP Server
BuildArch: noarch
%{?sysusers_requires_compat}

%description filesystem
The httpd-filesystem package contains the basic directory layout
for the Apache HTTP Server including the correct permissions
for the directories.

%package tools
Summary: Tools for use with the Apache HTTP Server

%description tools
The httpd-tools package contains tools which can be used with 
the Apache HTTP Server.

%package -n mod_ssl
Summary: SSL/TLS module for the Apache HTTP Server
Epoch: 1
BuildRequires: openssl-devel
Requires(pre): httpd-filesystem
Requires: httpd-core = 0:%{version}-%{release}, httpd-mmn = %{mmnisa}
Requires: sscg >= 3.0.3, /usr/bin/hostname
# Require an OpenSSL which supports PROFILE=SYSTEM
Conflicts: openssl-libs < 1:1.0.1h-4
# mod_ssl/mod_nss cannot both be loaded simultaneously
Conflicts: mod_nss

%description -n mod_ssl
The mod_ssl module provides strong cryptography for the Apache HTTP
server via the Secure Sockets Layer (SSL) and Transport Layer
Security (TLS) protocols.

%package -n mod_proxy_html
Summary: HTML and XML content filters for the Apache HTTP Server
Requires: httpd-core = 0:%{version}-%{release}, httpd-mmn = %{mmnisa}
BuildRequires: libxml2-devel
BuildRequires: make
Epoch: 1
Obsoletes: mod_proxy_html < 1:2.4.1-2

%description -n mod_proxy_html
The mod_proxy_html and mod_xml2enc modules provide filters which can
transform and modify HTML and XML content.

%package -n mod_ldap
Summary: LDAP authentication modules for the Apache HTTP Server
Requires: httpd-core = 0:%{version}-%{release}, httpd-mmn = %{mmnisa}
Requires: apr-util-ldap

%description -n mod_ldap
The mod_ldap and mod_authnz_ldap modules add support for LDAP
authentication to the Apache HTTP Server.

%package -n mod_session
Summary: Session interface for the Apache HTTP Server
Requires: httpd-core = 0:%{version}-%{release}, httpd-mmn = %{mmnisa}

%description -n mod_session
The mod_session module and associated backends provide an abstract
interface for storing and accessing per-user session data.

%package -n mod_lua
Summary: Lua scripting support for the Apache HTTP Server
Requires: httpd-core = 0:%{version}-%{release}, httpd-mmn = %{mmnisa}

%description -n mod_lua
The mod_lua module allows the server to be extended with scripts
written in the Lua programming language.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -S gendiff

# Patch in the vendor string
sed -i '/^#define PLATFORM/s/Unix/%{vstring}/' os/unix/os.h

# Prevent use of setcap in "install-suexec-caps" target.
sed -i '/suexec/s,setcap ,echo Skipping setcap for ,' Makefile.in

%if %{without engine}
: Forcibly disable ENGINE support in mod_ssl
sed -i.engine '/^#define MODSSL_HAVE_ENGINE_API/{s/1/0/}' modules/ssl/ssl_private.h
! diff -u modules/ssl/ssl_private.h{.engine,}
%endif

# Example conf for instances
cp $RPM_SOURCE_DIR/instance.conf .
sed < $RPM_SOURCE_DIR/httpd.conf >> instance.conf '
0,/^ServerRoot/d;
/# Supplemental configuration/,$d
/^ *CustomLog .logs/s,logs/,logs/${HTTPD_INSTANCE}_,
/^ *ErrorLog .logs/s,logs/,logs/${HTTPD_INSTANCE}_,
'
touch -r $RPM_SOURCE_DIR/instance.conf instance.conf
cp -p $RPM_SOURCE_DIR/server-status.conf server-status.conf

# Safety check: prevent build if defined MMN does not equal upstream MMN.
vmmn=`echo MODULE_MAGIC_NUMBER_MAJOR | cpp -include include/ap_mmn.h | sed -n '/^2/p'`
if test "x${vmmn}" != "x%{mmn}"; then
   : Error: Upstream MMN is now ${vmmn}, packaged MMN is %{mmn}
   : Update the mmn macro and rebuild.
   exit 1
fi

# A new logo which comes together with a new test page
cp %{SOURCE48} ./docs/icons/apache_pb3.png

# Provide default layout
cp $RPM_SOURCE_DIR/config.layout .

for f in httpd.conf htcacheclean.service httpd.service apachectl; do
   sed '
s,@MPM@,%{mpm},g
s,@DOCROOT@,%{docroot},g
s,@LOGDIR@,%{_localstatedir}/log/httpd,g
s|@BUG_REPORT_URL@|%{bugurl}|g
' < $RPM_SOURCE_DIR/${f}.xml > ${f}.xml
   xmlto man ${f}.xml
done

sed '/^#LoadModule mpm_%{mpm}_module /s/^#//' > 00-mpm.conf < \
    $RPM_SOURCE_DIR/00-mpm.conf
# Remove worker MPM LoadModule from 00-mpm.conf if not built
if echo %{mpms} | grep -q -v worker; then
    sed -i '/^. worker MPM/,/LoadModule mpm_worker/d' 00-mpm.conf
fi
touch -r $RPM_SOURCE_DIR/00-mpm.conf 00-mpm.conf

: Building with MMN %{mmn}, MMN-ISA %{mmnisa}
: Default MPM is %{mpm}, MPM list: %{mpms}
: Vendor string is '%{vstring}'
: Regex Engine: PCRE=%{with pcre} PCRE2=%{with pcre2}
: mod_ssl ENGINE support: %{with engine}

%build
# forcibly prevent use of bundled apr, apr-util, pcre
rm -rf srclib/{apr,apr-util,pcre}

# regenerate configure scripts
autoheader && autoconf || exit 1

# Before configure; fix location of build dir in generated apxs
%{__perl} -pi -e "s:\@exp_installbuilddir\@:%{_libdir}/httpd/build:g" \
        support/apxs.in

%set_build_flags

# Build the daemon
./configure \
        --prefix=%{_sysconfdir}/httpd \
        --exec-prefix=%{_prefix} \
        --bindir=%{_bindir} \
        --sbindir=%{_sbindir} \
        --mandir=%{_mandir} \
        --libdir=%{_libdir} \
        --sysconfdir=%{_sysconfdir}/httpd/conf \
        --includedir=%{_includedir}/httpd \
        --libexecdir=%{_libdir}/httpd/modules \
        --datadir=%{contentdir} \
        --enable-layout=Fedora \
        --with-installbuilddir=%{_libdir}/httpd/build \
        --enable-mpms-shared="%{mpms}" \
        --with-apr=%{_prefix} --with-apr-util=%{_prefix} \
        --enable-suexec --with-suexec \
        --enable-suexec-capabilities \
        --with-suexec-caller=%{suexec_caller} \
        --with-suexec-docroot=%{docroot} \
        --without-suexec-logfile \
        --with-suexec-syslog \
        --with-suexec-bin=%{_sbindir}/suexec \
        --with-suexec-uidmin=1000 --with-suexec-gidmin=1000 \
        --with-brotli \
        --enable-pie \
%if %{with pcre2}
        --with-pcre2=%{_bindir}/pcre2-config \
%endif
%if %{with pcre}
        --with-pcre=%{_bindir}/pcre-config \
%endif
        --enable-mods-shared=all \
        --enable-ssl --with-ssl --disable-distcache \
        --enable-proxy --enable-proxy-fdpass \
        --enable-cache \
        --enable-disk-cache \
        --enable-ldap --enable-authnz-ldap \
        --enable-cgid --enable-cgi --enable-authnz-fcgi \
        --enable-cgid-fdpassing \
        --enable-authn-anon --enable-authn-alias \
        --enable-systemd \
        --disable-imagemap --disable-file-cache \
        --disable-http2 \
        --disable-md \
        $*

if grep -q ac_cv_have_threadsafe_pollset=no config.log; then
   cat config.log
   : Failed to find thread-safe APR.
   exit 1
fi

%make_build

%install
rm -rf $RPM_BUILD_ROOT

%make_install

# Install systemd service files
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
for s in httpd.service htcacheclean.service httpd.socket \
         httpd@.service httpd-init.service; do
  install -p -m 644 $RPM_SOURCE_DIR/${s} \
                    $RPM_BUILD_ROOT%{_unitdir}/${s}
done

# install conf file/directory
mkdir $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d \
      $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.modules.d
install -m 644 $RPM_SOURCE_DIR/README.confd \
    $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/README
install -m 644 $RPM_SOURCE_DIR/README.confmod \
    $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.modules.d/README
for f in 00-base.conf 00-mpm.conf 00-lua.conf 01-cgi.conf 00-dav.conf \
         00-proxy.conf 00-ssl.conf 01-ldap.conf 00-proxyhtml.conf \
         01-ldap.conf 00-systemd.conf 01-session.conf 00-optional.conf \
         00-brotli.conf; do
  install -m 644 -p $RPM_SOURCE_DIR/$f \
        $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.modules.d/$f
done

install -m 644 -p 00-mpm.conf \
        $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.modules.d/00-mpm.conf

# install systemd override drop directory
# Web application packages can drop snippets into this location if
# they need ExecStart[pre|post].
mkdir $RPM_BUILD_ROOT%{_unitdir}/httpd.service.d \
      $RPM_BUILD_ROOT%{_unitdir}/httpd.socket.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/systemd/system/httpd.service.d

install -m 644 -p $RPM_SOURCE_DIR/10-listen443.conf \
      $RPM_BUILD_ROOT%{_unitdir}/httpd.socket.d/10-listen443.conf

for f in welcome.conf ssl.conf manual.conf userdir.conf; do
  install -m 644 -p $RPM_SOURCE_DIR/$f \
        $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/$f
done

# Split-out extra config shipped as default in conf.d:
for f in autoindex; do
  install -m 644 docs/conf/extra/httpd-${f}.conf \
        $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/${f}.conf
done

# Extra config trimmed:
rm -v docs/conf/extra/httpd-{ssl,userdir}.conf

rm $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf/*.conf
install -m 644 -p $RPM_SOURCE_DIR/httpd.conf \
   $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf/httpd.conf

mkdir $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m 644 -p $RPM_SOURCE_DIR/htcacheclean.sysconf \
   $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/htcacheclean

# tmpfiles.d configuration
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d 
install -m 644 -p $RPM_SOURCE_DIR/httpd.tmpfiles \
   $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/httpd.conf

# Other directories
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/httpd \
         $RPM_BUILD_ROOT/run/httpd/htcacheclean

# Substitute in defaults which are usually done (badly) by "make install"
sed -i \
   "/^DavLockDB/d;
    s,@@ServerRoot@@/user.passwd,/etc/httpd/conf/user.passwd,;
    s,@@ServerRoot@@/docs,%{docroot},;
    s,@@ServerRoot@@,%{docroot},;
    s,@@Port@@,80,;" \
    docs/conf/extra/*.conf

# Set correct path for httpd binary in apachectl script
sed 's,@HTTPDBIN@,%{_sbindir}/httpd,g' $RPM_SOURCE_DIR/apachectl.sh \
    > apachectl.sh

# Create cache directory
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cache/httpd \
         $RPM_BUILD_ROOT%{_localstatedir}/cache/httpd/proxy \
         $RPM_BUILD_ROOT%{_localstatedir}/cache/httpd/ssl

# Make the MMN accessible to module packages
echo %{mmnisa} > $RPM_BUILD_ROOT%{_includedir}/httpd/.mmn
mkdir -p $RPM_BUILD_ROOT%{_rpmconfigdir}/macros.d
cat > $RPM_BUILD_ROOT%{_rpmconfigdir}/macros.d/macros.httpd <<EOF
%%_httpd_mmn %{mmnisa}
%%_httpd_apxs %%{_libdir}/httpd/build/vendor-apxs
%%_httpd_modconfdir %%{_sysconfdir}/httpd/conf.modules.d
%%_httpd_confdir %%{_sysconfdir}/httpd/conf.d
%%_httpd_contentdir %{contentdir}
%%_httpd_moddir %%{_libdir}/httpd/modules
%%_httpd_requires Requires: httpd-mmn = %%{_httpd_mmn}
%%_httpd_statedir %%{_localstatedir}/lib/httpd
EOF

# Handle contentdir
mkdir $RPM_BUILD_ROOT%{contentdir}/noindex \
      $RPM_BUILD_ROOT%{contentdir}/server-status
ln -s ../../testpage/index.html \
      $RPM_BUILD_ROOT%{contentdir}/noindex/index.html
install -m 644 -p docs/server-status/* \
        $RPM_BUILD_ROOT%{contentdir}/server-status
rm -rf %{contentdir}/htdocs

# remove manual sources
find $RPM_BUILD_ROOT%{contentdir}/manual \( \
    -name \*.xml -o -name \*.xml.* -o -name \*.ent -o -name \*.xsl -o -name \*.dtd \
    \) -print0 | xargs -0 rm -f

# Strip the manual down just to English and replace the typemaps with flat files:
set +x
for f in `find $RPM_BUILD_ROOT%{contentdir}/manual -name \*.html -type f`; do
   if test -f ${f}.en; then
      cp ${f}.en ${f}
      rm ${f}.*
   fi
done
set -x

# Clean Document Root
rm -v $RPM_BUILD_ROOT%{docroot}/html/*.html \
      $RPM_BUILD_ROOT%{docroot}/cgi-bin/*

# Symlink for the powered-by-$DISTRO image:
ln -s ../../pixmaps/poweredby.png \
        $RPM_BUILD_ROOT%{contentdir}/icons/poweredby.png

# Symlink for the system logo
%if 0%{?rhel} >= 9
ln -s ../../pixmaps/system-noindex-logo.png \
        $RPM_BUILD_ROOT%{contentdir}/icons/system_noindex_logo.png
%endif

# symlinks for /etc/httpd
rmdir $RPM_BUILD_ROOT/etc/httpd/{state,run}
ln -s ../..%{_localstatedir}/log/httpd $RPM_BUILD_ROOT/etc/httpd/logs
ln -s ../..%{_localstatedir}/lib/httpd $RPM_BUILD_ROOT/etc/httpd/state
ln -s /run/httpd $RPM_BUILD_ROOT/etc/httpd/run
ln -s ../..%{_libdir}/httpd/modules $RPM_BUILD_ROOT/etc/httpd/modules

# install http-ssl-pass-dialog
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
install -m755 $RPM_SOURCE_DIR/httpd-ssl-pass-dialog \
        $RPM_BUILD_ROOT%{_libexecdir}/httpd-ssl-pass-dialog

# install http-ssl-gencerts
install -m755 $RPM_SOURCE_DIR/httpd-ssl-gencerts \
        $RPM_BUILD_ROOT%{_libexecdir}/httpd-ssl-gencerts

# Install scripts
install -m 755 apachectl.sh $RPM_BUILD_ROOT%{_sbindir}/apachectl
touch -r $RPM_SOURCE_DIR/apachectl.sh $RPM_BUILD_ROOT%{_sbindir}/apachectl
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/initscripts/legacy-actions/httpd
for f in graceful configtest; do
    install -p -m 755 $RPM_SOURCE_DIR/action-${f}.sh \
            $RPM_BUILD_ROOT%{_libexecdir}/initscripts/legacy-actions/httpd/${f}
done

# Install logrotate config
mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d
install -m 644 -p $RPM_SOURCE_DIR/httpd.logrotate \
        $RPM_BUILD_ROOT/etc/logrotate.d/httpd

# Install man pages
install -d $RPM_BUILD_ROOT%{_mandir}/man8 $RPM_BUILD_ROOT%{_mandir}/man5
install -m 644 -p httpd.service.8 httpd-init.service.8 httpd.socket.8 \
        httpd@.service.8 htcacheclean.service.8 apachectl.8 \
        $RPM_BUILD_ROOT%{_mandir}/man8
install -m 644 -p httpd.conf.5 \
        $RPM_BUILD_ROOT%{_mandir}/man5

# fix man page paths
sed -e "s|/usr/local/apache2/conf/httpd.conf|/etc/httpd/conf/httpd.conf|" \
    -e "s|/usr/local/apache2/conf/mime.types|/etc/mime.types|" \
    -e "s|/usr/local/apache2/conf/magic|/etc/httpd/conf/magic|" \
    -e "s|/usr/local/apache2/logs/error_log|/var/log/httpd/error_log|" \
    -e "s|/usr/local/apache2/logs/access_log|/var/log/httpd/access_log|" \
    -e "s|/usr/local/apache2/logs/httpd.pid|/run/httpd/httpd.pid|" \
    -e "s|/usr/local/apache2|/etc/httpd|" < docs/man/httpd.8 \
  > $RPM_BUILD_ROOT%{_mandir}/man8/httpd.8

# Make ap_config_layout.h libdir-agnostic
sed -i '/.*DEFAULT_..._LIBEXECDIR/d;/DEFAULT_..._INSTALLBUILDDIR/d' \
    $RPM_BUILD_ROOT%{_includedir}/httpd/ap_config_layout.h

# Fix path to instdso in special.mk
sed -i '/instdso/s,top_srcdir,top_builddir,' \
    $RPM_BUILD_ROOT%{_libdir}/httpd/build/special.mk

# vendor-apxs uses an unsanitized config_vars.mk which may
# have dependencies on redhat-rpm-config.  apxs uses the
# config_vars.mk with a sanitized config_vars.mk
cp -p $RPM_BUILD_ROOT%{_libdir}/httpd/build/config_vars.mk \
      $RPM_BUILD_ROOT%{_libdir}/httpd/build/vendor_config_vars.mk

# Sanitize CFLAGS & LIBTOOL in standard config_vars.mk
sed -e '/^[A-Z]*FLAGS = /s,-specs[^ ]*,,g' \
    -e '/^LIBTOOL/s,/.*/libtool,%{_bindir}/libtool,' \
    -i $RPM_BUILD_ROOT%{_libdir}/httpd/build/config_vars.mk
diff -u $RPM_BUILD_ROOT%{_libdir}/httpd/build/vendor_config_vars.mk \
     $RPM_BUILD_ROOT%{_libdir}/httpd/build/config_vars.mk || true

sed 's/config_vars.mk/vendor_config_vars.mk/' \
    $RPM_BUILD_ROOT%{_bindir}/apxs \
    > $RPM_BUILD_ROOT%{_libdir}/httpd/build/vendor-apxs
touch -r $RPM_BUILD_ROOT%{_bindir}/apxs \
      $RPM_BUILD_ROOT%{_libdir}/httpd/build/vendor-apxs
chmod 755 $RPM_BUILD_ROOT%{_libdir}/httpd/build/vendor-apxs

# Fix content dir in sysusers file and install it
install -p -D -m 0644 %{SOURCE49} %{buildroot}%{_sysusersdir}/httpd.conf

# Remove unpackaged files
rm -vf \
      $RPM_BUILD_ROOT%{_libdir}/*.exp \
      $RPM_BUILD_ROOT/etc/httpd/conf/mime.types \
      $RPM_BUILD_ROOT%{_libdir}/httpd/modules/*.exp \
      $RPM_BUILD_ROOT%{_libdir}/httpd/build/config.nice \
      $RPM_BUILD_ROOT%{_bindir}/{ap?-config,dbmmanage} \
      $RPM_BUILD_ROOT%{_sbindir}/{checkgid,envvars*} \
      $RPM_BUILD_ROOT%{contentdir}/htdocs/* \
      $RPM_BUILD_ROOT%{_mandir}/man1/dbmmanage.* \
      $RPM_BUILD_ROOT%{contentdir}/cgi-bin/*

rm -rf $RPM_BUILD_ROOT/etc/httpd/conf/{original,extra}

%pre filesystem
%sysusers_create_compat %{SOURCE49}

%post
%systemd_post httpd.service htcacheclean.service httpd.socket

%preun
%systemd_preun httpd.service htcacheclean.service httpd.socket

%postun
%systemd_postun httpd.service htcacheclean.service httpd.socket

%posttrans
test -f /etc/sysconfig/httpd-disable-posttrans || \
  /bin/systemctl try-restart --no-block httpd.service htcacheclean.service >/dev/null 2>&1 || :

%check
make -C server exports.o
nm --defined httpd > exports-actual.list
set +x
rv=0
nm --defined-only server/exports.o | \
  sed -n '/ap_hack_/{s/.* ap_hack_//;/^ap[ru]/d;p;}' | \
  while read sym; do
    if ! grep -q " "$sym\$ exports-actual.list; then
     echo ERROR: Symbol $sym missing in httpd exports
     rv=1
    fi
  done
if [ $rv -eq 0 ]; then
  echo PASS: Symbol export list verified.
fi
# Check the built modules are all PIC
if readelf -d $RPM_BUILD_ROOT%{_libdir}/httpd/modules/*.so | grep TEXTREL; then
   echo FAIL: Modules contain non-relocatable code
   rv=1
else
   echo PASS: No non-relocatable code in module builds
fi
# Ensure every mod_* that's built is loaded.
for f in $RPM_BUILD_ROOT%{_libdir}/httpd/modules/*.so; do
  m=${f##*/}
  if ! grep -q $m $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.modules.d/*.conf; then
    echo FAIL: Module $m not configured.  Disable it, or load it.
    rv=1
   else
    echo PASS: Module $m is configured and loaded.
  fi
done
# Ensure every mod_* referenced from a LoadModule is actually built
mods=`grep -Eh '^.?LoadModule' $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.modules.d/*.conf | sed 's,.*modules/,,'`
for m in $mods; do
  f=$RPM_BUILD_ROOT%{_libdir}/httpd/modules/${m}
  if ! test -x $f; then
    echo FAIL: Module $m is configured but not built.
    rv=1
  else
    echo PASS: Loaded module $m is installed.
  fi
done
set -x
exit $rv

%files
%{_mandir}/man8/*
%{_mandir}/man5/*
%exclude %{_mandir}/man8/httpd-init.*

%config(noreplace) %{_sysconfdir}/httpd/conf.modules.d/00-brotli.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.modules.d/00-systemd.conf
%{_libdir}/httpd/modules/mod_brotli.so
%{_libdir}/httpd/modules/mod_systemd.so

%{_unitdir}/httpd.service
%{_unitdir}/httpd@.service
%{_unitdir}/htcacheclean.service
%{_unitdir}/*.socket

%files core
%doc ABOUT_APACHE README CHANGES LICENSE VERSIONING NOTICE
%doc docs/conf/extra/*.conf
%doc instance.conf server-status.conf

%{_sysconfdir}/httpd/modules
%{_sysconfdir}/httpd/logs
%{_sysconfdir}/httpd/state
%{_sysconfdir}/httpd/run
%dir %{_sysconfdir}/httpd/conf

%config(noreplace) %{_sysconfdir}/httpd/conf/httpd.conf
%config(noreplace) %{_sysconfdir}/httpd/conf/magic

%config(noreplace) %{_sysconfdir}/logrotate.d/httpd

%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf
%exclude %{_sysconfdir}/httpd/conf.d/ssl.conf
%exclude %{_sysconfdir}/httpd/conf.d/manual.conf

%dir %{_sysconfdir}/httpd/conf.modules.d
%{_sysconfdir}/httpd/conf.modules.d/README

%config(noreplace) %{_sysconfdir}/httpd/conf.modules.d/*.conf
%exclude %{_sysconfdir}/httpd/conf.modules.d/00-brotli.conf
%exclude %{_sysconfdir}/httpd/conf.modules.d/00-systemd.conf
%exclude %{_sysconfdir}/httpd/conf.modules.d/00-ssl.conf
%exclude %{_sysconfdir}/httpd/conf.modules.d/00-proxyhtml.conf
%exclude %{_sysconfdir}/httpd/conf.modules.d/00-lua.conf
%exclude %{_sysconfdir}/httpd/conf.modules.d/01-ldap.conf
%exclude %{_sysconfdir}/httpd/conf.modules.d/01-session.conf

%config(noreplace) %{_sysconfdir}/sysconfig/htcacheclean
%{_prefix}/lib/tmpfiles.d/httpd.conf

%dir %{_libexecdir}/initscripts/legacy-actions/httpd
%{_libexecdir}/initscripts/legacy-actions/httpd/*

%{_sbindir}/httpd
%{_sbindir}/htcacheclean
%{_sbindir}/fcgistarter
%{_sbindir}/apachectl
%{_sbindir}/rotatelogs
%caps(cap_setuid,cap_setgid+pe) %attr(510,root,%{suexec_caller}) %{_sbindir}/suexec

%dir %{_libdir}/httpd
%dir %{_libdir}/httpd/modules
%{_libdir}/httpd/modules/mod*.so
%exclude %{_libdir}/httpd/modules/mod_brotli.so
%exclude %{_libdir}/httpd/modules/mod_systemd.so
%exclude %{_libdir}/httpd/modules/mod_auth_form.so
%exclude %{_libdir}/httpd/modules/mod_ssl.so
%exclude %{_libdir}/httpd/modules/mod_*ldap.so
%exclude %{_libdir}/httpd/modules/mod_proxy_html.so
%exclude %{_libdir}/httpd/modules/mod_xml2enc.so
%exclude %{_libdir}/httpd/modules/mod_session*.so
%exclude %{_libdir}/httpd/modules/mod_lua.so

%dir %{contentdir}/error
%dir %{contentdir}/error/include
%dir %{contentdir}/noindex
%dir %{contentdir}/server-status
%{contentdir}/icons/*
%{contentdir}/error/README
%{contentdir}/error/*.var
%{contentdir}/error/include/*.html
%{contentdir}/noindex/index.html
%{contentdir}/server-status/*

%attr(0710,root,apache) %dir /run/httpd
%attr(0700,apache,apache) %dir /run/httpd/htcacheclean
%attr(0700,root,root) %dir %{_localstatedir}/log/httpd
%attr(0700,apache,apache) %dir %{_localstatedir}/lib/httpd
%attr(0700,apache,apache) %dir %{_localstatedir}/cache/httpd
%attr(0700,apache,apache) %dir %{_localstatedir}/cache/httpd/proxy


%files filesystem
%dir %{_sysconfdir}/httpd
%dir %{_sysconfdir}/httpd/conf.d
%{_sysconfdir}/httpd/conf.d/README
%dir %{docroot}
%dir %{docroot}/cgi-bin
%dir %{docroot}/html
%dir %{contentdir}
%dir %{contentdir}/icons
%attr(755,root,root) %dir %{_unitdir}/httpd.service.d
%attr(755,root,root) %dir %{_unitdir}/httpd.socket.d
%attr(755,root,root) %dir %{_sysconfdir}/systemd/system/httpd.service.d
%{_sysusersdir}/httpd.conf

%files tools
%{_bindir}/ab
%{_bindir}/htdbm
%{_bindir}/htdigest
%{_bindir}/httxt2dbm
%{_bindir}/htpasswd
%{_bindir}/logresolve
%{_mandir}/man1/*
%doc LICENSE NOTICE
%exclude %{_bindir}/apxs
%exclude %{_mandir}/man1/apxs.1*

%files manual
%{contentdir}/manual
%config(noreplace) %{_sysconfdir}/httpd/conf.d/manual.conf

%files -n mod_ssl
%{_libdir}/httpd/modules/mod_ssl.so
%config(noreplace) %{_sysconfdir}/httpd/conf.modules.d/00-ssl.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/ssl.conf
%attr(0700,apache,root) %dir %{_localstatedir}/cache/httpd/ssl
%{_unitdir}/httpd-init.service
%{_libexecdir}/httpd-ssl-pass-dialog
%{_libexecdir}/httpd-ssl-gencerts
%{_unitdir}/httpd.socket.d/10-listen443.conf
%{_mandir}/man8/httpd-init.*

%files -n mod_proxy_html
%{_libdir}/httpd/modules/mod_proxy_html.so
%{_libdir}/httpd/modules/mod_xml2enc.so
%config(noreplace) %{_sysconfdir}/httpd/conf.modules.d/00-proxyhtml.conf

%files -n mod_ldap
%{_libdir}/httpd/modules/mod_*ldap.so
%config(noreplace) %{_sysconfdir}/httpd/conf.modules.d/01-ldap.conf

%files -n mod_session
%{_libdir}/httpd/modules/mod_session*.so
%{_libdir}/httpd/modules/mod_auth_form.so
%config(noreplace) %{_sysconfdir}/httpd/conf.modules.d/01-session.conf

%files -n mod_lua
%{_libdir}/httpd/modules/mod_lua.so
%config(noreplace) %{_sysconfdir}/httpd/conf.modules.d/00-lua.conf

%files devel
%{_includedir}/httpd
%{_bindir}/apxs
%{_mandir}/man1/apxs.1*
%dir %{_libdir}/httpd/build
%{_libdir}/httpd/build/*.mk
%{_libdir}/httpd/build/*.sh
%{_libdir}/httpd/build/vendor-apxs
%{_rpmconfigdir}/macros.d/macros.httpd

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.66-5
- Prepare for Oreon 11 (RP1)
