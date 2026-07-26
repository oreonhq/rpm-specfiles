%global source0_hash 2388e76ff7c4d47658f9ee500166fd60f3953a93d9e9225a61ebb1ea768231e6

Name:         poweradmin
Version:      2.1.7
Release:      23%{?dist}
Summary:      A friendly web-based DNS administration tool for Bert Hubert's PowerDNS server

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:      GPL-3.0-or-later
URL:          http://www.poweradmin.org
Source0:      https://www.poweradmin.org/download/%{name}-%{version}.tgz
Source1:      %{name}.conf
Source2:      %{name}-config.inc.php
Source3:      README.Fedora
BuildArch:    noarch

Requires:     httpd
Requires:     php
Requires:     php-pear(MDB2_Driver_mysqli)
Requires:     php-pear(MDB2_Driver_pgsql)
Requires:     php-mcrypt

%description
Poweradmin is a friendly web-based DNS administration tool for Bert Hubert's
PowerDNS server. The interface has full support for most of the features of
PowerDNS. It has full support for all zone types (master, native and slave),
for supermasters for automatic provisioning of slave zones, full support
for IPv6 and comes with multi-language support.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build

%install
%{__mkdir} -pv %{buildroot}/%{_datadir}/%{name}
%{__mkdir} -pv %{buildroot}/%{_sysconfdir}/httpd/conf.d/
%{__mkdir} -p %{buildroot}/%{_sysconfdir}/%{name}

%{__cp} -adpv ./* %{buildroot}/%{_datadir}/%{name}
%{__cp} -pv %{SOURCE1} %{buildroot}/%{_sysconfdir}/httpd/conf.d/%{name}.conf

%{__cp} %{SOURCE2} %{buildroot}/%{_sysconfdir}/%{name}/config.inc.php
%{__cp} %{SOURCE3} .
ln -s %{_sysconfdir}/%{name}/config.inc.php %{buildroot}/%{_datadir}/%{name}/inc/config.inc.php

%{__rm} -rfv %{buildroot}/%{_datadir}/%{name}/install
%{__rm} -rfv %{buildroot}/%{_datadir}/%{name}/README.md
%{__rm} -rfv %{buildroot}/%{_datadir}/%{name}/LICENSE

%files
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config.inc.php
%doc LICENSE README.md README.Fedora

%changelog
%autochangelog
