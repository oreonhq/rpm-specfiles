%global source0_hash 77f8e38c319d0b0efe9444c29179277157c5c2e5ddc40ec39f1f82faacebdcb4
Name:           python-azure-storage-blob
Version:        12.30.2
Release:        1%{?dist}
Summary:        Microsoft Azure Blob Storage Client Library for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob
Source0:        https://files.pythonhosted.org/packages/source/a/azure_storage_blob/azure_storage_blob-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-azure-storage-blob = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-azure-storage-blob
Summary:        Microsoft Azure Blob Storage Client Library for Python
%description -n python3-azure-storage-blob

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir azure_storage_blob-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-azure-storage-blob usr/lib/python3*/site-packages/azure_storage_blob* usr/lib64/python3*/site-packages/azure_storage_blob* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/azure_storage_blob* usr/lib64/python3*/site-packages/azure_storage_blob* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-azure-storage-blob -f %{oreon_filedir}/python3-azure-storage-blob.list

%changelog

%autochangelog
