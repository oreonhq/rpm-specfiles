%global source0_hash 1d55dd6005c3aaa95f75c555c7d7f555992a1cf849a93fd2fd6cdfd32ac9ccac

Name:           mod_evasive
Version:        2.4.0
Release:        4%{?dist}
Summary:        Denial of Service evasion module for Apache

License:        GPL-2.0-or-later
URL:            https://github.com/jvdmr/mod_evasive
Source0:        https://github.com/jvdmr/mod_evasive/archive/%{version}.tar.gz
Source1:        mod_evasive.conf

BuildRequires:  httpd-devel, gcc
BuildRequires:  pcre2-devel
Requires:       httpd
Requires:       httpd-mmn = %([ -a %{_includedir}/httpd/.mmn ] && cat %{_includedir}/httpd/.mmn || echo missing)

%description
mod_evasive is an evasive maneuvers module for Apache to provide evasive 
action in the event of an HTTP DoS or DDoS attack or brute force attack. It 
is also designed to be a detection and network management tool, and can be 
easily configured to talk to firewalls, routers, etc. mod_evasive presently 
reports abuses via email and syslog facilities. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build
apxs -Wc,"%{optflags}" -c mod_evasive24.c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -pm 755 \
    $RPM_BUILD_ROOT%{_libdir}/httpd/modules \
    $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
install -pm 755 .libs/mod_evasive24.so $RPM_BUILD_ROOT%{_libdir}/httpd/modules/
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/

%files
%doc README.md LICENSE CHANGELOG
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*
%{_libdir}/httpd/modules/*

%changelog
%autochangelog
