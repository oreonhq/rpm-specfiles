%global source0_hash c4a617aa46abf150ded1f5be0f02846f2b850d13db628dbcf080f59f5995bb52

Name:           auter
Version:        1.0.0
Release:        18%{?dist}
Summary:        Prepare and apply updates
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/rackerlabs/%{name}
Source0:        https://github.com/rackerlabs/%{name}/archive/%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  help2man
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
BuildRequires:  systemd
%endif
Requires:       crontabs
%if 0%{?fedora} >= 18
Requires:       dnf
%else
Requires:       yum
%endif

%description
auter (optionally) pre-downloads updates and then runs automatically on a
set schedule, optionally rebooting to finish applying the updates.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
help2man --section=1 ./auter -N -o auter.man -n "Automatic Update Transaction Execution by Rackspace" --include=auter.help2man-sections

%install
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
mkdir -p %{buildroot}%{_tmpfilesdir}
echo "d %{_rundir}/%{name} 0755 root root -" > %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_rundir}/%{name}
touch %{buildroot}%{_rundir}/%{name}/%{name}.pid
%else
mkdir -p %{buildroot}%{_localstatedir}/run/%{name}
touch %{buildroot}%{_localstatedir}/run/%{name}/%{name}.pid
%endif

install -d -p -m 0755 \
  %{buildroot}%{_sharedstatedir}/%{name} \
  %{buildroot}%{_var}/cache/%{name} \
  %{buildroot}%{_sysconfdir}/%{name}/pre-reboot.d \
  %{buildroot}%{_sysconfdir}/%{name}/post-reboot.d \
  %{buildroot}%{_sysconfdir}/%{name}/pre-apply.d \
  %{buildroot}%{_sysconfdir}/%{name}/post-apply.d \
  %{buildroot}%{_sysconfdir}/%{name}/pre-prep.d \
  %{buildroot}%{_sysconfdir}/%{name}/post-prep.d

install -D -p -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 %{name}.cron %{buildroot}%{_sysconfdir}/cron.d/%{name}
install -D -p -m 0755 %{name}.yumdnfModule %{buildroot}%{_usr}/lib/%{name}/auter.module
install -D -p -m 0644 %{name}.man %{buildroot}%{_mandir}/man1/%{name}.1
install -D -p -m 0644 %{name}.conf.man %{buildroot}%{_mandir}/man5/%{name}.conf.5
install -D -p -m 0644 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf

%post
# If this is the first time install, create the lockfile
if [ $1 -eq 1 ]; then
  /usr/bin/auter --enable
fi
exit 0

%preun
# If this is a complete removal, then remove lockfile
if [ $1 -eq 0 ]; then
 /usr/bin/auter --disable
fi
exit 0

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%doc README.md
%doc NEWS
%doc MAINTAINERS.md
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.conf.5*
%{_sharedstatedir}/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_var}/cache/auter
%dir %{_sysconfdir}/%{name}/pre-reboot.d
%dir %{_sysconfdir}/%{name}/post-reboot.d
%dir %{_sysconfdir}/%{name}/pre-apply.d
%dir %{_sysconfdir}/%{name}/post-apply.d
%dir %{_sysconfdir}/%{name}/pre-prep.d
%dir %{_sysconfdir}/%{name}/post-prep.d
%dir %{_usr}/lib/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%{_bindir}/%{name}
%{_usr}/lib/%{name}/auter.module
%if 0%{?el6}
%dir %{_localstatedir}/run/%{name}/
%ghost %{_localstatedir}/run/%{name}/%{name}.pid
%else
%dir %{_rundir}/%{name}/
%ghost %{_rundir}/%{name}/%{name}.pid
%{_tmpfilesdir}/%{name}.conf
%endif

%changelog
%autochangelog
