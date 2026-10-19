%global source0_hash 45fd80be8be26bc7ec53cbd2fd40d7c2f4b569553b76e43c3cd0842ba1085a68
Name: sqm-scripts
Version: 1.8.0
Release:        1%{?dist}
Summary:        Traffic shaper scripts for Smart Queue Management
License: GPL-2.0-only
URL: https://www.bufferbloat.net/projects/cerowrt/wiki/Smart_Queue_Management/
Source0:        https://github.com/tohojo/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: %{name}-1.4.0-run_service_after_network.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
"Smart Queue Management", or "SQM" is shorthand for an integrated network
system that performs better per-packet/per flow network scheduling, active
queue length management (AQM), traffic shaping/rate limiting, and QoS
(prioritization).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{make_build}
%install
%{make_install} UNIT_DIR=%{?buildroot}%{_unitdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
