%global source0_hash 868c2686a61b5f8e00a3e4721789b1ab46e6528fd773a5fbed07a6ecba7731e6
%global source8_hash ad7c478cb3aaa76c5f81f86727a3e6843645b0a1253f5684fb8a0beec0d22925
%global __provides_exclude_from %{_docdir}
%global __requires_exclude_from %{_docdir}
Summary:        Secure imap and pop3 server
Name: dovecot
Epoch: 1
Version: 2.4.5
%global prever %{nil}
Release:        1%{?dist}
License: MIT AND LGPL-2.1-only
URL: https://www.dovecot.org/
Source0:        https://www.%{name}.org/releases/2.4/%{name}-%{version}.tar.gz
Source1: dovecot.init
Source2: dovecot.pam
%global pigeonholever %{version}%{?prever}
Source8: https://pigeonhole.dovecot.org/releases/2.4/dovecot-pigeonhole-%{pigeonholever}.tar.gz
Source9: dovecot.sysconfig
Source10: dovecot.tmpfilesd
Source14: dovecot.conf.5
Source15: prestartscript
Source16: dovecot.sysusers
Patch1: dovecot-2.0-defaultconfig.patch
Patch2: dovecot-1.0.beta2-mkcert-permissions.patch
Patch3: dovecot-1.0.rc7-mkcert-paths.patch
Patch6: dovecot-2.1.10-waitonline.patch
Patch8: dovecot-2.2.20-initbysystemd.patch
Patch9: dovecot-2.2.22-systemd_w_protectsystem.patch
Patch15: dovecot-2.3.11-bigkey.patch
Patch16: dovecot-2.4.1-opensslhmac3.patch
Patch17: dovecot-2.3.15-fixvalcond.patch
Patch18: dovecot-2.3.15-valbasherr.patch
Patch19: dovecot-2.4.2-lua-5.5.patch
Patch24: dovecot-2.4.2-fixbuild.patch
Patch25: dovecot-2.4.2-ftbfs-workaround.patch
Patch26: dovecot-2.4.5-pr314.patch
Patch27: dovecot-2.4.5-test_w_small_pipe.patch
Requires: openssl >= 0.9.7f-4
Requires(pre): shadow-utils
Requires: systemd
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%global ssldir %{_sysconfdir}/pki/%{name}
ExcludeArch:    %{ix86}
%global restart_flag /run/%{name}/%{name}-restart-after-rpm-install
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  krb5-devel
BuildRequires:  libcap-devel
BuildRequires:  libcurl-devel
BuildRequires:  libicu-devel
BuildRequires:  libpq-devel
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  quota-devel
BuildRequires:  sqlite-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Dovecot is an IMAP server for Linux/UNIX-like systems, written with security 
primarily in mind.  It also contains a small POP3 server.  It supports mail 
in either of maildir or mbox formats.

The SQL drivers and authentication plug-ins are in their subpackages.

%package pigeonhole
Requires: %{name} = %{epoch}:%{version}-%{release}
Summary: Sieve and managesieve plug-in for dovecot
License: MIT AND LGPL-2.1-only
%description pigeonhole
This package provides sieve and managesieve plug-in for dovecot LDA.

%package pgsql
Requires: %{name} = %{epoch}:%{version}-%{release}
Summary: Postgres SQL back end for dovecot
%description pgsql
This package provides the Postgres SQL back end for dovecot-auth etc.

%package mysql
Requires: %{name} = %{epoch}:%{version}-%{release}
Summary: MySQL back end for dovecot
%description mysql
This package provides the MySQL back end for dovecot-auth etc.

%package devel
Requires: %{name} = %{epoch}:%{version}-%{release}
Summary: Development files for dovecot
%description devel
This package provides the development files for dovecot.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source8_hash}" = "none" || { f="%{SOURCE8}"; test -f "$f" || { echo "oreon: missing Source8 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source8_hash}" || { echo "oreon: Source8 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}%{?prever} -a 8

