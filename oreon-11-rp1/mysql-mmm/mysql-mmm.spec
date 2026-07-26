%global source0_hash bf29544810e61f5f8d3fce8f69db89c932b1ee0c0490eee69faca6e77e62b08b

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name: mysql-mmm
Version: 2.2.1
Release: 41%{?dist}
Summary: Multi-Master Replication Manager for MySQL
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: http://mysql-mmm.org
Source: http://mysql-mmm.org/_media/:mmm2:/%{name}-%{version}.tar.gz
Source1: mysql-mmm.logrotate
Source2: http://mysql-mmm.org/_media/:mmm2:/%{name}-%{version}.pdf
Source3: mmm_mon_log.conf
Source4: mmm_agent.conf
Source5: mmm_mon.conf
Source6: mmm_tools.conf
Source7: mmm_common.conf
Source8: mysql-mmm-agent.service
Source9: mysql-mmm-monitor.service

BuildArch: noarch
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: systemd

Provides: mmm = %{version}-%{release}
Provides: mysql-master-master = %{version}-%{release}

Patch0: mysql-mmm-2.1.0-paths.patch
Patch1: mysql-mmm-fix-bug-with-newer-net-arp.patch
Patch2: mysql-mmm-fix-cve-remote-command-injection.patch
Patch3: mysql-mmm-add-notify-cmd.patch
Patch4: mysql-mmm-suppress-uninitialized-warning.patch

%description
MMM (MySQL Master-Master Replication Manager) is a set of flexible scripts
to perform monitoring/failover and management of MySQL Master-Master
replication configurations (with only one node writable at any time). The
toolset also has the ability to read balance standard master/slave
configurations with any number of slaves, so you can use it to move virtual
IP addresses around a group of servers depending on whether they are behind
in replication. In addition to that, it also has scripts for data backups,
resynchronization between nodes etc.

%package agent
Summary: MMM Database Server Agent Daemon and Libraries
Requires: %{name} = %{version}-%{release}
Requires: iproute
Requires: perl-DBD-mysql
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Provides: mysql-master-master-agent = %{version}-%{release}
Provides: mmm-agent = %{version}-%{release}

%description agent
Agent daemon and libraries which run on each MySQL server and provides the
monitoring node with a simple set of remote services.

%package monitor
Summary: MMM Monitor Server Daemon and Libraries
Requires: %{name} = %{version}-%{release}
Requires: perl(Class::Singleton), perl(DBD::mysql), perl(Time::HiRes)
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Provides: mysql-master-master-monitor = %{version}-%{release}
Provides: mmm-monitor = %{version}-%{release}

%description monitor
Monitoring daemon and libraries that do all monitoring work and make all
decisions about roles moving and so on.

%package tools
Summary: MMM Control Scripts and Libraries
Requires: %{name} = %{version}-%{release}
Provides: mysql-master-master-tools = %{version}-%{release}
Provides: mmm-tools = %{version}-%{release}

%description tools
Scripts and libraries dedicated to management of the mmm_mond processes
by commands.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
cp -a %{SOURCE2} .

# currently the README included with mysql-mmm is zero-length
cat >>README <<EOF
Full documentation can be found at:

    %{_pkgdocdir}/%{name}-%{version}.pdf
EOF

%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
find . -type f -name "*.orig" -print0 | xargs -0r rm

%build

%install
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}/usr/sbin/mmm_* %{buildroot}%{_bindir}

%{__install} -D -p -m 0644 %SOURCE1 %{buildroot}%{_sysconfdir}/logrotate.d/mysql-mmm
%{__install} -d -m 0755 %{buildroot}%{_localstatedir}/lib/%{name}

# Replace config files
%{__rm} -f %{buildroot}%{_sysconfdir}/mysql-mmm/*.conf

%{__install} -p -m 0640 %SOURCE3 %{buildroot}%{_sysconfdir}/mysql-mmm/mmm_mon_log.conf
%{__install} -p -m 0640 %SOURCE4 %{buildroot}%{_sysconfdir}/mysql-mmm/mmm_agent.conf
%{__install} -p -m 0640 %SOURCE5 %{buildroot}%{_sysconfdir}/mysql-mmm/mmm_mon.conf
%{__install} -p -m 0640 %SOURCE6 %{buildroot}%{_sysconfdir}/mysql-mmm/mmm_tools.conf
%{__install} -p -m 0640 %SOURCE7 %{buildroot}%{_sysconfdir}/mysql-mmm/mmm_common.conf
%{__install} -D -p -m 0644 %SOURCE8 %{buildroot}%{_unitdir}/mysql-mmm-agent.service
%{__install} -D -p -m 0644 %SOURCE9 %{buildroot}%{_unitdir}/mysql-mmm-monitor.service

%{__rm} -rvf %{buildroot}%{_sysconfdir}/init.d/

%post agent
%systemd_post mysql-mmm-agent.service

%preun agent
%systemd_preun mysql-mmm-agent.service

%postun agent
%systemd_postun mysql-mmm-agent.service

%post monitor
%systemd_post mysql-mmm-monitor.service

%preun monitor
%systemd_preun mysql-mmm-monitor.service

%postun monitor
%systemd_postun mysql-mmm-monitor.service

%files
%doc COPYING README VERSION %{name}-%{version}.pdf
%dir %{_sysconfdir}/mysql-mmm
%attr(755,root,root) %dir %{_localstatedir}/lib/mysql-mmm
%attr(755,root,root) %dir %{_localstatedir}/log/mysql-mmm
%config(noreplace) %{_sysconfdir}/logrotate.d/mysql-mmm
%config(noreplace) %attr(640,root,root) %{_sysconfdir}/mysql-mmm/mmm_common.conf
%{perl_vendorlib}/MMM/Common

%files tools
%doc README
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/mysql-mmm/mmm_tools.conf
%{perl_vendorlib}/MMM/Tools
%{_libexecdir}/mysql-mmm/tools/
%{_bindir}/mmm_backup
%{_bindir}/mmm_clone
%{_bindir}/mmm_restore

%files agent
%doc README
%config(noreplace) %attr(640,root,root) %{_sysconfdir}/mysql-mmm/mmm_agent.conf
%{perl_vendorlib}/MMM/Agent
%{_libexecdir}/mysql-mmm/agent/
%{_bindir}/mmm_agentd
%{_unitdir}/mysql-mmm-agent.service

%files monitor
%doc README
%config(noreplace) %attr(640,root,root) %{_sysconfdir}/mysql-mmm/mmm_mon.conf
%config(noreplace) %attr(640,root,root) %{_sysconfdir}/mysql-mmm/mmm_mon_log.conf
%{perl_vendorlib}/MMM/Monitor
%{_libexecdir}/mysql-mmm/monitor/
%{_bindir}/mmm_mond
%{_bindir}/mmm_control
%{_unitdir}/mysql-mmm-monitor.service

%changelog
%autochangelog
