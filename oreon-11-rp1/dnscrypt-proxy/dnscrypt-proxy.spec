%global source0_hash 495c4f494d40068e5e3ddcb8748d91b90e99f2516060e3b59520b9f3d6148a9e
%bcond check 1
%global goipath         github.com/dnscrypt/dnscrypt-proxy
Version:                2.1.18
%global tag             2.1.14
%gometa -L -f
Name:           dnscrypt-proxy
Release:        1%{?dist}
Summary:        Flexible DNS proxy, with support for encrypted DNS protocols
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND Zlib
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{tag}/%{name}-%{tag}.tar.gz
Patch:          dnscrypt-proxy-2.1.14-custom_config.patch
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
A flexible DNS proxy, with support for modern encrypted DNS protocols such as
DNSCrypt v2, DNS-over-HTTPS, Anonymized DNSCrypt and ODoH (Oblivious DoH).

Features:

 - DNS traffic encryption and authentication. Supports DNS-over-HTTPS (DoH)
   using TLS 1.3 and QUIC, DNSCrypt, Anonymized DNS and ODoH
 - Client IP addresses can be hidden using Tor, SOCKS proxies or Anonymized
   DNS relays
 - DNS query monitoring, with separate log files for regular and suspicious
   queries
 - Filtering: block ads, malware, and other unwanted content. Compatible with
   all DNS services
 - Time-based filtering, with a flexible weekly schedule
 - Transparent redirection of specific domains to specific resolvers
 - Optional hot-reloading of configuration files (disabled by default from
   v2.1.10)
 - DNS caching, to reduce latency and improve privacy
 - Local IPv6 blocking to reduce latency on IPv4-only networks
 - Load balancing: pick a set of resolvers, dnscrypt-proxy will automatically
   measure and keep track of their speed, and balance the traffic across the
   fastest available ones.
 - Cloaking: like a HOSTS file on steroids, that can return preconfigured
   addresses for specific names, or resolve and return the IP address of other
   names. This can be used for local development as well as to enforce safe
   search results on Google, Yahoo, DuckDuckGo and Bing
 - Automatic background updates of resolvers lists
 - Can force outgoing connections to use TCP
 - Compatible with DNSSEC
 - Includes a local DoH server in order to support ECH (ESNI)

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1
rm -rfv dnscrypt-proxy/sources_test.go

%build

%global gomodulesmode GO111MODULE=on
for cmd in dnscrypt-proxy; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm 0644 dnscrypt-proxy/example-dnscrypt-proxy.toml %{buildroot}%{_sysconfdir}/%{name}/dnscrypt-proxy.toml
install -Dpm 0644 dnscrypt-proxy/example-allowed-ips.txt %{buildroot}%{_sysconfdir}/%{name}/allowed-ips.txt
install -Dpm 0644 dnscrypt-proxy/example-allowed-names.txt  %{buildroot}%{_sysconfdir}/%{name}/allowed-names.txt
install -Dpm 0644 dnscrypt-proxy/example-blocked-ips.txt  %{buildroot}%{_sysconfdir}/%{name}/blocked-ips.txt
install -Dpm 0644 dnscrypt-proxy/example-blocked-names.txt  %{buildroot}%{_sysconfdir}/%{name}/blocked-names.txt
install -Dpm 0644 dnscrypt-proxy/example-captive-portals.txt  %{buildroot}%{_sysconfdir}/%{name}/captive-portals.txt
install -Dpm 0644 dnscrypt-proxy/example-cloaking-rules.txt  %{buildroot}%{_sysconfdir}/%{name}/cloaking-rules.txt
install -Dpm 0644 dnscrypt-proxy/example-forwarding-rules.txt  %{buildroot}%{_sysconfdir}/%{name}/forwarding-rules.txt
install -Dpm 0644 %{S:3} %{buildroot}%{_unitdir}/dnscrypt-proxy.service
install -m 0755 -vd %{buildroot}%{_localstatedir}/cache/%{name}
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%post

%systemd_post dnscrypt-proxy.service
%preun

%systemd_preun dnscrypt-proxy.service
%postun

%systemd_postun_with_restart dnscrypt-proxy.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
