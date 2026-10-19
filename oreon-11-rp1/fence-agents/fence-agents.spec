%global source0_hash d753b7a5df9222d8e5c3dfbab85b12314850fb4f9bdb02bee10805e14228fef6
Name: fence-agents
Summary:        Set of unified programs capable of host isolation ("fencing")
Version: 4.17.0
Release:        1%{?dist}
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Group: System Environment/Base
URL: https://github.com/ClusterLabs/fence-agents
Source0:        https://github.com/ClusterLabs/fence-agents/archive/refs/tags/v%{version}.tar.gz#/fence-agents-%{version}.tar.gz
ExcludeArch: %{ix86}
%define boto3_br 1
%global allfenceagents %(cat <<EOF
fence-agents-alom \\
fence-agents-amt \\
fence-agents-amt-ws \\
fence-agents-apc \\
fence-agents-apc-snmp \\
fence-agents-aws \\
fence-agents-azure-arm \\
fence-agents-bladecenter \\
fence-agents-brocade \\
fence-agents-cdu \\
fence-agents-cisco-mds \\
fence-agents-cisco-ucs \\
fence-agents-cyberpower-ssh \\
fence-agents-docker \\
fence-agents-drac \\
fence-agents-drac5 \\
fence-agents-eaton-snmp \\
fence-agents-eaton-ssh \\
fence-agents-ecloud \\
fence-agents-emerson \\
fence-agents-eps \\
fence-agents-gce \\
fence-agents-hds-cb \\
fence-agents-hetzner-cloud \\
fence-agents-heuristics-ping \\
fence-agents-hpblade \\
fence-agents-ibmblade \\
fence-agents-ibmz \\
fence-agents-ibm-powervs \\
fence-agents-ibm-vpc \\
fence-agents-ifmib \\
fence-agents-ilo-moonshot \\
fence-agents-ilo-mp \\
fence-agents-ilo-ssh \\
fence-agents-ilo2 \\
fence-agents-intelmodular \\
fence-agents-ipdu \\
fence-agents-ipmilan \\
fence-agents-kdump \\
fence-agents-ldom \\
fence-agents-lpar \\
fence-agents-mpath \\
fence-agents-netio \\
fence-agents-nutanix-ahv \\
fence-agents-ovh \\
fence-agents-ovm \\
fence-agents-redfish \\
fence-agents-rhevm \\
fence-agents-rsa \\
fence-agents-rsb \\
fence-agents-sanbox2 \\
fence-agents-sbd \\
fence-agents-scsi \\
fence-agents-shelly \\
fence-agents-vbox \\
fence-virt \\
fence-agents-vmware \\
fence-agents-vmware-rest \\
fence-agents-vmware-soap \\
fence-agents-vmware-vcloud \\
fence-agents-wti \\
fence-agents-xenapi \\
fence-agents-zvm \\
EOF)
%ifarch x86_64 ppc64le
%global allfenceagents %(cat <<EOF
%{allfenceagents} \\
fence-agents-aws \\
fence-agents-compute \\
fence-agents-gce \\
fence-agents-ironic \\
fence-agents-openstack
EOF)
%endif
%if 0%{?suse_version} > 1500
%else
%endif
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel} || (0%{?oreon} >= 11)
%if %{boto3_br}
%endif
%else
%if %{boto3_br}
%endif
%endif
%if 0%{?suse_version}
%define nss_devel mozilla-nss-devel
%define nspr_devel mozilla-nspr-devel
%define systemd_units systemd
%else
%define nss_devel nss-devel
%define nspr_devel nspr-devel
%define systemd_units systemd-units
%endif
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*!!g')
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  corosynclib-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  libvirt-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  nspr-devel
BuildRequires:  nss-devel
BuildRequires:  openwsman-python3
BuildRequires:  python3-boto3
BuildRequires:  python3-devel
BuildRequires:  python3-httplib2
BuildRequires:  python3-pexpect
BuildRequires:  python3-pycurl
BuildRequires:  python3-requests
BuildRequires:  python3-suds
BuildRequires:  systemd-units
# /oreon:deps
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}
# prevent compilation of something that won't get used anyway
sed -i.orig 's|FENCE_ZVM=1|FENCE_ZVM=0|' configure.ac
echo %{version} > .tarball-version

%build

