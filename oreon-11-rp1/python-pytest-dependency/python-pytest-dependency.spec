%global source0_hash 246c24d2a5fc743a942cec4408853640e56a05ba58d46e5b213a1d4b738a2464
Name:           python-pytest-dependency
Version:        0.6.1
Release:        1%{?dist}
Summary:        Manage dependencies of tests
License:        Apache-2.0
URL:            https://github.com/RKrahl/pytest-dependency
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_dependency/pytest_dependency-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-dependency = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-dependency
Summary:        Manage dependencies of tests
%description -n python3-pytest-dependency

%prep
%global oreon_srcdir pytest_dependency-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-dependency usr/lib/python3*/site-packages/pytest_dependency* usr/lib64/python3*/site-packages/pytest_dependency* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_dependency* usr/lib64/python3*/site-packages/pytest_dependency* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-dependency -f %{oreon_filedir}/python3-pytest-dependency.list

%changelog

%autochangelog
