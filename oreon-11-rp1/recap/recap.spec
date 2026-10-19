%global source0_hash f8d473a4f383d8972c0f077c7b5c490f561b5afa10d0f20b0816cc067f038635
%bcond_without timers
Name: recap
Version: 2.1.0
Release:        1%{?dist}
Summary:        Generates reports of various system information
License: GPL-2.0-only
URL: https://github.com/rackerlabs/recap
Source0:        https://github.com/rackerlabs/recap/archive/%{version}/recap-%{version}.tar.gz
BuildArch: noarch
%if %{without timers}
Requires: crontabs
%endif
Requires: iotop
Requires: iproute
Requires: procps-ng
Requires: psmisc
Requires: sysstat >= 9
%if %{with timers}
Requires: systemd
%endif
Obsoletes: rs-sysmon < 0.9.5-2
Provides: rs-sysmon = %{version}-%{release}
# oreon:deps
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
This program is intended to be used as a companion for the reporting provided
by sysstat. It will create a set of reports summarizing hardware resource
utilization. The script also provides optional reporting on Apache, MySQL, and
network connections.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%install
export PREFIX=%{_prefix}
export DESTDIR=%{buildroot}
make install-base
make install-man
%if %{with timers}
make install-systemd
%else
make install-cron
%oreon_autofiles main
%endif
%posttrans

if [ -f /etc/recap.rpmsave ]; then
    mv -vf /etc/recap.conf /etc/recap.conf.rpmnew
    mv -vf /etc/recap.rpmsave /etc/recap.conf
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
