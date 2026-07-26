%global source0_hash d30ee75067b857773df84d540e09dc578223a43afe30ec4887fd2f6ac493dc9c

Name: sqm-scripts
Version: 1.6.0
Release: 7%{?dist}
Summary: Traffic shaper scripts for Smart Queue Management
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: https://www.bufferbloat.net/projects/cerowrt/wiki/Smart_Queue_Management/
Source0: https://github.com/tohojo/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Workaround for network-manager bug: https://github.com/tohojo/sqm-scripts/pull/129
Patch0: %{name}-1.4.0-run_service_after_network.patch
BuildArch: noarch
BuildRequires: make
%if 0%{?rhel}
BuildRequires: systemd
%else
BuildRequires: systemd-rpm-macros
%endif

%description
"Smart Queue Management", or "SQM" is shorthand for an integrated network
system that performs better per-packet/per flow network scheduling, active
queue length management (AQM), traffic shaping/rate limiting, and QoS
(prioritization).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%{make_build}

%install
%{make_install} UNIT_DIR=%{?buildroot}%{_unitdir}

%files
%doc README.md
%dir %{_sysconfdir}/sqm
%{_sysconfdir}/sqm/default.conf
%config(noreplace) %{_sysconfdir}/sqm/sqm.conf
%{_bindir}/sqm
%{_prefix}/lib/sqm
%{_unitdir}/sqm@.service
%{_tmpfilesdir}/sqm.conf

%changelog
%autochangelog
