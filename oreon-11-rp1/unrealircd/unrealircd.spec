%global source1_hash 684924eb780c536ab2abcb8e4ddb4f7057a21fb1df5f32015018d942efc24299
%global source0_hash e075375f469309bf1d54134bc914ec50a4ae3b09da6d2db2c11f9fa88d649370
%global sslcert %{_sysconfdir}/pki/%{name}/server.cert.pem
%global sslkey  %{_sysconfdir}/pki/%{name}/server.key.pem
%bcond_without  maxmind
%global pcre2   10.44
Summary:        Open Source IRC server
Name:           unrealircd
Version:        6.2.7
Release:        1%{?dist}
License:        GPL-1.0-or-later AND GPL-2.0-or-later AND BSD-3-Clause AND ISC AND LicenseRef-Fedora-Public-Domain AND MIT
URL:            https://www.unrealircd.org/
Source0:        https://www.unrealircd.org/downloads/%{name}-%{version}.tar.gz
Source1:        https://www.unrealircd.org/downloads/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-1D2D2B03A0B68ED11D68A24BA7A21B0A108FF4A9.gpg
Source3:        %{name}.service
Source4:        %{name}.tmpfilesd
Source5:        %{name}.sysusersd
Patch0:         unrealircd-6.0.6-crypto-policy.patch
Patch1:         unrealircd-6.1.8-geoip.patch
Patch2:         unrealircd-6.0.3-unrealircdctl.patch
Provides:       bundled(pcre2) = %{pcre2}
Requires(post): %{_bindir}/openssl
%{?systemd_requires}
%{?sysusers_requires_compat}
# oreon:deps
BuildRequires:  /bin/openssl
BuildRequires:  c-ares-devel
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  jansson-devel
BuildRequires:  libargon2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libmaxminddb-devel
BuildRequires:  libsodium-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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
BuildRequires:  libmaxminddb-devel >= 1.2.0
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
chmod -R g+rX,o+rX $RPM_BUILD_ROOT
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/{examples/example.conf,%{name}.conf}
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/examples/
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/modules.sources.list
rm -f $RPM_BUILD_ROOT%{_bindir}/unrealircd-upgrade-script
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/{%{name}/tls,pki/%{name}}/
ln -s ../pki/%{name}/ $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/tls
ln -sf ../tls/certs/ca-bundle.crt $RPM_BUILD_ROOT%{_sysconfdir}/pki/%{name}/curl-ca-bundle.crt
install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf
mkdir -p $RPM_BUILD_ROOT%{_rundir}/%{name}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n unrealircd-maxmind -f %{oreon_filedir}/unrealircd-maxmind.list

%changelog

%autochangelog
