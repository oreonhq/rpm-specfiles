%global source0_hash none

Name:		ipmctl
Version:	03.00.00.0468
Release:	9%{?dist}
Summary:	Utility for managing Intel Optane DC persistent memory modules
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/intel/ipmctl
Source:		https://github.com/intel/ipmctl/archive/v%{version}/%{name}-%{version}_with_edk2.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=1628752
ExclusiveArch:	x86_64

Requires:	libipmctl%{?_isa} = %{version}-%{release}
BuildRequires:	pkgconfig(libndctl)
BuildRequires:	cmake
BuildRequires:	python3
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	asciidoctor
BuildRequires:	systemd
Obsoletes:	ixpdimm-cli < 01.00.00.3000

Patch1: ipmctl-remove-uefi-spec-code.patch
Patch2: ipmctl-remove-always-true-conditional.patch
Patch3: ipmctl_remove_unused_functions.patch

%description
Utility for managing Intel Optane DC persistent memory modules
Supports functionality to:
Discover DCPMMs on the platform.
Provision the platform memory configuration.
View and update the firmware on DCPMMs.
Configure data-at-rest security on DCPMMs.
Track health and performance of DCPMMs.
Debug and troubleshoot DCPMMs.

%prep
%setup -q -n %{name}-%{version}
%patch -P1 -p1 
%patch -P2 -p1 
%patch -P3 -p1 

%package -n libipmctl
Summary:	Library for Intel DCPMM management
Obsoletes:	ixpdimm_sw < 01.00.00.3000
Obsoletes:	libixpdimm-common < 01.00.00.3000
Obsoletes:	libixpdimm-core < 01.00.00.3000
Obsoletes:	libixpdimm-cli < 01.00.00.3000
Obsoletes:	libixpdimm-cim < 01.00.00.3000
Obsoletes:	libixpdimm < 01.00.00.3000
Obsoletes:	ixpdimm-data < 01.00.00.3000

%description -n libipmctl
An Application Programming Interface (API) library for managing Intel Optane DC
persistent memory modules.

%package -n libipmctl-devel
Summary:	Development packages for libipmctl
Requires:	libipmctl%{?_isa} = %{version}-%{release}
Obsoletes:	ixpdimm-devel < 01.00.00.3000
Obsoletes:	ixpdimm_sw-devel < 01.00.00.3000

%description -n libipmctl-devel
API for development of Intel Optane DC persistent memory management utilities.

%build
%cmake -DBUILDNUM=%{version} -DCMAKE_INSTALL_PREFIX=/ \
    -DLINUX_PRODUCT_NAME=%{name} \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir} \
    -DCMAKE_INSTALL_BINDIR=%{_bindir} \
    -DCMAKE_INSTALL_DATAROOTDIR=%{_datarootdir} \
    -DCMAKE_INSTALL_MANDIR=%{_mandir} \
    -DCMAKE_INSTALL_LOCALSTATEDIR=%{_localstatedir} \
    -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
    -DRELEASE=ON \
    -DRPM_BUILD=ON
%cmake_build

%install
%{!?_cmake_version: cd build}
%cmake_install

%post -n libipmctl -p /sbin/ldconfig

%postun -n libipmctl -p /sbin/ldconfig

%files -n ipmctl
%{_bindir}/ipmctl
%{_mandir}/man1/ipmctl*

%files -n libipmctl
%{_libdir}/libipmctl.so.5*
%dir %{_datadir}/doc/ipmctl
%doc %{_datadir}/doc/ipmctl/ipmctl_default.conf
%doc %{_datadir}/doc/ipmctl/LICENSE
%doc %{_datadir}/doc/ipmctl/edk2_License.txt
%doc %{_datadir}/doc/ipmctl/thirdpartynotice.txt
%config(noreplace) %{_datadir}/ipmctl/ipmctl.conf
%dir %{_localstatedir}/log/ipmctl
%config(noreplace) %{_sysconfdir}/logrotate.d/ipmctl

%files -n libipmctl-devel
%{_libdir}/libipmctl.so
%{_includedir}/nvm_types.h
%{_includedir}/nvm_management.h
%{_includedir}/export_api.h
%{_includedir}/NvmSharedDefs.h
%{_libdir}/pkgconfig/libipmctl.pc

%changelog
%autochangelog
