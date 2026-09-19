%global source0_hash 29ed0e8b1abe5f4590132f456b6f9cbf0866b89fabf836bc9474fde706e2e13e

%global pypi_name pydocstyle

Name:       python-%{pypi_name}
Version:    6.3.0
Release:    %autorelease
Summary:    Python docstring style checker

# SPDX
License:    MIT
URL:        https://github.com/PyCQA/pydocstyle/
Source:     %{pypi_source %{pypi_name}}
Patch:      https://github.com/PyCQA/pydocstyle/pull/656.patch
# Fix python3.14 test failure
# (D401: First line should be in imperative mood (perhaps 'Add', not 'Adding')
# NOTE: Upstream has archived the repository and it is not possible to submit PRs anymore
Patch:      pydocstyle-py3.14.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
A static analysis tool for checking compliance with Python docstring
conventions.

It supports most of PEP 257 out of the box, but it should not be considered a
reference implementation.}

%description %_description

%package -n python3-%{pypi_name}
Summary:    %{summary}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

# Manually set the correct project version. Upstream does it dynamically when
# building a release with GitHub Actions by executing:
# 'poetry version ${{ github.event.release.tag_name }}'.
sed -r -i 's/(version = ")0.0.0-dev/\1%{version}/' pyproject.toml

# Remove (incorrect) Python shebang from package's __main__.py file.
sed -i '\|/usr/bin/env|d' src/pydocstyle/__main__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{pypi_name}

%check
# Disable "install_package" fixure for integration tests since we want the
# tests to be run against the system-installed version of the package.
sed -i '/pytestmark = pytest.mark.usefixtures("install_package")/d' \
    src/tests/test_integration.py
# Replace 'python(2|3)?' with '%%{__python3}' in tests that run pydocstyle as
# a named Python module.
sed -E -i 's|"python(2\|3)?( -m pydocstyle)|"%{__python3}\2|' \
    src/tests/test_integration.py

%pytest -v src/tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE-MIT
%{_bindir}/pydocstyle

%changelog
%autochangelog
