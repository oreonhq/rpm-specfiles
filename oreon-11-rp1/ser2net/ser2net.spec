%global source0_hash 99ab72b7b252020ae76ece5f883b74155ed94206e243e14066bb67b93f05d7ed
Version:        4.6.8
%global forgeurl https://github.com/cminyard/ser2net
%forgemeta
Name:           ser2net
Release:        1%{?dist}
Summary:        Proxy that allows TCP/UDP to serial port connections
License:        GPL-2.0-only
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.sysusers
%if 0%{?el9}
%else
%endif
%{?sysusers_requires_compat}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libgensio)
BuildRequires:  pkgconfig(libgensiomdns)
BuildRequires:  pkgconfig(libgensioosh)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
ser2net provides a way for a user to connect from a network connection to a 
serial port. It provides all the serial port setup, a configuration file to 
configure the ports, a control login for modifying port parameters, 
monitoring ports, and controlling ports.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%build

autoreconf -f -i
%configure
%make_build
%install
%make_install
install -Dpm0644 %{name}.yaml %{buildroot}%{_sysconfdir}/%{name}/%{name}.yaml
install -Dpm0644 %{name}.service  %{buildroot}%{_unitdir}/%{name}.service
install -Dpm0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf
%oreon_autofiles main

%pre

%sysusers_create_compat %{SOURCE1}
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
