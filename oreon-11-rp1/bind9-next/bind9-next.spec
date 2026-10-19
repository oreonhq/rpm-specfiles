%global source4_hash 48eb719545eb32d4889ae1b7ae6e395b257f57e653ac335c6af1445e10cdc05f
%global source2_hash c12502741951f26daff681b7835e60e9ac55216ec2a503199086376bbc953e62
%global source0_hash bec622d80eeaa5a97b3cebc2afb6545c888e6e5fca98f63b04fd958d26463d7b
%bcond_with    SYSTEMTEST
%bcond_without SUDO
%bcond_without GSSTSIG
%bcond_without JSON
%bcond_without GEOIP2
%bcond_without UNITTEST
%bcond_with    UNITTEST_ALL
%bcond_without DNSTAP
%bcond_without LMDB
%bcond_without DOC
%bcond_with    TSAN
%bcond_without DTRACE
%bcond_with    OPENSSL_ENGINE
%bcond         JEMALLOC  0%{?fedora}
%{?!bind_uid:  %global bind_uid  25}
%{?!bind_gid:  %global bind_gid  25}
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global        bind_dir          /var/named
%global        chroot_prefix     %{bind_dir}/chroot
%global        chroot_create_directories /dev /run/named %{_localstatedir}/{log,named,tmp} \\\
                                         %{_sysconfdir}/{crypto-policies/back-ends,pki/dnssec-keys,pki/tls,named} \\\
                                         %{_libdir}/bind %{_libdir}/named %{_datadir}/{GeoIP,dns-root-data} /proc/sys/net/ipv4
%global forgeurl0 https://gitlab.isc.org/isc-projects/bind9
%undefine _strict_symbol_defs_build
%global upname bind
%define upname_compat() \
%if "%{name}" != "%{upname}" \
Provides: %1 = %{version}-%{release} \
Conflicts: %1 \
%endif
Summary:        The Berkeley Internet Name Domain (BIND) DNS (Domain Name System) server
Name:     bind9-next
License:  MPL-2.0 AND ISC AND BSD-3-clause AND MIT AND BSD-2-clause
Version:  9.21.26
Release:        1%{?dist}
Epoch:    32
Url:      https://www.isc.org/downloads/bind/
VCS:      git:%{forgeurl0}
Source0:        https://downloads.isc.org/isc/%{upname}9/%{version}/%{upname}-%{version}.tar.xz
Source1:  named.sysconfig
Source2:  https://downloads.isc.org/isc/bind9/%{version}/%{upname}-%{version}.tar.xz.asc
Source3:  named.logrotate
Source4:  https://www.isc.org/docs/isc-keyblock.asc
Source16: named.conf
Source18: named.localhost
Source19: named.loopback
Source20: named.empty
Source23: named.rfc1912.zones
Source25: named.conf.sample
Source27: named-mkroot.sh
Source35: bind.tmpfiles.d
Source37: named.service
Source38: named-chroot.service
Source41: setup-named-chroot.sh
Source42: generate-rndc-key.sh
Source43: named.rwtab
Source44: named-chroot-setup.service
Source46: named-setup-rndc.service
Source48: setup-named-softhsm.sh
Source49: named-chroot.files
Patch1: bind-9.16-redhat_doc.patch
Patch4: bind-9.21-unittest-qpdb-i386.patch
%{?systemd_ordering}
Requires:       coreutils
Requires(post): shadow-utils
Requires(post): glibc-common
Requires(post): grep
Requires:       dns-root-data
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Recommends:     %{name}-utils %{name}-dnssec-utils
%upname_compat %{upname}
Obsoletes:      %{name}-pkcs11 < 32:9.18.4-2
Conflicts:      bind-dyndb-ldap
%if %{with JEMALLOC}
%endif
%if %{with OPENSSL_ENGINE}
%endif
%if %{with UNITTEST}
%endif
%if %{with UNITTEST} || %{with SYSTEMTEST}
%endif
%if %{with SYSTEMTEST}
%if %{with SUDO}
%endif
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
%if %{with TSAN}
%endif
%if %{with DTRACE}
%endif
# oreon:deps
BuildRequires:  dns-root-data
BuildRequires:  doxygen
BuildRequires:  findutils
BuildRequires:  fstrm-devel
BuildRequires:  gcc
BuildRequires:  gdb
BuildRequires:  gzip
BuildRequires:  jemalloc-devel
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
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libedit)
BuildRequires:  protobuf-c-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  sed
BuildRequires:  selinux-policy
BuildRequires:  softhsm
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemtap
BuildRequires:  systemtap-sdt-devel
BuildRequires:  systemtap-sdt-dtrace
BuildRequires:  userspace-rcu-devel
BuildRequires:  util-linux
BuildRequires:  xz
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
Obsoletes: %{name}-license < 32:9.21.11-5
Provides: %{name}-libs-lite = %{epoch}:%{version}-%{release}
Obsoletes: %{name}-libs-lite < 32:9.16.13
Obsoletes: %{name}-pkcs11-libs < 32:9.18.4-2
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

:;

