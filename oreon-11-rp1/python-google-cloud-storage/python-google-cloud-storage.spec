%global source0_hash b24e74b493c60b19b83462933a83bb831e45b6ca4924b0d75eac8e176b58b3a7
Name:           python-google-cloud-storage
Version:        3.14.1
Release:        1%{?dist}
Summary:        Google Cloud Storage API client library
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-storage
Source0:        https://files.pythonhosted.org/packages/source/g/google_cloud_storage/google_cloud_storage-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-google-cloud-storage = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-google-cloud-storage
Summary:        Google Cloud Storage API client library
%description -n python3-google-cloud-storage

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir google_cloud_storage-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-google-cloud-storage usr/lib/python3*/site-packages/google_cloud_storage* usr/lib64/python3*/site-packages/google_cloud_storage* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/google_cloud_storage* usr/lib64/python3*/site-packages/google_cloud_storage* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-google-cloud-storage -f %{oreon_filedir}/python3-google-cloud-storage.list

%changelog

%autochangelog
