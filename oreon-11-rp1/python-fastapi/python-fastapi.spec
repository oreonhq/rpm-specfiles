%global source0_hash e8822fc40db1e1858054d7a949a888695bc9bdce70139178e33bd2871a453ca1
Name:           python-fastapi
Version:        0.141.1
Release:        1%{?dist}
Summary:        FastAPI framework, high performance, easy to learn, fast to code, ready for production
License:        MIT
URL:            https://github.com/fastapi/fastapi
Source0:        https://files.pythonhosted.org/packages/source/f/fastapi/fastapi-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-Downstream-only-run-test_fastapi_cli-without-coverag.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fastapi = %{version}-%{release}
# /oreon:deps
%package -n       python3-fastapi+standard
Summary:        Metapackage for python3-fastapi standard extras
Requires:       python3-fastapi = %{version}-%{release}
Requires:       python3dist(fastapi-cli[standard]) >= 0.0.32
Requires:       python3dist(fastar) >= 0.9.0
Requires:       python3dist(httpx) >= 0.23.0
Requires:       python3dist(httpx) < 1.0.0
Requires:       python3dist(jinja2) >= 3.1.5
Requires:       python3dist(python-multipart) >= 0.0.18
Requires:       python3dist(email-validator) >= 2.0.0
Requires:       python3dist(uvicorn[standard]) >= 0.12.0
Requires:       python3dist(pydantic-settings) >= 2.0.0
Requires:       python3dist(pydantic-extra-types) >= 2.0.0
Provides:       python3dist(fastapi[standard]) = %{version}-%{release}

%description -n python3-fastapi+standard
Metapackage for python3-fastapi standard extras.

%package -n       python3-fastapi+standard-no-fastapi-cloud-cli
Summary:        Metapackage for python3-fastapi standard-no-fastapi-cloud-cli extras
Requires:       python3-fastapi = %{version}-%{release}
Requires:       python3dist(fastapi-cli[standard-no-fastapi-cloud-cli]) >= 0.0.32
Requires:       python3dist(httpx) >= 0.23.0
Requires:       python3dist(httpx) < 1.0.0
Requires:       python3dist(jinja2) >= 3.1.5
Requires:       python3dist(python-multipart) >= 0.0.18
Requires:       python3dist(email-validator) >= 2.0.0
Requires:       python3dist(uvicorn[standard]) >= 0.12.0
Requires:       python3dist(pydantic-settings) >= 2.0.0
Requires:       python3dist(pydantic-extra-types) >= 2.0.0
Provides:       python3dist(fastapi[standard-no-fastapi-cloud-cli]) = %{version}-%{release}

%description -n python3-fastapi+standard-no-fastapi-cloud-cli
Metapackage for python3-fastapi standard-no-fastapi-cloud-cli extras.

%package -n       python3-fastapi+all
Summary:        Metapackage for python3-fastapi all extras
Requires:       python3-fastapi = %{version}-%{release}
Requires:       python3dist(fastapi-cli[standard]) >= 0.0.32
Requires:       python3dist(httpx) >= 0.23.0
Requires:       python3dist(httpx) < 1.0.0
Requires:       python3dist(jinja2) >= 3.1.5
Requires:       python3dist(python-multipart) >= 0.0.18
Requires:       python3dist(itsdangerous) >= 1.1.0
Requires:       python3dist(pyyaml) >= 5.3.1
Requires:       python3dist(email-validator) >= 2.0.0
Requires:       python3dist(uvicorn[standard]) >= 0.12.0
Requires:       python3dist(pydantic-settings) >= 2.0.0
Requires:       python3dist(pydantic-extra-types) >= 2.0.0
Provides:       python3dist(fastapi[all]) = %{version}-%{release}

%description -n python3-fastapi+all
Metapackage for python3-fastapi all extras.

%description

%package -n     python3-fastapi
Summary:        FastAPI framework, high performance, easy to learn, fast to code, ready for production
# oreon:reqs
Requires:       python3dist(annotated-doc) >= 0.0.2
Requires:       python3dist(pydantic) >= 2.9.0
Requires:       python3dist(starlette) >= 0.46.0
Requires:       python3dist(typing-extensions) >= 4.8.0
Requires:       python3dist(typing-inspection) >= 0.4.2
# /oreon:reqs
%description -n python3-fastapi

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir fastapi-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fastapi usr/lib/python3*/site-packages/fastapi* usr/lib64/python3*/site-packages/fastapi* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fastapi* usr/lib64/python3*/site-packages/fastapi* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-fastapi -f %{oreon_filedir}/python3-fastapi.list

%changelog

%autochangelog
