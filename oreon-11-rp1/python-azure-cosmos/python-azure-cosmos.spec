%global source0_hash d692928a54d88163e96d41d8f899229ca2f6a6bf21973ece2bfc1f72d4b4edd8
Name:           python-azure-cosmos
Version:        4.17.1
Release:        1%{?dist}
Summary:        Microsoft Azure Cosmos Client Library for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        https://files.pythonhosted.org/packages/source/a/azure_cosmos/azure_cosmos-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-azure-cosmos = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-azure-cosmos
Summary:        Microsoft Azure Cosmos Client Library for Python
%description -n python3-azure-cosmos

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir azure_cosmos-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-azure-cosmos usr/lib/python3*/site-packages/azure_cosmos* usr/lib64/python3*/site-packages/azure_cosmos* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/azure_cosmos* usr/lib64/python3*/site-packages/azure_cosmos* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-azure-cosmos -f %{oreon_filedir}/python3-azure-cosmos.list

%changelog

%autochangelog
