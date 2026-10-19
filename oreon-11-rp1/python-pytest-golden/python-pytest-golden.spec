%global source0_hash 968d01ab05d330fa10b310545fe8fd9aeb75d3a5b9a513fdbe91b89230b68938
Name:           python-pytest-golden
Version:        1.0.1
Release:        1%{?dist}
Summary:        Plugin for pytest that offloads expected outputs to data files
License:        MIT
URL:            https://github.com/oprypin/pytest-golden
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_golden/pytest_golden-%{version}.tar.gz
BuildArch:      noarch
Patch:          https://github.com/oprypin/pytest-golden/pull/8.patch#/pytest-golden-drop-atomicwrites.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-golden = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-golden
Summary:        Plugin for pytest that offloads expected outputs to data files
# oreon:reqs
Requires:       python3dist(pytest) >= 6.1.2
Requires:       python3dist(ruamel.yaml) < 1.0
Requires:       python3dist(ruamel.yaml) >= 0.16.12
Requires:       python3dist(testfixtures) >= 6.15.0
# /oreon:reqs
%description -n python3-pytest-golden

%prep
%global oreon_srcdir pytest_golden-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-golden usr/lib/python3*/site-packages/pytest_golden* usr/lib64/python3*/site-packages/pytest_golden* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_golden* usr/lib64/python3*/site-packages/pytest_golden* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-golden -f %{oreon_filedir}/python3-pytest-golden.list

%changelog

%autochangelog
