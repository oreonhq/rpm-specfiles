%global source0_hash 8684abfd4914ea01f1e2f7b24524739344421d8f3f12286fb3100fb5681e1181
Name:           python-pytest-lazy-fixtures
Version:        1.4.1
Release:        1%{?dist}
Summary:        Allows you to use fixtures in @pytest.mark.parametrize.
License:        MIT
URL:            https://github.com/dev-petrov/pytest-lazy-fixtures
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_lazy_fixtures/pytest_lazy_fixtures-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-lazy-fixtures = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-lazy-fixtures
Summary:        Allows you to use fixtures in @pytest.mark.parametrize.
# oreon:reqs
Requires:       python3dist(pytest) >= 7
# /oreon:reqs
%description -n python3-pytest-lazy-fixtures

%prep
%global oreon_srcdir pytest_lazy_fixtures-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-lazy-fixtures usr/lib/python3*/site-packages/pytest_lazy_fixtures* usr/lib64/python3*/site-packages/pytest_lazy_fixtures* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_lazy_fixtures* usr/lib64/python3*/site-packages/pytest_lazy_fixtures* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-lazy-fixtures -f %{oreon_filedir}/python3-pytest-lazy-fixtures.list

%changelog

%autochangelog
