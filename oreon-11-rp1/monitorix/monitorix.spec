%global source0_hash 0dcd356827d3fc1ce251fe4871b595575e96d8e49e9bdceef82d9a05ae14f363

%global __requires_exclude perl\\(Monitorix\\)|perl\\(HTTPServer\\)
%global __provides_exclude perl\\(

Name:              monitorix
Version:           3.16.0
Release:           4%{?dist}
Summary:           A free, open source, lightweight system monitoring tool
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:           GPL-2.0-or-later
URL:               http://www.monitorix.org
Source0:           http://www.monitorix.org/%{name}-%{version}.tar.gz
BuildArch:         noarch
BuildRequires:     perl-interpreter
BuildRequires:     perl-generators
BuildRequires:     systemd
Requires:          logrotate
Requires:          perl(DBD::mysql)
Requires:          perl(DBD::Pg)
Requires:          perl(IO::Socket::SSL)
Requires:          perl(Time::HiRes)
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

%description
Monitorix is a free, open source and lightweight system monitoring tool
designed to monitor as many services and system resources as possible. It has
been created to be used under production Linux/UNIX servers, but due to its
simplicity and small size may also be used on embedded devices as well.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i 's|#!/usr/bin/env perl|#!/usr/bin/perl|' %{name}
sed -i 's|#!/usr/bin/env perl|#!/usr/bin/perl|' %{name}.cgi

%build
# Nothing to build.

%install
install -pDm644 docs/%{name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/conf.d
install -pDm644 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -pDm755 %{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_prefix}/lib/%{name}
install -pDm644 lib/*.pm %{buildroot}%{_prefix}/lib/%{name}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/www
install -pDm644 logo_top.png %{buildroot}%{_sharedstatedir}/%{name}/www
install -pDm644 logo_bot.png %{buildroot}%{_sharedstatedir}/%{name}/www
install -pDm644 %{name}ico.png %{buildroot}%{_sharedstatedir}/%{name}/www
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/www/imgs
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/www/cgi
install -pDm755 %{name}.cgi %{buildroot}%{_sharedstatedir}/%{name}/www/cgi
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/www/css
install -pDm644 css/*.css %{buildroot}%{_sharedstatedir}/%{name}/www/css
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/reports
install -pDm644 reports/*.html %{buildroot}%{_sharedstatedir}/%{name}/reports
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/usage
mkdir -p %{buildroot}%{_mandir}/man5
mkdir -p %{buildroot}%{_mandir}/man8
install -pDm644 man/man5/%{name}.conf.5 %{buildroot}%{_mandir}/man5
install -pDm644 man/man8/%{name}.8 %{buildroot}%{_mandir}/man8
install -pDm644 docs/%{name}.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -pDm644 docs/%{name}.service %{buildroot}%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc Changes README README.nginx
%doc docs/%{name}-alert.sh docs/%{name}-apache.conf docs/%{name}-lighttpd.conf
%doc docs/htpasswd.pl
%license COPYING
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%dir %{_sysconfdir}/%{name}/conf.d
%dir %{_sharedstatedir}/%{name}/
%dir %{_sharedstatedir}/%{name}/www
%dir %{_sharedstatedir}/%{name}/www/cgi
%dir %{_sharedstatedir}/%{name}/www/css
%dir %{_sharedstatedir}/%{name}/reports
%{_sharedstatedir}/%{name}/www/css/*.css
%{_sharedstatedir}/%{name}/reports/*.html
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man8/%{name}.8*
%{_unitdir}/%{name}.service
%{_bindir}/%{name}
%{_prefix}/lib/%{name}/
%{_sharedstatedir}/%{name}/www/logo_top.png
%{_sharedstatedir}/%{name}/www/logo_bot.png
%{_sharedstatedir}/%{name}/www/%{name}ico.png
%{_sharedstatedir}/%{name}/www/cgi/%{name}.cgi
%attr(755,nobody,nobody) %{_sharedstatedir}/%{name}/www/imgs
%attr(755,root,root) %{_sharedstatedir}/%{name}/usage

%changelog
%autochangelog
