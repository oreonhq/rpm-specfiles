%global source0_hash b0b56e08c0d6dee5ad98270cdede05ff68b9c2be05fc25ebcaddd70c52ab8766

Name:           ppc64-diag
Version:        2.7.11
Release:        1%{?dist}
Summary:        PowerLinux Platform Diagnostics
URL:            https://github.com/power-ras/%{name}
License:        GPL-2.0-only
ExclusiveArch:  ppc %{power64}
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libservicelog-devel
BuildRequires:  flex
BuildRequires:  perl-interpreter
BuildRequires:  byacc
BuildRequires:  libvpd-devel >= 2.2.9
BuildRequires:  ncurses-devel
BuildRequires:  librtas-devel >= 1.4.0
BuildRequires:  systemd-units
BuildRequires:  systemd-devel
BuildRequires:  libtool
BuildRequires:  bison

Requires:       ppc64-diag-rtas >= 2.7.6
Requires:       servicelog
Requires:       lsvpd
Requires:       powerpc-utils >= 1.3.0

Source0:        https://github.com/power-ras/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz#/ppc64-diag-2.7.11.tar.gz
Source1:        https://raw.githubusercontent.com/power-ras/%{name}/HEAD/add_regex.8
Source2:        https://raw.githubusercontent.com/power-ras/%{name}/HEAD/convert_dt_node_props.8
Source3:        https://raw.githubusercontent.com/power-ras/%{name}/HEAD/extract_opal_dump.8
Source4:        https://raw.githubusercontent.com/power-ras/%{name}/HEAD/extract_platdump.8
Source5:        https://raw.githubusercontent.com/power-ras/%{name}/HEAD/rtas_errd.8

# fix paths and permissions
Patch0:         ppc64-diag-2.7.9-fedora.patch
# Upstream fixes

%description
This package contains various diagnostic tools for PowerLinux.
These tools captures the diagnostic events from Power Systems
platform firmware, SES enclosures and device drivers, and
write events to servicelog database. It also provides automated
responses to urgent events such as environmental conditions and
predictive failures, if appropriate modifies the FRUs fault
indicator(s) and provides event notification to system
administrators or connected service frameworks.

%package        rtas
Summary:        rtas_errd daemon
# PCI hotplug support on PowerKVM guest depends on below powerpc-utils version.
Requires:       powerpc-utils-core >= 1.3.7-5

%description rtas
This package contains only rtas_errd daemon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Fix warning mangling shebang
sed -i '1s|^#! */bin/sh|#! /usr/bin/sh|' scripts/rtas_errd scripts/opal_errd rtas_errd/rc.powerfail

%build
./autogen.sh
%configure
make %{?_smp_mflags} V=1

%install
make install DESTDIR=$RPM_BUILD_ROOT
chmod 644 COPYING
rm -f $RPM_BUILD_ROOT%{_docdir}/ppc64-diag/*
mkdir -p $RPM_BUILD_ROOT/%{_libexecdir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/ses_pages
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/log/dump
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/log/opal-elog

install -m 644 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} $RPM_BUILD_ROOT/%{_mandir}/man8/
# Fix warning mangling shebang
chmod 644 $RPM_BUILD_ROOT/%{_libexecdir}/%{name}/servevent_parse.pl

%files
%license COPYING
%doc README.md
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/ses_pages
%dir %{_localstatedir}/log/%{name}/diag_disk
%dir %{_localstatedir}/log/dump
%dir %{_localstatedir}/log/opal-elog
%{_mandir}/man8/*
%{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/message_catalog/
%{_libexecdir}/%{name}/ppc64_diag_migrate
%{_libexecdir}/%{name}/ppc64_diag_mkrsrc
%{_libexecdir}/%{name}/ppc64_diag_notify
%{_libexecdir}/%{name}/ppc64_diag_setup
%{_libexecdir}/%{name}/lp_diag_setup
%{_libexecdir}/%{name}/lp_diag_notify
%{_libexecdir}/%{name}/servevent_parse.pl
%{_datadir}/%{name}/message_catalog/*
%{_unitdir}/opal_errd.service
%{_sysconfdir}/cron.daily/run_diag_encl
%{_sysconfdir}/cron.daily/run_diag_nvme

# get rid of obsolete initscripts for rhel >=7
%exclude %{_libexecdir}/%{name}/rtas_errd
%exclude %{_libexecdir}/%{name}/opal_errd

# exclude stuffs which are moved to rtas
%exclude %{_mandir}/man8/convert_dt_node_props*
%exclude %{_mandir}/man8/extract_platdump*
%exclude %{_mandir}/man8/rtas_errd*
%exclude %{_sbindir}/convert_dt_node_props
%exclude %{_sbindir}/extract_platdump
%exclude %{_sbindir}/rtas_errd

%files rtas
%license COPYING
%dir %{_sysconfdir}/%{name}
%{_mandir}/man8/convert_dt_node_props*
%{_mandir}/man8/extract_platdump*
%{_mandir}/man8/rtas_errd*
%config(noreplace) %{_sysconfdir}/%{name}/ppc64-diag.config
%config(noreplace) %{_sysconfdir}/%{name}/diag_nvme.config
%{_bindir}/convert_dt_node_props
%{_bindir}/extract_platdump
%{_bindir}/rtas_errd
%{_sysconfdir}/rc.powerfail
%{_unitdir}/rtas_errd.service

%post
# Post-install script --------------------------------------------------
%{_libexecdir}/%{name}/lp_diag_setup --register >/dev/null 2>&1
%{_libexecdir}/%{name}/ppc64_diag_setup --register >/dev/null 2>&1
if [ "$1" = "1" ]; then # first install
    systemctl -q enable opal_errd.service >/dev/null
    systemctl start opal_errd.service >/dev/null
elif [ "$1" = "2" ]; then # upgrade
    systemctl restart opal_errd.service >/dev/null
    systemctl daemon-reload > /dev/null 2>&1
fi

%preun
# Pre-uninstall script -------------------------------------------------
if [ "$1" = "0" ]; then # last uninstall
    systemctl stop opal_errd.service >/dev/null
    systemctl -q disable opal_errd.service
    %{_libexecdir}/%{name}/ppc64_diag_setup --unregister >/dev/null
    %{_libexecdir}/%{name}/lp_diag_setup --unregister >/dev/null
    systemctl daemon-reload > /dev/null 2>&1
fi

%triggerin -- librtas
# trigger on librtas upgrades ------------------------------------------
if [ "$2" = "2" ]; then
    systemctl restart opal_errd.service >/dev/null
    systemctl restart rtas_errd.service >/dev/null
fi

 
%post rtas
if [ "$1" = "1" ]; then # first install
    systemctl -q enable rtas_errd.service >/dev/null
    systemctl start rtas_errd.service >/dev/null
elif [ "$1" = "2" ]; then # upgrade
    systemctl restart rtas_errd.service >/dev/null
    systemctl daemon-reload > /dev/null 2>&1
fi

%preun rtas
if [ "$1" = "0" ]; then # last uninstall
    systemctl stop rtas_errd.service >/dev/null
    systemctl -q disable rtas_errd.service
    systemctl daemon-reload > /dev/null 2>&1
fi

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.7.11-1
- Import
