%global source0_hash b30490dfa74e3aac2276105525590135212352f5dd7e5acf8f62f6a89ed6f2d0

%bcond falcon 1

%global srcname openapi-core
%global modname openapi_core

Name:           python-%{srcname}
Version:        0.22.0
Release:        %autorelease
Summary:        OpenAPI client-side and server-side support

License:        BSD-3-Clause
URL:            https://github.com/python-openapi/%{srcname}
Source:         %{pypi_source %{modname}}

# Allow Starlette 0.50, 0.51, 0.52
# Not upstreamable until a FastAPI release supports 0.52
Patch:          allow_starlette_0.52.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  tomcli

# Test dependencies; see [tool.poetry.dev-dependencies], but note that this
# contains both test dependencies and unwanted linters etc., as well as some
# packages that are not directly required by the tests, such as webob and
# strict-rfc3339.
BuildRequires:  python3dist(pytest) >= 8
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(responses)

# This is not directly imported in the tests, but is implicitly required for
# some of the Django integration tests.
BuildRequires:  python3dist(djangorestframework)
# This is not directly imported in the tests, but is implicitly required for
# some of the FastAPI and Starlette integration tests.
BuildRequires:  python3dist(httpx)

%global _description %{expand:
Openapi-core is a Python library that adds client-side and server-side
support for the OpenAPI v3.0 and OpenAPI v3.1 specification.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%pyproject_extras_subpkg -n python3-openapi-core aiohttp django %{?with_falcon:falcon} fastapi flask requests starlette

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version} -p1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/^--cov[-=]/d' pyproject.toml
# We cannot respect a SemVer or version range pin on FastAPI; it updates
# frequently, with usually-tiny breaking changes.
sed -r -i \
    -e 's/(fastapi = \{version = ")\^/\1>=/' \
    -e 's/(fastapi = \{version = ".*),<[^"]+/\1/' \
    pyproject.toml
# Erroring on DeprecationWarnings makes sense upstream, but is probably too
# strict for distribution packaging.
#
# This specifically works around:
#
# DeprecationWarning: 'asyncio.get_event_loop_policy' is deprecated and slated
# for removal in Python 3.16
tomcli set pyproject.toml lists delitem \
    tool.pytest.ini_options.filterwarnings error

%generate_buildrequires

%pyproject_buildrequires -x aiohttp -x django %{?with_falcon:-x falcon} -x fastapi -x flask -x requests -x starlette

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%if %{without falcon}
ignore="${ignore-} --ignore=tests/integration/contrib/falcon"
%endif

%pytest ${ignore-}

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
