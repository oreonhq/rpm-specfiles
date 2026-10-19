%global source0_hash afc626507ced2c6beca912cb1a6233bf515af538121ecd21501aaa5dc82602f5
Name:           python-azure-mgmt-cdn
Version:        14.0.0
Release:        1%{?dist}
Summary:        Microsoft Azure Cdn Management Client Library for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        https://files.pythonhosted.org/packages/source/a/azure_mgmt_cdn/azure_mgmt_cdn-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-azure-mgmt-cdn = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-azure-mgmt-cdn
Summary:        Microsoft Azure Cdn Management Client Library for Python
# oreon:reqs
Requires:       python3dist(azure-mgmt-core) >= 1.6.0
Requires:       python3dist(isodate) >= 0.6.1
Requires:       python3dist(typing-extensions) >= 4.6.0
# /oreon:reqs
%description -n python3-azure-mgmt-cdn

%prep
%global oreon_srcdir azure_mgmt_cdn-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-azure-mgmt-cdn usr/lib/python3*/site-packages/azure_mgmt_cdn* usr/lib64/python3*/site-packages/azure_mgmt_cdn* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/azure_mgmt_cdn* usr/lib64/python3*/site-packages/azure_mgmt_cdn* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-azure-mgmt-cdn -f %{oreon_filedir}/python3-azure-mgmt-cdn.list

%changelog

%autochangelog
