%global source0_hash 1f2e5fb71d1f6f4ff31d8992674f2368465bc2f25cd94018015c3ddbfc5c617f
Name:           python-os-service-types
Version:        1.9.0
Release:        1%{?dist}
Summary:        Python library for consuming OpenStack sevice-types-authority data
License:        Apache-2.0
URL:            https://docs.openstack.org/os-service-types/
Source0:        https://files.pythonhosted.org/packages/source/o/os_service_types/os_service_types-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-os-service-types = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-os-service-types
Summary:        Python library for consuming OpenStack sevice-types-authority data
%description -n python3-os-service-types

%prep
%global oreon_srcdir os_service_types-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-os-service-types usr/lib/python3*/site-packages/os_service_types* usr/lib64/python3*/site-packages/os_service_types* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/os_service_types* usr/lib64/python3*/site-packages/os_service_types* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-os-service-types -f %{oreon_filedir}/python3-os-service-types.list

%changelog

%autochangelog
