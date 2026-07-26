%global source0_hash 98c297cdeaa0d8f7d792f18beeaba039e966fc8d9f66752276aebfba05c31dad

Summary:        Postfix policyd to combine complex restrictions in a ruleset
Name:           postfwd
Version:        2.03
Release:        13%{?dist}
License:        BSD-3-Clause
URL:            https://postfwd.org/
Source0:        https://github.com/postfwd/postfwd/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.sysconfig
Source3:        %{name}.tmpfilesd
Source4:        %{name}.sysusersd
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  systemd-rpm-macros
Requires:       perl(Digest::MD5)
Requires:       perl(Net::CIDR::Lite)
Requires:       perl(NetAddr::IP)
Requires:       perl(Storable)
Requires:       perl(Time::HiRes)
Requires:       %{_bindir}/more
Requires:       %{_bindir}/pod2text
%{?systemd_requires}
%{?sysusers_requires_compat}

%description
Postfwd is written in Perl to combine complex Postfix restrictions in a
ruleset similar to those of the most firewalls. The program uses the
Postfix policy delegation protocol to control access to the mail system
before a message has been accepted. It allows to choose an action (e.g.
reject, dunno) for a combination of several SMTP parameters (like sender
and recipient address, size or the client's TLS fingerprint).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT{%{_localstatedir}/lib,%{_rundir}}/%{name}/
install -D -p -m 0755 sbin/%{name}3 $RPM_BUILD_ROOT%{_sbindir}/%{name}3
ln -s %{name}3 $RPM_BUILD_ROOT%{_sbindir}/%{name}
install -D -p -m 0640 etc/%{name}.cf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/%{name}.cf
install -D -p -m 0644 man/man8/%{name}3.8 $RPM_BUILD_ROOT%{_mandir}/man8/%{name}3.8
ln -sf %{name}3.8.gz $RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8.gz
install -D -p -m 0755 tools/%{name}-client.pl $RPM_BUILD_ROOT%{_bindir}/%{name}-client
install -D -p -m 0755 tools/hapolicy/hapolicy $RPM_BUILD_ROOT%{_libexecdir}/%{name}/hapolicy
install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf

# Rename changelog for %%doc inclusion
mv -f doc/postfwd3.CHANGELOG CHANGELOG

%pre
%sysusers_create_compat %{SOURCE4}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license doc/LICENSE
%doc README.md CHANGELOG {etc,plugins}/postfwd.*.sample*
%doc doc/{arch,quick}.html doc/postfwd-ARCH.png doc/postfwd3.{html,txt}
%doc tools/hapolicy/hapolicy.{html,txt} tools/hapolicy/hapolicy0?.png
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/%{name}.cf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{_bindir}/%{name}-client
%{_sbindir}/%{name}
%{_sbindir}/%{name}3
%dir %{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/hapolicy
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/%{name}3.8*
%dir %attr(0750,%{name},%{name}) %{_rundir}/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}/

%changelog
%autochangelog
