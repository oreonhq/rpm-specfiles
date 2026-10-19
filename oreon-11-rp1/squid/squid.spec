%global source2_hash 15e5f517cfd0b985def66f4cb1278e0c855abe2b426f259d14d13ad2f999660f
%global source1_hash d8839fc2fad6f5a05aac42928a3061ca2d318e31dc8cd72aa8211b1fb1291c34
%global source0_hash e3bd613b91b1c498ec2992276063342a85cd6edddd5521294e04f44bc055da9b
%define __perl_requires %{SOURCE98}
%define version_underscore %(echo %{version} | tr '.' '_')
Name:     squid
Version:  7.7
Release:        1%{?dist}
Summary:        The Squid proxy caching server
Epoch:    7
License:  GPL-2.0-or-later AND (LGPL-2.0-or-later AND MIT AND BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND BSD-4-Clause-UC AND LicenseRef-Fedora-Public-Domain AND Beerware)
URL:      http://www.squid-cache.org
Source0:        https://github.com/%{name}-cache/%{name}/releases/download/SQUID_%{version_underscore}/%{name}-%{version}.tar.xz
Source1:        https://github.com/squid-cache/squid/releases/download/SQUID_%{version_underscore}/squid-%{version}.tar.xz.asc
Source2:  http://www.squid-cache.org/pgp.asc
Source3:  squid.logrotate
Source4:  squid.sysconfig
Source5:  squid.pam
Source6:  squid.nm
Source7:  squid.service
Source8:  cache_swap.sh
Source9:  squid.sysusers
Source98: perl-requires-squid.sh
Patch201: squid-6.1-config.patch
Patch202: squid-6.1-location.patch
Patch203: squid-6.1-perlpath.patch
Patch204: squid-6.1-symlink-lang-err.patch
Requires: bash gawk
Requires: httpd-filesystem
%{?systemd_requires}
%{?sysusers_requires_compat}
Conflicts: NetworkManager < 1.20
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  krb5-devel
BuildRequires:  libcap-devel
BuildRequires:  libecap-devel
BuildRequires:  libtdb-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Squid is a high-performance proxy caching server for Web clients,
supporting FTP and HTTP data objects. Unlike traditional
caching software, Squid handles all requests in a single,
non-blocking, I/O-driven process. Squid keeps meta data and especially
hot objects cached in RAM, caches DNS lookups, supports non-blocking
DNS lookups, and implements negative caching of failed requests.

Squid consists of a main server program squid, a Domain Name System
lookup program (dnsserver), a program for retrieving FTP data
(ftpget), and some management and client tools.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -p1

# https://bugzilla.redhat.com/show_bug.cgi?id=1679526
# Patch in the vendor documentation and used different location for documentation
sed -i 's|@SYSCONFDIR@/squid.conf.documented|%{_pkgdocdir}/squid.conf.documented|' src/squid.8.in

%build

%configure \
   --libexecdir=%{_libdir}/squid \
   --datadir=%{_datadir}/squid \
   --sysconfdir=%{_sysconfdir}/squid \
   --with-logdir='%{_localstatedir}/log/squid' \
   --with-pidfile='/run/squid.pid' \
   --disable-dependency-tracking \
   --enable-eui \
   --enable-follow-x-forwarded-for \
   --enable-auth \
   --enable-auth-basic="DB,fake,getpwnam,LDAP,NCSA,PAM,POP3,RADIUS,SASL,SMB" \
   --enable-auth-ntlm="fake" \
   --enable-auth-digest="file,LDAP" \
   --enable-auth-negotiate="kerberos" \
   --enable-external-acl-helpers="LDAP_group,time_quota,session,unix_group,wbinfo_group,kerberos_ldap_group" \
   --enable-storeid-rewrite-helpers="file" \
   --enable-cache-digests \
   --enable-cachemgr-hostname=localhost \
   --enable-delay-pools \
   --enable-epoll \
   --enable-icap-client \
   --enable-ident-lookups \
   %ifnarch %{power64} ia64 x86_64 s390x aarch64
   --with-large-files \
   %endif
   --enable-linux-netfilter \
   --enable-removal-policies="heap,lru" \
   --enable-snmp \
   --enable-ssl \
   --enable-ssl-crtd \
   --enable-storeio="aufs,diskd,ufs,rock" \
   --enable-diskio \
   --enable-wccpv2 \
   --disable-esi \
   --enable-ecap \
   --with-aio \
   --with-default-user="squid" \
   --with-dl \
   --with-openssl \
   --with-pthreads \
   --disable-arch-native \
   --disable-security-cert-validators \
   --disable-strict-error-checking \
   --with-swapdir=%{_localstatedir}/spool/squid \
   --enable-translation
