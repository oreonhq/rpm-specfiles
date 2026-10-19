%global source0_hash b14fc94a3223a2835ff5688e17d8e107b27c7cd7c4114138f2ac81373723705d
Name:           python-azure-data-tables
Version:        12.7.0
Release:        1%{?dist}
Summary:        Microsoft Azure Azure Data Tables Client Library for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables
Source0:        https://files.pythonhosted.org/packages/source/a/azure_data_tables/azure_data_tables-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-azure-data-tables = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-azure-data-tables
Summary:        Microsoft Azure Azure Data Tables Client Library for Python
%description -n python3-azure-data-tables

%prep
%global oreon_srcdir azure_data_tables-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-azure-data-tables usr/lib/python3*/site-packages/azure_data_tables* usr/lib64/python3*/site-packages/azure_data_tables* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/azure_data_tables* usr/lib64/python3*/site-packages/azure_data_tables* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-azure-data-tables -f %{oreon_filedir}/python3-azure-data-tables.list

%changelog

%autochangelog
