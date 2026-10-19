%global source0_hash cc4bd2158fd0dd80639142af06dc70c119bbfd6f79d53da4482e0b2c849af7ca
Name:           python-azure-mgmt-storage
Version:        25.1.0
Release:        1%{?dist}
Summary:        Microsoft Azure Storage Management Client Library for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        https://files.pythonhosted.org/packages/source/a/azure_mgmt_storage/azure_mgmt_storage-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-azure-mgmt-storage = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-azure-mgmt-storage
Summary:        Microsoft Azure Storage Management Client Library for Python
# oreon:reqs
Requires:       python3dist(azure-mgmt-core) >= 1.6.0
Requires:       python3dist(isodate) >= 0.6.1
Requires:       python3dist(typing-extensions) >= 4.6.0
# /oreon:reqs
%description -n python3-azure-mgmt-storage

%prep
%global oreon_srcdir azure_mgmt_storage-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-azure-mgmt-storage usr/lib/python3*/site-packages/azure_mgmt_storage* usr/lib64/python3*/site-packages/azure_mgmt_storage* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/azure_mgmt_storage* usr/lib64/python3*/site-packages/azure_mgmt_storage* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-azure-mgmt-storage -f %{oreon_filedir}/python3-azure-mgmt-storage.list

%changelog

%autochangelog
