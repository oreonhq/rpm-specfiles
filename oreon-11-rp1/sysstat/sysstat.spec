%global source0_hash 8aa2054c56c941ab30e1b14ad2e0076a7e6d6bf01f50e22d954885b8a7f9a679
Summary:        Collection of performance monitoring tools for Linux
Name: sysstat
Version: 12.8.0
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: https://sysstat.github.io
Source0:        https://github.com/sysstat/sysstat/archive/refs/tags/v%{version}.tar.gz#/sysstat-%{version}.tar.gz
Source1: sysstat-tmpfiles.conf
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%ifnarch %{ix86}
%endif
%else
%endif
Requires: findutils
Requires: xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  lm_sensors-devel
BuildRequires:  make
BuildRequires:  pcp-libs-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
The sysstat package contains the sar, sadf, mpstat, iostat, tapestat,
pidstat, cifsiostat and sa tools for Linux.
The sar command collects and reports system activity information.
The information collected by sar can be saved in a file in a binary
format for future inspection. The statistics reported by sar concern
I/O transfer rates, paging activity, process-related activities,
interrupts, network activity, memory and swap space utilization, CPU
utilization, kernel activities and TTY statistics, among others. Both
UP and SMP machines are fully supported.
The sadf command may  be used to display data collected by sar in
various formats (CSV, PCP, XML, etc.).
The iostat command reports CPU utilization and I/O statistics for disks.
The tapestat command reports statistics for tapes connected to the system.
The mpstat command reports global and per-processor statistics.
The pidstat command reports statistics for Linux tasks (processes).
The cifsiostat command reports I/O statistics for CIFS file systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
    --enable-install-cron \
    --enable-copy-only \
    --disable-file-attr \
    --disable-stripping \
    --docdir='%{_pkgdocdir}' \
    --with-systemdsystemunitdir='%{_unitdir}' \
    --with-systemdsleepdir='%{_unitdir}-sleep' \
    sadc_options='-S DISK' \
    history=28 \
    compressafter=31
%make_build
%install
%make_install
%find_lang %{name}
rm %{buildroot}%{_docdir}/%{name}/COPYING
mkdir -p ${RPM_BUILD_ROOT}%{_tmpfilesdir}
install -p -m 644 %SOURCE1 ${RPM_BUILD_ROOT}%{_tmpfilesdir}/%{name}.conf
%oreon_autofiles main

%post

%systemd_post sysstat.service sysstat-collect.timer sysstat-summary.timer
%preun

%systemd_preun sysstat.service sysstat-collect.timer sysstat-summary.timer
if [[ $1 -eq 0 ]]; then
    rm -rf %{_localstatedir}/log/sa/*
fi
%postun

%systemd_postun sysstat.service sysstat-collect.timer sysstat-summary.timer
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
