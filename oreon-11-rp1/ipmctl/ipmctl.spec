%global source0_hash 30de3a90fd3ccc7711dc621453570cc5b47a6196d91167a90794f942d9596be1
Name:		ipmctl
Version:	03.00.00.0468
Release:        1%{?dist}
Summary:        Utility for managing Intel Optane DC persistent memory modules
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/intel/ipmctl
Source0:        https://github.com/intel/ipmctl/archive/v%{version}/%{name}-%{version}_with_edk2.tar.gz
ExclusiveArch:	x86_64
Requires:	libipmctl%{?_isa} = %{version}-%{release}
Obsoletes:	ixpdimm-cli < 01.00.00.3000
Patch1: ipmctl-remove-uefi-spec-code.patch
Patch2: ipmctl-remove-always-true-conditional.patch
Patch3: ipmctl_remove_unused_functions.patch
# oreon:deps
BuildRequires:  asciidoctor
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libndctl)
BuildRequires:  python3
BuildRequires:  systemd
# /oreon:deps
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
%oreon_autofiles libipmctl usr/*/lib*.so.*
%oreon_autofiles libipmctl-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post -n libipmctl -p /sbin/ldconfig

%postun -n libipmctl -p /sbin/ldconfig

%files -f %{oreon_filedir}/main.list
%files -n libipmctl -f %{oreon_filedir}/libipmctl.list
%files -n libipmctl-devel -f %{oreon_filedir}/libipmctl-devel.list

%changelog

%autochangelog
