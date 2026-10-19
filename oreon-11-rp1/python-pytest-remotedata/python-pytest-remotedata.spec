%global source0_hash ad3eaa2691feecc2071890764d30e06211547577f965e2e4424435c5d887278d
Name:           python-pytest-remotedata
Version:        0.4.2
Release:        1%{?dist}
Summary:        Pytest plugin for controlling remote data access.
License:        BSD-3-Clause
URL:            https://github.com/astropy/pytest-remotedata
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_remotedata/pytest_remotedata-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.1
Requires:       python3-pytest-remotedata = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-remotedata
Summary:        Pytest plugin for controlling remote data access.
%description -n python3-pytest-remotedata

%prep
%global oreon_srcdir pytest_remotedata-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-remotedata usr/lib/python3*/site-packages/pytest_remotedata* usr/lib64/python3*/site-packages/pytest_remotedata* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_remotedata* usr/lib64/python3*/site-packages/pytest_remotedata* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-remotedata -f %{oreon_filedir}/python3-pytest-remotedata.list

%changelog

%autochangelog
