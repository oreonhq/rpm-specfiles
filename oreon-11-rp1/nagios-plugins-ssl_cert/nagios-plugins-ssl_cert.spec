%global source0_hash 1d87a862678769bfff474fa418c76b3cb91e88f31b3fa4dfa1d9deb2e1cecbb0
%global nagiospluginsdir %{_libdir}/nagios/plugins
Name:           nagios-plugins-ssl_cert
Version:        2.54.0
Release:        1%{?dist}
Summary:        Nagios Plugin - check_ssl_cert
License:        GPL-3.0-or-later
URL:            https://exchange.nagios.org/directory/Plugins/Network-Protocols/HTTP/check_ssl_cert/details
Source0:        https://github.com/matteocorti/check_ssl_cert/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       /usr/bin/bash
Requires:       /usr/bin/bc
Requires:       /usr/bin/curl
Requires:       /usr/bin/date
Requires:       /usr/bin/openssl
Requires:       nagios-plugins
Requires:       perl(Date::Parse)
Recommends:     /usr/bin/dig
Recommends:     /usr/bin/expand
Recommends:     /usr/bin/timeout
Recommends:     /usr/sbin/ip
%global debug_package %{nil}
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
A POSIX shell script (that can be used as a Nagios/Icinga plugin) to check an
SSL/TLS connection and certificate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir check_ssl_cert-%{version}
%oreon_prep
%build

%install
%make_install DESTDIR=%{buildroot}/%{nagiospluginsdir} MANDIR=%{buildroot}/%{_mandir}
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
