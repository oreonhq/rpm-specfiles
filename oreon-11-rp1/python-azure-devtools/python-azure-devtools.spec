%global source0_hash 99276808760fab263ba3f7ac67b527c06a6e7510805f856fb76754e1ad76dcf7
Name:           python-azure-devtools
Version:        1.2.0
Release:        1%{?dist}
Summary:        Microsoft Azure Development Tools for SDK
License:        MIT
URL:            https://github.com/Azure/azure-python-devtools
Source0:        https://files.pythonhosted.org/packages/source/a/azure-devtools/azure-devtools-%{version}.tar.gz
BuildArch:      noarch
Patch0:         python-azure-devtools-requirements-fix.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-azure-devtools = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-azure-devtools
Summary:        Microsoft Azure Development Tools for SDK
%description -n python3-azure-devtools

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir azure-devtools-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-azure-devtools usr/lib/python3*/site-packages/azure_devtools* usr/lib64/python3*/site-packages/azure_devtools* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/azure_devtools* usr/lib64/python3*/site-packages/azure_devtools* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-azure-devtools -f %{oreon_filedir}/python3-azure-devtools.list

%changelog

%autochangelog
