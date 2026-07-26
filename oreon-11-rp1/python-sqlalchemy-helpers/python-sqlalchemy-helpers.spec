%global source0_hash d1b874b2e22cc7b10bcec030f7b53bf65ccea66f1d4e4dec3f33d8e748298901

%{?!python3_pkgversion:%global python3_pkgversion 3}

%global pypi_name sqlalchemy-helpers
%global srcname sqlalchemy_helpers

Name:           python-sqlalchemy-helpers
Version:        1.0.1
Release:        7%{?dist}
Summary:        Set of helpers to integrate SQLAlchemy and Alembic in a project
License:        LGPL-3.0-or-later
URL:            https://github.com/fedora-infra/sqlalchemy-helpers
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-asyncio
BuildRequires:  python%{python3_pkgversion}-pytest-mock
BuildRequires:  python%{python3_pkgversion}-pydantic
BuildRequires:  python%{python3_pkgversion}-pydantic-settings
BuildRequires:  python%{python3_pkgversion}-aiosqlite
BuildRequires:  python%{python3_pkgversion}-asyncpg

# Add missing dependency
# https://github.com/fedora-infra/sqlalchemy-helpers/commit/f0dfdb777729f898790c8c6cb163f5a48e7bf055
BuildRequires:  python%{python3_pkgversion}-sqlalchemy+asyncio
Requires:       python%{python3_pkgversion}-sqlalchemy+asyncio

%global _description %{expand:
This project contains tools to use SQLAlchemy and Alembic in a project.

It has Flask and FastAPI integrations, and other framework integrations could
be added in the future.

The full documentation is on ReadTheDocs:
https://sqlalchemy-helpers.readthedocs.io
}

%description %_description

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t -x flask

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{srcname}

%check
%{pytest} tests

%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%license LICENSES/*
%doc README.md docs

%changelog
%autochangelog
