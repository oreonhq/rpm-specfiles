%global source0_hash 01f488e955ed0e0049777bee598bf1f647dd524e06f544c31a24e68f8d775a51
Name:           python-pytest-testmon
Version:        2.2.0
Release:        1%{?dist}
Summary:        selects tests affected by changed files and methods
License:        MIT
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_testmon/pytest_testmon-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-testmon = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-testmon
Summary:        selects tests affected by changed files and methods
# oreon:reqs
Requires:       python3dist(coverage) < 8
Requires:       python3dist(coverage) >= 6
Requires:       python3dist(pytest) < 10
Requires:       python3dist(pytest) >= 5
# /oreon:reqs
%description -n python3-pytest-testmon

%prep
%global oreon_srcdir pytest_testmon-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-testmon usr/lib/python3*/site-packages/pytest_testmon* usr/lib64/python3*/site-packages/pytest_testmon* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_testmon* usr/lib64/python3*/site-packages/pytest_testmon* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-testmon -f %{oreon_filedir}/python3-pytest-testmon.list

%changelog

%autochangelog
