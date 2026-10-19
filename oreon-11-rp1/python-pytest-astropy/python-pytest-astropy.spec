%global source0_hash 0bdff1fa67a7856ec899c6f7810a86911253d76201a30822d7e4ef14b671bdc0
Name:           python-pytest-astropy
Version:        0.12.0
Release:        1%{?dist}
Summary:        Meta-package containing dependencies for testing
License:        ...
URL:            https://github.com/astropy/pytest-astropy
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_astropy/pytest_astropy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 30.3.0
Requires:       python3-pytest-astropy = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-astropy
Summary:        Meta-package containing dependencies for testing
%description -n python3-pytest-astropy

%prep
%global oreon_srcdir pytest_astropy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-astropy usr/lib/python3*/site-packages/pytest_astropy* usr/lib64/python3*/site-packages/pytest_astropy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_astropy* usr/lib64/python3*/site-packages/pytest_astropy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-astropy -f %{oreon_filedir}/python3-pytest-astropy.list

%changelog

%autochangelog
