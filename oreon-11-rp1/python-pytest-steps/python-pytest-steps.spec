%global source0_hash d210dfbd34bda3c318dd10d1764a90dedb5d945b8734c3f5914a87140e642217
Name:           python-pytest-steps
Version:        1.8.0
Release:        1%{?dist}
Summary:        Create step-wise / incremental tests in pytest.
License:        ...
URL:            https://github.com/smarie/python-pytest-steps
Source0:        https://files.pythonhosted.org/packages/source/p/pytest-steps/pytest-steps-%{version}.tar.gz
BuildArch:      noarch
Patch:          pytest-steps-1.7.2-no-pytest-runner.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 39.2
Requires:       python3-pytest-steps = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-steps
Summary:        Create step-wise / incremental tests in pytest.
%description -n python3-pytest-steps

%prep
%global oreon_srcdir pytest-steps-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-steps usr/lib/python3*/site-packages/pytest_steps* usr/lib64/python3*/site-packages/pytest_steps* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_steps* usr/lib64/python3*/site-packages/pytest_steps* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-steps -f %{oreon_filedir}/python3-pytest-steps.list

%changelog

%autochangelog
