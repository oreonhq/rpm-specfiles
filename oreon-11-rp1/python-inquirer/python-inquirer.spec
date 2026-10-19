%global source0_hash 60d169fddffe297e2f8ad54ab33698249ccfc3fc377dafb1e5cf01a0efb9cbe5
Name:           python-inquirer
Version:        3.4.1
Release:        1%{?dist}
Summary:        Collection of common interactive command line user interfaces, based on Inquirer.js
License:        MIT
URL:            https://github.com/magmax/python-inquirer
Source0:        https://files.pythonhosted.org/packages/source/i/inquirer/inquirer-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-inquirer = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-inquirer
Summary:        Collection of common interactive command line user interfaces, based on Inquirer.js
%description -n python3-inquirer

%prep
%global oreon_srcdir inquirer-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-inquirer usr/lib/python3*/site-packages/inquirer* usr/lib64/python3*/site-packages/inquirer* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/inquirer* usr/lib64/python3*/site-packages/inquirer* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-inquirer -f %{oreon_filedir}/python3-inquirer.list

%changelog

%autochangelog
