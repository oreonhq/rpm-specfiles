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
%bcond tests %{undefined rhel}
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-jsonschema = %{version}-%{release}
# /oreon:deps
%package -n       python3-jsonschema+format
Summary:        Metapackage for python3-jsonschema format extras
Requires:       python3-jsonschema = %{version}-%{release}
Requires:       python3dist(jsonpointer) > 1.13
Requires:       python3dist(webcolors) >= 1.11
Provides:       python3dist(jsonschema[format]) = %{version}-%{release}

%description -n python3-jsonschema+format
Metapackage for python3-jsonschema format extras.

%package -n       python3-jsonschema+format-nongpl
Summary:        Metapackage for python3-jsonschema format-nongpl extras
Requires:       python3-jsonschema = %{version}-%{release}
Requires:       python3dist(jsonpointer) > 1.13
Requires:       python3dist(rfc3986-validator) > 0.1.0
Requires:       python3dist(rfc3987-syntax) >= 1.1.0
Requires:       python3dist(webcolors) >= 24.6.0
Provides:       python3dist(jsonschema[format-nongpl]) = %{version}-%{release}

%description -n python3-jsonschema+format-nongpl
Metapackage for python3-jsonschema format-nongpl extras.

%description %{common_description}

%package -n     python3-%{pypi_name}
Summary:        Implementation of JSON Schema validation for Python
%description -n python3-%{pypi_name} %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{pypi_name}-%{version}

# Requires a checkout of the JSON-Schema-Test-Suite
# https://github.com/json-schema-org/JSON-Schema-Test-Suite
rm jsonschema/tests/test_jsonschema_test_suite.py

# Test dependency on (python-)virtue would only be required if we used nox to
# run the tests.
tomcli set pyproject.toml lists delitem dependency-groups.test virtue

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/jsonschema* usr/lib64/python3*/site-packages/jsonschema* usr/bin/*

%check

%pyproject_check_import -e '*.benchmarks*' -e '*.tests*'
%if %{with tests}
%{py3_test_envvars} trial-3 %{pypi_name}
%endif
%files
%files -n python3-jsonschema -f %{oreon_filedir}/python3-jsonschema.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.26.0-1
- Prepare for Oreon 11 (RP1)
