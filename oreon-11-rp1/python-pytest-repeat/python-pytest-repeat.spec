%global source0_hash d92ac14dfaa6ffcfe6917e5d16f0c9bc82380c135b03c2a5f412d2637f224485
Name:           python-pytest-repeat
Version:        0.9.4
Release:        1%{?dist}
Summary:        pytest plugin for repeating tests
License:        MPL-2.0
URL:            https://github.com/pytest-dev/pytest-repeat
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_repeat/pytest_repeat-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-repeat = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-repeat
Summary:        pytest plugin for repeating tests
%description -n python3-pytest-repeat

%prep
%global oreon_srcdir pytest_repeat-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-repeat usr/lib/python3*/site-packages/pytest_repeat* usr/lib64/python3*/site-packages/pytest_repeat* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_repeat* usr/lib64/python3*/site-packages/pytest_repeat* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-repeat -f %{oreon_filedir}/python3-pytest-repeat.list

%changelog

%autochangelog
