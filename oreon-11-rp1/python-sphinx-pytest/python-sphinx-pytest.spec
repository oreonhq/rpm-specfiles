%global source0_hash 141a3d6b6cd8616ded72a949a2e7ba8b95e811e58f1118fa1ddeb8c61c3b6364
Name:           python-sphinx-pytest
Version:        0.3.0
Release:        1%{?dist}
Summary:        Helpful pytest fixtures for sphinx extensions.
License:        MIT
URL:            https://github.com/sphinx-extensions2/sphinx-pytest
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx_pytest/sphinx_pytest-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-sphinx-pytest = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sphinx-pytest
Summary:        Helpful pytest fixtures for sphinx extensions.
%description -n python3-sphinx-pytest

%prep
%global oreon_srcdir sphinx_pytest-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinx-pytest usr/lib/python3*/site-packages/sphinx_pytest* usr/lib64/python3*/site-packages/sphinx_pytest* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_pytest* usr/lib64/python3*/site-packages/sphinx_pytest* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sphinx-pytest -f %{oreon_filedir}/python3-sphinx-pytest.list

%changelog

%autochangelog
