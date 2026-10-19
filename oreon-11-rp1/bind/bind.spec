%global source17_hash eecb45f6b6bfa19f5bab3179997e0498653a5eafca1e36f1257cc3015d6b32af
%global source4_hash 48eb719545eb32d4889ae1b7ae6e395b257f57e653ac335c6af1445e10cdc05f
%global source2_hash 1173e82d0777a79ff509b8727513c92a3edc8762f0270ef1088c4de8284ca07a
%global source0_hash a24f93be94712a8c11752294410f2f8a2510ec7fdc931d207fc61cdf30e54f4d
%bcond_with    SYSTEMTEST
%bcond_with    CRYPTO_POLICY_RSA1
%bcond_without GSSTSIG
%bcond_without JSON
%bcond_without GEOIP2
%bcond_with    JEMALLOC
%bcond_without UNITTEST
%bcond_with    UNITTEST_ALL
%bcond_without DNSTAP
%bcond_without LMDB
%bcond_without DOC
%bcond_with    TSAN
%bcond_with    QUERYTRACE
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global        bind_dir          /var/named
%global        chroot_prefix     %{bind_dir}/chroot
%global        chroot_create_directories /dev /run/named %{_localstatedir}/{log,named,tmp} \\\
                                         %{_sysconfdir}/{crypto-policies/back-ends,pki/dnssec-keys,named} \\\
                                         %{_libdir}/bind %{_libdir}/named %{_datadir}/{GeoIP,named} /proc/sys/net/ipv4
%define bind_export_libs isc dns isccfg irs
%{!?_export_dir:%global _export_dir /bind9-export/}
%undefine _strict_symbol_defs_build
%global upname bind
%define upname_compat() \
%if "%{name}" != "%{upname}" \
Provides: %1 = %{version}-%{release} \
Conflicts: %1 \
%endif
Summary:        The Berkeley Internet Name Domain (BIND) DNS (Domain Name System) server
Name:     bind
License:  MPL-2.0 AND ISC AND MIT AND BSD-3-Clause AND BSD-2-Clause
Version:  9.18.50
Release:        1%{?dist}
Epoch:    32
Url:      https://www.isc.org/downloads/bind/
Source0:        https://downloads.isc.org/isc/%{name}9/%{version}/%{name}-%{version}.tar.xz
Source1:  named.sysconfig
Source2:        https://downloads.isc.org/isc/bind9/%{version}/%{upname}-%{version}.tar.xz.asc
Source3:  named.logrotate
Source4:  https://www.isc.org/docs/isc-keyblock.asc
Source16: named.conf
Source17: https://www.internic.net/domain/named.root
Source18: named.localhost
Source19: named.loopback
Source20: named.empty
Source23: named.rfc1912.zones
Source25: named.conf.sample
Source27: named.root.key
Source35: bind.tmpfiles.d
Source36: trusted-key.key
Source37: named.service
Source38: named-chroot.service
Source41: setup-named-chroot.sh
Source42: generate-rndc-key.sh
Source43: named.rwtab
Source44: named-chroot-setup.service
Source46: named-setup-rndc.service
Source48: setup-named-softhsm.sh
Source49: named-chroot.files
Source50: named.sysusers
Source51: bind-chroot.tmpfiles.d
Patch10: bind-9.5-PIE.patch
Patch16: bind-9.16-redhat_doc.patch
Patch26: bind-9.18-unittest-netmgr-unstable.patch
Patch28: bind-9.20-nsupdate-tls.patch
Patch29: bind-9.20-nsupdate-tls-doc.patch
Patch30: bind-9.20-nsupdate-tls-test.patch
Patch31: bind-9.18-pkcs11-provider.patch
Patch32: bind-9.18-partial-additional-records.patch
Patch33: bind-9.18-dig-idn-input-always.patch
Patch34: bind-9.18-dig-idn-input-always-test.patch
%{?systemd_ordering}
%{?sysusers_requires_compat}
Requires:       coreutils
Requires(post): shadow-utils
Requires(post): glibc-common
Requires(post): grep
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Recommends:     %{name}-utils %{name}-dnssec-utils
%upname_compat  %{upname}
Obsoletes:      %{name}-pkcs11 < 32:9.18.4-2
%if %{with OPENSSL_ENGINE}
%endif
%if %{with UNITTEST}
%endif
%if %{with UNITTEST} || %{with SYSTEMTEST}
%endif
%if %{with SYSTEMTEST}
%endif
%if %{with GSSTSIG}
%endif
%if %{with LMDB}
%endif
%if %{with JSON}
%endif
%if %{with GEOIP2}
%endif
%if %{with DNSTAP}
%endif
%if %{with DOC}
%endif
%if %{with DOCPDF}
%endif
%if %{with TSAN}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  doxygen
BuildRequires:  findutils
BuildRequires:  fstrm-devel
BuildRequires:  gcc
BuildRequires:  json-c-devel
BuildRequires:  krb5-devel
BuildRequires:  libcap-devel
BuildRequires:  libcmocka-devel
BuildRequires:  libidn2-devel
BuildRequires:  libmaxminddb-devel
BuildRequires:  libnghttp2-devel
BuildRequires:  libtool
BuildRequires:  libuv-devel
BuildRequires:  libxml2-devel
BuildRequires:  lmdb-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  protobuf-c-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  sed
BuildRequires:  selinux-policy
BuildRequires:  softhsm
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
BIND (Berkeley Internet Name Domain) is an implementation of the DNS
(Domain Name System) protocols. BIND includes a DNS server (named),
which resolves host names to IP addresses; a resolver library
(routines for applications to use when interfacing with DNS); and
tools for verifying that the DNS server is operating properly.

