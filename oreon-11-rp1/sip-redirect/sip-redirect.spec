%global source0_hash ad1104e1aaa56016a6dece684df93e7a382035de921116f60fc735a7212f459b

Summary:           Tiny IPv4 and IPv6 SIP redirect server written in Perl
Summary(de):       Ein winziger, in Perl geschriebener, SIP Redirekt-Server
Name:              sip-redirect
Version:           0.2.0
Release:           25%{?dist}
License:           GPL-2.0-or-later
URL:               https://ftp.robert-scheck.de/linux/%{name}/
Source0:           https://ftp.robert-scheck.de/linux/%{name}/%{name}-%{version}.tar.gz
Source1:           sip-redirect.sysusersd
BuildArch:         noarch
BuildRequires:     make
BuildRequires:     perl-generators
BuildRequires:     systemd
BuildRequires:     systemd-rpm-macros
Requires:          logrotate
Requires:          perl(Socket) >= 1.95
%{?systemd_requires}
%{?sysusers_requires_compat}

%description
sip-redirect is a tiny SIP redirect server written in Perl. It is IPv4 and
IPv6 capable, but the IPv6 support is optional. The RFC 3261 was the base for
this simple and very configurable implementation. There is neither TCP nor
multicast support programmed in.

%description -l de
sip-redirect ist ein winziger, in Perl geschriebener, SIP Redirekt-Server. Er
unterstützt IPv4 und IPv6, aber der IPv6-Support ist optional. Als Grundlage
für diese einfache und sehr konfigurierbare Implementation wurde die RFC 3261
verwendet. Es wurde keine Unterstützung für TCP und für Multicast eingebaut.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
%make_install

# Declarative allocation of system users and groups
install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf

%pre
%sysusers_create_compat %{SOURCE1}

%post
touch %{_localstatedir}/log/%{name} > /dev/null 2>&1 || :
chown sip:sip %{_localstatedir}/log/%{name} > /dev/null 2>&1 || :
chmod 0640 %{_localstatedir}/log/%{name} > /dev/null 2>&1 || :
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%ghost %attr(0640,sip,sip) %{_localstatedir}/log/%{name}

%changelog
%autochangelog
