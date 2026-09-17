%global source0_hash 15f24d26da0ccfc073abcdef0309f281e4684f2aa71126f826572c4c845e8dd9

%define _hardened_build 1

Name:           babeld
Version:        1.13.1
Release:        8%{?dist}
Summary:        Ad-hoc network routing daemon

License:        MIT
URL:            http://www.pps.univ-paris-diderot.fr/~jch/software/babel/
Source0:        http://www.pps.univ-paris-diderot.fr/~jch/software/files/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.conf
Source3:        %{name}.logrotate
BuildRequires:	systemd gcc
BuildRequires: make
Conflicts:      quagga

%description
Babel is a loop-avoiding distance-vector routing protocol roughly
based on HSDV and AODV, but with provisions for link cost estimation
and redistribution of routes from other routing protocols.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
install -Dpm 755 babeld $RPM_BUILD_ROOT%{_sbindir}/babeld
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -Dpm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/babeld.conf
install -Dpm 644 babeld.man $RPM_BUILD_ROOT/%{_mandir}/man8/babeld.8
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/lib/
install -Dp -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/babeld

%post
%systemd_post babeld.service
  
%preun
%systemd_preun babeld.service

%postun
%systemd_postun_with_restart babeld.service

%files
%license LICENCE
%doc CHANGES README
%{_sbindir}/babeld
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/babeld.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/babeld
%{_mandir}/man8/babeld.8.*
%ghost %attr(0600,root,root) %{_localstatedir}/lib/babel-state
%ghost %attr(0600,root,root) %{_localstatedir}/log/babel.log

%changelog
%autochangelog