# Create a sysusers.d config file
cat >bind9-next.sysusers.conf <<EOF
g named %{bind_gid}
u named %{bind_uid} 'Named' /var/named -
EOF

# get rid of rpath issues
sed -e '/install_rpath:/ d' -i meson.build

%build

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
export CFLAGS CPPFLAGS
export STD_CDEFINES="$CPPFLAGS"
install -p -m 0755 %{SOURCE27} ./named-mkroot.sh # create named.root.key
./named-mkroot.sh
[ -f named.root.key ]
LIBDIR_SUFFIX=
export LIBDIR_SUFFIX
%meson \
  --includedir=%{_includedir}/bind9 \
  -Didn=enabled \
  -Dfuzzing=disabled \
%if %{without DTRACE}
  -Dtracing=disabled \
%endif
%if %{with GEOIP2}
  -Dgeoip=enabled \
%endif
%if %{with GSSTSIG}
  -Dgssapi=enabled \
%endif
%if %{with LMDB}
  -Dlmdb=enabled \
%else
  -Dlmdb=disabled \
%endif
%if %{with JSON}
  -Dstats-json=enabled \
%endif
%if %{with DNSTAP}
  -Ddnstap=enabled \
%endif
%if %{with UNITTEST}
  -Dcmocka=enabled \
%endif
%if %{with DOC}
  -Ddoc=enabled \
%endif
%if %{without JEMALLOC}
  -Djemalloc=disabled \
%endif
;
%if %{with DNSTAP}
  pushd lib
  SRCLIB="../../../lib"
  (cd dns && ln -s ${SRCLIB}/dns/dnstap.proto)
  popd
%endif
%meson_build
%if %{with DOC}
  %meson_build man arm arm-epub
%endif
%if %{with SYSTEMTEST}
  %meson_build system-test-dependencies
%endif
gzip doc/changelog/changelog-*.rst
%check

export ISC_BENCHMARK_LOOPS=20
%if %{with UNITTEST} || %{with SYSTEMTEST}
  eval "$(bash %{SOURCE48} -A "`pwd`/softhsm-tokens")"
%endif
%if %{with TSAN}
export TSAN_OPTIONS="log_exe_name=true log_path=ThreadSanitizer exitcode=0"
%endif
LD_LIBRARY_PATH="$LD_LIBRARY_PATH:${RPM_BUILD_ROOT}%{_libdir}" \
  ${RPM_BUILD_ROOT}%{_bindir}/named-checkconf ${RPM_BUILD_ROOT}%{_sysconfdir}/named.root.key
%if %{with UNITTEST}
  CPUS=$(lscpu -p=cpu,core | grep -v '^#' | wc -l)
  THREADS="$CPUS"
  COREPATTERN="$(cat /proc/sys/kernel/core_pattern)"
%if %{without UNITTEST_ALL}
  export CI=true
%endif
  if [ "$CPUS" -gt 16 ]; then
    ORIGFILES=$(ulimit -n)
    THREADS=16
    export ISC_TASK_WORKERS="$THREADS"
    ulimit -n 8092 || : # Requires on some machines with many cores
  fi
  e=0
  %meson_test --num-processes ${THREADS} || e=$?
  if [ "$e" -ne 0 ]; then
    echo "ERROR: test failed. Aborting."
    exit $e;
  fi;
  [ "$CPUS" -gt 16 ] && ulimit -n $ORIGFILES || :