%package libs
Summary: Libraries used by the BIND DNS packages
Provides: %{name}-license = %{epoch}:%{version}-%{release}
Provides: %{name}-libs-lite = %{epoch}:%{version}-%{release}
Obsoletes: %{name}-libs-lite < 32:9.16.13
Obsoletes: %{name}-pkcs11-libs < 32:9.18.4-2
Obsoletes: %{name}-license < 32:9.18.30-3
%description libs
Contains heavyweight version of BIND suite libraries used by both named DNS
server and utilities in %{name}-utils package.

%package utils
Summary: Utilities for querying DNS name servers
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Provides: dnsutils = %{epoch}:%{version}-%{release}
Obsoletes: %{name}-pkcs11-utils < 32:9.18.4-2
%upname_compat %{upname}-utils
%description utils
Bind-utils contains a collection of utilities for querying DNS (Domain
Name System) name servers to find out information about Internet
hosts. These tools will provide you with the IP addresses for given
host names, as well as other information about registered domains and
network addresses.

You should install %{name}-utils if you need to get information from DNS name
servers.

%package dnssec-utils
Summary: DNSSEC keys and zones management utilities
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Recommends: %{name}-utils
Obsoletes: python3-%{name} < 32:9.18.0
Obsoletes: %{name}-dnssec-doc < 32:9.18.4-2
%upname_compat %{upname}-dnssec-utils
%description dnssec-utils
%{name}-dnssec-utils contains a collection of utilities for editing
DNSSEC keys and BIND zone files. These tools provide generation,
revocation and verification of keys and DNSSEC signatures in zone files.

You should install %{name}-dnssec-utils if you need to sign a DNS zone
or maintain keys for it.

%package devel
Summary:  Header files and libraries needed for bind-dyndb-ldap
Provides: %{name}-lite-devel = %{epoch}:%{version}-%{release}
Obsoletes: %{name}-lite-devel < 32:9.16.6-3
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: openssl-devel%{?_isa} libxml2-devel%{?_isa}
Requires: libcap-devel%{?_isa}
%upname_compat %{upname}-devel
%if %{with GSSTSIG}
Requires: krb5-devel%{?_isa}
%endif
%if %{with LMDB}
Requires: lmdb-devel%{?_isa}
%endif
%if %{with JSON}
Requires:  json-c-devel%{?_isa}
%endif
%if %{with DNSTAP}
Requires:  fstrm-devel%{?_isa} protobuf-c-devel%{?_isa}
%endif
%if %{with GEOIP2}
Requires:  libmaxminddb-devel%{?_isa}
%endif
%description devel
The %{name}-devel package contains full version of the header files and libraries
required for building bind-dyndb-ldap. Upstream no longer supports nor recommends
bind libraries for third party applications.