# standardize name, so we don't have to update patches and scripts
mv dovecot-pigeonhole-%{pigeonholever} dovecot-pigeonhole

%patch -P 1 -p2 -b .default-settings
%patch -P 2 -p1 -b .mkcert-permissions
%patch -P 3 -p1 -b .mkcert-paths
%patch -P 6 -p2 -b .waitonline
%patch -P 8 -p2 -b .initbysystemd
%patch -P 9 -p1 -b .systemd_w_protectsystem
%patch -P 15 -p1 -b .bigkey
%patch -P 16 -p1 -b .opensslhmac3
%patch -P 17 -p2 -b .fixvalcond
%patch -P 18 -p1 -b .valbasherr
%patch -P 19 -p1 -b .lua55
%patch -P 24 -p1 -b .fixbuild
%patch -P 25 -p1 -b .ftbfs-workaround
%patch -P 26 -p1 -b .pr314
%patch -P 27 -p1 -b .test_w_small_pipe
cp run-test-valgrind.supp dovecot-pigeonhole/
# valgrind would fail with shell wrapper
echo "testsuite" >dovecot-pigeonhole/run-test-valgrind.exclude

%build

%global _hardened_build 1
export CFLAGS="%{__global_cflags} -fno-strict-aliasing -fstack-reuse=none"
export LDFLAGS="-Wl,-z,now -Wl,-z,relro %{?__global_ldflags}"
mkdir -p m4
if [ -d /usr/share/gettext/m4 ]
then
  autoreconf -I . -I /usr/share/gettext/m4 
else
  autoreconf -I . -fiv #required for aarch64 support
fi
%configure                       \
    --enable-experimental-mail-utf8 \
    INSTALL_DATA="install -c -p -m644" \
    --with-rundir=%{_rundir}/%{name}   \
    --with-systemd               \
    --docdir=%{_docdir}/%{name}  \
    --disable-static             \
    --disable-rpath              \
    --with-nss                   \
    --with-shadow                \
    --with-pam                   \
    --with-gssapi=plugin         \
    --with-ldap=plugin           \
    --with-sql=plugin            \
    --with-pgsql                 \
    --with-mysql                 \
    --with-sqlite                \
    --with-zlib                  \
    --with-zstd                  \
    --with-libcap                \
    --with-icu                   \
    --without-libstemmer         \
    --without-lua                \
    --without-lucene             \
    --without-exttextcat         \
    --with-ssl=openssl           \
    --with-ssldir=%{ssldir}      \
    --with-solr                  \
    --with-docs                  \
    systemdsystemunitdir=%{_unitdir}
sed -i 's|/etc/ssl|/etc/pki/dovecot|' doc/mkcert.sh # doc/example-config/conf.d/10-ssl.conf
%make_build
pushd dovecot-pigeonhole
[ -f configure ] || autoreconf -fiv
[ -f ChangeLog ] || echo "Pigeonhole ChangeLog is not available, yet" >ChangeLog
%configure                             \
    INSTALL_DATA="install -c -p -m644" \
    --disable-static                   \
    --with-dovecot=../                 \
    --without-unfinished-features
