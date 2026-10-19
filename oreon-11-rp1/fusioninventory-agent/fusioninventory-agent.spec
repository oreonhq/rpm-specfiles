%global source0_hash 83e0e350cc82781f1142e4bc8deea901324a23f9d64e8ead80102dfd680a83df
%global debug_package %{nil}
Name:        fusioninventory-agent
Summary:        FusionInventory agent
License:     GPL-2.0-or-later
URL:         http://fusioninventory.org/
Version:     2.6
Release:        1%{?dist}
Source0:        https://github.com/fusioninventory/%{name}/releases/download/%{version}/FusionInventory-Agent-%{version}.tar.gz
Source1:     %{name}.cron
Source10:    %{name}.service
Requires:  perl-FusionInventory-Agent = %{version}-%{release}
Requires:  cronie
%ifarch %{ix86} x86_64
Requires:  dmidecode
%endif
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(setup\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Win32|setup\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(English)
BuildRequires:  perl(Module::AutoInstall)
BuildRequires:  perl(Module::Install::Include)
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
BuildRequires:  systemd
# /oreon:deps
%description
FusionInventory Agent is an application designed to help a network
or system administrator to keep track of the hardware and software
configurations of computers that are installed on the network.

This agent can send information about the computer to a OCS Inventory NG
or GLPI server with the FusionInventory for GLPI plugin.

You can add additional packages for optional tasks:

* fusioninventory-agent-task-network
    Network Discovery and Inventory support
* fusioninventory-agent-inventory
    Local inventory support for FusionInventory
* fusioninventory-agent-task-deploy
    Software deployment support
* fusioninventory-agent-task-esx
    vCenter/ESX/ESXi remote inventory
* fusioninventory-agent-task-collect
    Custom information retrieval support
* fusioninventory-agent-task-wakeonlan
    Wake o lan task

%package -n perl-FusionInventory-Agent
Summary:        Libraries for Fusioninventory agent
BuildArch:      noarch
Requires:       perl(LWP)
Requires:       perl(Net::CUPS)
Requires:       perl(Net::SSLeay)
Requires:       perl(Proc::Daemon)
Requires:       perl(Socket::GetAddrInfo)
%description -n perl-FusionInventory-Agent
Libraries for Fusioninventory agent.

%package task-esx
Summary:    FusionInventory plugin to inventory vCenter/ESX/ESXi
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
%description task-esx
fusioninventory-agent-task-ESX ask the running service agent to inventory an 
VMWare vCenter/ESX/ESXi server through SOAP interface

%package task-network
Summary:    NetDiscovery and NetInventory task for FusionInventory
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description task-network
fusioninventory-task-netdiscovery and fusioninventory-task-netinventory

%package task-deploy
Summary:    Software deployment support for FusionInventory agent
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Requires:   perl(Archive::Extract)
%description task-deploy
This package provides software deployment support for FusionInventory-agent

%package task-wakeonlan
Summary:    WakeOnLan task for FusionInventory
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
%description task-wakeonlan
fusioninventory-task-wakeonlan

%package task-inventory
Summary:    Inventory task for FusionInventory
Requires:   %{name} = %{version}-%{release}
Requires:   perl(Net::CUPS)
Requires:   perl(Parse::EDID)
%description task-inventory
fusioninventory-task-inventory

%package task-collect
Summary:    Custom information retrieval support for FusionInventory agent
Requires:   %{name} = %{version}-%{release}
%description task-collect
This package provides custom information retrieval support for
FusionInventory agent

%package cron
Summary:    Cron for FusionInventory agent
Requires:   %{name} = %{version}-%{release}
%description cron
fusioninventory cron task

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n FusionInventory-Agent-%{version}

# Remove bundled modules
rm -rf ./inc
sed -e '/^inc\//d' -i MANIFEST

sed \
    -e "s/logger = .*/logger = syslog/" \
    -e "s/logfacility = .*/logfacility = LOG_DAEMON/" \
    -e 's|#include "conf\.d/"|include "conf\.d/"|' \
    -i etc/agent.cfg

cat <<EOF | tee %{name}.conf
#
# Fusion Inventory Agent Configuration File
# used by hourly cron job to override the %{name}.cfg setup.
#
# /!\
# USING THIS FILE TO OVERRIDE SERVICE OPTIONS IS DEPRECATED!
# See %{_unitdir}/%{name}.service notice
#
# Add tools directory if needed (tw_cli, hpacucli, ipssend, ...)
PATH=/sbin:/bin:/usr/sbin:/usr/bin
# Global options (debug for verbose log)
OPTIONS="--debug "

# Mode, change to "cron" to activate
# - none (default on install) no activity
# - cron (inventory only) use the cron.hourly
OCSMODE[0]=none
# OCS Inventory or FusionInventory server URI
# OCSSERVER[0]=your.ocsserver.name
# OCSSERVER[0]=http://your.ocsserver.name/ocsinventory
# OCSSERVER[0]=http://your.glpiserveur.name/glpi/plugins/fusioninventory/
# corresponds with --local=%{_localstatedir}/lib/%{name}
# OCSSERVER[0]=local
# Wait before inventory (for cron mode)
OCSPAUSE[0]=120
# Administrative TAG (optional, must be filed before first inventory)
OCSTAG[0]=

EOF

%build

perl Makefile.PL \
     PREFIX=%{_prefix} \
     SYSCONFDIR=%{_sysconfdir}/fusioninventory \
     LOCALSTATEDIR=%{_localstatedir}/lib/%{name} \
     VERSION=%{version}-%{release}
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/fusioninventory/conf.d
mkdir -p %{buildroot}%{_sysconfdir}/systemd/system/%{name}.service.d
install -m 644 -D  %{name}.conf  %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -m 755 -Dp %{SOURCE1}    %{buildroot}%{_sysconfdir}/cron.hourly/%{name}
install -m 644 -D  %{SOURCE10}   %{buildroot}%{_unitdir}/%{name}.service
%oreon_autofiles perl-FusionInventory-Agent usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%post

%systemd_post fusioninventory-agent.service
%preun

%systemd_preun fusioninventory-agent.service
%postun

%systemd_postun_with_restart fusioninventory-agent.service
%files -f %{oreon_filedir}/main.list
%files -n perl-FusionInventory-Agent -f %{oreon_filedir}/perl-FusionInventory-Agent.list
%files -n fusioninventory-agent-task-esx -f %{oreon_filedir}/fusioninventory-agent-task-esx.list
%files -n fusioninventory-agent-task-network -f %{oreon_filedir}/fusioninventory-agent-task-network.list
%files -n fusioninventory-agent-task-deploy -f %{oreon_filedir}/fusioninventory-agent-task-deploy.list
%files -n fusioninventory-agent-task-wakeonlan -f %{oreon_filedir}/fusioninventory-agent-task-wakeonlan.list
%files -n fusioninventory-agent-task-inventory -f %{oreon_filedir}/fusioninventory-agent-task-inventory.list
%files -n fusioninventory-agent-task-collect -f %{oreon_filedir}/fusioninventory-agent-task-collect.list
%files -n fusioninventory-agent-cron -f %{oreon_filedir}/fusioninventory-agent-cron.list

%changelog

%autochangelog
