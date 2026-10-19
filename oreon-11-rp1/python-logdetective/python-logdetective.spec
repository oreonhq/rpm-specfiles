%global source0_hash e9e45e293b57d47aafe01e3a76928e718e7f6852bdc8d47afe69eddbebaa268e
Name:           python-logdetective
Version:        4.10.2
Release:        1%{?dist}
Summary:        Analyze logs with a template miner and an LLM to discover errors and suggest solutions.
License:        Apache-2.0
URL:            https://github.com/fedora-copr/logdetective
Source0:        https://files.pythonhosted.org/packages/source/l/logdetective/logdetective-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-logdetective = %{version}-%{release}
# /oreon:deps
%package -n       python3-logdetective+server
Summary:        Metapackage for python3-logdetective server extras
Requires:       python3-logdetective = %{version}-%{release}
Requires:       python3dist(fastapi) >= 0.111.1
Requires:       python3dist(fastapi) < 1.0.0
Requires:       python3dist(sqlalchemy) >= 2.0.36
Requires:       python3dist(sqlalchemy) < 3.0.0
Requires:       python3dist(alembic) >= 1.13.3
Requires:       python3dist(alembic) < 2.0.0
Requires:       python3dist(tenacity) >= 9.1.0
Requires:       python3dist(tenacity) < 9.2.0
Requires:       python3dist(sentry-sdk[fastapi]) >= 2.17.0
Requires:       python3dist(sentry-sdk[fastapi]) < 3.0.0
Requires:       python3dist(koji) >= 1.35.0
Requires:       python3dist(koji) < 2.0.0
Requires:       python3dist(asyncpg) >= 0.30.0
Requires:       python3dist(asyncpg) < 1.0.0
Requires:       python3dist(python-gitlab) >= 4.4.0
Requires:       python3dist(httpx) >= 0.28.1
Requires:       python3dist(httpx) < 1.0.0
Requires:       python3dist(starlette) < 2.0.0
Requires:       python3dist(uvicorn) >= 0.44.0
Requires:       python3dist(gunicorn) >= 25.3.0
Requires:       python3dist(fastembed) >= 0.8.0
Requires:       python3dist(pgvector) >= 0.4.2
Requires:       python3dist(google-cloud-aiplatform) >= 1.158.0
Provides:       python3dist(logdetective[server]) = %{version}-%{release}

%description -n python3-logdetective+server
Metapackage for python3-logdetective server extras.

%package -n       python3-logdetective+server-testing
Summary:        Metapackage for python3-logdetective server-testing extras
Requires:       python3-logdetective = %{version}-%{release}
Requires:       python3dist(fastapi) >= 0.111.1
Requires:       python3dist(fastapi) < 1.0.0
Requires:       python3dist(sqlalchemy) >= 2.0.36
Requires:       python3dist(sqlalchemy) < 3.0.0
Requires:       python3dist(alembic) >= 1.13.3
Requires:       python3dist(alembic) < 2.0.0
Requires:       python3dist(tenacity) >= 9.1.0
Requires:       python3dist(tenacity) < 9.2.0
Requires:       python3dist(sentry-sdk[fastapi]) >= 2.17.0
Requires:       python3dist(sentry-sdk[fastapi]) < 3.0.0
Requires:       python3dist(koji) >= 1.35.0
Requires:       python3dist(koji) < 2.0.0
Requires:       python3dist(asyncpg) >= 0.30.0
Requires:       python3dist(asyncpg) < 1.0.0
Requires:       python3dist(python-gitlab) >= 4.4.0
Requires:       python3dist(httpx) >= 0.28.1
Requires:       python3dist(httpx) < 1.0.0
Requires:       python3dist(starlette) < 2.0.0
Requires:       python3dist(uvicorn) >= 0.44.0
Requires:       python3dist(gunicorn) >= 25.3.0
Requires:       python3dist(fastembed) >= 0.8.0
Requires:       python3dist(pgvector) >= 0.4.2
Requires:       python3dist(google-cloud-aiplatform) >= 1.158.0
Provides:       python3dist(logdetective[server-testing]) = %{version}-%{release}

%description -n python3-logdetective+server-testing
Metapackage for python3-logdetective server-testing extras.

%package -n       python3-logdetective+testing
Summary:        Metapackage for python3-logdetective testing extras
Requires:       python3-logdetective = %{version}-%{release}
Requires:       python3dist(asciidoc) >= 10.2.1
Requires:       python3dist(asciidoc) < 11.0.0
Provides:       python3dist(logdetective[testing]) = %{version}-%{release}

%description -n python3-logdetective+testing
Metapackage for python3-logdetective testing extras.

%description

%package -n     python3-logdetective
Summary:        Analyze logs with a template miner and an LLM to discover errors and suggest solutions.
# oreon:reqs
Requires:       python3dist(aiohttp) < 4.0.0
Requires:       python3dist(aiohttp) >= 3.7.4
Requires:       python3dist(beeai-framework) >= 0.1.81
Requires:       python3dist(drain3-improved) >= 0.10.0
Requires:       python3dist(huggingface-hub) < 2.0.0
Requires:       python3dist(huggingface-hub) >= 1.0.0
Requires:       python3dist(litellm)
Requires:       python3dist(llama-cpp-python) < 1.0.0
Requires:       python3dist(llama-cpp-python) > 0.2.56
Requires:       python3dist(numpy) >= 1.26.0
Requires:       python3dist(pydantic) < 3.0.0
Requires:       python3dist(pydantic) >= 2.8.2
Requires:       python3dist(pyyaml) < 7.0.0
Requires:       python3dist(pyyaml) >= 6.0.1
# /oreon:reqs
%description -n python3-logdetective

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir logdetective-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-logdetective usr/lib/python3*/site-packages/logdetective* usr/lib64/python3*/site-packages/logdetective* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/logdetective* usr/lib64/python3*/site-packages/logdetective* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-logdetective -f %{oreon_filedir}/python3-logdetective.list

%changelog

%autochangelog
