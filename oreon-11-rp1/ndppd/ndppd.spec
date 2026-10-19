%global source0_hash 969d438462e0c65a8c9060d8d263c5c47ba8145fb9aaa663864bbad11ad7eb7a
Name:           ndppd
Version:        0.2.6
Release:        1%{?dist}
Summary:        NDP Proxy Daemon
License:        GPL-3.0-or-later
URL:            https://github.com/DanielAdolfsson/ndppd
Source0:        https://github.com/DanielAdolfsson/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.conf
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
ndppd, or NDP Proxy Daemon, is a daemon that proxies neighbor discovery
messages. It listens for neighbor solicitations on a specified interface
and responds with neighbor advertisements - as described in RFC 4861
section 7.2.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%make_build
%install
%make_install PREFIX="%{_prefix}" SBINDIR="%{buildroot}%{_sbindir}"
install -Dpm0644 -t %{buildroot}%{_unitdir} ndppd.service
install -Dpm0644 %SOURCE1 %{buildroot}%{_tmpfilesdir}/ndppd.conf
install -dm0755 %{buildroot}/run/%{name}
install -Dpm0644 ndppd.conf-dist %{buildroot}%{_sysconfdir}/ndppd.conf
%oreon_autofiles main

%postun

%systemd_postun_with_restart %{name}.service
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
