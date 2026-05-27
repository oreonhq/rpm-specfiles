%global source0_hash 2d095c8cfcbc847caec746d62cdc8d0bff1ec1bc72ef7c674c721e04da6ab333

# hardened build if not overridden
%{!?_hardened_build:%global _hardened_build 1}

%if %{?_hardened_build}%{!?_hardened_build:0}
%global harden -pie -Wl,-z,relro,-z,now
%endif

Summary: ACPI Event Daemon
Name: acpid
Version: 2.0.34
Release: 17%{?dist}
License: GPL-2.0-or-later
Source: http://downloads.sourceforge.net/acpid2/%{name}-%{version}.tar.xz
Source3: acpid.power.conf
Source4: acpid.power.sh
Source5: acpid.service
Source6: acpid.sysconfig
Source7: acpid.socket
# https://sourceforge.net/p/acpid2/tickets/14/
Patch0: acpid-2.0.32-kacpimon-dynamic-connections.patch
%if 0%{?rhel}
ExclusiveArch: x86_64 aarch64 riscv64
%endif
URL: http://sourceforge.net/projects/acpid2/
BuildRequires: systemd, gcc
BuildRequires: make
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: systemd

%description
acpid is a daemon that dispatches ACPI events to user-space programs.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%patch -P0 -p1 -b .kacpimon-dynamic-connections

%build
%configure
make %{?_smp_mflags} CFLAGS="%{optflags} %{?harden}"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
make install DESTDIR=%{buildroot} docdir=%{_docdir}/%{name}

mkdir -p %{buildroot}%{_sysconfdir}/acpi/events
mkdir -p %{buildroot}%{_sysconfdir}/acpi/actions
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig

chmod 755 %{buildroot}%{_sysconfdir}/acpi/events
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/acpi/events/powerconf
install -p -m 755 %{SOURCE4} %{buildroot}%{_sysconfdir}/acpi/actions/power.sh
install -p -m 644 %{SOURCE5} %{SOURCE7} %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/sysconfig/acpid

%files
%doc %{_docdir}/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket
%dir %{_sysconfdir}/acpi
%dir %{_sysconfdir}/acpi/events
%dir %{_sysconfdir}/acpi/actions
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/acpi/events/powerconf
%config(noreplace) %attr(0755,root,root) %{_sysconfdir}/acpi/actions/power.sh
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/sysconfig/acpid
%{_bindir}/acpi_listen
%{_sbindir}/acpid
%{_sbindir}/kacpimon
%{_mandir}/man8/acpid.8.gz
%{_mandir}/man8/acpi_listen.8.gz
%{_mandir}/man8/kacpimon.8.gz

%pre
if [ "$1" = "2" ]; then
	conflist=`ls %{_sysconfdir}/acpi/events/*.conf 2> /dev/null`
	RETCODE=$?
	if [ $RETCODE -eq 0 ]; then
		for i in $conflist; do
			rmdot=`echo $i | sed 's/.conf/conf/'`
			mv $i $rmdot
		done
	fi
fi

%post
%systemd_post %{name}.socket %{name}.service

%preun
%systemd_preun %{name}.socket %{name}.service

%postun
%systemd_postun_with_restart %{name}.socket %{name}.service

%triggerun -- %{name} < 2.0.10-2
	/sbin/chkconfig --del acpid >/dev/null 2>&1 || :
	/bin/systemctl try-restart acpid.service >/dev/null 2>&1 || :

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.34-17
- Prepare for Oreon 11 (RP1)
