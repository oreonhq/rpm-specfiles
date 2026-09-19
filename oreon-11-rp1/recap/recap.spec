%global source0_hash f8d473a4f383d8972c0f077c7b5c490f561b5afa10d0f20b0816cc067f038635

%if %{defined rhel} && 0%{?rhel} <= 7 || %{defined fedora} && 0%{?fedora} < 30
%bcond_with timers
%else
%bcond_without timers
%endif

Name: recap
Version: 2.1.0
Release: 22%{?dist}
Summary: Generates reports of various system information
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: https://github.com/rackerlabs/recap
Source0: https://github.com/rackerlabs/recap/archive/%{version}/recap-%{version}.tar.gz
BuildArch: noarch
%if %{without timers}
Requires: crontabs
%endif
Requires: iotop
Requires: iproute
%if 0%{?rhel} && 0%{?rhel} < 7
Requires: procps
%else
Requires: procps-ng
%endif
Requires: psmisc
Requires: sysstat >= 9

%if %{defined rhel} && 0%{?rhel} > 7 || %{defined fedora}
Recommends: elinks
%endif

BuildRequires: make
%if %{with timers}
BuildRequires: systemd
Requires: systemd
%endif
Obsoletes: rs-sysmon < 0.9.5-2
Provides: rs-sysmon = %{version}-%{release}

%description
This program is intended to be used as a companion for the reporting provided
by sysstat. It will create a set of reports summarizing hardware resource
utilization. The script also provides optional reporting on Apache, MySQL, and
network connections.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%install
export PREFIX=%{_prefix}
export DESTDIR=%{buildroot}
%if %{defined fedora} && 0%{?fedora} >= 42
export BINPATH=/bin
%endif
make install-base
make install-man

%if %{with timers}
make install-systemd
%else
make install-cron
%endif

%posttrans
# https://github.com/rackerlabs/recap/pull/137
if [ -f /etc/recap.rpmsave ]; then
    mv -vf /etc/recap.conf /etc/recap.conf.rpmnew
    mv -vf /etc/recap.rpmsave /etc/recap.conf
fi

%files
%license COPYING
%doc README.md CHANGELOG.md
%dir %{_localstatedir}/log/recap
%dir %{_localstatedir}/log/recap/backups
%dir %{_localstatedir}/log/recap/snapshots
%if %{defined fedora} && 0%{?fedora} < 42
%{_sbindir}/recap
%{_sbindir}/recaplog
%{_sbindir}/recaptool
%else
%{_bindir}/recap
%{_bindir}/recaplog
%{_bindir}/recaptool
%endif

# systemd unit files
%if %{with timers}
%{_unitdir}/recap.service
%{_unitdir}/recaplog.service
%{_unitdir}/recap-onboot.service
%{_unitdir}/recap.timer
%{_unitdir}/recaplog.timer
%{_unitdir}/recap-onboot.timer
%else
# crontab
%config(noreplace) %{_sysconfdir}/cron.d/recap
%endif

%config(noreplace) %{_sysconfdir}/recap.conf
%{_mandir}/man5/recap.conf.5.gz
%{_mandir}/man8/recap.8.gz
%{_mandir}/man8/recaplog.8.gz
%{_mandir}/man8/recaptool.8.gz

# core functions
%{_prefix}/lib/recap/core/fdisk
%{_prefix}/lib/recap/core/mysql
%{_prefix}/lib/recap/core/netstat
%{_prefix}/lib/recap/core/ps
%{_prefix}/lib/recap/core/pstree
%{_prefix}/lib/recap/core/resources
%{_prefix}/lib/recap/core/send_mail

# plugins
%{_prefix}/lib/recap/plugins-available/docker_top
%{_prefix}/lib/recap/plugins-available/http_status
%{_prefix}/lib/recap/plugins-available/kernel_cmd
%{_prefix}/lib/recap/plugins-available/redis
%{_prefix}/lib/recap/plugins-available/system_locks
%dir %{_prefix}/lib/recap/plugins-enabled

%changelog
%autochangelog
