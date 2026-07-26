%global source0_hash 8205736d0de258283e337f6fbc35892cb54fac19e10b770f4dc8b0941b1a08a5

%if 0%{?fedora} || 0%{?rhel} > 7
# Explicity require python3 on Fedora to help track which packages 
# no longer need python2.
%global use_python3 1
%else
%global use_python3 0
%endif

Name:		acme-tiny
Version:	5.0.1
Release:	14%{?dist}
Summary:	Tiny auditable script to issue, renew Let's Encrypt certificates

License:	MIT
URL:		https://github.com/diafygi/%{name}
Source0:	https://github.com/diafygi/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	acme-tiny-sign.sh
Source2:	cert-check.py
Source3:	acme.conf
Source6:	acme-tiny.timer
Source7:	acme-tiny.service
Source8:	README-fedora.md
# simple script hook to kick services when cert is updated
Source9:	notify.sh
Source10:	acme-tiny-notify.service
Source11:	acme-tiny.conf

Requires(pre): shadow-utils
BuildRequires: systemd-rpm-macros
%{?systemd_requires}
Requires: %{name}-core = %{version}-%{release}
BuildArch:	noarch
%if 0%{?fedora}
Suggests: httpd, mod_ssl, nginx
Enhances: httpd, mod_ssl, nginx
%endif

%description
This is a tiny, auditable script that you can throw on your server to issue and
renew Let's Encrypt certificates. Since it has to be run on your server and
have access to your private Let's Encrypt account key, I tried to make it as
tiny as possible (currently less than 200 lines). The only prerequisites are
python and openssl.  

Well, that and a web server - but then you only need this with a web server.
This package adds a simple directory layout and timer service that runs
acme_tiny on installed CSRs as the acme user for privilege separation.

%package core
Summary: Core python module of acme-tiny
Requires:	openssl
%if 0%{?rhel} >= 5 && 0%{?rhel} < 7
# EL6 uses python2.6, which does not include argparse
Requires:	python-argparse
%endif
BuildArch: noarch

%description core
Includes only the core acme_tiny.py script and its dependencies.
Alternate frameworks that use acme_tiny.py can install this to avoid pulling in
unneeded packages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE8} .
sed -i.orig -e '1,1 s,^.*python$,#!/usr/bin/python,' acme_tiny.py
%if %{use_python3}
sed -i.old -e '1,1 s/python$/python3/' *.py
%endif

echo 'u acme - "Tiny Auditable ACME Client" %{_sharedstatedir}/acme' >acme.sysusers.conf

%build

%install
mkdir -p %{buildroot}/var/www/challenges
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_sharedstatedir}/acme/{private,csr,certs,.notify}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/notify.d
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
chmod 0700 %{buildroot}%{_sharedstatedir}/acme/private

install -m 0755 acme-tiny-sign.sh %{buildroot}%{_libexecdir}/%{name}/sign
install -m 0755 %{SOURCE9} %{buildroot}%{_libexecdir}/%{name}/notify
install -m 0755 acme_tiny.py %{buildroot}%{_sbindir}/acme_tiny
ln -sf acme_tiny %{buildroot}%{_sbindir}/%{name}
ln -sf %{_libexecdir}/%{name}/sign %{buildroot}%{_sbindir}/acme-tiny-sign
ln -sf %{_libexecdir}/%{name}/notify %{buildroot}%{_sysconfdir}/%{name}/notify.sh
install -m 0755 cert-check.py %{buildroot}%{_sbindir}/cert-check
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/httpd/conf.d
mkdir -p %{buildroot}%{_unitdir}
install -pm 644	 %{SOURCE6} %{buildroot}%{_unitdir}
install -pm 644	 %{SOURCE7} %{buildroot}%{_unitdir}
install -pm 644	 %{SOURCE10} %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -m 0644 -D acme.sysusers.conf %{buildroot}%{_sysusersdir}/acme.conf

%pre
getent group acme > /dev/null || groupadd -r acme
getent passwd acme > /dev/null || /usr/sbin/useradd -g acme \
	-c "Tiny Auditable ACME Client" \
	-r -d %{_sharedstatedir}/acme -s /sbin/nologin acme
exit 0

%post
%systemd_post acme-tiny.service acme-tiny-notice.service acme-tiny.timer

%postun
%systemd_postun_with_restart acme-tiny.service acme-tiny-notice.service acme-tiny.timer

%preun
%systemd_preun acme-tiny.service acme-tiny-notice.service acme-tiny.timer

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README-fedora.md
%attr(0755,acme,acme) /var/www/challenges
%attr(-,acme,acme) %{_sharedstatedir}/acme
%{_libexecdir}/%{name}
%config(noreplace) %{_sysconfdir}/httpd/conf.d/acme.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/*
%{_sbindir}/acme-tiny-sign
%{_sbindir}/cert-check
%{_sbindir}/%{name}
%{_sysconfdir}/%{name}
%{_sysusersdir}/acme.conf

%files core
%license LICENSE
%doc README.md
%{_sbindir}/acme_tiny

%changelog
%autochangelog
