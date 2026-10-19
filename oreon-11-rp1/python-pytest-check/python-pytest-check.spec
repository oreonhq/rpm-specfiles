%global source0_hash 2d8c9f1fe5cceb0b41c480e1454e95e9ed6a3a534bf2c7e3e0f39167b11cf88b
Name:           python-pytest-check
Version:        2.9.1
Release:        1%{?dist}
Summary:        A pytest plugin that allows multiple failures per test.
License:        ...
URL:            https://github.com/okken/pytest-check
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_check/pytest_check-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-check = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytest-check+dev
Summary:        Metapackage for python3-pytest-check dev extras
Requires:       python3-pytest-check = %{version}-%{release}
Provides:       python3dist(pytest-check[dev]) = %{version}-%{release}

%description -n python3-pytest-check+dev
Metapackage for python3-pytest-check dev extras.

%description

%package -n     python3-pytest-check
Summary:        A pytest plugin that allows multiple failures per test.
# oreon:reqs
Requires:       python3dist(pytest) >= 7.0.0
Requires:       python3dist(typing-extensions) < 5
Requires:       python3dist(typing-extensions) >= 4.12.2
# /oreon:reqs
%description -n python3-pytest-check

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pytest_check-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-check usr/lib/python3*/site-packages/pytest_check* usr/lib64/python3*/site-packages/pytest_check* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_check* usr/lib64/python3*/site-packages/pytest_check* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-check -f %{oreon_filedir}/python3-pytest-check.list

%changelog

%autochangelog
