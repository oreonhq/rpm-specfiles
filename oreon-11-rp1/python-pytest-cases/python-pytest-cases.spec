%global source0_hash 451f9e3ecd5d2d81a4362c10c441126f5b3d1ae3a7efaf59f60b1fb930df2d69
Name:           python-pytest-cases
Version:        3.10.1
Release:        1%{?dist}
Summary:        Separate test code from test cases in pytest.
License:        ...
URL:            https://github.com/smarie/python-pytest-cases
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_cases/pytest_cases-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) < 82
BuildRequires:  python3dist(setuptools) >= 39.2
Requires:       python3-pytest-cases = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-cases
Summary:        Separate test code from test cases in pytest.
%description -n python3-pytest-cases

%prep
%global oreon_srcdir pytest_cases-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-cases usr/lib/python3*/site-packages/pytest_cases* usr/lib64/python3*/site-packages/pytest_cases* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_cases* usr/lib64/python3*/site-packages/pytest_cases* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-cases -f %{oreon_filedir}/python3-pytest-cases.list

%changelog

%autochangelog
