%global source0_hash 1904e60117fa73f12383076db314cd2e9fb62c1adc18b0439e758de9a640f4e7
Name: eth-tools
Version: 12.1.0.0
Release:        1%{?dist}
Summary:        Intel Ethernet Fabric Suite basic tools and libraries for fabric management
License: BSD-3-Clause
Url: https://github.com/intel/eth-fast-fabric
Source0:        https://github.com/intel/eth-fast-fabric/releases/download/v%{version}/eth-fast-fabric-%{version}.tar.gz
ExclusiveArch: x86_64
Epoch: 1
# oreon:deps
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  net-snmp-devel
BuildRequires:  perl-generators
BuildRequires:  rdma-core-devel
BuildRequires:  tcl-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n eth-fast-fabric-%{version_no_tilde}

%build

export CFLAGS="$RPM_OPT_FLAGS -Wno-error=deprecated-openmp -Wno-deprecated"
export CXXFLAGS="$RPM_OPT_FLAGS -Wno-error=deprecated-openmp -Wno-deprecated"
cd OpenIb_Host
OPA_FEATURE_SET=opa10 CLOCAL='%build_cflags -Wno-error=deprecated-openmp -Wno-deprecated' CCLOCAL='%build_cxxflags -Wno-error=deprecated-openmp -Wno-deprecated' LDLOCAL='%build_ldflags' ./ff_build.sh %{_builddir}
%install
cd eth-fast-fabric-%{version_no_tilde}
BUILDDIR=%{_builddir} DESTDIR=%{buildroot} LIBDIR=%{_prefix}/lib OpenIb_Host/ff_install.sh
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n eth-tools-basic -f %{oreon_filedir}/eth-tools-basic.list
%files -n eth-tools-fastfabric -f %{oreon_filedir}/eth-tools-fastfabric.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:12.1.0.1-6
- Import
