%global source0_hash 5aa171c48a21db8dc17e96b7e4d5a80cdbd30979c963a654b6974b8bb1e0efe1

# spec file for ocsinventory-agent
#
# Copyright (c) 2007-2014 Remi Collet
# Copyright (c) 2016-2017 Philippe Beaumont
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#

# Can, optionaly, be define at build time (see README.RPM)
# - ocstag    : administrative tag
# - ocsserver : OCS Inventory NG communication serveur

# Avoid empty debuginfo package, arched only for dep
%global debug_package %{nil}

# Official release version
%global official_version 2.10.4

Name:      ocsinventory-agent
Summary:   Open Computer and Software Inventory Next Generation client

Version:   2.10.4
Release:   7%{?dist}

Source0:   https://github.com/OCSInventory-NG/UnixAgent/releases/download/v%{official_version}/Ocsinventory-Unix-Agent-%{official_version}.tar.gz

Source11:   %{name}.README

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:   GPL-2.0-or-later
URL:       http://www.ocsinventory-ng.org/

BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: make
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(Config)
BuildRequires: perl(English)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(inc::Module::Install)
BuildRequires: perl(Module::Install::Metadata)
BuildRequires: perl(Module::Install::Scripts)
BuildRequires: perl(Module::Install::WriteAll)
BuildRequires: perl(strict)
BuildRequires: sed

%if 0%{?rhel} >= 7
BuildRequires: systemd
Requires(post): systemd
%else
BuildRequires: systemd-rpm-macros
Requires(post): systemd
%endif

###
#  NOTE: rpmlint: the runtime requirments change depending on the arch
#        so while this package contains no binaries, it is arch dependant.
###
Requires: perl-Ocsinventory-Agent = %{version}-%{release}
%ifarch %{ix86} x86_64 ia64
Requires:  dmidecode
%endif

Requires:  logrotate

Obsoletes: ocsinventory-client < %{version}
Provides:  ocsinventory-client = %{version}-%{release}

%{?perl_default_filter}

%description
Open Computer and Software Inventory Next Generation is an application
designed to help a network or system administrator keep track of computer
configuration and software installed on the network. 

It also allows deploying software, commands or files on Windows and
Linux client computers.

%{name} provides the client for Linux (Unified Unix Agent).

%description -l fr
Open Computer and Software Inventory Next Generation est une application
destinée à aider l'administrateur système ou réseau à garder un oeil sur
la configuration des machines du réseau et sur les logiciels qui y sont
installés. 

Elle autorise aussi la télédiffusion (ou déploiement) de logiciels, 
de commandes ou de fichiers sur les clients Windows ou Linux.

%{name} fournit le client pour Linux (Agent Unix Unifié)

%package -n perl-Ocsinventory-Agent
Summary:   Libraries %{name}
BuildArch: noarch

Requires:  perl(Data::UUID)
Requires:  perl(Digest::MD5)
Requires:  perl(File::Temp)
Requires:  perl(HTTP::Request)
Requires:  perl(LWP) > 6
Requires:  perl(LWP::Protocol)
Requires:  perl(LWP::Protocol::http)
Requires:  perl(LWP::Protocol::https)
Requires:  perl(Net::IP)
Requires:  perl(Net::Netmask)
Requires:  perl(Net::SNMP)
Requires:  perl(Net::SSLeay)
Requires:  perl(XML::Simple)
Requires: net-tools
Requires: pciutils
Requires: smartmontools
Requires: which
%if 0%{?fedora} >= 25 || 0%{?rhel} >= 8
Recommends: perl(Net::Cups)
Recommends: perl(Net::Ping)
Recommends: perl(Parse::EDID)
Recommends: perl(Proc::Daemon)
Recommends: perl(Proc::PID::File)
Recommends: ipmitool
Suggests: monitor-edid
Suggests: nmap
Suggests: perl(Nmap::Parser)
%endif

Conflicts: %{name} < %{version}

%description  -n perl-Ocsinventory-Agent
Perl libraries for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Ocsinventory-Unix-Agent-%{version}
#%%autopatch -p1
rm -f lib/Ocsinventory/Agent/Network.pm.orig

sed -e 's/\r//' -i snmp/mibs/local/6876.xml

# Remove bundled modules
rm -rf ./inc
if [[ -e MANIFEST ]]; then
  perl -MConfig -i -ne 'print $_ unless m{^inc/}' MANIFEST
fi

###
# NOTE: rpmlint will complain about these macros in comments
#       they are on purpose to permit the comments to match
#       what the values used by the build environment.
###
cat <<EOF >%{name}.conf
# 
# OCS Inventory "Unix Unified Agent" Configuration File
# used by the ocsinventory-agent.service and
# related timers.
#

# Add tools directory if needed (tw_cli, hpacucli, ipssend, ...)
PATH=/sbin:/bin:/usr/sbin:/usr/bin

%if 0%{?ocsserver:1}
# Mode, change to "none" to disable
OCSMODE[0]=cron

# used to override the %{name}.cfg setup.
OCSSERVER[0]=%{ocsserver}

# runs in addition to the remote report
# corresponds with --local=%{_localstatedir}/lib/%{name}
# OCSSERVER[1]=local
%else
# Mode, change to "cron" to activate
OCSMODE[0]=none

