%global source0_hash 42876d195ee2ded19e5f72d7664096eee314928aa36ad346719ba5b25818fc84
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: audit
Version: 4.2.1
Release: 4%{?dist}
Summary: User space tools for kernel auditing
License: GPL-2.0-or-later
URL: https://github.com/linux-audit/audit-userspace
Source0: https://github.com/linux-audit/audit-userspace/archive/refs/tags/v%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: libcap-ng-devel
BuildRequires: openldap-devel

Requires: audit-libs%{?_isa} = %{version}-%{release}
Requires: audit-rules%{?_isa} = %{version}-%{release}

%description
User space tools and daemon for the Linux kernel audit subsystem.

%package libs
Summary: Dynamic libraries for the Linux audit framework

%description libs
The libaudit, libauparse, and libauplugin libraries.

%package libs-devel
Summary: Development files for the Linux audit libraries
Requires: audit-libs%{?_isa} = %{version}-%{release}
Obsoletes: audit-devel < 4.2.1-4

%description libs-devel
Headers, pkg-config files, and man pages for the audit libraries.

%package rules
Summary: audit rules and utilities
Requires: audit-libs%{?_isa} = %{version}-%{release}

%description rules
auditctl, augenrules, and sample audit rules.

%package -n audispd-plugins
Summary: Plugins for the audit event dispatcher
Requires: audit%{?_isa} = %{version}-%{release}
Requires: audit-libs%{?_isa} = %{version}-%{release}

%description -n audispd-plugins
af_unix, filter, remote, and syslog plugins for the audit dispatcher.

%package -n audispd-plugins-zos
Summary: z/OS remote plugin for the audit event dispatcher
Requires: audit%{?_isa} = %{version}-%{release}
Requires: audit-libs%{?_isa} = %{version}-%{release}

%description -n audispd-plugins-zos
Plugin forwarding audit events to a z/OS remote server.

%prep
%oreon_sha256
%autosetup -n audit-userspace-%{version} -p1
autoreconf -fi

%build
%oreon_configure --disable-static --without-python3 --without-golang --with-libcap-ng --enable-zos-remote
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
mkdir -p %{buildroot}%{_sysconfdir}/audit/rules.d %{buildroot}%{_localstatedir}/log/audit %{buildroot}%{_localstatedir}/spool/audit

%ldconfig_scriptlets libs

%files
%license COPYING
%{_sbindir}/auditd
%{_sbindir}/aureport
%{_sbindir}/ausearch
%{_bindir}/aulast
%{_bindir}/aulastlog
%{_bindir}/ausyscall
%{_prefix}/lib/systemd/system/auditd.service
%{_prefix}/lib/tmpfiles.d/audit.conf
%dir %{_libexecdir}/initscripts
%dir %{_libexecdir}/initscripts/legacy-actions
%{_libexecdir}/initscripts/legacy-actions/auditd/
%attr(0700,root,root) %dir %{_localstatedir}/log/audit
%dir %{_sysconfdir}/audit/plugins.d
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/audit/auditd.conf
%{_datadir}/bash-completion/completions/aureport
%{_datadir}/bash-completion/completions/ausearch
%{_mandir}/man5/auditd.conf.5*
%{_mandir}/man5/auditd.cron.5*
%{_mandir}/man5/auditd-plugins.5*
%{_mandir}/man8/auditd.8*
%{_mandir}/man8/aulast.8*
%{_mandir}/man8/aulastlog.8*
%{_mandir}/man8/aureport.8*
%{_mandir}/man8/ausearch.8*
%{_mandir}/man8/ausyscall.8*

%files libs
%license COPYING.LIB
%{_libdir}/libaudit.so.1
%{_libdir}/libaudit.so.1.*
%{_libdir}/libauparse.so.0
%{_libdir}/libauparse.so.0.*
%{_libdir}/libauplugin.so.1
%{_libdir}/libauplugin.so.1.*
%config(noreplace) %{_sysconfdir}/libaudit.conf
%{_mandir}/man5/libaudit.conf.5*

%files libs-devel
%{_includedir}/audit-records.h
%{_includedir}/audit_logging.h
%{_includedir}/auparse-defs.h
%{_includedir}/auparse.h
%{_includedir}/auplugin.h
%{_includedir}/libaudit.h
%{_libdir}/libaudit.so
%{_libdir}/libauparse.so
%{_libdir}/libauplugin.so
%{_libdir}/pkgconfig/audit.pc
%{_libdir}/pkgconfig/auparse.pc
%{_datadir}/aclocal/audit.m4
%{_mandir}/man3/*.3*
%{_mandir}/man5/ausearch-expression.5*

%files rules
%{_sbindir}/auditctl
%{_sbindir}/augenrules
%{_prefix}/lib/systemd/system/audit-rules.service
%dir %{_sysconfdir}/audit
%dir %attr(0750,root,root) %{_sysconfdir}/audit/rules.d
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/audit/audit-stop.rules
%{_datadir}/audit-rules/
%{_datadir}/bash-completion/completions/auditctl
%{_datadir}/bash-completion/completions/augenrules
%{_mandir}/man7/audit.rules.7*
%{_mandir}/man8/auditctl.8*
%{_mandir}/man8/augenrules.8*

%files -n audispd-plugins
%{_sbindir}/audisp-af_unix
%{_sbindir}/audisp-filter
%{_sbindir}/audisp-remote
%{_sbindir}/audisp-syslog
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/audit/audisp-filter.conf
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/audit/audisp-remote.conf
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/audit/plugins.d/af_unix.conf
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/audit/plugins.d/au-remote.conf
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/audit/plugins.d/filter.conf
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/audit/plugins.d/syslog.conf
%attr(0700,root,root) %dir %{_localstatedir}/spool/audit
%{_mandir}/man5/audisp-remote.conf.5*
%{_mandir}/man8/audisp-af_unix.8*
%{_mandir}/man8/audisp-filter.8*
%{_mandir}/man8/audisp-remote.8*
%{_mandir}/man8/audisp-syslog.8*

%files -n audispd-plugins-zos
%{_sbindir}/audispd-zos-remote
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/audit/plugins.d/audispd-zos-remote.conf
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/audit/zos-remote.conf
%{_mandir}/man5/zos-remote.conf.5*
%{_mandir}/man8/audispd-zos-remote.8*
