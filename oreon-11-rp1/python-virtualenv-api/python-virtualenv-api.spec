%global source0_hash fe368b9f35afd6fe3f20bf3291b6290fa5b855e66da79a46dc57b458f9f74bb7
%bcond tests 0
Name:           python-virtualenv-api
Version:        2.1.18
Release:        1%{?dist}
Summary:        An API for virtualenv/pip
License:        BSD-2-Clause
URL:            https://github.com/sjkingo/virtualenv-api
Source0:        https://github.com/sjkingo/virtualenv-api/archive/%{version}/virtualenv-api-%{version}.tar.gz
Patch:          %{url}/pull/52.patch
Patch:          %{url}/pull/48.patch
Patch:          %{url}/pull/56.patch
BuildArch:      noarch
%global common_description %{expand:
virtualenv is a tool to create isolated Python environments. Unfortunately, it
does not expose a native Python API. This package aims to provide an API in the
form of a wrapper around virtualenv.
It can be used to create and delete environments and perform package management
inside the environment.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-virtualenv-api = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n     python3-virtualenv-api
Summary:        An API for virtualenv/pip
Requires:       /usr/bin/virtualenv
Requires:       /usr/bin/pip
%description -n python3-virtualenv-api %{common_description}

%prep

%autosetup -p1
%py3_shebang_fix example.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-virtualenv-api usr/lib/python3*/site-packages/virtualenv_api* usr/lib64/python3*/site-packages/virtualenv_api* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/virtualenv_api* usr/lib64/python3*/site-packages/virtualenv_api* usr/bin/*

%check

%if %{with tests}
%{py3_test_envvars} '%{python3}' -m unittest -v tests.py
%endif
%files
%files -n python3-virtualenv-api -f %{oreon_filedir}/python3-virtualenv-api.list

%changelog

%autochangelog