%package chroot
Summary:        A chroot runtime environment for the ISC BIND DNS server, named(8)
Prefix:         %{chroot_prefix}
Requires:       grep
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%upname_compat %{upname}-chroot
%if "%{name}" != "%{upname}"
Conflicts:      %{upname}-sdb-chroot
%endif
%description chroot
This package contains a tree of files which can be used as a
chroot(2) jail for the named(8) program from the BIND package.
Based on the code from Jan "Yenya" Kasprzak <kas@fi.muni.cz>

%if %{with DOC}
%package doc
Summary:   BIND 9 Administrator Reference Manual
Requires:  python3-sphinx_rtd_theme
BuildArch: noarch
%description doc
BIND (Berkeley Internet Name Domain) is an implementation of the DNS
(Domain Name System) protocols. BIND includes a DNS server (named),
which resolves host names to IP addresses; a resolver library
(routines for applications to use when interfacing with DNS); and
tools for verifying that the DNS server is operating properly.

This package contains BIND 9 Administrator Reference Manual
in HTML and PDF format.
%end

%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{upname}-%{version} -p1

# Sparc and s390 arches need to use -fPIE
%ifarch sparcv9 sparc64 s390 s390x
for i in bin/named/Makefile.am; do
  sed -i 's|fpie|fPIE|g' $i
done
%endif

# allow running as root from mock or test machines
sed -e 's, "enable-developer",& \&\& systemctl is-system-running \&>/dev/null \&\& ! [ -e /mnt/tests ],' \
    -i bin/tests/system/run.sh

:;

%build

%define _configure "../configure"
%define unit_prepare_build() \
  find lib -name 'K*.key' -exec cp -uv '{}' "%{1}/{}" ';' \
  find lib -name 'testdata' -type d -exec cp -Tav '{}' "%{1}/{}" ';' \
  find lib -name 'testkeys' -type d -exec cp -Tav '{}' "%{1}/{}" ';' \
%define systemtest_prepare_build() \
  cp -Tuav bin/tests "%{1}/bin/tests/" \
%if %{with OPENSSL_ENGINE}
CPPFLAGS="$CPPFLAGS -DOPENSSL_API_COMPAT=10100"
%else
CPPFLAGS="$CPPFLAGS -DOPENSSL_NO_ENGINE=1"
%endif
%if %{with TSAN}
  CFLAGS+=" -O1 -fsanitize=thread -fPIE -pie"
%endif
%if %{with QUERYTRACE}
  CFLAGS+=" -DWANT_QUERYTRACE"
%endif
export CFLAGS CPPFLAGS
export STD_CDEFINES="$CPPFLAGS"
sed -i -e \
's/([bind_VERSION_EXTRA],\s*\([^)]*\))/([bind_VERSION_EXTRA], \1-RH)/' \
configure.ac
autoreconf --force --install
mkdir build
pushd build
LIBDIR_SUFFIX=
export LIBDIR_SUFFIX
%configure \
  --localstatedir=%{_var} \
  --with-pic \
  --disable-static \
  --includedir=%{_includedir}/bind9 \
  --with-tuning=large \
  --with-libidn2 \
%if %{with GEOIP2}
  --with-maxminddb \
%endif
%if %{with GSSTSIG}
  --with-gssapi=yes \
%endif
%if %{with LMDB}
  --with-lmdb=yes \
%else
  --with-lmdb=no \
%endif
%if %{with JSON}
  --with-json-c \
%endif
%if %{with DNSTAP}
  --enable-dnstap \
%endif
%if %{with UNITTEST}
  --with-cmocka \
%endif
%if %{without JEMALLOC}
  --without-jemalloc \
%endif
  --enable-fixed-rrset \
  --enable-full-report \
  CPPFLAGS="$CPPFLAGS" \
;
%if %{with DNSTAP}
  pushd lib
  SRCLIB="../../../lib"
  (cd dns && ln -s ${SRCLIB}/dns/dnstap.proto)
  popd
%endif
%if %{with DOCPDF}
export TEXMFVAR="`pwd`"
export TEXMFCONFIG="`pwd`"
fmtutil-user --listcfg || :
fmtutil-user --missing || :
%endif
%make_build
%if %{with DOC}
  make doc
%endif
popd # build
%unit_prepare_build build
%systemtest_prepare_build build
%check

%if %{with UNITTEST} || %{with SYSTEMTEST}
  eval "$(bash %{SOURCE48} -A "`pwd`/softhsm-tokens")"
