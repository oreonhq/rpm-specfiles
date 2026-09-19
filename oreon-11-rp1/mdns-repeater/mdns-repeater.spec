%global source0_hash e9595a75a0511236892f69fde66cbf81bc08f9cec5363b1f726ff56299ad9968

Summary:        Multicast DNS repeater
Name:           mdns-repeater
Version:        1.11
Release:        15%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/kennylevinsen/mdns-repeater
Source0:        https://github.com/kennylevinsen/mdns-repeater/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.sysconfig
Source3:        %{name}.tmpfilesd
Patch0:         mdns-repeater-1.11-pidfile.patch
BuildRequires:  gcc
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}

%description
mdns-repeater is a Multicast DNS repeater for Linux. Multicast DNS
uses the 224.0.0.51 address, which is "administratively scoped" and
does not leave the subnet.

This program re-broadcasts mDNS packets from one interface to other
interfaces.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
gcc \
  $RPM_OPT_FLAGS $RPM_LD_FLAGS \
  -DHGVERSION="\"%{version}\"" \
  -DPIDFILE="\"%{_rundir}/%{name}/%{name}.pid\"" \
  %{name}.c -o %{name}

%install
install -D -p -m 0755 %{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}
install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
mkdir -p $RPM_BUILD_ROOT%{_rundir}/%{name}/

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE.txt
%doc README.txt
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%{_sbindir}/%{name}
%dir %attr(0750,root,root) %{_rundir}/%{name}/

%changelog
%autochangelog
