%global source0_hash 6eb108a88554be371feb2eba9715fa0e3f7baca7b3f00c19ec417fc7ce5b3834
Name:           python-azure-storage-queue
Version:        12.17.0
Release:        1%{?dist}
Summary:        Microsoft Azure Azure Queue Storage Client Library for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-queue
Source0:        https://files.pythonhosted.org/packages/source/a/azure_storage_queue/azure_storage_queue-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-azure-storage-queue = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-azure-storage-queue
Summary:        Microsoft Azure Azure Queue Storage Client Library for Python
%description -n python3-azure-storage-queue

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir azure_storage_queue-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-azure-storage-queue usr/lib/python3*/site-packages/azure_storage_queue* usr/lib64/python3*/site-packages/azure_storage_queue* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/azure_storage_queue* usr/lib64/python3*/site-packages/azure_storage_queue* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-azure-storage-queue -f %{oreon_filedir}/python3-azure-storage-queue.list

%changelog

%autochangelog
