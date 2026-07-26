%global source0_hash 1fe3f25a392b74db1fe62868e19e883acd1dc0e1f318715299920fcc5e166f97

Summary:        Generic RADIUS proxy with RadSec support
Name:           radsecproxy
Version:        1.11.2
Release:        3%{?dist}
License:        BSD-3-Clause
URL:            https://radsecproxy.github.io/
Source0:        https://github.com/radsecproxy/radsecproxy/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/radsecproxy/radsecproxy/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/210FA7FB28E45779777BAA1C5963D59C3D68633B
Source3:        %{name}.conf
Source4:        %{name}.service
Source5:        %{name}.logrotate
Source6:        %{name}.tmpfilesd
Source7:        %{name}.sysusersd
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  nettle-devel
BuildRequires:  openssl-devel
BuildRequires:  systemd-rpm-macros
Requires:       logrotate
%{?systemd_requires}
%{?sysusers_requires_compat}

%description
radsecproxy is a generic RADIUS proxy that in addition to usual RADIUS UDP
transport, also supports TLS (RadSec), as well as RADIUS over TCP and DTLS.
The aim is for the proxy to have sufficient features to be flexible, while
at the same time to be small, efficient and easy to configure.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build
%configure
%make_build

%install
%make_install

mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir}/pki,%{_rundir},%{_localstatedir}/{lib,log}}/%{name}/
install -D -p -m 0640 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}
install -D -p -m 0644 %{SOURCE6} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE7} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf
chmod 644 tools/*.sh

%check
make check

%pre
%sysusers_create_compat %{SOURCE7}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc AUTHORS ChangeLog radsecproxy.conf-example THANKS tools
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %attr(0750,root,%{name}) %{_sysconfdir}/pki/%{name}/
%{_bindir}/%{name}-conf
%{_bindir}/%{name}-hash
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/%{name}-hash.8*
%{_mandir}/man5/%{name}.conf.5*
%dir %attr(0750,%{name},%{name}) %{_rundir}/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/log/%{name}/

%changelog
%autochangelog
