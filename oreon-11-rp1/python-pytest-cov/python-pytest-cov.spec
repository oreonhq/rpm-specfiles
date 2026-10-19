%global source0_hash 30674f2b5f6351aa09702a9c8c364f6a01c27aae0c1366ae8016160d1efc56b2
Name:           python-pytest-cov
Version:        7.1.0
Release:        1%{?dist}
Summary:        Pytest plugin for measuring coverage.
License:        MIT
URL:            https://github.com/pytest-dev/pytest-cov
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_cov/pytest_cov-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-cov = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytest-cov+testing
Summary:        Metapackage for python3-pytest-cov testing extras
Requires:       python3-pytest-cov = %{version}-%{release}
Provides:       python3dist(pytest-cov[testing]) = %{version}-%{release}

%description -n python3-pytest-cov+testing
Metapackage for python3-pytest-cov testing extras.

%description

%package -n     python3-pytest-cov
Summary:        Pytest plugin for measuring coverage.
# oreon:reqs
Requires:       python3dist(coverage[toml]) >= 7.10.6
Requires:       python3dist(pluggy) >= 1.2
Requires:       python3dist(pytest) >= 7
# /oreon:reqs
%description -n python3-pytest-cov

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pytest_cov-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-cov usr/lib/python3*/site-packages/pytest_cov* usr/lib64/python3*/site-packages/pytest_cov* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_cov* usr/lib64/python3*/site-packages/pytest_cov* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-cov -f %{oreon_filedir}/python3-pytest-cov.list

%changelog

%autochangelog