%make_build
%check

make check
%install
%make_install
echo "
ScriptAlias /Squid/cgi-bin/cachemgr.cgi %{_libdir}/squid/cachemgr.cgi
<Location /Squid/cgi-bin/cachemgr.cgi>
 Require local
</Location>" > $RPM_BUILD_ROOT/squid.httpd.tmp
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/NetworkManager/dispatcher.d
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/squid
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/squid
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/squid
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/squid
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_unitdir}
install -m 755 %{SOURCE8} $RPM_BUILD_ROOT%{_libexecdir}/squid
install -m 644 $RPM_BUILD_ROOT/squid.httpd.tmp $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/squid.conf
install -m 755 %{SOURCE6} $RPM_BUILD_ROOT%{_prefix}/lib/NetworkManager/dispatcher.d/20-squid
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/squid
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/spool/squid
chmod 644 contrib/url-normalizer.pl contrib/user-agents.pl
mkdir -p $RPM_BUILD_ROOT/usr/share/snmp/mibs
mv $RPM_BUILD_ROOT/usr/share/squid/mib.txt $RPM_BUILD_ROOT/usr/share/snmp/mibs/SQUID-MIB.txt
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/squid/squid.conf.documented
rm -f $RPM_BUILD_ROOT/squid.httpd.tmp
install -p -D -m 0644 %{SOURCE9} %{buildroot}%{_sysusersdir}/squid.conf
%oreon_autofiles main

%pre

%sysusers_create_compat %{SOURCE9}
for i in /var/log/squid /var/spool/squid ; do
        if [ -d $i ] ; then
                for adir in `find $i -maxdepth 0 \! -user squid`; do
                        chown -R squid:squid $adir
                done
        fi
done
exit 0
%pretrans -p <lua>

-- temporarilly commented until https://bugzilla.redhat.com/show_bug.cgi?id=1936422 is resolved
--
-- previously /usr/share/squid/errors/es-mx was symlink, now it is directory since squid v5
-- see https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement/
-- Define the path to the symlink being replaced below.
--
-- path = "/usr/share/squid/errors/es-mx"
-- st = posix.stat(path)
-- if st and st.type == "link" then
--   os.remove(path)
-- end
-- Due to a bug #447156
paths = {"/usr/share/squid/errors/zh-cn", "/usr/share/squid/errors/zh-tw"}
for key,path in ipairs(paths)
do
  st = posix.stat(path)
  if st and st.type == "directory" then
    status = os.rename(path, path .. ".rpmmoved")
    if not status then
      suffix = 0
      while not status do
        suffix = suffix + 1
        status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
      end
      os.rename(path, path .. ".rpmmoved")
    end
  end
end
%post

%systemd_post squid.service
%preun

%systemd_preun squid.service
%postun

%systemd_postun_with_restart squid.service
%triggerin -- samba-common

if ! getent group wbpriv >/dev/null 2>&1 ; then
  /usr/sbin/groupadd -g 88 wbpriv >/dev/null 2>&1 || :
fi
/usr/sbin/usermod -a -G wbpriv squid >/dev/null 2>&1 || \
    chgrp squid /var/cache/samba/winbindd_privileged >/dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.4-1
- Prepare for Oreon 11 (RP1)
