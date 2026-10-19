%global source0_hash f1da374a15ba7605cf378347f96bc8b678d3d7c0765269c8242cfe5b0789c571
%bcond selinux 1
%bcond pam 1
%bcond audit 1
%bcond inotify 1
Summary:        Cron daemon for executing programs at set times
Name:      cronie
Version:   1.7.2
Release:        1%{?dist}
License:   GPL-2.0-or-later AND BSD-3-Clause AND BSD-2-Clause AND ISC AND LGPL-2.1-or-later
URL:       https://github.com/cronie-crond/cronie
Source0:        https://github.com/cronie-crond/cronie/releases/download/cronie-%{version}/cronie-%{version}.tar.gz
Source1:   cronie-tmpfiles.conf
Source2:   cronie-anacron-tmpfiles.conf
Patch:     0001-do-no-leak-file-descriptors.patch
Patch:     make_error_func_prototype_complete.patch
Patch:     fix_range_parsing.patch
Patch:     move_parsing_code.patch
Patch:     crontab-fix-backup-failure.patch
Patch:     forward-XDG_SESSION_CLASS-to-PAM-for-session-classification.patch
Requires:  dailyjobs
%if %{with selinux}
Requires:      libselinux >= 2.0.64
%endif
%if %{with pam}
Requires:      pam >= 1.0.1
%endif
%if %{with audit}
%endif
Obsoletes:        %{name}-sysvinit < %{version}-%{release}
Requires(post):   coreutils sed
%if 0%{?fedora} && 0%{?fedora} < 28 || 0%{?rhel} && 0%{?rhel} < 8 || (0%{?oreon} >= 11)
%{?systemd_requires}
%else
%{?systemd_ordering} # does not exist on Fedora27/RHEL7
%endif
# oreon:deps
BuildRequires:  audit-libs-devel
BuildRequires:  gcc
BuildRequires:  libselinux-devel
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  systemd
# /oreon:deps
%description
Cronie contains the standard UNIX daemon crond that runs specified programs at
scheduled times and related tools. It is a fork of the original vixie-cron and
has security and configuration enhancements like the ability to use pam and
SELinux.

%package anacron
Summary:   Utility for running regular jobs
Requires:  crontabs
Provides:  dailyjobs
Provides:  anacron = 2.4
Obsoletes: anacron <= 2.3
Requires(post): coreutils
Requires:  %{name} = %{version}-%{release}
%description anacron
Anacron is part of cronie that is used for running jobs with regular
periodicity which do not have exact time of day of execution.

The default settings of anacron execute the daily, weekly, and monthly
jobs, but anacron allows setting arbitrary periodicity of jobs.

Using anacron allows running the periodic jobs even if the system is often
powered off and it also allows randomizing the time of the job execution
for better utilization of resources shared among multiple systems.

%package noanacron
Summary:   Utility for running simple regular jobs in old cron style
Provides:  dailyjobs
Requires:  crontabs
Requires:  %{name} = %{version}-%{release}
%description noanacron
Old style of running {hourly,daily,weekly,monthly}.jobs without anacron. No
extra features.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
    %{?with_pam:--with-pam} \
    %{?with_selinux:--with-selinux} \
    %{?with_audit:--with-audit} \
    %{?with_inotify:--with-inotify} \
    --enable-anacron \
    --enable-pie \
    --enable-relro
%make_build V=2
%install
%make_install DESTMAN=$RPM_BUILD_ROOT%{_mandir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/
mkdir -pm755 $RPM_BUILD_ROOT%{_sysconfdir}/cron.d/
%if ! %{with pam}
    rm -f $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/crond
%endif
install -m 644 crond.sysconfig $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/crond
touch $RPM_BUILD_ROOT%{_sysconfdir}/cron.deny
install -m 644 contrib/anacrontab $RPM_BUILD_ROOT%{_sysconfdir}/anacrontab
install -c -m755 contrib/0hourly $RPM_BUILD_ROOT%{_sysconfdir}/cron.d/0hourly
mkdir -pm 755 $RPM_BUILD_ROOT%{_sysconfdir}/cron.hourly
install -c -m755 contrib/0anacron $RPM_BUILD_ROOT%{_sysconfdir}/cron.hourly/0anacron
install -m 644 contrib/dailyjobs $RPM_BUILD_ROOT/%{_sysconfdir}/cron.d/dailyjobs
install -m 644 -D contrib/cronie.systemd $RPM_BUILD_ROOT/usr/lib/systemd/system/crond.service
install -m 644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_tmpfilesdir}/cronie.conf
install -m 644 -D %{SOURCE2} $RPM_BUILD_ROOT%{_tmpfilesdir}/cronie-anacron.conf
%oreon_autofiles cronie-anacron usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cronie-noanacron usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post crond.service
systemd-tmpfiles --create %{_tmpfilesdir}/cronie.conf 2>/dev/null || :
%post anacron

systemd-tmpfiles --create %{_tmpfilesdir}/cronie-anacron.conf 2>/dev/null || :
%preun

%systemd_preun crond.service
%postun

%systemd_postun_with_restart crond.service
%triggerun -- cronie-anacron < 1.4.1

cp -a /etc/crontab /etc/crontab.rpmsave
sed -e '/^01 \* \* \* \* root run-parts \/etc\/cron\.hourly/d'\
  -e '/^02 4 \* \* \* root run-parts \/etc\/cron\.daily/d'\
  -e '/^22 4 \* \* 0 root run-parts \/etc\/cron\.weekly/d'\
  -e '/^42 4 1 \* \* root run-parts \/etc\/cron\.monthly/d' /etc/crontab.rpmsave > /etc/crontab
exit 0
%triggerun -- cronie < 1.4.7-2

/usr/bin/systemd-sysv-convert --save crond
/bin/systemctl enable crond.service >/dev/null 2>&1
/bin/chkconfig --del crond >/dev/null 2>&1 || :
/bin/systemctl try-restart crond.service >/dev/null 2>&1 || :
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
%triggerin -- pam, glibc, libselinux

/bin/systemctl try-restart crond.service >/dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list
%files -n cronie-anacron -f %{oreon_filedir}/cronie-anacron.list
%files -n cronie-noanacron -f %{oreon_filedir}/cronie-noanacron.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7.2-1
- Import
