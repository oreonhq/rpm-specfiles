%global source0_hash e48fc69401135dc08d2cd4ff58dbdbfce9b7485f76fc9049d97848e313c08dda

Summary: Collection of performance monitoring tools for Linux
Name: sysstat
Version: 12.7.9
Release: 2%{?dist}
License: GPL-2.0-or-later

URL: https://sysstat.github.io
Source:        https://github.com/sysstat/sysstat/archive/refs/tags/v12.7.9.tar.gz

Source1: sysstat-tmpfiles.conf

# PCP is no longer available for %%{ix86} on F40
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
%ifnarch %{ix86}
BuildRequires: pcp-libs-devel
%endif
%else
BuildRequires: pcp-libs-devel
%endif

BuildRequires: gcc
BuildRequires: gettext
BuildRequires: git
BuildRequires: lm_sensors-devel
BuildRequires: make
BuildRequires: systemd-rpm-macros

Requires: findutils
Requires: xz

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -S git_am

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

# Do not install the license as documentation
rm %{buildroot}%{_docdir}/%{name}/COPYING

# tmpfiles config
mkdir -p ${RPM_BUILD_ROOT}%{_tmpfilesdir}
install -p -m 644 %SOURCE1 ${RPM_BUILD_ROOT}%{_tmpfilesdir}/%{name}.conf

%post
%systemd_post sysstat.service sysstat-collect.timer sysstat-summary.timer

%preun
%systemd_preun sysstat.service sysstat-collect.timer sysstat-summary.timer
if [[ $1 -eq 0 ]]; then
    # Remove sa logs if removing sysstat completely
    rm -rf %{_localstatedir}/log/sa/*
fi

%postun
%systemd_postun sysstat.service sysstat-collect.timer sysstat-summary.timer

%files -f %{name}.lang
%license COPYING
%doc CHANGES CREDITS FAQ.md README.md
%config(noreplace) %{_sysconfdir}/sysconfig/sysstat
%config(noreplace) %{_sysconfdir}/sysconfig/sysstat.ioconf
%{_bindir}/cifsiostat
%{_bindir}/iostat
%{_bindir}/mpstat
%{_bindir}/pidstat
%{_bindir}/sadf
%{_bindir}/sar
%{_bindir}/tapestat
%{_libdir}/sa
%{_unitdir}/sysstat*
%{_systemd_util_dir}/system-sleep/sysstat*
%{_mandir}/man1/cifsiostat.1*
%{_mandir}/man1/iostat.1*
%{_mandir}/man1/mpstat.1*
%{_mandir}/man1/pidstat.1*
%{_mandir}/man1/sadf.1*
%{_mandir}/man1/sar.1*
%{_mandir}/man1/tapestat.1*
%{_mandir}/man5/sysstat.5*
%{_mandir}/man8/sa1.8*
%{_mandir}/man8/sa2.8*
%{_mandir}/man8/sadc.8*
%{_localstatedir}/log/sa
%{_tmpfilesdir}/%{name}.conf

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12.7.9-2
- Prepare for Oreon 11 (RP1)