export PYTHON="%{__python3}"
./autogen.sh
%{configure} \
%if %{defined _tmpfilesdir}
	SYSTEMD_TMPFILES_DIR=%{_tmpfilesdir} \
	--with-fencetmpdir=/run/fence-agents
%endif
CFLAGS="$(echo '%{optflags}')" make %{_smp_mflags}
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/%{_unitdir}/
install -m 0644 agents/virt/fence_virtd.service %{buildroot}/%{_unitdir}/
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel} || (0%{?oreon} >= 11)
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/fence
%endif
chmod 0755 %{buildroot}%{_datadir}/fence/*.py
rm -rf %{buildroot}/usr/share/doc/fence-agents
rm -f %{buildroot}/%{_libdir}/%{name}/*.*a
rm -f %{buildroot}/%{_libdir}/fence-virt/*.*a
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

ccs_update_schema > /dev/null 2>&1 ||:
if [ $1 -eq 1 ] ; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%preun

if [ $1 -eq 0 ] ; then
    /bin/systemctl --no-reload disable fence_virtd.service &> /dev/null || :
    /bin/systemctl stop fence_virtd.service &> /dev/null || :
fi
%postun

/bin/systemctl daemon-reload &> /dev/null || :
if [ $1 -ge 1 ] ; then
    /bin/systemctl try-restart fence_virtd.service &> /dev/null || :
fi
%triggerun -- fence_virtd < 0.3.0-1

/usr/bin/systemd-sysv-convert --save fence_virtd &> /dev/null || :
/sbin/chkconfig --del fence_virtd &> /dev/null || :
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
/bin/systemctl try-restart fence_virtd.service &> /dev/null || :
%description
A collection of executables to handle isolation ("fencing") of possibly
misbehaving hosts by the means of remote power management, blocking
network, storage, or similar. They operate through a unified interface
(calling conventions) devised for the original Red Hat clustering solution.

%package common
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Common base for Fence Agents
Requires: python3-pexpect python3-pycurl
BuildArch: noarch
%description common
A collection of executables to handle isolation ("fencing") of possibly
misbehaving hosts by the means of remote power management, blocking
network, storage, or similar.

This package contains support files including the Python fencing library.
%package all
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND Apache-2.0
Summary: Set of unified programs capable of host isolation ("fencing")
Requires: %{allfenceagents}
Provides: fence-agents = %{version}-%{release}
Obsoletes: fence-agents < 3.1.13
%description all
A collection of executables to handle isolation ("fencing") of possibly
misbehaving hosts by the means of remote power management, blocking
network, storage, or similar.

This package serves as a catch-all for all supported fence agents.
%package aliyun
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND Apache-2.0 AND BSD-3-Clause AND MIT
Group: System Environment/Base
Summary: Fence agent for Alibaba Cloud (Aliyun)
Requires: fence-agents-common >= %{version}-%{release}
Requires: python3-jmespath >= 0.9.0
Obsoletes: %{name} < %{version}-%{release}
%description aliyun
The fence-agents-aliyun package contains a fence agent for Alibaba Cloud (Aliyun) instances.
%package alom
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for SUN ALOM
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version} || (0%{?oreon} >= 11)
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description alom
Fence agent for SUN ALOM.
%package amt
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Intel AMT devices
Requires: amtterm
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description amt
Fence agent for AMT compatibile devices that are accessed via
3rd party software.
%package amt-ws
License: Apache-2.0
Summary: Fence agent for Intel AMT (WS-Man) devices
Requires: fence-agents-common = %{version}-%{release}
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel} || (0%{?oreon} >= 11)
Requires: openwsman-python3
%else
Requires: python3-openwsman
%endif
BuildArch: noarch
%description amt-ws
Fence agent for AMT (WS-Man) devices.
%package apc
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for APC devices
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version} || (0%{?oreon} >= 11)
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description apc
Fence agent for APC devices that are accessed via telnet or SSH.
%package apc-snmp
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agents for APC devices (SNMP)
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description apc-snmp
Fence agents for APC devices that are accessed via the SNMP protocol.
%package aws
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Amazon AWS
Requires: fence-agents-common = %{version}-%{release}
Requires: python3-boto3
BuildArch: noarch
Obsoletes: fence-agents < 3.1.13
%description aws
Fence agent for Amazon AWS instances.
%package aws-vpc-net
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Amazon AWS VPC network and power fencer
Requires: fence-agents-common = %{version}-%{release}
Requires: python3-boto3
BuildArch: noarch
Obsoletes: fence-agents < 3.1.13
%description aws-vpc-net
Fence agent for Amazon AWS instances that fences by modifying aws sec groups
%package azure-arm
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Azure Resource Manager
Requires: fence-agents-common = %{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 9 || (0%{?oreon} >= 11)
Requires: python3-azure-sdk
%else
Requires: python3-azure-common
Requires: python3-azure-identity
Requires: python3-azure-mgmt-compute
Requires: python3-azure-mgmt-network
%if 0%{?rhel} && 0%{?rhel} < 10 || (0%{?oreon} >= 11)
Requires: python3-msrestazure
%endif
%endif
BuildArch: noarch
Obsoletes: fence-agents < 3.1.13
%description azure-arm
Fence agent for Azure Resource Manager instances.
%package bladecenter
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for IBM BladeCenter
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version} || (0%{?oreon} >= 11)
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description bladecenter
Fence agent for IBM BladeCenter devices that are accessed
via telnet or SSH.
%package brocade
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Brocade switches
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version} || (0%{?oreon} >= 11)
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description brocade
Fence agent for Brocade devices that are accessed via telnet or SSH.
%package cdu
License: GPL-3.0-only
Summary: Fence agent for a Sentry Switch CDU
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description cdu
Fence agent for Sentry Switch CDU power switch.
%package cisco-mds
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Cisco MDS 9000 series
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description cisco-mds
Fence agent for Cisco MDS 9000 series devices that are accessed
via the SNMP protocol.
%package cisco-ucs
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Cisco UCS series
Requires: python3-pycurl
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description cisco-ucs
Fence agent for Cisco UCS series devices that are accessed
via the SNMP protocol.
%package compute
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Nova compute nodes
Requires: python3-requests
Requires: python3-novaclient
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description compute
Fence agent for Nova compute nodes.
%package cyberpower-ssh
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for CyberPower network PDUs
Requires: openssh-clients
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description cyberpower-ssh
%package docker
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Docker
Requires: python3-pycurl
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description docker
Fence agent for Docker images that are accessed over HTTP.
%package drac
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Dell DRAC
Requires: telnet
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description drac
Fence agent for Dell DRAC IV series devices that are accessed
via telnet.
%package drac5
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Dell DRAC 5
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version} || (0%{?oreon} >= 11)
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description drac5
Fence agent for Dell DRAC 5 series devices that are accessed
via telnet or SSH.
%package eaton-snmp
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Eaton network power switches
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description eaton-snmp
Fence agent for Eaton network power switches that are accessed
via the SNMP protocol.
%package eaton-ssh
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Eaton network power switches
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description eaton-ssh
Fence agent for Eaton network power switches that are accessed
via the serial protocol tunnel over SSH.
%package ecloud
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for eCloud and eCloud VPC
Requires: python3-requests
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ecloud
Fence agent for eCloud and eCloud VPC from ANS Group Limited
%package emerson
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Emerson devices (SNMP)
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description emerson
Fence agent for Emerson devices that are accessed via
the SNMP protocol.
%package eps
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for ePowerSwitch 8M+ power switches
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description eps
Fence agent for ePowerSwitch 8M+ power switches that are accessed
via the HTTP(s) protocol.
%package gce
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for GCE (Google Cloud Engine)
Requires: fence-agents-common = %{version}-%{release}
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel} || (0%{?oreon} >= 11)
Requires: python3-google-api-client
%else
Requires: python3-google-api-python-client
%endif
BuildArch: noarch
Obsoletes: fence-agents < 3.1.13
%description gce
Fence agent for GCE (Google Cloud Engine) instances.
%package hds-cb
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Hitachi Compute Blade systems
Requires: telnet
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description hds-cb
Fence agent for Hitachi Compute Blades that are accessed via telnet.
%package hetzner-cloud
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Hetzner Cloud
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
Obsoletes: fence-agents < 3.1.13
%description hetzner-cloud
Fence agent for Hetzner Cloud.
%package heuristics-ping
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Pseudo fence agent to affect other agents based on ping-heuristics
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
Obsoletes: fence-agents < 3.1.13
%description heuristics-ping
Fence pseudo agent used to affect other agents based on
ping-heuristics.
%package hpblade
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for HP BladeSystem devices
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version} || (0%{?oreon} >= 11)
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description hpblade
Fence agent for HP BladeSystem devices that are accessed via telnet
or SSH.
%package ibmblade
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for IBM BladeCenter
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ibmblade
Fence agent for IBM BladeCenter devices that are accessed
via the SNMP protocol.
%package ibmz
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for IBM z LPARs
Requires: python3-requests
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ibmz
Fence agent for IBM z LPARs that are accessed via the HMC
Web Services REST API.
%package ibm-powervs
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for IBM PowerVS
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ibm-powervs
Fence agent for IBM PowerVS that are accessed via REST API.
%package ibm-vpc
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for IBM Cloud VPC
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ibm-vpc
Fence agent for IBM Cloud VPC that are accessed via REST API.
%package ifmib
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for devices with IF-MIB interfaces
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ifmib
Fence agent for IF-MIB interfaces that are accessed via
the SNMP protocol.
%package ilo2
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agents for HP iLO2 devices
Requires: gnutls-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ilo2
Fence agents for HP iLO2 devices that are accessed via
the HTTP(s) protocol.
%package ilo-moonshot
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for HP iLO Moonshot devices
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version} || (0%{?oreon} >= 11)
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ilo-moonshot
Fence agent for HP iLO Moonshot devices that are accessed
via telnet or SSH.
%package ilo-mp
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for HP iLO MP devices
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version} || (0%{?oreon} >= 11)
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ilo-mp
Fence agent for HP iLO MP devices that are accessed via telnet or SSH.
%package ilo-ssh
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agents for HP iLO devices over SSH
Requires: openssh-clients
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ilo-ssh
Fence agents for HP iLO devices that are accessed via telnet or SSH.
%package intelmodular
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for devices with Intel Modular interfaces
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description intelmodular
Fence agent for Intel Modular interfaces that are accessed
via the SNMP protocol.
%package ipdu
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for IBM iPDU network power switches
Requires: net-snmp-utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ipdu
Fence agent for IBM iPDU network power switches that are accessed
via the SNMP protocol.
%package ipmilan
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agents for devices with IPMI interface
Requires: /usr/bin/ipmitool
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ipmilan
Fence agents for devices with IPMI interface.
%package ironic
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for OpenStack's Ironic (Bare Metal as a service)
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ironic
Fence agent for OpenStack's Ironic (Bare Metal as a service) service.
%package kdump
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for use with kdump crash recovery service
Requires: fence-agents-common = %{version}-%{release}
%description kdump
Fence agent for use with kdump crash recovery service.
%package kubevirt
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for KubeVirt platform
Requires: python3-openshift >= 0.12.1
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description kubevirt
Fence agent for KubeVirt platform.
%package ldom
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Sun LDom virtual machines
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version} || (0%{?oreon} >= 11)
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ldom
Fence agent for APC devices that are accessed via telnet or SSH.
%package lpar
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for IBM LPAR
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version} || (0%{?oreon} >= 11)
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description lpar
Fence agent for IBM LPAR devices that are accessed via telnet or SSH.
%package mpath
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for reservations over Device Mapper Multipath
Requires: device-mapper-multipath
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description mpath
Fence agent for SCSI persistent reservation over
Device Mapper Multipath.
%package netio
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Koukaam NETIO devices
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version} || (0%{?oreon} >= 11)
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description netio
Fence agent for Koukaam NETIO devices that are accessed
via telnet or SSH.
%package nutanix-ahv
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Nutanix AHV
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
Obsoletes: fence-agents < 3.1.13
%description nutanix-ahv
Fence agent for Nutanix AHV clusters.
%package openstack
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for OpenStack's Nova service
Requires: python3-requests
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description openstack
Fence agent for OpenStack's Nova service.
%package ovh
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for OVH provider
%if 0%{?suse_version} > 1500
Requires: python3-suds-community
%else
Requires: python3-suds
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ovh
Fence agent for OVH hosting provider.
%package ovm
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Oracle VM provider
Requires: python3-requests
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description ovm
Fence agent for Oracle VM provider.
%package pve
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for PVE
Requires: python3-pycurl
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description pve
Fence agent for PVE.
%package raritan
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Raritan Dominion PX
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description raritan
Fence agent for Raritan Dominion PX.
%package rcd-serial
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for RCD serial
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description rcd-serial
Fence agent for RCD serial.
%package redfish
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Group: System Environment/Base
Summary: Fence agent for Redfish
Requires: fence-agents-common >= %{version}-%{release}
Requires: python3-requests
Obsoletes: fence-agents < 3.1.13
%description redfish
The fence-agents-redfish package contains a fence agent for Redfish
%package rhevm
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for RHEV-M
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description rhevm
Fence agent for RHEV-M via REST API.
%package rsa
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for IBM RSA II
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version} || (0%{?oreon} >= 11)
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description rsa
Fence agent for IBM RSA II devices that are accessed
via telnet or SSH.
%package rsb
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Fujitsu RSB
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version} || (0%{?oreon} >= 11)
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description rsb
Fence agent for Fujitsu RSB devices that are accessed
via telnet or SSH.
%package sanbox2
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for QLogic SANBox2 FC switches
Requires: telnet
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description sanbox2
Fence agent for QLogic SANBox2 switches that are accessed via telnet.
%package sbd
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for SBD (storage-based death)
Requires: sbd
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description sbd
Fence agent for SBD (storage-based death).
%package scsi
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for SCSI persistent reservations
Requires: sg3_utils
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description scsi
Fence agent for SCSI persistent reservations.
%package shelly
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Shelly Switches
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description shelly
Fence agent for Shelly Switches.
%package vbox
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for VirtualBox
Requires: openssh-clients
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description vbox
Fence agent for VirtualBox dom0 accessed via SSH.
%package virsh
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for virtual machines based on libvirt
Requires: openssh-clients /usr/bin/virsh
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description virsh
Fence agent for virtual machines that are accessed via SSH.
%package vmware
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for VMWare with VI Perl Toolkit or vmrun
Requires: python3-pexpect
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description vmware
Fence agent for VMWare accessed with VI Perl Toolkit or vmrun.
%package vmware-rest
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for VMWare with REST API
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
Obsoletes: fence-agents < 3.1.13
%description vmware-rest
Fence agent for VMWare with REST API.
%package vmware-soap
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for VMWare with SOAP API v4.1+
%if 0%{?suse_version} > 1500
Requires: python3-suds-community
%else
Requires: python3-suds
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description vmware-soap
Fence agent for VMWare with SOAP API v4.1+.
%package vmware-vcloud
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for VMWare vCloud Director
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
Obsoletes: fence-agents < 3.1.13
%description vmware-vcloud
Fence agent for VMWare vCloud Director.
%package wti
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for WTI Network power switches
Requires: openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version} || (0%{?oreon} >= 11)
Recommends: telnet
%endif
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description wti
Fence agent for WTI network power switches that are accessed
via telnet or SSH.
%package xenapi
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for Citrix XenServer over XenAPI
Requires: python3-pexpect
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description xenapi
Fence agent for Citrix XenServer accessed over XenAPI.
%package zvm
License: GPL-2.0-or-later AND LGPL-2.0-or-later
Summary: Fence agent for IBM z/VM over IP
Requires: fence-agents-common = %{version}-%{release}
BuildArch: noarch
%description zvm
Fence agent for IBM z/VM over IP.
%package -n fence-virt
Summary: A pluggable fencing framework for virtual machines
Requires(post):	systemd-sysv %{systemd_units}
Requires(preun):	%{systemd_units}
Requires(postun):	%{systemd_units}
%description -n fence-virt
Fencing agent for virtual machines.
%package -n fence-virtd
Summary: Daemon which handles requests from fence-virt
%description -n fence-virtd
This package provides the host server framework, fence_virtd,
for fence_virt.  The fence_virtd host daemon is resposible for
processing fencing requests from virtual machines and routing
the requests to the appropriate physical machine for action.
%package -n fence-virtd-multicast
Summary:  Multicast listener for fence-virtd
Requires: fence-virtd
%description -n fence-virtd-multicast
Provides multicast listener capability for fence-virtd.
%package -n fence-virtd-serial
Summary:  Serial VMChannel listener for fence-virtd
Requires: libvirt >= 0.6.2
Requires: fence-virtd
%description -n fence-virtd-serial
Provides serial VMChannel listener capability for fence-virtd.
%package -n fence-virtd-tcp
Summary:  TCP listener for fence-virtd
Requires: fence-virtd
%description -n fence-virtd-tcp
Provides TCP listener capability for fence-virtd.
%package -n fence-virtd-libvirt
Summary:  Libvirt backend for fence-virtd
Requires: libvirt >= 0.6.0
Requires: fence-virtd
%description -n fence-virtd-libvirt
Provides fence_virtd with a connection to libvirt to fence
virtual machines.  Useful for running a cluster of virtual
machines on a desktop.
%package -n fence-virtd-cpg
Summary:  CPG/libvirt backend for fence-virtd
Requires: corosynclib
Requires: fence-virtd
%description -n fence-virtd-cpg
Provides fence_virtd with a connection to libvirt to fence
virtual machines. Uses corosync CPG to keep track of VM
locations to allow for non-local VMs to be fenced when VMs
are located on corosync cluster nodes.
%files -f %{oreon_filedir}/main.list
%files -n fence-agents-common -f %{oreon_filedir}/fence-agents-common.list
%files -n fence-agents-all -f %{oreon_filedir}/fence-agents-all.list
%files -n fence-agents-alom -f %{oreon_filedir}/fence-agents-alom.list
%files -n fence-agents-amt -f %{oreon_filedir}/fence-agents-amt.list
%files -n fence-agents-amt-ws -f %{oreon_filedir}/fence-agents-amt-ws.list
%files -n fence-agents-apc -f %{oreon_filedir}/fence-agents-apc.list
%files -n fence-agents-apc-snmp -f %{oreon_filedir}/fence-agents-apc-snmp.list
%files -n fence-agents-aws -f %{oreon_filedir}/fence-agents-aws.list
%files -n fence-agents-aws-vpc-net -f %{oreon_filedir}/fence-agents-aws-vpc-net.list
%files -n fence-agents-azure-arm -f %{oreon_filedir}/fence-agents-azure-arm.list
%files -n fence-agents-bladecenter -f %{oreon_filedir}/fence-agents-bladecenter.list
%files -n fence-agents-brocade -f %{oreon_filedir}/fence-agents-brocade.list
%files -n fence-agents-cdu -f %{oreon_filedir}/fence-agents-cdu.list
%files -n fence-agents-cisco-mds -f %{oreon_filedir}/fence-agents-cisco-mds.list
%files -n fence-agents-cisco-ucs -f %{oreon_filedir}/fence-agents-cisco-ucs.list
%files -n fence-agents-cyberpower-ssh -f %{oreon_filedir}/fence-agents-cyberpower-ssh.list
%files -n fence-agents-docker -f %{oreon_filedir}/fence-agents-docker.list
%files -n fence-agents-drac -f %{oreon_filedir}/fence-agents-drac.list
%files -n fence-agents-drac5 -f %{oreon_filedir}/fence-agents-drac5.list
%files -n fence-agents-eaton-snmp -f %{oreon_filedir}/fence-agents-eaton-snmp.list
%files -n fence-agents-eaton-ssh -f %{oreon_filedir}/fence-agents-eaton-ssh.list
%files -n fence-agents-ecloud -f %{oreon_filedir}/fence-agents-ecloud.list
%files -n fence-agents-emerson -f %{oreon_filedir}/fence-agents-emerson.list
%files -n fence-agents-eps -f %{oreon_filedir}/fence-agents-eps.list
%files -n fence-agents-gce -f %{oreon_filedir}/fence-agents-gce.list
%files -n fence-agents-hds-cb -f %{oreon_filedir}/fence-agents-hds-cb.list
%files -n fence-agents-hetzner-cloud -f %{oreon_filedir}/fence-agents-hetzner-cloud.list
%files -n fence-agents-heuristics-ping -f %{oreon_filedir}/fence-agents-heuristics-ping.list
%files -n fence-agents-hpblade -f %{oreon_filedir}/fence-agents-hpblade.list
%files -n fence-agents-ibmblade -f %{oreon_filedir}/fence-agents-ibmblade.list
%files -n fence-agents-ibmz -f %{oreon_filedir}/fence-agents-ibmz.list
%files -n fence-agents-ibm-powervs -f %{oreon_filedir}/fence-agents-ibm-powervs.list
%files -n fence-agents-ibm-vpc -f %{oreon_filedir}/fence-agents-ibm-vpc.list
%files -n fence-agents-ifmib -f %{oreon_filedir}/fence-agents-ifmib.list
%files -n fence-agents-ilo2 -f %{oreon_filedir}/fence-agents-ilo2.list
%files -n fence-agents-ilo-moonshot -f %{oreon_filedir}/fence-agents-ilo-moonshot.list
%files -n fence-agents-ilo-mp -f %{oreon_filedir}/fence-agents-ilo-mp.list
%files -n fence-agents-ilo-ssh -f %{oreon_filedir}/fence-agents-ilo-ssh.list
%files -n fence-agents-intelmodular -f %{oreon_filedir}/fence-agents-intelmodular.list
%files -n fence-agents-ipdu -f %{oreon_filedir}/fence-agents-ipdu.list
%files -n fence-agents-ipmilan -f %{oreon_filedir}/fence-agents-ipmilan.list
%files -n fence-agents-kdump -f %{oreon_filedir}/fence-agents-kdump.list
%files -n fence-agents-kubevirt -f %{oreon_filedir}/fence-agents-kubevirt.list
%files -n fence-agents-ldom -f %{oreon_filedir}/fence-agents-ldom.list
%files -n fence-agents-lpar -f %{oreon_filedir}/fence-agents-lpar.list
%files -n fence-agents-mpath -f %{oreon_filedir}/fence-agents-mpath.list
%files -n fence-agents-netio -f %{oreon_filedir}/fence-agents-netio.list
%files -n fence-agents-nutanix-ahv -f %{oreon_filedir}/fence-agents-nutanix-ahv.list
%files -n fence-agents-ovh -f %{oreon_filedir}/fence-agents-ovh.list
%files -n fence-agents-ovm -f %{oreon_filedir}/fence-agents-ovm.list
%files -n fence-agents-pve -f %{oreon_filedir}/fence-agents-pve.list
%files -n fence-agents-raritan -f %{oreon_filedir}/fence-agents-raritan.list
%files -n fence-agents-rcd-serial -f %{oreon_filedir}/fence-agents-rcd-serial.list
%files -n fence-agents-redfish -f %{oreon_filedir}/fence-agents-redfish.list
%files -n fence-agents-rhevm -f %{oreon_filedir}/fence-agents-rhevm.list
%files -n fence-agents-rsa -f %{oreon_filedir}/fence-agents-rsa.list
%files -n fence-agents-rsb -f %{oreon_filedir}/fence-agents-rsb.list
%files -n fence-agents-sanbox2 -f %{oreon_filedir}/fence-agents-sanbox2.list
%files -n fence-agents-sbd -f %{oreon_filedir}/fence-agents-sbd.list
%files -n fence-agents-scsi -f %{oreon_filedir}/fence-agents-scsi.list
%files -n fence-agents-shelly -f %{oreon_filedir}/fence-agents-shelly.list
%files -n fence-agents-vbox -f %{oreon_filedir}/fence-agents-vbox.list
%files -n fence-agents-virsh -f %{oreon_filedir}/fence-agents-virsh.list
%files -n fence-agents-vmware -f %{oreon_filedir}/fence-agents-vmware.list
%files -n fence-agents-vmware-rest -f %{oreon_filedir}/fence-agents-vmware-rest.list
%files -n fence-agents-vmware-soap -f %{oreon_filedir}/fence-agents-vmware-soap.list
%files -n fence-agents-vmware-vcloud -f %{oreon_filedir}/fence-agents-vmware-vcloud.list
%files -n fence-agents-wti -f %{oreon_filedir}/fence-agents-wti.list
%files -n fence-agents-xenapi -f %{oreon_filedir}/fence-agents-xenapi.list
%files -n fence-agents-zvm -f %{oreon_filedir}/fence-agents-zvm.list
%files -n fence-virt -f %{oreon_filedir}/fence-virt.list
%files -n fence-virtd -f %{oreon_filedir}/fence-virtd.list
%files -n fence-virtd-multicast -f %{oreon_filedir}/fence-virtd-multicast.list
%files -n fence-virtd-serial -f %{oreon_filedir}/fence-virtd-serial.list
%files -n fence-virtd-tcp -f %{oreon_filedir}/fence-virtd-tcp.list
%files -n fence-virtd-libvirt -f %{oreon_filedir}/fence-virtd-libvirt.list
%files -n fence-virtd-cpg -f %{oreon_filedir}/fence-virtd-cpg.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.17.0-2
- Import
