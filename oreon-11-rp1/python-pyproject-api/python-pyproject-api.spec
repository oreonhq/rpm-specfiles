%global source0_hash 999ba9741fca3519a3876482cd2eddbce250c31c42c031506c5ea5610f1d3589
Name:           python-pyproject-api
Version:        1.11.1
Release:        1%{?dist}
Summary:        API to interact with the python pyproject.toml based projects
License:        MIT
URL:            https://pyproject-api.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/p/pyproject_api/pyproject_api-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyproject-api = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyproject-api
Summary:        API to interact with the python pyproject.toml based projects
%description -n python3-pyproject-api

%prep
%global oreon_srcdir pyproject_api-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyproject-api usr/lib/python3*/site-packages/pyproject_api* usr/lib64/python3*/site-packages/pyproject_api* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyproject_api* usr/lib64/python3*/site-packages/pyproject_api* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyproject-api -f %{oreon_filedir}/python3-pyproject-api.list

%changelog

%autochangelog
