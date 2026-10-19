%global source0_hash f039d1490818d337280f63a915bba54076b2b6569b83f3923cd5c5e2f3fc4387
Name:           python-azure-mgmt-resource-deployments
Version:        2.0.0
Release:        1%{?dist}
Summary:        Microsoft Azure Deployments Management Client Library for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        https://files.pythonhosted.org/packages/source/a/azure_mgmt_resource_deployments/azure_mgmt_resource_deployments-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-azure-mgmt-resource-deployments = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-azure-mgmt-resource-deployments
Summary:        Microsoft Azure Deployments Management Client Library for Python
# oreon:reqs
Requires:       python3dist(azure-mgmt-core) >= 1.6.0
Requires:       python3dist(isodate) >= 0.6.1
Requires:       python3dist(typing-extensions) >= 4.6.0
# /oreon:reqs
%description -n python3-azure-mgmt-resource-deployments

%prep
%global oreon_srcdir azure_mgmt_resource_deployments-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-azure-mgmt-resource-deployments usr/lib/python3*/site-packages/azure_mgmt_resource_deployments* usr/lib64/python3*/site-packages/azure_mgmt_resource_deployments* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/azure_mgmt_resource_deployments* usr/lib64/python3*/site-packages/azure_mgmt_resource_deployments* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-azure-mgmt-resource-deployments -f %{oreon_filedir}/python3-azure-mgmt-resource-deployments.list

%changelog

%autochangelog