%endif
%if %{with SYSTEMTEST}
  SUDO=
  pushd bin/tests/system/
  if perl ./testsock.pl
  then
    CONFIGURED=already
  else
    %if %{with SUDO}
      if [ -x /usr/sbin/capsh ] && ! /usr/sbin/capsh --has-p=cap_net_admin; then
        echo "Not running as privileged user, using sudo"
        SUDO=sudo
      fi
    %endif
    CONFIGURED=
    $SUDO sh ./ifconfig.sh up
    perl ./testsock.pl && CONFIGURED=build
  fi
  popd
  if [ -n "$CONFIGURED" ]
  then
    pushd bin/tests/system
    export CI_SYSTEM=yes # allow running tests as root
    chown -R ${USER} . # Can be unknown user
    e=0
    pytest -n ${THREADS} --capture=tee-sys || e=$?
    [ "$CONFIGURED" = build ] && $SUDO sh ./ifconfig.sh down
    if [ "$e" -ne 0 ]; then
      echo "ERROR: failed running 'pytest' in system tests. Aborting."
      ls -1 "$(pwd)"/*_tmp_*
      for TMPTEST in *_tmp_*
      do
        echo "# $TMPTEST"
        cat $TMPTEST/pytest.log.txt
      done
      exit $e;
    fi;
    popd
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
%meson_install
rm -f ${RPM_BUILD_ROOT}/etc/bind.keys
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
install -pm 644 %{SOURCE37} ${RPM_BUILD_ROOT}%{_unitdir}
install -pm 644 %{SOURCE38} ${RPM_BUILD_ROOT}%{_unitdir}
install -pm 644 %{SOURCE44} ${RPM_BUILD_ROOT}%{_unitdir}
install -pm 644 %{SOURCE46} ${RPM_BUILD_ROOT}%{_unitdir}
mkdir -p ${RPM_BUILD_ROOT}%{_libexecdir}
install -pm 755 %{SOURCE41} ${RPM_BUILD_ROOT}%{_libexecdir}/setup-named-chroot.sh
install -pm 755 %{SOURCE42} ${RPM_BUILD_ROOT}%{_libexecdir}/generate-rndc-key.sh
install -pm 755 %{SOURCE48} ${RPM_BUILD_ROOT}%{_libexecdir}/setup-named-softhsm.sh
install -pm 644 %SOURCE3 ${RPM_BUILD_ROOT}/etc/logrotate.d/named
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
install -pm 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/named
install -pm 644 %{SOURCE49} ${RPM_BUILD_ROOT}%{_sysconfdir}/named-chroot.files
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
pushd %{_vpath_builddir}
cp -a arm/ ${RPM_BUILD_ROOT}%{_pkgdocdir}/html/
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
cp -p arm-epub/Bv9ARM.epub ${RPM_BUILD_ROOT}%{_pkgdocdir}
popd
cp -p doc/changelog/changelog-history.rst* doc/notes/notes-*.rst* \
      ${RPM_BUILD_ROOT}%{_pkgdocdir}
%endif
touch ${RPM_BUILD_ROOT}%{_localstatedir}/log/named.log
install -m 640 %{SOURCE16} ${RPM_BUILD_ROOT}%{_sysconfdir}/named.conf
touch ${RPM_BUILD_ROOT}%{_sysconfdir}/rndc.{key,conf}
install -m 644 -p named.root.key ${RPM_BUILD_ROOT}%{_sysconfdir}/named.root.key
ln -s "%{_datadir}/dns-root-data/root.key" ${RPM_BUILD_ROOT}%{_sysconfdir}/trusted-key.key
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/named
mkdir -p ${RPM_BUILD_ROOT}%{_localstatedir}/named
ln -s "%{_datadir}/dns-root-data/root.hints" ${RPM_BUILD_ROOT}%{_localstatedir}/named/named.ca
install -m 640 %{SOURCE18} ${RPM_BUILD_ROOT}%{_localstatedir}/named/named.localhost
install -m 640 %{SOURCE19} ${RPM_BUILD_ROOT}%{_localstatedir}/named/named.loopback
install -m 640 %{SOURCE20} ${RPM_BUILD_ROOT}%{_localstatedir}/named/named.empty
install -m 640 %{SOURCE23} ${RPM_BUILD_ROOT}%{_sysconfdir}/named.rfc1912.zones
mkdir -p sample/etc sample/var/named/{data,slaves}
install -m 644 %{SOURCE25} sample/etc/named.conf
install -m 644 %{SOURCE16} named.conf.default
install -m 644 %{SOURCE23} sample/etc/named.rfc1912.zones
install -m 644 %{SOURCE18} %{SOURCE19} %{SOURCE20}  sample/var/named
ln -s "%{_datadir}/dns-root-data/root.hints" sample/var/named/named.ca
for f in my.internal.zone.db slaves/my.slave.internal.zone.db slaves/my.ddns.internal.zone.db my.external.zone.db; do 
  echo '@ in soa localhost. root 1 3H 15M 1W 1D
  ns localhost.' > sample/var/named/$f; 
done
:;
mkdir -p ${RPM_BUILD_ROOT}%{_tmpfilesdir}
install -m 644 %{SOURCE35} ${RPM_BUILD_ROOT}%{_tmpfilesdir}/named.conf
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/rwtab.d
install -m 644 %{SOURCE43} ${RPM_BUILD_ROOT}%{_sysconfdir}/rwtab.d/named
install -m0644 -D bind9-next.sysusers.conf %{buildroot}%{_sysusersdir}/bind9-next.conf
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
%triggerun -- bind < 32:9.9.0-0.6.rc1

/sbin/chkconfig --del named >/dev/null 2>&1 || :
/bin/systemctl try-restart named.service >/dev/null 2>&1 || :
%triggerpostun -- bind < 32:9.18.4-2, selinux-policy, policycoreutils

if [ -x %{_sbindir}/selinuxenabled ] && [ -x %{_sbindir}/getsebool ] && [ -x %{_sbindir}/setsebool ] \
   && %{_sbindir}/selinuxenabled && [ -x %{_sbindir}/named ]; then
  WRITEBOOL="$(LC_ALL=C %{_sbindir}/getsebool named_write_master_zones)"
  if [ "echo ${WRITEBOOL#named_write_master_zones --> }" = "off" ]; then
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
%files -n bind9-next-libs -f %{oreon_filedir}/bind9-next-libs.list
%files -n bind9-next-utils -f %{oreon_filedir}/bind9-next-utils.list
%files -n bind9-next-dnssec-utils -f %{oreon_filedir}/bind9-next-dnssec-utils.list
%files -n bind9-next-devel -f %{oreon_filedir}/bind9-next-devel.list
%files -n bind9-next-chroot -f %{oreon_filedir}/bind9-next-chroot.list
%files -n bind9-next-doc -f %{oreon_filedir}/bind9-next-doc.list

%changelog

%autochangelog
