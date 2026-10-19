%global source0_hash 6956ddfb65ca1d07e7e3d99e2c5359d82300f4cb062e6049563bd2c106f72d5c
Name:           python-pytest-rerunfailures
Version:        16.7
Release:        1%{?dist}
Summary:        pytest plugin to re-run tests to eliminate flaky failures
License:        MPL-2.0
URL:            https://github.com/pytest-dev/pytest-rerunfailures
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_rerunfailures/pytest_rerunfailures-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-pytest-rerunfailures = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-rerunfailures
Summary:        pytest plugin to re-run tests to eliminate flaky failures
# oreon:reqs
Requires:       python3dist(packaging) >= 17.1
Requires:       python3dist(pytest) >= 8.2
# /oreon:reqs
%description -n python3-pytest-rerunfailures

%prep
%global oreon_srcdir pytest_rerunfailures-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-rerunfailures usr/lib/python3*/site-packages/pytest_rerunfailures* usr/lib64/python3*/site-packages/pytest_rerunfailures* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_rerunfailures* usr/lib64/python3*/site-packages/pytest_rerunfailures* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-rerunfailures -f %{oreon_filedir}/python3-pytest-rerunfailures.list

%changelog

%autochangelog
