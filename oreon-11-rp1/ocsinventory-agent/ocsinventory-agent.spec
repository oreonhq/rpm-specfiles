%global source0_hash 5aa171c48a21db8dc17e96b7e4d5a80cdbd30979c963a654b6974b8bb1e0efe1
%global debug_package %{nil}
%global official_version 2.10.4
Name:      ocsinventory-agent
Summary:        Open Computer and Software Inventory Next Generation client
Version:   2.10.4
Release:        7%{?dist}
Source0:        https://github.com/OCSInventory-NG/UnixAgent/releases/download/v%{version}/Ocsinventory-Unix-Agent-%{version}.tar.gz
Source11:   %{name}.README
License:   GPL-2.0-or-later
URL:       http://www.ocsinventory-ng.org/
Requires(post): systemd
Requires: perl-Ocsinventory-Agent = %{version}-%{release}
%ifarch %{ix86} x86_64 ia64
Requires:  dmidecode
%endif
Requires:  logrotate
Obsoletes: ocsinventory-client < %{version}
Provides:  ocsinventory-client = %{version}-%{release}
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(English)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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
%if 0%{?fedora} >= 25 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
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
rm -rf %{buildroot}%{perl_vendorlib}/Ocsinventory/Agent/Backend/OS/Win32*
rm -f %{buildroot}%{perl_vendorarch}/auto/Ocsinventory/Unix/Agent/.packlist
rm -f %{buildroot}%{perl_vendorarch}/../perllocal.pod
rm %{buildroot}%{perl_vendorlib}/Ocsinventory/Unix/postinst.pl
rm %{buildroot}%{_sbindir}/ipdiscover
find %{buildroot} -type f -exec chmod 644 {} \;
find %{buildroot} -type f -name .DS_Store -exec rm {} \;
find %{buildroot} -type f -name ._.DS_Store -exec rm {} \;
%oreon_autofiles perl-Ocsinventory-Agent usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post ocsinventory-agent-onboot.timer
%systemd_post ocsinventory-agent-hourly.timer
%systemd_post ocsinventory-agent-daily.timer
%files -f %{oreon_filedir}/main.list
%files -n perl-Ocsinventory-Agent -f %{oreon_filedir}/perl-Ocsinventory-Agent.list

%changelog

%autochangelog