%endif
%if %{with TSAN}
export TSAN_OPTIONS="log_exe_name=true log_path=ThreadSanitizer exitcode=0"
%endif
%if %{with UNITTEST}
  pushd build
  CPUS=$(lscpu -p=cpu,core | grep -v '^#' | wc -l)
  THREADS="$CPUS"
%if %{without UNITTEST_ALL}
  export CI=true
%endif
  if [ "$CPUS" -gt 16 ]; then
    ORIGFILES=$(ulimit -n)
    THREADS=16
    ulimit -n 8092 || : # Requires on some machines with many cores
  fi
  e=0
  make unit -j${THREADS} || e=$?
  cat tests/*/test-suite.log
  if [ "$e" -ne 0 ]; then
    echo "ERROR: this build of BIND failed 'make unit'. Aborting."
    exit $e;
  fi;
  [ "$CPUS" -gt 16 ] && ulimit -n $ORIGFILES || :
  popd
%endif
%if %{with SYSTEMTEST}
if perl bin/tests/system/testsock.pl
then
  CONFIGURED=already
else
  CONFIGURED=
  sh bin/tests/system/ifconfig.sh up
  perl bin/tests/system/testsock.pl && CONFIGURED=build
fi
if [ -n "$CONFIGURED" ]
then
  set -e
  %if %{with CRYPTO_POLICY_RSA1}
    OPENSSL_CONF="$(mktemp openssl-XXXXXX.cnf)"
    cat > "$OPENSSL_CONF" << 'EOF'
.include = /etc/ssl/openssl.cnf
[evp_properties]
rh-allow-sha1-signatures = yes
EOF
    export OPENSSL_CONF
  %endif
  pushd build/bin/tests
  chown -R ${USER} . # Can be unknown user
  %make_build test
  e=$?
  popd
  [ "$CONFIGURED" = build ] && sh bin/tests/system/ifconfig.sh down
  %if %{with CRYPTO_POLICY_RSA1}
    export -b OPENSSL_CONF
  %endif
  if [ "$e" -ne 0 ]; then
    echo "ERROR: this build of BIND failed 'make test'. Aborting."
    exit $e;
  fi;
else
  echo 'SKIPPED: tests require root, CAP_NET_ADMIN or already configured test addresses.'
fi
%endif
:
%install
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/{bind,named}
mkdir -p ${RPM_BUILD_ROOT}%{_localstatedir}/named/{slaves,data,dynamic}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/{man1,man5,man8}
mkdir -p ${RPM_BUILD_ROOT}/run/named
mkdir -p ${RPM_BUILD_ROOT}%{_localstatedir}/log
for D in %{chroot_create_directories}
do
  mkdir -p ${RPM_BUILD_ROOT}/%{chroot_prefix}${D}
done
pushd ${RPM_BUILD_ROOT}/%{chroot_prefix}/var
ln -s ../run run
popd
touch ${RPM_BUILD_ROOT}/%{chroot_prefix}%{_sysconfdir}/named.conf
pushd build
%make_install
popd
rm -f ${RPM_BUILD_ROOT}/etc/bind.keys
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
install -m 644 %{SOURCE37} ${RPM_BUILD_ROOT}%{_unitdir}
install -m 644 %{SOURCE38} ${RPM_BUILD_ROOT}%{_unitdir}
install -m 644 %{SOURCE44} ${RPM_BUILD_ROOT}%{_unitdir}
install -m 644 %{SOURCE46} ${RPM_BUILD_ROOT}%{_unitdir}
mkdir -p ${RPM_BUILD_ROOT}%{_sysusersdir}
install -m 644 %{SOURCE50} ${RPM_BUILD_ROOT}%{_sysusersdir}/named.conf
mkdir -p ${RPM_BUILD_ROOT}%{_libexecdir}
install -m 755 %{SOURCE41} ${RPM_BUILD_ROOT}%{_libexecdir}/setup-named-chroot.sh
install -m 755 %{SOURCE42} ${RPM_BUILD_ROOT}%{_libexecdir}/generate-rndc-key.sh
install -m 755 %{SOURCE48} ${RPM_BUILD_ROOT}%{_libexecdir}/setup-named-softhsm.sh
install -m 644 %SOURCE3 ${RPM_BUILD_ROOT}/etc/logrotate.d/named
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
install -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/named
install -m 644 %{SOURCE49} ${RPM_BUILD_ROOT}%{_sysconfdir}/named-chroot.files
%if "%{_sbindir}" != "%{_bindir}"
ln -s ../bin/{named-checkconf,named-checkzone,named-compilezone} %{buildroot}%{_sbindir}/
%endif
find ${RPM_BUILD_ROOT}/%{_libdir} -name '*.la' -exec '/bin/rm' '-f' '{}' ';';
%if %{without DNSTAP}
rm -f ${RPM_BUILD_ROOT}%{_mandir}/man1/dnstap-read.1* || true
%endif
%if %{without LMDB}
rm -f ${RPM_BUILD_ROOT}%{_mandir}/man8/named-nzd2nzf.8* || true
%endif
pushd ${RPM_BUILD_ROOT}%{_mandir}/man8
ln -s ddns-confgen.8.gz tsig-keygen.8.gz
popd
pushd ${RPM_BUILD_ROOT}%{_mandir}/man1
ln -s named-checkzone.1.gz named-compilezone.1.gz
popd
%if %{with DOC}
mkdir -p ${RPM_BUILD_ROOT}%{_pkgdocdir}
cp -a build/doc/arm/_build/html ${RPM_BUILD_ROOT}%{_pkgdocdir}
rm -rf ${RPM_BUILD_ROOT}%{_pkgdocdir}/html/.{buildinfo,doctrees}
(cd ${RPM_BUILD_ROOT}%{_pkgdocdir} && ln -s html/index.html Bv9ARM.html)
for DIR in %{python3_sitelib}/sphinx_rtd_theme/static/*
do
  BASE=$(basename -- "$DIR")
  BINDTHEMEDIR="${RPM_BUILD_ROOT}%{_pkgdocdir}/html/_static/$BASE"
  if [ -d "$BINDTHEMEDIR" ]; then
    rm -rf "$BINDTHEMEDIR"
    ln -sr "${RPM_BUILD_ROOT}${DIR}" "$BINDTHEMEDIR"
  fi
done
%endif
%if %{with DOCPDF}
cp -p build/doc/arm/_build/latex/Bv9ARM.pdf ${RPM_BUILD_ROOT}%{_pkgdocdir}
%endif
touch ${RPM_BUILD_ROOT}%{_localstatedir}/log/named.log
install -m 640 %{SOURCE16} ${RPM_BUILD_ROOT}%{_sysconfdir}/named.conf
touch ${RPM_BUILD_ROOT}%{_sysconfdir}/rndc.{key,conf}
install -m 644 %{SOURCE27} ${RPM_BUILD_ROOT}%{_sysconfdir}/named.root.key
install -m 644 %{SOURCE36} ${RPM_BUILD_ROOT}%{_sysconfdir}/trusted-key.key
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/named
install -p -m 644 %{SOURCE17} ${RPM_BUILD_ROOT}%{_sysconfdir}/named.ca
ln -sr ${RPM_BUILD_ROOT}%{_sysconfdir}/named.ca \
       ${RPM_BUILD_ROOT}%{_localstatedir}/named/named.ca
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/named
install -p -m 644 %{SOURCE18} ${RPM_BUILD_ROOT}%{_datadir}/named/named.localhost
install -p -m 644 %{SOURCE19} ${RPM_BUILD_ROOT}%{_datadir}/named/named.loopback
install -p -m 644 %{SOURCE20} ${RPM_BUILD_ROOT}%{_datadir}/named/named.empty
mkdir -p ${RPM_BUILD_ROOT}%{_localstatedir}/named
for FILE in named.{localhost,loopback,empty}
do
  ln -sr "${RPM_BUILD_ROOT}%{_datadir}/named/$FILE" \
         "${RPM_BUILD_ROOT}%{_localstatedir}/named/$FILE"
done
install -p -m 640 %{SOURCE23} ${RPM_BUILD_ROOT}%{_sysconfdir}/named.rfc1912.zones
mkdir -p sample/etc sample/var/named/{data,slaves}
install -m 644 %{SOURCE25} sample/etc/named.conf
install -m 644 %{SOURCE16} named.conf.default
install -m 644 %{SOURCE23} sample/etc/named.rfc1912.zones
ln -s %{_sysconfdir}/named.ca sample/var/named/named.ca
for FILE in named.{localhost,loopback,empty}; do
  ln -s %{_datadir}/named/$FILE sample/var/named/$FILE
done
for f in my.internal.zone.db slaves/my.slave.internal.zone.db slaves/my.ddns.internal.zone.db my.external.zone.db; do 
  echo '@ in soa localhost. root 1 3H 15M 1W 1D
  ns localhost.' > sample/var/named/$f; 
done
:;
mkdir -p ${RPM_BUILD_ROOT}%{_tmpfilesdir}
install -p -m 644 %{SOURCE35} ${RPM_BUILD_ROOT}%{_tmpfilesdir}/named.conf
install -p -m 644 %{SOURCE51} ${RPM_BUILD_ROOT}%{_tmpfilesdir}/%{name}-chroot.conf
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/rwtab.d
install -p -m 644 %{SOURCE43} ${RPM_BUILD_ROOT}%{_sysconfdir}/rwtab.d/named
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%?ldconfig
if [ "$1" -eq 1 ]; then
  [ -x /sbin/restorecon ] && /sbin/restorecon /etc/rndc.* /etc/named.* >/dev/null 2>&1 ;
  [ -e /etc/rndc.key ] && chown root:named /etc/rndc.key
  [ -e /etc/rndc.key ] && chmod 0640 /etc/rndc.key
else
  if getent passwd named | grep ':/bin/false$' >/dev/null; then
    /sbin/usermod -s /sbin/nologin named
  fi
  if /usr/bin/named-checkconf -p /etc/named.conf 2>/dev/null | grep -q named.iscdlv.key
  then
    echo "Replacing obsolete named.iscdlv.key with named.root.key..."
    if cp -Rf --preserve=all --remove-destination /etc/named.conf /etc/named.conf.rpmbackup; then
      sed -e 's/named\.iscdlv\.key/named.root.key/' \
        /etc/named.conf.rpmbackup > /etc/named.conf || \
      mv /etc/named.conf.rpmbackup /etc/named.conf
    fi
  fi
fi
%systemd_post named.service
:;
%preun

%systemd_preun named.service
%postun

%?ldconfig
%systemd_postun_with_restart named.service
%define chroot_fix_devices() \
if [ $1 -gt 1 ]; then \
  for DEV in "%{1}/dev"/{null,random,zero}; do \
    if [ -e "$DEV" -a "$(/bin/stat --printf="%G %a" "$DEV")" = "root 644" ]; \
    then \
      /bin/chmod 0664 "$DEV" \
      /bin/chgrp named "$DEV" \
    fi \
  done \
fi
%triggerpostun -- bind < 32:9.18.4-2, selinux-policy, policycoreutils

if [ -x %{_sbindir}/selinuxenabled ] && [ -x %{_sbindir}/getsebool ] && [ -x %{_sbindir}/setsebool ] \
   && %{_sbindir}/selinuxenabled && [ -x %{_sbindir}/named ]; then
  WRITEBOOL="$(LC_ALL=C %{_sbindir}/getsebool named_write_master_zones)"
  if [ "${WRITEBOOL#named_write_master_zones --> }" = "off" ]; then
    echo "Restoring new sebool default of named_write_master_zones..."
    %{_sbindir}/setsebool -P named_write_master_zones=1 || :
  fi
fi
%ldconfig_scriptlets libs
%post chroot

%systemd_post named-chroot.service
%chroot_fix_devices %{chroot_prefix}
:;
%posttrans chroot

if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon %{chroot_prefix}/dev/* > /dev/null 2>&1;
fi;
%preun chroot

%systemd_preun named-chroot.service named-chroot-setup.service
:;
%postun chroot

%systemd_postun_with_restart named-chroot.service
%files -f %{oreon_filedir}/main.list
%files -n bind-libs -f %{oreon_filedir}/bind-libs.list
%files -n bind-utils -f %{oreon_filedir}/bind-utils.list
%files -n bind-dnssec-utils -f %{oreon_filedir}/bind-dnssec-utils.list
%files -n bind-devel -f %{oreon_filedir}/bind-devel.list
%files -n bind-chroot -f %{oreon_filedir}/bind-chroot.list
%files -n bind-doc -f %{oreon_filedir}/bind-doc.list

%changelog

%autochangelog
