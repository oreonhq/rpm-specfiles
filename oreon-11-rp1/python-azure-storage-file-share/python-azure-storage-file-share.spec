%global source0_hash 08cf8bc436df532cdb9bfdfce7bb10c5f1d83d51360954cd8eef56cbccf4300a
Name:           python-azure-storage-file-share
Version:        12.26.0
Release:        1%{?dist}
Summary:        Microsoft Azure Azure File Share Storage Client Library for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-file-share
Source0:        https://files.pythonhosted.org/packages/source/a/azure_storage_file_share/azure_storage_file_share-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-azure-storage-file-share = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-azure-storage-file-share
Summary:        Microsoft Azure Azure File Share Storage Client Library for Python
%description -n python3-azure-storage-file-share

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir azure_storage_file_share-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-azure-storage-file-share usr/lib/python3*/site-packages/azure_storage_file_share* usr/lib64/python3*/site-packages/azure_storage_file_share* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/azure_storage_file_share* usr/lib64/python3*/site-packages/azure_storage_file_share* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-azure-storage-file-share -f %{oreon_filedir}/python3-azure-storage-file-share.list

%changelog

%autochangelog
