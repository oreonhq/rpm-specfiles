%global source0_hash 06d524155d399be30640d58b4fba976b2917c157d3e3b833d29bd7698a0fe082

%{!?lua_version: %global lua_version %{lua: print(string.sub(_VERSION, 5))}}

%global sslcert    %{_sysconfdir}/pki/%{name}/localhost.crt
%global sslkey     %{_sysconfdir}/pki/%{name}/localhost.key

Summary:           Flexible communications server for Jabber/XMPP
Name:              prosody
Version:           13.0.4
Release:           1%{?dist}
License:           MIT
URL:               https://prosody.im/
Source0:           https://prosody.im/downloads/source/%{name}-%{version}.tar.gz
Source1:           https://prosody.im/downloads/source/%{name}-%{version}.tar.gz.asc
Source2:           https://keys.openpgp.org/vks/v1/by-fingerprint/32A9EDDE3609931EB98CEAC315907E8E7BDD6BFE
Source3:           prosody.service
Source4:           prosody.logrotate
Source5:           prosody.tmpfilesd
Source6:           prosody.sysusersd
Source7:           prosody-localhost.cfg.lua
Source8:           prosody-example.com.cfg.lua
Patch0:            prosody-13.0.0-config.patch
BuildRequires:     gnupg2
BuildRequires:     gcc
BuildRequires:     make
BuildRequires:     libicu-devel
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:     openssl-devel >= 3.0.0
%else
BuildRequires:     openssl3-devel
%endif
BuildRequires:     lua
BuildRequires:     lua-devel
BuildRequires:     systemd-rpm-macros
Requires:          %{_bindir}/openssl
Requires(post):    %{_bindir}/openssl
Requires:          lua(abi) = %{lua_version}
Requires:          lua-filesystem
Requires:          lua-expat
Requires:          lua-socket
Requires:          lua-sec
Recommends:        lua-unbound
Recommends:        lua-readline
%{?systemd_requires}
%{?sysusers_requires_compat}

# Testsuite in %%check
BuildRequires:     lua-filesystem
BuildRequires:     lua-expat
BuildRequires:     lua-socket
BuildRequires:     lua-sec
BuildRequires:     lua-unbound
BuildRequires:     %{_bindir}/openssl
BuildRequires:     %{_sbindir}/ss

%description
Prosody is a flexible communications server for Jabber/XMPP written in Lua.
It aims to be easy to use, and light on resources. For developers it aims
to be easy to extend and give a flexible system on which to rapidly develop
added functionality, or prototype new protocols.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch -P0 -p1 -b .config

# https://fedoraproject.org/wiki/Changes/dropingOfCertPemFile
%if 0%{?fedora} >= 43 || 0%{?rhel} >= 11
sed -e '/^[[:space:]]*cafile = "/d' -i core/certmanager.lua
%endif

%build
./configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --idn-library=icu \
  --add-cflags="$RPM_OPT_FLAGS %{?el8:$(pkg-config --cflags-only-I openssl3)}" \
  --add-ldflags="$RPM_LD_FLAGS %{?el8:$(pkg-config --libs-only-L openssl3)}" \
  --no-example-certs
%make_build

# Make prosody-migrator
%make_build -C tools/migration

%install
mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir}/pki,%{_localstatedir}/{lib,log}/%{name}}/
%make_install

# Install prosody-migrator
%make_install -C tools/migration

# Install ejabberd2prosody
install -p -m 0755 tools/ejabberd2prosody.lua $RPM_BUILD_ROOT%{_bindir}/ejabberd2prosody
sed -e 's@;../?.lua@;%{_libdir}/%{name}/util/?.lua;%{_libdir}/%{name}/?.lua;@' \
  -i $RPM_BUILD_ROOT%{_bindir}/ejabberd2prosody
touch -c -r tools/ejabberd2prosody.lua $RPM_BUILD_ROOT%{_bindir}/ejabberd2prosody
install -p -m 0644 tools/erlparse.lua $RPM_BUILD_ROOT%{_libdir}/%{name}/util/

# Move certificates directory and symlink it
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/certs/ $RPM_BUILD_ROOT%{_sysconfdir}/pki/%{name}/
ln -s ../pki/%{name}/ $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/certs

