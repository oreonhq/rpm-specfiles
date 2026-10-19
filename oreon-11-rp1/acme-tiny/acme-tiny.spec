%global source0_hash c036e6e62037f5736c5c6810b6e3fd951f33dc4cda41cc169d7800d06e6ba3d0
%global use_python3 0
Name:		acme-tiny
Version:	5.0.3
Release:        1%{?dist}
Summary:        Tiny auditable script to issue, renew Let's Encrypt certificates
License:	MIT
URL:		https://github.com/diafygi/%{name}
Source0:        https://github.com/diafygi/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	acme-tiny-sign.sh
Source2:	cert-check.py
Source3:	acme.conf
Source6:	acme-tiny.timer
Source7:	acme-tiny.service
Source8:	README-fedora.md
Source9:	notify.sh
Source10:	acme-tiny-notify.service
Source11:	acme-tiny.conf
Requires(pre): shadow-utils
%{?systemd_requires}
Requires: %{name}-core = %{version}-%{release}
BuildArch:	noarch
# oreon:deps
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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
%oreon_autofiles acme-tiny-core usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n acme-tiny-core -f %{oreon_filedir}/acme-tiny-core.list

%changelog

%autochangelog
