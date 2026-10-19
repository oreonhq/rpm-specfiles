%global source0_hash 7b05f2fcac4fb67fc9f77a7d4c5d98a0f3099fb73b57c69ec1b080773994671b
Name:           python-azure-monitor-query
Version:        2.0.0
Release:        1%{?dist}
Summary:        Microsoft Corporation Azure Monitor Query Client Library for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python/tree/main/sdk
Source0:        https://files.pythonhosted.org/packages/source/a/azure_monitor_query/azure_monitor_query-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-azure-monitor-query = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-azure-monitor-query
Summary:        Microsoft Corporation Azure Monitor Query Client Library for Python
%description -n python3-azure-monitor-query

%prep
%global oreon_srcdir azure_monitor_query-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-azure-monitor-query usr/lib/python3*/site-packages/azure_monitor_query* usr/lib64/python3*/site-packages/azure_monitor_query* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/azure_monitor_query* usr/lib64/python3*/site-packages/azure_monitor_query* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-azure-monitor-query -f %{oreon_filedir}/python3-azure-monitor-query.list

%changelog

%autochangelog
