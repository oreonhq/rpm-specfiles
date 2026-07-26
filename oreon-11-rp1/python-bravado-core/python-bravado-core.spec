%global source0_hash c5784d5ce6dd506c2d2460e652ff57b0eea46b1abde06207be290d2ff5fabe24

Name:           python-bravado-core
Version:        6.1.0
Release:        %autorelease
Summary:        Library for adding Swagger support to clients and servers

License:        BSD-3-Clause
URL:            https://github.com/Yelp/bravado-core
# PyPI tarball is missing tests
Source:         %{url}/archive/v%{version}/bravado-core-%{version}.tar.gz
# https://github.com/Yelp/bravado-core/pull/393
Patch:          0001-Use-standard-library-mock-when-possible.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
bravado-core is a Python library that adds client-side and server-side support
for the OpenAPI Specification v2.0.}

%description %_description

%package -n     python3-bravado-core
Summary:        %{summary}

%description -n python3-bravado-core %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n bravado-core-%{version} -p 1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l bravado_core

%check
# Recursive tests seem to hang forever, skip for now
# Profiling tests require pytest-benchmark[histogram], skip for now
%pytest -v \
    -k 'not recursive' \
    --ignore tests/profiling

%files -n python3-bravado-core -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
