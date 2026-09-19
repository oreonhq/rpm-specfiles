%global source0_hash f22980844eb6a7c0266ffc70f111b9c7e7c7c13da38c3b439afc7eab3d7c9c8e

%global pypi_name gql

Name:           python-%{pypi_name}
Version:        4.0.0
Release:        %autorelease
Summary:        GraphQL client for Python

License:        MIT
URL:            https://github.com/graphql-python/gql
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel

%description
This is a GraphQL client for Python 3.7+. Plays nicely with graphene,
graphql-core, graphql-js and any other GraphQL implementation
compatible with the spec.

GQL architecture is inspired by React-Relay and Apollo-Client.

%pyproject_extras_subpkg -n python3-gql aiohttp websockets requests httpx botocore

%package -n     python3-%{pypi_name}
Summary:        GraphQL client for Python
Suggests:       python3-%{pypi_name}+aiohttp = %{version}-%{release}
Suggests:       python3-%{pypi_name}+http    = %{version}-%{release}

%description -n python3-%{pypi_name}
This is a GraphQL client for Python 3.7+. Plays nicely with graphene,
graphql-core, graphql-js and any other GraphQL implementation
compatible with the spec.

GQL architecture is inspired by React-Relay and Apollo-Client.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# Remove the deps expansion from tox.ini
# and reply on the -x tests
sed -i 's/^deps = .*$/deps =/' tox.ini

# Do not update setuptools
sed -i 's/pip install -U setuptools//' tox.ini

# Relax some versioniong
sed -i -E '/tests_requires\s*=\s*\[/,/]/ {
  s/"pytest==[^"]*"/"pytest"/
  s/"pytest-asyncio==[^"]*"/"pytest-asyncio"/
  s/"pytest-cov==[^"]*"/"pytest-cov"/
  s/"vcrpy==[^"]*"/"vcrpy"/
}' setup.py

%generate_buildrequires
%pyproject_buildrequires -t -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files gql

%check
# Upstream hard codes an older version of pytest-asyncio - should be adapted
# https://pytest-asyncio.readthedocs.io/en/latest/how-to-guides/migrate_from_0_21.html
# Dsiable a few tests that should be adapted.
%if 0%{?fedora} >= 41 
 rm tests/starwars/test_introspection.py
 rm tests/starwars/test_dsl.py
 rm tests/test_async_client_validation.py
 rm tests/test_transport.py
 rm tests/test_transport_batch.py
%endif

%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%{_bindir}/gql-cli
%doc README.md

%changelog
%autochangelog