%make_build
popd
%install
rm -rf $RPM_BUILD_ROOT
%make_install
mv $RPM_BUILD_ROOT/%{_docdir}/%{name} %{_builddir}/%{name}-%{version}%{?prever}/docinstall
pushd dovecot-pigeonhole
%make_install
mv $RPM_BUILD_ROOT/%{_docdir}/%{name} $RPM_BUILD_ROOT/%{_docdir}/%{name}-pigeonhole
install -m 644 AUTHORS ChangeLog COPYING COPYING.LGPL INSTALL NEWS README $RPM_BUILD_ROOT/%{_docdir}/%{name}-pigeonhole
popd
install -p -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/dovecot
install -p -D -m 644 %{SOURCE14} $RPM_BUILD_ROOT%{_mandir}/man5/dovecot.conf.5
install -p -D -m 755 %{SOURCE15} $RPM_BUILD_ROOT%{_libexecdir}/dovecot/prestartscript
install -p -D -m 0644 %{SOURCE16} $RPM_BUILD_ROOT%{_sysusersdir}/dovecot.conf
mkdir -p $RPM_BUILD_ROOT%{ssldir}/certs
mkdir -p $RPM_BUILD_ROOT%{ssldir}/private
touch $RPM_BUILD_ROOT%{ssldir}/certs/dovecot.pem
chmod 600 $RPM_BUILD_ROOT%{ssldir}/certs/dovecot.pem
touch $RPM_BUILD_ROOT%{ssldir}/private/dovecot.pem
chmod 600 $RPM_BUILD_ROOT%{ssldir}/private/dovecot.pem
install -p -D -m 644 %{SOURCE10} $RPM_BUILD_ROOT%{_tmpfilesdir}/dovecot.conf
mkdir -p $RPM_BUILD_ROOT/run/dovecot/{login,empty,token-login}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/dovecot/conf.d
install -p -m 644 $RPM_BUILD_ROOT/%{_docdir}/%{name}-pigeonhole/example-config/conf.d/*.conf $RPM_BUILD_ROOT%{_sysconfdir}/dovecot/conf.d
install -p -m 644 $RPM_BUILD_ROOT/%{_docdir}/%{name}-pigeonhole/example-config/conf.d/*.conf.ext $RPM_BUILD_ROOT%{_sysconfdir}/dovecot/conf.d ||:
install -p -m 644 doc/dovecot-openssl.cnf $RPM_BUILD_ROOT%{ssldir}/dovecot-openssl.cnf
install -p -m755 doc/mkcert.sh $RPM_BUILD_ROOT%{_libexecdir}/%{name}/mkcert.sh
mkdir -p $RPM_BUILD_ROOT/var/lib/dovecot
find $RPM_BUILD_ROOT%{_libdir}/%{name}/ -name '*.la' | xargs rm -f
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/dovecot/README
pushd docinstall
rm -f securecoding.txt thread-refs.txt
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%pre

if [ "$1" = "2" ]; then
  rm -f %restart_flag
  /bin/systemctl is-active %{name}.service >/dev/null 2>&1 && touch %restart_flag ||:
  /bin/systemctl stop %{name}.service >/dev/null 2>&1
fi
%post

if [ $1 -eq 1 ]
then
  %systemd_post dovecot.service
fi
install -d -m 0755 -g dovecot -d /run/dovecot
install -d -m 0755 -d /run/dovecot/empty
install -d -m 0750 -g dovenull -d /run/dovecot/login
install -d -m 0750 -g dovenull -d /run/dovecot/token-login
[ -x /sbin/restorecon ] && /sbin/restorecon -R /run/dovecot ||:
%preun

if [ $1 = 0 ]; then
        /bin/systemctl disable dovecot.service dovecot.socket >/dev/null 2>&1 || :
        /bin/systemctl stop dovecot.service dovecot.socket >/dev/null 2>&1 || :
    rm -rf /run/dovecot
fi
%postun

/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ "$1" -ge "1" -a -e %restart_flag ]; then
    /bin/systemctl start dovecot.service >/dev/null 2>&1 || :
rm -f %restart_flag
fi
%posttrans

if [ -e %restart_flag ]; then
    /bin/systemctl start dovecot.service >/dev/null 2>&1 || :
rm -f %restart_flag
fi
%check

%ifnarch aarch64
if ! make check
then
    find . -name test-suite.log | xargs cat ||:
    exit 1
fi
cd dovecot-pigeonhole
make check ||:
%endif
%files -f %{oreon_filedir}/main.list
%files -n dovecot-pigeonhole -f %{oreon_filedir}/dovecot-pigeonhole.list
%files -n dovecot-pgsql -f %{oreon_filedir}/dovecot-pgsql.list
%files -n dovecot-mysql -f %{oreon_filedir}/dovecot-mysql.list
%files -n dovecot-devel -f %{oreon_filedir}/dovecot-devel.list

%changelog

%autochangelog
