%global source0_hash d340789d6f43cac901fc14f52b15723279bd66db4db7a6506d969417c36cdf04
Name:           python-pytest-postgresql
Version:        9.1.0
Release:        1%{?dist}
Summary:        Postgresql fixtures and fixture factories for Pytest.
License:        LGPL-3.0-or-later
URL:            https://github.com/dbfixtures/pytest-postgresql
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_postgresql/pytest_postgresql-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.13
BuildRequires:  python3dist(uv-build) >= 0.11
Requires:       python3-pytest-postgresql = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytest-postgresql+async
Summary:        Metapackage for python3-pytest-postgresql async extras
Requires:       python3-pytest-postgresql = %{version}-%{release}
Requires:       python3dist(aiofiles) >= 23.0
Requires:       python3dist(pytest-asyncio) >= 1.4
Provides:       python3dist(pytest-postgresql[async]) = %{version}-%{release}

%description -n python3-pytest-postgresql+async
Metapackage for python3-pytest-postgresql async extras.

%description

%package -n     python3-pytest-postgresql
Summary:        Postgresql fixtures and fixture factories for Pytest.
# oreon:reqs
Requires:       python3dist(mirakuru) >= 2.6.0
Requires:       python3dist(port-for) >= 0.7.3
Requires:       python3dist(psycopg) >= 3.0.0
Requires:       python3dist(pytest) >= 8.2
# /oreon:reqs
%description -n python3-pytest-postgresql

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pytest_postgresql-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-postgresql usr/lib/python3*/site-packages/pytest_postgresql* usr/lib64/python3*/site-packages/pytest_postgresql* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_postgresql* usr/lib64/python3*/site-packages/pytest_postgresql* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-postgresql -f %{oreon_filedir}/python3-pytest-postgresql.list

%changelog

%autochangelog
