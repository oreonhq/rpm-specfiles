%global source0_hash 659b012ffdcf9737cc05821e1b66589bb58b182fb79b6336a67834d04b2d20a3

%global sslcert %{_sysconfdir}/pki/%{name}/server.cert.pem
%global sslkey  %{_sysconfdir}/pki/%{name}/server.key.pem

%bcond_without  maxmind
%global pcre2   10.44

Summary:        Open Source IRC server
Name:           unrealircd
Version:        6.1.10
Release:        3%{?dist}
# UnrealIRCd declares itself as GPL-2.0-or-later as it's the common denominator for
# a GPL-1.0-or-later and GPL-2.0-or-later mixture, breakdown of other source codes:
# BSD-3-Clause: include/mempool.h and src/mempool.c
# ISC: src/openssl_hostname_validation.c
# LicenseRef-Fedora-Public-Domain: include/crypt_blowfish.h and src/crypt_blowfish.c
# MIT: include/openssl_hostname_validation.h
License:        GPL-1.0-or-later AND GPL-2.0-or-later AND BSD-3-Clause AND ISC AND LicenseRef-Fedora-Public-Domain AND MIT
URL:            https://www.unrealircd.org/
Source0:        https://www.unrealircd.org/downloads/%{name}-%{version}.tar.gz
Source1:        https://www.unrealircd.org/downloads/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-1D2D2B03A0B68ED11D68A24BA7A21B0A108FF4A9.gpg
Source3:        %{name}.service
Source4:        %{name}.tmpfilesd
Source5:        %{name}.sysusersd
# Apply Fedora system-wide crypto policy
Patch0:         unrealircd-6.0.6-crypto-policy.patch
# Disable GeoIP to avoid dependency to legacy GeoIP
Patch1:         unrealircd-6.1.8-geoip.patch
# Same options like in unrealircd(ctl) shell script
Patch2:         unrealircd-6.0.3-unrealircdctl.patch
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  %{_bindir}/openssl
BuildRequires:  openssl-devel
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  pcre2-devel >= 10.36
%else
Provides:       bundled(pcre2) = %{pcre2}
%endif
BuildRequires:  libargon2-devel >= 20161029
BuildRequires:  libsodium-devel >= 1.0.16
BuildRequires:  c-ares-devel >= 1.6.0
BuildRequires:  jansson-devel >= 2.0.0
BuildRequires:  libcurl-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  systemd-rpm-macros
Requires(post): %{_bindir}/openssl
%{?systemd_requires}
%{?sysusers_requires_compat}

%description
UnrealIRCd is an Open Source IRC server based on the branch of IRCu called
Dreamforge, formerly used by the DALnet IRC network. Since the beginning of
development on UnrealIRCd in May of 1999, it has become a highly advanced
IRCd with a strong focus on modularity, an advanced and highly configurable
configuration file. Key features include SSL/TLS, cloaking, advanced anti-
flood and anti-spam systems, swear filtering and module support.

%if %{with maxmind}
%package maxmind
Summary:        GeoIP module using MaxMind databases for UnrealIRCd
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  libmaxminddb-devel >= 1.4.3
%else
BuildRequires:  libmaxminddb-devel >= 1.2.0
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description maxmind
UnrealIRCd is an Open Source IRC server with a strong focus on modularity.

This package provides an UnrealIRCd module to support GeoIP using MaxMind's
GeoIP2 C library and databases.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch -P0 -p1 -b .crypto-policy
touch -c -r doc/conf/examples/example.conf{.crypto-policy,}
%patch -P1 -p1 -b .geoip
touch -c -r doc/conf/modules.default.conf{.geoip,}
%patch -P2 -p1 -b .unrealircdctl

# Ensure the bundled PCRE2 tarball matches the version in this spec file
! tar tfz extras/pcre2.tar.gz | grep -E -m 1 -v '^pcre2-%{pcre2}/'

%build
%if 0%{?rhel} == 8
# Bundling option for PCRE2 in UnrealIRCd itself is not really suitable for
# distribution packaging, thus build it first and pretend it as system one.
BUNDLED=$PWD/extras/pcre2
tar xfz extras/pcre2.tar.gz -C extras
cd extras/pcre2-%{pcre2}/
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure --enable-jit --enable-shared=no
%make_build
%make_install DESTDIR=$BUNDLED
cd $OLDPWD
sed \
  -e "s|^libdir=.*|libdir=$BUNDLED%{_libdir}|" \
  -e "s|^includedir=.*|includedir=$BUNDLED%{_includedir}|" \
  -i $BUNDLED%{_libdir}/pkgconfig/libpcre2-8.pc
