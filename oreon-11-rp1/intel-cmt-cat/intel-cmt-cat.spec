%global libpqos_ver 6.0.1
%global desc %{expand: \
This package provides basic support for Intel Resource Director Technology
including, Cache Monitoring Technology (CMT), Memory Bandwidth Monitoring
(MBM), Cache Allocation Technology (CAT), Code and Data Prioritization 
(CDP) and Memory Bandwidth Allocation (MBA).}

Name:		intel-cmt-cat
Version:	25.04
Release:	4%{?dist}
Summary:	Intel cache monitoring and allocation technology config tool

License:	BSD-3-Clause
URL: 		https://github.com/intel/intel-cmt-cat
Source: 	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:		0001-alter-install-paths.patch
Patch1:		0002-remove-build-and-install-of-examples.patch
Patch2:		0003-allow-debian-flags-to-be-added.patch

ExclusiveArch:	x86_64

BuildRequires:	gcc
BuildRequires:	make

%description
%{desc}

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel %{desc}

Development files.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%make_build

%install
%make_install BIN_DIR="%{buildroot}%{_bindir}" SBIN_DIR="%{buildroot}%{_sbindir}"

%ldconfig_scriptlets

%files
%license LICENSE
%doc ChangeLog README.md
%{_bindir}/membw
%{_sbindir}/pqos
%{_sbindir}/pqos-msr
%{_sbindir}/pqos-os
%{_sbindir}/rdtset
%{_libdir}/libpqos.so.6
%{_libdir}/libpqos.so.%{libpqos_ver}
%{_mandir}/man8/membw.8*
%{_mandir}/man8/pqos.8*
%{_mandir}/man8/pqos-msr.8*
%{_mandir}/man8/pqos-os.8*
%{_mandir}/man8/rdtset.8*

%files -n %{name}-devel
%{_includedir}/pqos.h
%{_libdir}/libpqos.so

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.04-4
- Import
