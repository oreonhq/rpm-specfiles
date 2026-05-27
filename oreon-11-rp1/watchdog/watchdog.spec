%global source0_hash b8e7c070e1b72aee2663bdc13b5cc39f76c9232669cfbb1ac0adc7275a3b019d

Summary:          Software and/or Hardware watchdog daemon
Name:             watchdog
Version:          5.16
Release:          12%{?dist}
License:          GPL-2.0-or-later

URL:              http://sourceforge.net/projects/watchdog/
Source0:          http://downloads.sourceforge.net/watchdog/watchdog-%{version}.tar.gz
Source2:          README.watchdog.ipmi
Source3:          README.Fedora
Source4:          watchdog.service
Source5:          watchdog-ping.service

# Fixes building on glibc without RPC.  Sent upstream 2019-02-06.
Patch1:           0001-Choose-libtirpc-or-another-RPC-library-for-XDR-heade.patch
# Fixes potentional mem leak
Patch2:           0002-mem-leak-verbose.patch

# Non-upstream patch to document SELinux support.
Patch99:          0099-watchdog-5.16-rhseldoc.patch

BuildRequires: make
BuildRequires:    gcc
BuildRequires:    libtirpc-devel
BuildRequires:    systemd-units
# Required because patches touch configure.ac and Makefile.am:
BuildRequires:    autoconf, automake

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
The watchdog program can be used as a powerful software watchdog daemon 
or may be alternately used with a hardware watchdog device such as the 
IPMI hardware watchdog driver interface to a resident Baseboard 
Management Controller (BMC).  watchdog periodically writes to /dev/watchdog; 
the interval between writes to /dev/watchdog is configurable through settings 
in the watchdog config file.  This configuration file is also used to 
set the watchdog to be used as a hardware watchdog instead of its default 
software watchdog operation.  In either case, if the device is open but not 
written to within the configured time period, the watchdog timer expiration 
will trigger a machine reboot. When operating as a software watchdog, the 
ability to reboot will depend on the state of the machine and interrupts.  
When operating as a hardware watchdog, the machine will experience a hard 
reset (or whatever action was configured to be taken upon watchdog timer 
expiration) initiated by the BMC.

 
%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}-%{version}
%patch 1 -p1
%patch 2 -p1
%patch 99 -p1 -b .rhseldoc
autoreconf -i

cp %{SOURCE2} .
cp %{SOURCE3} .
%if 0%{?rhel} || 0%{?oreon}
mv README.Fedora README.RHEL
%endif

mv README README.orig
iconv -f ISO-8859-1 -t UTF-8 < README.orig > README


%build
%configure \
    CFLAGS="%{__global_cflags} -I/usr/include/tirpc" \
    LDFLAGS="%{__global_ldflags} -ltirpc"
make %{?_smp_mflags}


%install
install -d -m0755 ${RPM_BUILD_ROOT}%{_sysconfdir}
install -d -m0755 ${RPM_BUILD_ROOT}%{_sysconfdir}/watchdog.d
make DESTDIR=${RPM_BUILD_ROOT} install
install -Dp -m0644 %{SOURCE4} ${RPM_BUILD_ROOT}%{_unitdir}/watchdog.service
install -Dp -m0644 %{SOURCE5} ${RPM_BUILD_ROOT}%{_unitdir}/watchdog-ping.service
install -Dd -m0755 ${RPM_BUILD_ROOT}%{_libexecdir}/watchdog/scripts
rm %{name}.sysconfig


%post
%systemd_post watchdog.service

%preun 
%systemd_preun watchdog.service
%systemd_preun watchdog.ping.service

%postun 
%systemd_postun_with_restart watchdog.service
%systemd_postun_with_restart watchdog.ping.service

%triggerun -- watchdog < 5.9-4
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply watchdog
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save watchdog >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del watchdog >/dev/null 2>&1 || :
/bin/systemctl try-restart watchdog.service >/dev/null 2>&1 || :
/bin/systemctl try-restart watchdog-ping.service >/dev/null 2>&1 || :


%files
%doc AUTHORS ChangeLog COPYING examples/ IAFA-PACKAGE NEWS README TODO README.watchdog.ipmi
%if 0%{?rhel} || 0%{?oreon}
%doc README.RHEL
%else
%doc README.Fedora
%endif
%config(noreplace) %{_sysconfdir}/watchdog.conf
%{_sysconfdir}/watchdog.d
%{_sbindir}/watchdog
%{_sbindir}/wd_identify
%{_sbindir}/wd_keepalive
%{_mandir}/man5/watchdog.conf.5*
%{_mandir}/man8/watchdog.8*
%{_mandir}/man8/wd_identify.8*
%{_mandir}/man8/wd_keepalive.8*
%{_unitdir}/watchdog.service
%{_unitdir}/watchdog-ping.service
%{_libexecdir}/watchdog/scripts


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.16-12
- Import
