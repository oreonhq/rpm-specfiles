%global source0_hash 0c26707e2efad8aa1bfc5b7ce170f3fccc2e4918ff85989ba9ffa9facb2be326

%global pypi_name jsonschema

%global common_description %{expand:
jsonschema is an implementation of JSON Schema for Python (supporting
2.7+, including Python 3).

 - Full support for Draft 7, Draft 6, Draft 4 and Draft 3
 - Lazy validation that can iteratively report all validation errors.
 - Small and extensible
 - Programmatic querying of which properties or items failed validation.}

Name:           python-%{pypi_name}
Summary:        Implementation of JSON Schema validation for Python
Version:        4.26.0
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/Julian/jsonschema
Source0:        https://files.pythonhosted.org/packages/source/j/jsonschema/jsonschema-4.26.0.tar.gz#/python-jsonschema-4.26.0.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  tomcli

# test requirements
%bcond tests %{undefined rhel}

%if %{with tests}
# For “trial-3”
BuildRequires:  python3dist(twisted)
%endif

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%description -n python3-%{pypi_name} %{common_description}

%pyproject_extras_subpkg -n python3-%{pypi_name} format format-nongpl


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{pypi_name}-%{version}

# Requires a checkout of the JSON-Schema-Test-Suite
# https://github.com/json-schema-org/JSON-Schema-Test-Suite
rm jsonschema/tests/test_jsonschema_test_suite.py

# Test dependency on (python-)virtue would only be required if we used nox to
# run the tests.
tomcli set pyproject.toml lists delitem dependency-groups.test virtue

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-g test}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%check
%pyproject_check_import -e '*.benchmarks*' -e '*.tests*'
%if %{with tests}
%{py3_test_envvars} trial-3 %{pypi_name}
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license COPYING json/LICENSE
%doc README.rst
%{_bindir}/jsonschema

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.26.0-1
- Prepare for Oreon 11 (RP1)
