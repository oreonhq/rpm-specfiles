%global source0_hash 2cf0b6ce6e102de040fcc0257511ffd62d2ed6c86f5c5083cce9860c025e8ed9

%global extras daphne,uvicorn,examples

Name:           python-sse-starlette
Version:        3.2.0
Release:        %autorelease
Summary:        SSE plugin for Starlette

License:        BSD-3-Clause
URL:            https://github.com/sysid/sse-starlette
Source0:        %{url}/archive/v%{version}/sse-starlette-%{version}.tar.gz

BuildSystem:    pyproject
BuildOption(install):  -l sse_starlette
BuildOption(generate_buildrequires): -x %{extras}

BuildArch:      noarch
BuildRequires:  tomcli
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
# Used during tests
BuildRequires:  python3-httpx
BuildRequires:  python3-asgi-lifespan
BuildRequires:  python3-async-timeout
BuildRequires:  python3-portend
BuildRequires:  python3-psutil
BuildRequires:  python3-requests
BuildRequires:  python3-tenacity
BuildRequires:  python3-pytest-asyncio

%global _description %{expand:
SSE plugin for Starlette.}

%description %_description

%package -n     python3-sse-starlette
Summary:        %{summary}

%description -n python3-sse-starlette %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sse-starlette-%{version} -p1

# Relax daphne dependency
tomcli set pyproject.toml arrays replace project.optional-dependencies.daphne "daphne>=([0-9]+\.[0-9]+\.[0-9]+)" "daphne>=4.1,<4.3"

%pyproject_extras_subpkg -n python3-sse-starlette %{extras}

%files -n python3-sse-starlette -f %{pyproject_files}
%license LICENSE

%check
%pyproject_check_import
# This requires testcontainers which is not available in Fedora
%pytest --ignore tests/integration/test_multiple_consumers.py

%changelog
%autochangelog
