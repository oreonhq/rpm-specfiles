%global source0_hash e9c575a5873ef168ddbe340ed9e97ce9edb4492ccc821e4b2ac6bb1f0ed515d2
Name:           python-pytest-randomly
Version:        5.0.0
Release:        1%{?dist}
Summary:        Pytest plugin to randomly order tests and control random.seed.
License:        MIT
URL:            https://github.com/pytest-dev/pytest-randomly
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_randomly/pytest_randomly-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.13
BuildRequires:  python3dist(uv-build) >= 0.12.1
Requires:       python3-pytest-randomly = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-randomly
Summary:        Pytest plugin to randomly order tests and control random.seed.
# oreon:reqs
Requires:       python3dist(pytest) >= 8
# /oreon:reqs
%description -n python3-pytest-randomly

%prep
%global oreon_srcdir pytest_randomly-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-randomly usr/lib/python3*/site-packages/pytest_randomly* usr/lib64/python3*/site-packages/pytest_randomly* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_randomly* usr/lib64/python3*/site-packages/pytest_randomly* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-randomly -f %{oreon_filedir}/python3-pytest-randomly.list

%changelog

%autochangelog
