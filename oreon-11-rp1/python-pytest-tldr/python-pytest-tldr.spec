%global source0_hash 5c0ccc6991276c8489ff1720f1498d5130690bb8504aaf8c7bd115bf91abc035
Name:           python-pytest-tldr
Version:        0.2.6
Release:        1%{?dist}
Summary:        A pytest plugin that limits the output to just the things you need.
License:        BSD-3-Clause
URL:            https://github.com/freakboy3742/pytest-tldr
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_tldr/pytest_tldr-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) == 80.9.0
BuildRequires:  python3dist(setuptools-scm) == 9.2.2
Requires:       python3-pytest-tldr = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-tldr
Summary:        A pytest plugin that limits the output to just the things you need.
# oreon:reqs
Requires:       python3dist(pytest) >= 7.0.0
# /oreon:reqs
%description -n python3-pytest-tldr

%prep
%global oreon_srcdir pytest_tldr-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-tldr usr/lib/python3*/site-packages/pytest_tldr* usr/lib64/python3*/site-packages/pytest_tldr* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_tldr* usr/lib64/python3*/site-packages/pytest_tldr* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-tldr -f %{oreon_filedir}/python3-pytest-tldr.list

%changelog

%autochangelog
