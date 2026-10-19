%global source0_hash f750aa3e22f839b637a073647510d7aa3adf7496e21f3c875b7a368c71d37487
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Name:           rkhunter
Version:        1.4.6
Release:        1%{?dist}
Summary:        A host-based tool to scan for rootkits, backdoors and local exploits
License:        GPL-2.0-or-later
URL:            http://rkhunter.sourceforge.net/
Source0:        http://downloads.sourceforge.net/rkhunter/rkhunter-%{version}.tar.gz
Source2:        01-rkhunter
Source3:        rkhunter.sysconfig
Patch0:         rkhunter-1.4.6-fedoraconfig.patch
Patch1:         rkhunter-1.4.6-drop-libkeyutils-check.patch
Patch2:         rkhunter-1.4.6-ssh.d.patch
Patch3:         rkhunter-1.4.6-grep.patch
Patch4:         rkhunter-1.4.6-grep-fix.patch
Patch5:         rkhunter-1.4.6-journald-config.patch
Patch6:         rkhunter-1.4.6-Li0n-fix.patch
BuildArch:      noarch
Requires:       coreutils, binutils, kmod, findutils, grep
Requires:       e2fsprogs, procps, lsof, iproute, wget
Requires:       perl-interpreter, perl(strict), perl(IO::Socket), s-nail, logrotate
Requires:       crontabs
# oreon:deps
BuildRequires:  perl-generators
# /oreon:deps
%description
Rootkit Hunter (RKH) is an easy-to-use tool which checks
computers running UNIX (clones) for the presence of rootkits
and other unwanted tools.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%{__cat} <<'EOF' >%{name}.logrotate
%{_localstatedir}/log/%{name}/%{name}.log {
    weekly
    notifempty
    create 640 root root
}
EOF

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -m755 -p ${RPM_BUILD_ROOT}%{_bindir}
%{__mkdir} -m755 -p ${RPM_BUILD_ROOT}%{_sysconfdir}/{cron.daily,sysconfig,logrotate.d}
%{__mkdir} -m755 -p ${RPM_BUILD_ROOT}%{_datadir}/%{name}/scripts
%{__mkdir} -m755 -p ${RPM_BUILD_ROOT}%{_pkgdocdir}
%{__mkdir} -m755 -p ${RPM_BUILD_ROOT}%{_mandir}/man8
%{__mkdir} -m700 -p ${RPM_BUILD_ROOT}%{_var}/lib/%{name}
%{__mkdir} -m755 -p ${RPM_BUILD_ROOT}%{_var}/lib/%{name}/db
%{__mkdir} -m755 -p ${RPM_BUILD_ROOT}%{_var}/log/%{name}
%{__mkdir} -m755 -p ${RPM_BUILD_ROOT}%{_var}/lib/%{name}/db/i18n
%{__install} -m755 -p files/%{name}             ${RPM_BUILD_ROOT}%{_bindir}/
%{__install} -m644 -p files/backdoorports.dat   ${RPM_BUILD_ROOT}%{_var}/lib/%{name}/db/
%{__install} -m644 -p files/mirrors.dat         ${RPM_BUILD_ROOT}%{_var}/lib/%{name}/db/
%{__install} -m644 -p files/programs_bad.dat    ${RPM_BUILD_ROOT}%{_var}/lib/%{name}/db/
%{__install} -m644 -p files/i18n/cn             ${RPM_BUILD_ROOT}%{_var}/lib/%{name}/db/i18n/
%{__install} -m644 -p files/i18n/en             ${RPM_BUILD_ROOT}%{_var}/lib/%{name}/db/i18n/
%{__install} -m644 -p files/CHANGELOG           ${RPM_BUILD_ROOT}%{_pkgdocdir}
%{__install} -m644 -p files/LICENSE             ${RPM_BUILD_ROOT}%{_pkgdocdir}
%{__install} -m644 -p files/README              ${RPM_BUILD_ROOT}%{_pkgdocdir}
%{__install} -m755 -p files/check_modules.pl    ${RPM_BUILD_ROOT}%{_datadir}/%{name}/scripts/
%{__install} -m644 -p files/*.8                 ${RPM_BUILD_ROOT}%{_mandir}/man8/
%{__install} -m755 -p %{SOURCE2}                ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.daily/%{name}
%{__install} -m644 -p %{name}.logrotate         ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}
%{__install} -m640 -p files/%{name}.conf        ${RPM_BUILD_ROOT}%{_sysconfdir}/
%{__install} -m640 -p %{SOURCE3}                ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
