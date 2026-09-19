%global source0_hash a4622e817d2b2a9b878653f085585bd57f3838cc546cca6028d3b73ffcac0d52

%define _hardened_build 1

Name:           ahcpd
Version:        0.53
Release:        37%{?dist}
Summary:        Ad-hoc network configuration daemon

License:        MIT
URL:            http://www.pps.univ-paris-diderot.fr/~jch/software/ahcp/
Source0:        http://www.pps.univ-paris-diderot.fr/~jch/software/files/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.conf
Source3:        %{name}.logrotate
BuildRequires: 	systemd gcc
BuildRequires: make

%description
AHCP is a configuration protocol that can replace DHCP on networks without 
transitive connectivity, such as mesh networks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="%{?__global_ldflags}" %{?_smp_mflags}

%install
install -Dpm 755 ahcpd $RPM_BUILD_ROOT%{_sbindir}/ahcpd
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -Dpm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/ahcpd.conf
install -Dpm 644 ahcpd.man $RPM_BUILD_ROOT/%{_mandir}/man8/ahcpd.8
install -Dp -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/ahcpd
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/ahcpd/leases/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ahcp/
install -Dpm 755 ahcp-config.sh $RPM_BUILD_ROOT%{_sysconfdir}/ahcp/ahcp-config.sh

%post
%systemd_post ahcpd.service
  
%preun
%systemd_preun ahcpd.service

%postun
%systemd_postun ahcpd.service

%files
%doc CHANGES LICENCE README
%{_sbindir}/ahcpd
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/ahcpd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/ahcpd
%{_mandir}/man8/ahcpd.8.gz
%ghost %attr(0600,root,root) %{_localstatedir}/log/ahcpd.log
%config(noreplace) %{_sysconfdir}/ahcp/

%changelog
%autochangelog
