%global source0_hash f2d45f36dd11f507f895aff2f8bd1bf4c58197cdbfa9cd72e9e5f09855dd2ba6
%bcond mypy 1
Name:           python-typeguard
Version:        4.6.0
Release:        1%{?dist}
Summary:        Run-time type checker for Python
License:        MIT
URL:            https://github.com/agronholm/typeguard
Source0:        https://github.com/agronholm/typeguard/archive/%{version}/typeguard-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
This library provides run-time type checking for functions defined with PEP 484
argument (and return) type annotations.}
# oreon:deps
BuildRequires:  tomcli
# /oreon:deps
%description %{common_description}

%package -n python3-typeguard
Summary:        Run-time type checker for Python
Obsoletes:      python-typeguard-doc < 4.2.1-2
%description -n python3-typeguard %{common_description}

%prep

%autosetup -p1
# Downstream-only: do not treat warnings in tests as errors
#
# This makes sense for upstream development and CI, but is too strict for
# distribution packaging.
tomcli set pyproject.toml lists delitem \
    'tool.pytest.ini_options.filterwarnings' error

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem dependency-groups.test 'coverage\b.*'

%if %{without mypy}
tomcli set pyproject.toml lists delitem dependency-groups.test 'mypy\b.*'
%endif

%build -p

export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%install
%pyproject_install
%oreon_autofiles python3-typeguard usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{without mypy}
k="${k-}${k+ and }not test_negative"
k="${k-}${k+ and }not test_positive"
%endif
%pytest -k "${k-}" -v -rs
%files -f %{oreon_filedir}/main.list
%files -n python3-typeguard -f %{oreon_filedir}/python3-typeguard.list

%changelog

%autochangelog