export PKG_CONFIG_PATH="$BUNDLED%{_libdir}/pkgconfig"
%endif

# https://github.com/unrealircd/unrealircd/pull/183
%if %{with maxmind} && 0%{?rhel} == 8
sed -e 's|libmaxminddb >= 1.4.3|libmaxminddb >= 1.2.0|g' -i configure
%endif

# Mention new unrealircdctl tool rather than shell script
for file in src/{conf,ircd,misc,modulemanager,proc_io_server,unrealircdctl}.c doc/conf/examples/*.conf; do
  sed -e 's|\./unrealircd\([ "]\)|unrealircdctl\1|g' ${file} > ${file}.tmp
  touch -c -r ${file} ${file}.tmp && mv -f ${file}.tmp ${file}
done

%configure \
  --enable-ssl \
  --with-system-pcre2 \
  --with-system-argon2 \
  --with-system-sodium \
  --with-system-cares \
  --with-system-jansson \
  --enable-libcurl \
  %{?with_maxmind:--enable-libmaxminddb=yes} \
  --with-bindir=%{_bindir} \
  --with-scriptdir=unused \
  --with-confdir=%{_sysconfdir}/%{name} \
  --with-modulesdir=%{_libdir}/%{name} \
  --with-logdir=%{_localstatedir}/log/%{name} \
  --with-cachedir=%{_localstatedir}/cache/%{name} \
  --with-tmpdir=%{_localstatedir}/lib/%{name}/tmp \
  --with-datadir=%{_localstatedir}/lib/%{name} \
  --with-docdir=unused \
  --with-pidfile=%{_rundir}/%{name}/%{name}.pid \
  --with-controlfile=%{_rundir}/%{name}/%{name}.ctl \
  --with-permissions=0640 \
  --enable-dynamic-linking \
  --with-privatelibdir=no
%make_build

%install
%make_install

# Fix strange default permissions
chmod -R g+rX,o+rX $RPM_BUILD_ROOT

# Provide default configuration based on default example
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/{examples/example.conf,%{name}.conf}
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/examples/

# Remove module repository configuration (for module manager)
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/modules.sources.list

# Remove upgrade script intended only for source code users
rm -f $RPM_BUILD_ROOT%{_bindir}/unrealircd-upgrade-script

# Move tls directory and symlink it
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/{%{name}/tls,pki/%{name}}/
ln -s ../pki/%{name}/ $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/tls
ln -sf ../tls/certs/ca-bundle.crt $RPM_BUILD_ROOT%{_sysconfdir}/pki/%{name}/curl-ca-bundle.crt

# Install systemd and tmpfiles files
install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf
mkdir -p $RPM_BUILD_ROOT%{_rundir}/%{name}/

%pre
%sysusers_create_compat %{SOURCE5}

%post
%systemd_post %{name}.service

if [ ! -f %{sslkey} ]; then
  umask 077
  %{_bindir}/openssl genrsa 4096 > %{sslkey} 2> /dev/null
  chown root:%{name} %{sslkey}
  chmod 640 %{sslkey}
fi

if [ ! -f %{sslcert} ]; then
  FQDN=`hostname 2> /dev/null`
  if [ "x${FQDN}" = "x" ]; then
    FQDN=localhost.localdomain
  fi

  %{_bindir}/openssl req -new -key %{sslkey} -x509 -sha256 -days 365 -set_serial $RANDOM -out %{sslcert} \
    -subj "/C=--/ST=SomeState/L=SomeCity/O=SomeOrganization/OU=SomeOrganizationalUnit/CN=${FQDN}/emailAddress=root@${FQDN}"
  chmod 644 %{sslcert}
fi

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc doc/Authors doc/coding-guidelines doc/tao.of.irc
%doc README.md doc/RELEASE-NOTES.md
%dir %attr(0750,root,%{name}) %{_sysconfdir}/pki/%{name}/
%{_sysconfdir}/pki/%{name}/curl-ca-bundle.crt
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/*.conf
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/aliases/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/aliases/*.conf
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/help/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/help/*.conf
%{_sysconfdir}/%{name}/tls
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{_bindir}/%{name}
%{_bindir}/unrealircdctl
%{_libdir}/%{name}/
%{?with_maxmind:%exclude %{_libdir}/%{name}/geoip_maxmind.so}
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/cache/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}/tmp/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/log/%{name}/
%dir %attr(0755,%{name},%{name}) %{_rundir}/%{name}/

%if %{with maxmind}
%files maxmind
%{_libdir}/%{name}/geoip_maxmind.so
%endif

%changelog
%autochangelog
