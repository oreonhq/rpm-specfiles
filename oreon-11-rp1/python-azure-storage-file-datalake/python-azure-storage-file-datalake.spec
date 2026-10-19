%global source0_hash 34813c6f3e9bf1636898cec62529dd2ced189cd2c677160ec69ef88c3b72da7f
Name:           python-azure-storage-file-datalake
Version:        12.25.0
Release:        1%{?dist}
Summary:        Microsoft Azure File DataLake Storage Client Library for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        https://files.pythonhosted.org/packages/source/a/azure_storage_file_datalake/azure_storage_file_datalake-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-azure-storage-file-datalake = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-azure-storage-file-datalake
Summary:        Microsoft Azure File DataLake Storage Client Library for Python
%description -n python3-azure-storage-file-datalake

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir azure_storage_file_datalake-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-azure-storage-file-datalake usr/lib/python3*/site-packages/azure_storage_file_datalake* usr/lib64/python3*/site-packages/azure_storage_file_datalake* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/azure_storage_file_datalake* usr/lib64/python3*/site-packages/azure_storage_file_datalake* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-azure-storage-file-datalake -f %{oreon_filedir}/python3-azure-storage-file-datalake.list

%changelog

%autochangelog
