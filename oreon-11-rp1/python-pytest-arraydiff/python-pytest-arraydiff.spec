%global source0_hash 70e2a9183af5b4f05f694727beb30eb5fc6712632b240ef259ec60984a629b1a
Name:           python-pytest-arraydiff
Version:        0.7.0
Release:        1%{?dist}
Summary:        pytest plugin to help with comparing array output from tests
License:        BSD-3-Clause
URL:            https://github.com/astropy/pytest-arraydiff
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_arraydiff/pytest_arraydiff-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.1
Requires:       python3-pytest-arraydiff = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-arraydiff
Summary:        pytest plugin to help with comparing array output from tests
%description -n python3-pytest-arraydiff

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pytest_arraydiff-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-arraydiff usr/lib/python3*/site-packages/pytest_arraydiff* usr/lib64/python3*/site-packages/pytest_arraydiff* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_arraydiff* usr/lib64/python3*/site-packages/pytest_arraydiff* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-arraydiff -f %{oreon_filedir}/python3-pytest-arraydiff.list

%changelog

%autochangelog
