%global source0_hash c4ed13c04880ccc3a85a99645dcb64134beac8ab0607fe32a4d07e1057ad73b7
%define _hardened_build 1
Name:           babeld
Version:        1.14
Release:        1%{?dist}
Summary:        Ad-hoc network routing daemon
License:        MIT
URL:            http://www.pps.univ-paris-diderot.fr/~jch/software/babel/
Source0:        http://www.pps.univ-paris-diderot.fr/~jch/software/files/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.conf
Source3:        %{name}.logrotate
Conflicts:      quagga
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
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
%oreon_autofiles main

%post

%systemd_post babeld.service
%preun

%systemd_preun babeld.service
%postun

%systemd_postun_with_restart babeld.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