# Install systemd unit files and tmpfiles
install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}
install -D -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE6} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf
mkdir -p $RPM_BUILD_ROOT/run/%{name}/

# Keep configuration file timestamp
touch -c -r prosody.cfg.lua.dist.config $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/prosody.cfg.lua

# Install virtual host configuration
install -D -p -m 0644 %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/conf.d/localhost.cfg.lua
install -D -p -m 0644 %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/conf.d/example.com.cfg.lua

# Fix permissions for rpmlint
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/%{name}/util/*.so

# Fix incorrect end-of-line encoding
for file in doc/stanza.txt doc/session.txt doc/roster_format.txt; do
  sed -e 's/\r//g' ${file} > ${file}.eol
  touch -c -r ${file} ${file}.eol; mv -f ${file}.eol ${file}
done

%check
# Prepare test environment
mkdir -p tests/data/
cp -prf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/{*.cfg.lua,conf.d/} certs/ tests/
sed -e '/^log = {/,/}/d' -e '/^\(certificates\|pidfile\) =/d' -i tests/%{name}.cfg.lua  # Avoid 'duplicate option' warnings
echo 'certificates = "certs"' >> tests/%{name}.cfg.lua  # Relative to configuration
echo 'log = { "*console" }' >> tests/%{name}.cfg.lua  # Create no log files
echo 'pidfile = "'$PWD'/tests/prosody.pid"' >> tests/%{name}.cfg.lua  # Absolute path
echo 'unbound = { resolvconf = false, hoststxt = false }' >> tests/%{name}.cfg.lua  # Disable /etc/{resolv.conf,hosts} usage
echo 'admin_socket = "'$PWD'/tests/prosody.sock"' >> tests/%{name}.cfg.lua  # Avoid bind error for /run/prosody/prosody.sock
(. ./config.unix 2> /dev/null && sed -e "1s| lua\$| ${RUNWITH}|" -i %{name} %{name}ctl)
sed -e 's/^keysize=.*/keysize=4096/' -i tests/certs/{GNUmakefile,makefile}
make -C tests/certs localhost.crt
export LUA_PATH="$RPM_BUILD_ROOT%{_libdir}/%{name}/?.lua;;"
export LUA_CPATH="$RPM_BUILD_ROOT%{_libdir}/%{name}/?.so;;"
export PROSODY_CFGDIR="$PWD/tests"
export PROSODY_DATADIR="$PWD/tests/data"

# Run some common commands
./%{name}ctl about
./%{name}ctl start
./%{name}ctl status
for cnt in $(seq 1 5); do ss -lnpt | grep :5222 && ss -lnpt | grep :5269 && break || sleep 1; done
echo 'QUIT' | openssl s_client -connect localhost:5222 -starttls xmpp -name localhost -CAfile tests/certs/localhost.crt
echo 'QUIT' | openssl s_client -connect localhost:5269 -starttls xmpp-server -name localhost -CAfile tests/certs/localhost.crt
echo -e 'Fish\nFish' | ./%{name}ctl adduser tux@localhost
ls -l tests/data/localhost/{accounts,account_roles}/tux.dat
echo -e 'Penguin\nPenguin' | ./%{name}ctl passwd tux@localhost
./%{name}ctl deluser tux@localhost
./%{name}ctl stop

%pre
%sysusers_create_compat %{SOURCE6}

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
  chmod 0644 %{sslcert}
fi

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%doc AUTHORS CHANGES HACKERS README doc/*
%{_bindir}/%{name}
%{_bindir}/%{name}ctl
%{_bindir}/%{name}-migrator
%{_bindir}/ejabberd2prosody
%{_libdir}/%{name}/
%dir %attr(0750,root,%{name}) %{_sysconfdir}/pki/%{name}/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/pki/%{name}/*
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/*.cfg.lua
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/conf.d/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/*.cfg.lua
%{_sysconfdir}/%{name}/certs
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%dir %attr(0755,%{name},%{name}) /run/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/log/%{name}/
%{_mandir}/man1/%{name}ctl.1*

%changelog
%autochangelog
