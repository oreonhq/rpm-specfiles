%global source0_hash 7397d48865b1e743f437466586de1621bd1960da467227b7d05e400da5aad176
%global snapshot_date 20190603
%global snapshot_commit 9e74f2d
Summary:        Root crontab files used to schedule the execution of programs
Name: crontabs
Version: 1.11^%{snapshot_date}git%{snapshot_commit}
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: https://github.com/cronie-crond/crontabs
Source0:        https://github.com/cronie-crond/%{name}/releases/download/%{name}-%{snapshot_date}/%{name}-1.11-%{snapshot_date}git.tar.gz
BuildArch: noarch
Requires: sed
Requires: cronie
# oreon:deps

# /oreon:deps
%description
This package is used by Fedora mainly for executing files by cron.

The crontabs package contains root crontab files and directories.
You will need to install cron daemon to run the jobs from the crontabs.
The cron daemon such as cronie or fcron checks the crontab files to
see when particular commands are scheduled to be executed.  If commands
are scheduled, it executes them.

Crontabs handles a basic system function, so it should be installed on
your system.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%(echo %{version}|cut -d\^ -f1)

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/cron.{hourly,daily,weekly,monthly}
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man4/
install -m644 ./crontab $RPM_BUILD_ROOT/etc/crontab
install -m755 ./run-parts $RPM_BUILD_ROOT/usr/bin/run-parts
install -m644 ./{crontabs,run-parts}.4 $RPM_BUILD_ROOT/%{_mandir}/man4/
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig/
touch $RPM_BUILD_ROOT/etc/sysconfig/run-parts
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.11^%{snapshot_date}git%{snapshot_commit}-1
- Prepare for Oreon 11 (RP1)
