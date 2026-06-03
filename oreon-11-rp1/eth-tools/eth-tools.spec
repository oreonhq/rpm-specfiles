%global source0_hash 1904e60117fa73f12383076db314cd2e9fb62c1adc18b0439e758de9a640f4e7

Name: eth-tools
Version: 12.1.0.0
Release: 6%{?dist}
Summary: Intel Ethernet Fabric Suite basic tools and libraries for fabric management

License: BSD-3-Clause
Url: https://github.com/intel/eth-fast-fabric
Source: %url/releases/download/v%{version_no_tilde}/eth-fast-fabric-%{version_no_tilde}.tar.gz
ExclusiveArch: x86_64
# The Intel(R) Ethernet Fabric Suite product line is only available on x86_64 platforms at this time.

Epoch: 1

%description
This package contains the tools necessary to manage an Intel Ethernet fabric.

%package basic
Summary: Management level tools and scripts

Requires: rdma bc

Requires: expect%{?_isa}, (tcl8%{?_isa} or tcl%{?_isa} < 1:9), libibverbs-utils%{?_isa}, librdmacm-utils%{?_isa}, net-snmp%{?_isa}, net-snmp-utils%{?_isa}
BuildRequires: make
BuildRequires: expat-devel
BuildRequires: gcc-c++
BuildRequires: tcl-devel < 1:9
BuildRequires: rdma-core-devel
BuildRequires: net-snmp-devel


%description basic
Contains basic tools for fabric management necessary on all compute nodes.

%package fastfabric
Summary: Management level tools and scripts
Requires: eth-tools-basic%{?_isa} >= %{version}-%{release}

BuildRequires: perl-generators

%description fastfabric
Contains tools for managing fabric on a management node.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n OpenIb_Host

%build
cd eth-fast-fabric-%{version_no_tilde}/OpenIb_Host
OPA_FEATURE_SET=opa10 CLOCAL='%build_cflags' CCLOCAL='%build_cxxflags' LDLOCAL='%build_ldflags' ./ff_build.sh %{_builddir}

%install
cd eth-fast-fabric-%{version_no_tilde}
BUILDDIR=%{_builddir} DESTDIR=%{buildroot} LIBDIR=%{_prefix}/lib OpenIb_Host/ff_install.sh

%files basic
%dir %{_sysconfdir}/eth-tools/
%{_sbindir}/ethbw
%{_sbindir}/ethcapture
%{_sbindir}/ethshmcleanup
%{_prefix}/lib/eth-tools/setup_self_ssh
%{_prefix}/lib/eth-tools/usemem
%{_prefix}/lib/eth-tools/ethipcalc
%{_prefix}/lib/eth-tools/stream
%{_prefix}/lib/eth-tools/ethudstress
%{_mandir}/man1/ethbw.1*
%{_mandir}/man1/ethcapture.1*
%{_mandir}/man1/ethshmcleanup.1*
%{_datadir}/eth-tools/samples/dsa_setup
%{_datadir}/eth-tools/samples/dsa.service
%{_datadir}/eth-tools/samples/mgt_config.xml-sample
%config(noreplace) %{_sysconfdir}/eth-tools/mgt_config.xml

%files fastfabric
%{_sbindir}/*
%exclude %{_sbindir}/ethbw
%exclude %{_sbindir}/ethcapture
%exclude %{_sbindir}/ethshmcleanup
%{_prefix}/lib/eth-tools/*
%exclude %{_prefix}/lib/eth-tools/setup_self_ssh
%exclude %{_prefix}/lib/eth-tools/usemem
%exclude %{_prefix}/lib/eth-tools/ethipcalc
%exclude %{_prefix}/lib/eth-tools/stream
%exclude %{_prefix}/lib/eth-tools/ethudstress
%{_datadir}/eth-tools/*
%exclude %{_datadir}/eth-tools/samples/dsa_setup
%exclude %{_datadir}/eth-tools/samples/dsa.service
%exclude %{_datadir}/eth-tools/samples/mgt_config.xml-sample
%{_mandir}/man8/eth*.8*
%{_usrsrc}/eth/*
%config(noreplace) %{_sysconfdir}/eth-tools/ethfastfabric.conf
%config(noreplace) %{_sysconfdir}/eth-tools/ethmon.conf
%config(noreplace) %{_sysconfdir}/eth-tools/allhosts
%config(noreplace) %{_sysconfdir}/eth-tools/hosts
%config(noreplace) %{_sysconfdir}/eth-tools/switches
%{_sysconfdir}/eth-tools/ethmon.si.conf
%config(noreplace) /usr/lib/eth-tools/osid_wrapper

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:12.1.0.1-6
- Import