# can be used to override the %{name}.cfg setup.
# OCSSERVER[0]=your.ocsserver.name
# 
# corresponds with --local=%{_localstatedir}/lib/%{name}
# OCSSERVER[0]=local
%endif

# Wait before inventory 
OCSPAUSE[0]=100

# Administrative TAG (optional, must be filed before first inventory)
OCSTAG[0]=%{?ocstag}

# If you need an HTTP/HTTPS proxy, fill this out
# OCSPROXYSERVER[0]='http://user:pass@proxy:port'
EOF

cat <<EOF >%{name}.cfg
# 
# OCS Inventory "Unix Unified Agent" Configuration File
#
# options used by timers or /etc/sysconfig/%{name} overide these.
#

# Server URL, unconmment if needed
# server = your.ocsserver.name
local = %{_localstatedir}/lib/%{name}

# Administrative TAG (optional, must be filed before first inventory)
# tag = %{?ocsserver:yourtag}

# How to log, can be File,Stderr,Syslog
logger = Stderr
logfile = %{_localstatedir}/log/%{name}/%{name}.log
EOF

cp %{SOURCE11} README.RPM

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
rm run-postinst

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete

if [[ "%{_bindir}" != "%{_sbindir}" ]]; then
    # Move exe to right directory
    mv %{buildroot}%{_bindir} %{buildroot}%{_sbindir}
fi

mkdir -p %{buildroot}%{_localstatedir}/{log,lib}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/{logrotate.d,sysconfig,ocsinventory/softwares}

mkdir %{buildroot}%{_localstatedir}/lib/%{name}/download
cp -pr snmp %{buildroot}%{_localstatedir}/lib/%{name}/snmp

install -pm 644 %{name}.conf %{buildroot}%{_sysconfdir}/sysconfig/%{name}

mkdir -p %{buildroot}/%{_libexecdir}/%{name}
sed -e 's;/etc/;%{_sysconfdir}/;' \
    -e 's;/var/;%{_localstatedir}/;' \
    -e 's;/usr/sbin/;%{_sbindir}/;' \
    contrib/cron/ocsinventory-agent.cron > %{buildroot}%{_libexecdir}/%{name}/ocsinventory-agent.cron
cp contrib/cron/ocsinventory-agent.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

mkdir -p %{buildroot}/%{_unitdir}
cp contrib/cron/systemd/* %{buildroot}/%{_unitdir}/

install -m 644 %{name}.cfg %{buildroot}/%{_sysconfdir}/ocsinventory/%{name}.cfg
install -m 644 etc/ocsinventory-agent/modules.conf %{buildroot}/%{_sysconfdir}/ocsinventory/modules.conf

# Remove some unusefull files (which brings unresolvable deps)
rm -rf %{buildroot}%{perl_vendorlib}/Ocsinventory/Agent/Backend/OS/Win32*

# Drop extra files
rm -f %{buildroot}%{perl_vendorarch}/auto/Ocsinventory/Unix/Agent/.packlist
rm -f %{buildroot}%{perl_vendorarch}/../perllocal.pod

# Only need for manual installation
rm %{buildroot}%{perl_vendorlib}/Ocsinventory/Unix/postinst.pl

# Provided by ocsinventtory-ipdiscover
rm %{buildroot}%{_sbindir}/ipdiscover

# the source comes with some odd permissions set
# just fix them to make sense
find %{buildroot} -type f -exec chmod 644 {} \;
find %{buildroot} -type f -name .DS_Store -exec rm {} \;
find %{buildroot} -type f -name ._.DS_Store -exec rm {} \;

%post

# See if sysadmin requested ocs agent run on boot
%systemd_post ocsinventory-agent-onboot.timer

# See if sysadmin requested ocs agent hourly run
%systemd_post ocsinventory-agent-hourly.timer

# See if sysadmin requested ocs agent daily run
%systemd_post ocsinventory-agent-daily.timer

%files
%defattr(644,root,root,755)
%attr(0755, root, root) %{_sbindir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_libexecdir}/%{name}/
%attr(0755, root, root) %{_libexecdir}/%{name}/ocsinventory-agent.cron
%dir %{_localstatedir}/log/%{name}
%{_mandir}/man1/%{name}*
%{_unitdir}/*

%files -n perl-Ocsinventory-Agent
%defattr(644,root,root,755)
%doc AUTHORS Changes README.md THANKS README.RPM
%doc etc/ocsinventory-agent/softwares/example.sh
%license LICENSE
%config(noreplace) %{_sysconfdir}/ocsinventory/%{name}.cfg
%config(noreplace) %{_sysconfdir}/ocsinventory/modules.conf
%{perl_vendorlib}/Ocsinventory
%attr(0755, root, root) %{perl_vendorlib}/Ocsinventory/Agent.pm
%{_mandir}/man3/Ocs*
%dir %{_localstatedir}/lib/%{name}
%{_localstatedir}/lib/%{name}/download
%{_localstatedir}/lib/%{name}/snmp
%dir %{_sysconfdir}/ocsinventory
%dir %{_sysconfdir}/ocsinventory/softwares

%changelog
%autochangelog
