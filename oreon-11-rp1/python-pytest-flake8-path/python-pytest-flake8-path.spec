%global source0_hash bbb696a61d5845f44668302ad0c48af106c0eeef70bcc807ad59999ef45467fd
Name:           python-pytest-flake8-path
Version:        1.7.0
Release:        1%{?dist}
Summary:        A pytest fixture for testing flake8 plugins.
License:        MIT
URL:            https://github.com/adamchainz/pytest-flake8-path
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_flake8_path/pytest_flake8_path-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-pytest-flake8-path = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-flake8-path
Summary:        A pytest fixture for testing flake8 plugins.
%description -n python3-pytest-flake8-path

%prep
%global oreon_srcdir pytest_flake8_path-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-flake8-path usr/lib/python3*/site-packages/pytest_flake8_path* usr/lib64/python3*/site-packages/pytest_flake8_path* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_flake8_path* usr/lib64/python3*/site-packages/pytest_flake8_path* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-flake8-path -f %{oreon_filedir}/python3-pytest-flake8-path.list

%changelog

%autochangelog
