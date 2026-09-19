%global source0_hash f750aa3e22f839b637a073647510d7aa3adf7496e21f3c875b7a368c71d37487

# In f20+ use unversioned docdirs, otherwise the old versioned one
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           rkhunter
Version:        1.4.6
Release:        32%{?dist}
Summary:        A host-based tool to scan for rootkits, backdoors and local exploits

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://rkhunter.sourceforge.net/
Source0:        http://downloads.sourceforge.net/rkhunter/rkhunter-%{version}.tar.gz
Source2:        01-rkhunter
Source3:        rkhunter.sysconfig
Patch0:         rkhunter-1.4.6-fedoraconfig.patch
# libkeyutils is an actual legit library now, so this old check is a false positive.
Patch1:         rkhunter-1.4.6-drop-libkeyutils-check.patch
# have ssh checks use the sshd.d directoy config files too.
Patch2:         rkhunter-1.4.6-ssh.d.patch
# Fix grep/egrep changes in f38+
Patch3:         rkhunter-1.4.6-grep.patch
# Fix grep warning about escaping / in f42+
Patch4:         rkhunter-1.4.6-grep-fix.patch
# Fix systemd-journald config path
Patch5:         rkhunter-1.4.6-journald-config.patch
# Fix false positive Li0n detection due to bin/sbin merge
Patch6:         rkhunter-1.4.6-Li0n-fix.patch
BuildArch:      noarch
BuildRequires:      perl-generators

Requires:       coreutils, binutils, kmod, findutils, grep
Requires:       e2fsprogs, procps, lsof, iproute, wget
Requires:       perl-interpreter, perl(strict), perl(IO::Socket), s-nail, logrotate
Requires:       crontabs

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
# Nothing to be built

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
# Don't ship these unless we want to Require the perl modules
#%{__install} -m750 -p files/filehashmd5.pl      ${RPM_BUILD_ROOT}%{_prefix}/lib/%{name}/scripts/
#%{__install} -m750 -p files/filehashsha1.pl     ${RPM_BUILD_ROOT}%{_prefix}/lib/%{name}/scripts/
%{__install} -m755 -p %{SOURCE2}                ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.daily/%{name}
%{__install} -m644 -p %{name}.logrotate         ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}
%{__install} -m640 -p files/%{name}.conf        ${RPM_BUILD_ROOT}%{_sysconfdir}/
%{__install} -m640 -p %{SOURCE3}                ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{name}

%files
%doc %{_pkgdocdir}/*
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/scripts
%{_sysconfdir}/cron.daily/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_var}/lib/%{name}
%dir %{_var}/lib/%{name}/db
%ghost %{_var}/lib/%{name}/db/mirrors.dat
%ghost %{_var}/lib/%{name}/db/programs_bad.dat
%ghost %{_var}/lib/%{name}/db/backdoorports.dat
%{_var}/lib/%{name}/db/i18n
%dir %{_var}/log/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %{_pkgdocdir}
%{_mandir}/man8/*

%changelog
%autochangelog
