%global source0_hash 366b146133c71cf3e63c50ee75fd6a0c2e7763b8d239c6ef6f22333be57b13f7

Name:		ntpstat
Version:	0.6
Release:	15%{?dist}
Summary:	Utility to print NTP synchronization status

License:	MIT
URL:		https://github.com/mlichvar/ntpstat
Source0:        https://github.com/mlichvar/ntpstat/archive/0.6/ntpstat-0.6.tar.gz
BuildArch:	noarch

BuildRequires:	make
Requires:	(ntpsec or chrony)
# ntpstat was split off from the ntp package
Conflicts:	ntp < 4.2.8p10-4

%description
This package contains a script which prints a brief summary of the system
clock's synchronisation status when the ntpd or chronyd daemon is running.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

%build

%install
make install bindir=$RPM_BUILD_ROOT%{_bindir} mandir=$RPM_BUILD_ROOT%{_mandir}

%files
%license COPYING
%doc NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6-15
- Prepare for Oreon 11 (RP1)
