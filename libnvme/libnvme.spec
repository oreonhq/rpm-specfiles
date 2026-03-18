# RHEL 8 compatibility
%{!?version_no_tilde: %define version_no_tilde %{shrink:%(echo '%{version}' | tr '~' '-')}}

Name:    libnvme
Summary: Linux-native nvme device management library
Version: 1.16.1
Release: 2%{?dist}
License: LGPL-2.1-or-later
URL:     https://github.com/linux-nvme/libnvme
Source0: %{url}/archive/v%{version_no_tilde}/%{name}-%{version_no_tilde}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: swig
BuildRequires: python3-devel

BuildRequires: meson >= 0.62
BuildRequires: json-c-devel >= 0.13
BuildRequires: openssl-devel
BuildRequires: dbus-devel
BuildRequires: keyutils-libs-devel
%if 0%{?fedora} || 0%{?rhel} > 9
BuildRequires: kernel-headers >= 5.15
%endif

%description
Provides type definitions for NVMe specification structures,
enumerations, and bit fields, helper functions to construct,
dispatch, and decode commands and payloads, and utilities to connect,
scan, and manage nvme devices on a Linux system.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides header files to include and libraries to link with
for Linux-native nvme device management.
%package doc
Summary: Reference manual for libnvme
BuildArch: noarch
BuildRequires: perl-interpreter
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme

%description doc
This package contains the reference manual for %{name}.

%package -n python3-libnvme
Summary:  Python3 bindings for libnvme
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides:  python3-nvme = %{version}-%{release}
Obsoletes: python3-nvme < 1.0~rc7
%{?python_provide:%python_provide python3-libnvme}

%description -n python3-libnvme
This package contains Python bindings for libnvme.

%prep
%autosetup -p1 -n %{name}-%{version_no_tilde}

%build
%meson -Dpython=enabled -Dlibdbus=enabled -Ddocs=all -Ddocs-build=true -Dhtmldir=%{_pkgdocdir} -Dliburing=disabled
%meson_build

%install
%meson_install
%{__install} -pm 644 README.md %{buildroot}%{_pkgdocdir}
%{__install} -pm 644 doc/config-schema.json %{buildroot}%{_pkgdocdir}
mv %{buildroot}%{_pkgdocdir}/nvme/html %{buildroot}%{_pkgdocdir}/html
rm -rf %{buildroot}%{_pkgdocdir}/nvme
mv %{buildroot}/usr/*.rst %{buildroot}%{_pkgdocdir}/
rm -r %{buildroot}%{_pkgdocdir}/html/{.buildinfo,.doctrees/}

%ldconfig_scriptlets

%files
%license COPYING ccan/licenses/*
%{_libdir}/libnvme.so.1
%{_libdir}/libnvme.so.1.16.1
%{_libdir}/libnvme-mi.so.1
%{_libdir}/libnvme-mi.so.1.16.1

%files devel
%{_libdir}/libnvme.so
%{_libdir}/libnvme-mi.so
%{_includedir}/libnvme.h
%{_includedir}/libnvme-mi.h
%dir %{_includedir}/nvme
%{_includedir}/nvme/*.h
%{_libdir}/pkgconfig/*.pc

%files doc
%doc %{_pkgdocdir}
%{_mandir}/man2/*.2*

%files -n python3-libnvme
%dir %{python3_sitearch}/libnvme
%{python3_sitearch}/libnvme/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.16.1-2
- Prepare for Oreon 11 (RP1)
