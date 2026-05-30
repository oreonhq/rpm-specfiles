%global source0_hash bb066b389d7c9bb9d84a35738032b85c30cba7d949f758192adc72c9477fd3b8

%bcond_without pam

Summary:    Job spooling tools
Name:       at
Version:    3.2.5
Release:    21%{?dist}
# http://packages.debian.org/changelogs/pool/main/a/at/current/copyright
# + install-sh is MIT license with changes under Public Domain
License:    GPL-3.0-or-later AND GPL-2.0-or-later AND ISC
URL:        http://ftp.debian.org/debian/pool/main/a/at

Source:        http://software.calhariz.com/at/at_%{version}.orig.tar.gz
# git upstream source git://git.debian.org/git/collab-maint/at.git
Source1:    pam_atd
Source2:    at-tmpfiles.conf
Source3:    atd.sysconf
Source5:    atd.systemd

Patch:      at-3.2.5-address-sast.patch
Patch:      at-aarch64.patch
Patch:      at-3.2.5-make.patch
Patch:      at-3.2.5-pam.patch
Patch:      at-3.1.14-opt_V.patch
Patch:      at-3.2.2-shell.patch
Patch:      at-3.2.5-nitpicks.patch
Patch:      at-3.1.14-fix_no_export.patch
Patch:      at-3.2.5-mailwithhostname.patch
Patch:      at-3.2.5-aborted-jobs.patch
Patch:      at-3.2.5-noabort.patch
Patch:      at-3.1.16-fclose-error.patch
Patch:      at-3.1.16-clear-nonjobs.patch
Patch:      at-3.2.2-lock-locks.patch
Patch:      at-3.1.23-document-n.patch
Patch:      at-3.1.20-log-jobs.patch
Patch:      at-3.2.5-past-date.patch

BuildRequires: gcc
BuildRequires: flex flex-static bison autoconf
BuildRequires: libselinux-devel >= 1.27.9
BuildRequires: perl(Test::Harness)
BuildRequires: perl(Test::More)
BuildRequires: systemd-rpm-macros

%if %{with pam}
BuildRequires: pam-devel
%endif
Conflicts: crontabs <= 1.5
# No, I'm not kidding
BuildRequires: smtpdaemon
BuildRequires: make

Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

# at-sysvinit subpackage dropped
Obsoletes: at-sysvinit < 3.1.16-1

%description
At and batch read commands from standard input or from a specified
file. At allows you to specify that a command will be run at a
particular time. Batch will execute commands when the system load
levels drop to a particular level. Both commands use user's shell.

You should install the at package if you need a utility for
time-oriented job control. Note: If it is a recurring job that will
need to be repeated at the same time every day/week, etc. you should
use crontab instead.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -N
cp %{SOURCE1} .
%autopatch -p1

%build
# uselles files
rm -f lex.yy.* y.tab.*

%configure --with-atspool=%{_localstatedir}/spool/at/spool \
    --with-jobdir=%{_localstatedir}/spool/at \
    --with-daemon_username=root  \
    --with-daemon_groupname=root \
    --with-selinux \
    %{?with_pam:--with-pam}

make

%install
make install \
    DAEMON_USERNAME=`id -nu` \
    DAEMON_GROUPNAME=`id -ng` \
    DESTDIR=%{buildroot} \
    sbindir=%{_bindir} \
    bindir=%{_bindir} \
    datadir=%{_datadir} \
    prefix=%{_prefix} \
    exec_prefix=%{_prefix} \
    docdir=%{_prefix}/doc \
    mandir=%{_mandir} \
    etcdir=%{_sysconfdir} \
    ATJOB_DIR=%{_localstatedir}/spool/at \
    ATSPOOL_DIR=%{_localstatedir}/spool/at/spool \
    INSTALL_ROOT_USER=`id -nu` \
    INSTALL_ROOT_GROUP=`id -nu`;

echo > %{buildroot}%{_sysconfdir}/at.deny
mkdir docs
cp  %{buildroot}%{_prefix}/doc/at/* docs/

mkdir -p %{buildroot}%{_sysconfdir}/pam.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/atd

mkdir -p %{buildroot}/etc/sysconfig
install -m 644 %{SOURCE3} %{buildroot}/etc/sysconfig/atd

# install systemd initscript
mkdir -p %{buildroot}/%{_unitdir}/
install -m 644 %{SOURCE5} %{buildroot}/%{_unitdir}/atd.service

# install tmpfiles configuration
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/at.conf

# remove unpackaged files from the buildroot
rm -r  %{buildroot}%{_prefix}/doc
# Remove .SEQ file created by make install - tmpfiles will create it
rm -f %{buildroot}%{_localstatedir}/spool/at/.SEQ

%check
make test

%post
%systemd_post atd.service

# Create directories and files using tmpfiles
%tmpfiles_create at.conf

%preun
%systemd_preun atd.service

%postun
%systemd_postun_with_restart atd.service

%triggerun -- at < 3.1.12-6
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply atd
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save atd

# The package is allowed to autostart:
/bin/systemctl enable atd.service >/dev/null 2>&1

/sbin/chkconfig --del atd >/dev/null 2>&1 || :
/bin/systemctl try-restart atd.service >/dev/null 2>&1 || :
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%files
%license Copyright COPYING
%doc README timespec ChangeLog
%attr(0644,root,root)       %config(noreplace) %{_sysconfdir}/at.deny
%attr(0644,root,root)       %config(noreplace) %{_sysconfdir}/sysconfig/atd
%attr(0644,root,root)       %config(noreplace) %{_sysconfdir}/pam.d/atd
%attr(0700,root,root)       %dir %{_localstatedir}/spool/at
%attr(0700,root,root)       %dir %{_localstatedir}/spool/at/spool
%{_tmpfilesdir}/at.conf
%{_bindir}/atrun
%attr(0755,root,root)       %{_bindir}/atd
%{_mandir}/man*/*
%{_bindir}/batch
%{_bindir}/atrm
%{_bindir}/atq
%attr(4755,root,root)       %{_bindir}/at
%{_datadir}/at/
%attr(0644,root,root)       /%{_unitdir}/atd.service

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.2.5-21
- Prepare for Oreon 11 (RP1)
