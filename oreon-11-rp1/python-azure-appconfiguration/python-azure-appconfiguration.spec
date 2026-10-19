%global source0_hash 399677f56348e9107d7a97a7e47db6723c7d2c617fedbea6881eda7b8eed995b
Name:           python-azure-appconfiguration
Version:        1.9.0
Release:        1%{?dist}
Summary:        Microsoft Corporation Azure App Configuration Data Client Library for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        https://files.pythonhosted.org/packages/source/a/azure_appconfiguration/azure_appconfiguration-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-azure-appconfiguration = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-azure-appconfiguration
Summary:        Microsoft Corporation Azure App Configuration Data Client Library for Python
# oreon:reqs
Requires:       python3dist(azure-core) >= 1.37.0
Requires:       python3dist(isodate) >= 0.6.1
Requires:       python3dist(typing-extensions) >= 4.6.0
# /oreon:reqs
%description -n python3-azure-appconfiguration

%prep
%global oreon_srcdir azure_appconfiguration-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-azure-appconfiguration usr/lib/python3*/site-packages/azure_appconfiguration* usr/lib64/python3*/site-packages/azure_appconfiguration* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/azure_appconfiguration* usr/lib64/python3*/site-packages/azure_appconfiguration* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-azure-appconfiguration -f %{oreon_filedir}/python3-azure-appconfiguration.list

%changelog

%autochangelog
