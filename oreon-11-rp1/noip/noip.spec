%global source0_hash 82b9bafab96a0c53b21aaef688bf70b3572e26217b5e2072bdb09da3c4a6f593
Name:		noip
Version:	2.1.9
Release:        45%{?dist}
Summary:        A dynamic DNS update client
License:	GPL-2.0-or-later
URL:		http://www.no-ip.com
Source0:        http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz
Source1:	noip.service
Patch0:		noip.patch
%{?systemd_requires}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
Keep your current IP address in sync with your No-IP host or domain with 
this Dynamic Update Client (DUC). The client continually checks for IP 
address changes in the background and automatically updates the DNS at 
No-IP whenever it changes.

N.B. You need to run
	%# noip2 -C
before starting the service.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-1
%patch -P0 -p1
sed -i 's|@OPTFLAGS@|%{optflags}|g;s|@SBINDIR@|%{buildroot}%{_sbindir}|g;s|@SYSCONFDIR@|%{buildroot}%{_sysconfdir}|g' Makefile

# Create a sysusers.d config file
cat >noip.sysusers.conf <<EOF
u noip - 'No-ip daemon user' /var/run/noip -
EOF

%build

make %{?_smp_mflags}
%install
install -D -p -m 755 noip2 %{buildroot}/%{_sbindir}/noip2
mkdir -p %{buildroot}/%{_sysconfdir}
touch %{buildroot}/%{_sysconfdir}/no-ip2.conf
install -Dm644  %{SOURCE1} %{buildroot}%{_unitdir}/noip.service
install -m0644 -D noip.sysusers.conf %{buildroot}%{_sysusersdir}/noip.conf
%oreon_autofiles main

%post

%systemd_post noip.service
%preun

%systemd_preun noip.service
%postun

%systemd_postun_with_restart noip.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
