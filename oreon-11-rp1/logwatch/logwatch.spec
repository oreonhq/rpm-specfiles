%global source0_hash 5913783d52fe02a18fd796acee2335eeca43cb17e913eca33e2f211e64f2fcdb
%global _unitdir /usr/lib/systemd/system
Summary:        Analyzes and Reports on system logs
Name: logwatch
Version: 7.15
Release:        1%{?dist}
License: MIT
URL: https://sourceforge.net/projects/logwatch/
Source0:        https://sourceforge.net/projects/logwatch/files/%{name}-%{version}/%{name}-%{version}.tar.gz
Requires: grep
Requires: dnf5
Requires: perl(Date::Manip)
Requires: perl(diagnostics)
Requires: perl(Errno)
Requires: perl(File::Basename)
Requires: perl(lib)
Requires: perl(re)
Requires: perl(Socket)
Requires: perl(subs)
Requires: perl(Time::Local)
Requires: perl(URI::URL)
Requires: perl(vars)
Requires: perl(warnings)
Requires: crontabs
BuildArchitectures: noarch
# oreon:deps
BuildRequires:  perl-generators
# /oreon:deps
%description
Logwatch is a customizable, pluggable log-monitoring system.  It will go
through your logs for a given period of time and make a report in the areas
that you wish with the detail that you wish.  Easy to use - works right out
of the package on many systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
install -m 0755 -d %{buildroot}%{_var}/cache/logwatch
install -m 0755 -d %{buildroot}%{_sysconfdir}/logwatch/scripts
install -m 0755 -d %{buildroot}%{_sysconfdir}/logwatch/scripts/services
install -m 0755 -d %{buildroot}%{_sysconfdir}/logwatch/conf
install -m 0755 -d %{buildroot}%{_sysconfdir}/logwatch/conf/logfiles
install -m 0755 -d %{buildroot}%{_sysconfdir}/logwatch/conf/services
install -m 0755 -d %{buildroot}%{_sysconfdir}/cron.daily
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/default.conf/logfiles
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/default.conf/services
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/default.conf/html
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/dist.conf/logfiles
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/dist.conf/services
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/scripts/services
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/scripts/shared
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/lib
install -m 0755 -d %{buildroot}%{_sbindir}
install -m 0755 -d %{buildroot}%{_mandir}/man1
install -m 0755 -d %{buildroot}%{_mandir}/man5
install -m 0755 -d %{buildroot}%{_mandir}/man8
for i in scripts/logfiles/* ; do
   if [ $(ls $i | wc -l) -ne 0 ] ; then
      install -m 0755 -d %{buildroot}%{_datadir}/logwatch/$i
      install -m 0644 $i/* %{buildroot}%{_datadir}/logwatch/$i
   fi
done
install -m 0755 scripts/logwatch.pl %{buildroot}%{_datadir}/logwatch/scripts/logwatch.pl
install -m 0644 scripts/services/* %{buildroot}%{_datadir}/logwatch/scripts/services
install -m 0644 scripts/shared/* %{buildroot}%{_datadir}/logwatch/scripts/shared
install -m 0644 conf/*.conf %{buildroot}%{_datadir}/logwatch/default.conf
install -m 0644 conf/logfiles/* %{buildroot}%{_datadir}/logwatch/default.conf/logfiles
install -m 0644 conf/services/* %{buildroot}%{_datadir}/logwatch/default.conf/services
install -m 0644 conf/html/* %{buildroot}%{_datadir}/logwatch/default.conf/html
install -m 0644 lib/* %{buildroot}%{_datadir}/logwatch/lib
install -m 0644 amavis-logwatch.1 %{buildroot}%{_mandir}/man1
install -m 0644 postfix-logwatch.1 %{buildroot}%{_mandir}/man1
install -m 0644 logwatch.conf.5 %{buildroot}%{_mandir}/man5
ln -s logwatch.conf.5 %{buildroot}%{_mandir}/man5/ignore.conf.5
ln -s logwatch.conf.5 %{buildroot}%{_mandir}/man5/override.conf.5
install -m 0644 logwatch.8 %{buildroot}%{_mandir}/man8
install -m 0755 scheduler/logwatch.cron %{buildroot}%{_sysconfdir}/cron.daily/0logwatch
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 scheduler/logwatch.timer %{buildroot}%{_unitdir}/logwatch.timer
install -m 0644 scheduler/logwatch.service %{buildroot}%{_unitdir}/logwatch.service
install -m 0644 scheduler/systemd.conf %{buildroot}%{_datadir}/logwatch/default.conf/systemd.conf
ln -s ../../%{_datadir}/logwatch/scripts/logwatch.pl %{buildroot}/%{_sbindir}/logwatch
echo "###### REGULAR EXPRESSIONS IN THIS FILE WILL BE TRIMMED FROM REPORT OUTPUT #####" > %{buildroot}%{_sysconfdir}/logwatch/conf/ignore.conf
echo "# Local configuration options go here (defaults are in %{_datadir}/logwatch/default.conf/logwatch.conf)" > %{buildroot}%{_sysconfdir}/logwatch/conf/logwatch.conf
echo "# Configuration overrides for specific logfiles/services may be placed here." > %{buildroot}%{_sysconfdir}/logwatch/conf/override.conf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
