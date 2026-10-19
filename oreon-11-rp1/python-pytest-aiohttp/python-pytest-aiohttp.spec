%global source0_hash 3aa9c9fe26e543eaccc7eb0add381c685ba3ed3e2fed0af74540f63bcd31458d
Name:           python-pytest-aiohttp
Version:        1.1.1
Release:        1%{?dist}
Summary:        Pytest plugin for aiohttp support
License:        ...
URL:            https://github.com/aio-libs/pytest-aiohttp
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_aiohttp/pytest_aiohttp-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 82.0.1
BuildRequires:  python3dist(setuptools-scm) >= 10.0.5
BuildRequires:  python3dist(wheel) >= 0.47.0
Requires:       python3-pytest-aiohttp = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-aiohttp
Summary:        Pytest plugin for aiohttp support
%description -n python3-pytest-aiohttp

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pytest_aiohttp-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-aiohttp usr/lib/python3*/site-packages/pytest_aiohttp* usr/lib64/python3*/site-packages/pytest_aiohttp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_aiohttp* usr/lib64/python3*/site-packages/pytest_aiohttp* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-aiohttp -f %{oreon_filedir}/python3-pytest-aiohttp.list

%changelog

%autochangelog
