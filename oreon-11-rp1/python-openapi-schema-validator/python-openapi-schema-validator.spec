%global source0_hash 723108995e01e4ce9f49e526d0ac1b0211aec0b34913b3913dde18c879c44264
%bcond tests 1
Name:           python-openapi-schema-validator
Version:        0.9.0
Release:        1%{?dist}
Summary:        OpenAPI schema validator for Python
License:        BSD-3-Clause
URL:            https://github.com/python-openapi/openapi-schema-validator
Source0:        https://github.com/python-openapi/openapi-schema-validator/archive/%{version}/openapi-schema-validator-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
%global common_description %{expand:
Openapi-schema-validator is a Python library that validates schema against:
  • OpenAPI Schema Specification v3.0 which is an extended subset of the JSON
    Schema Specification Wright Draft 00.
  • OpenAPI Schema Specification v3.1 which is an extended superset of the JSON
    Schema Specification Draft 2020-12.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-openapi-schema-validator = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-openapi-schema-validator
Summary:        OpenAPI schema validator for Python
%description -n python3-openapi-schema-validator %{common_description}

%prep

%autosetup -p1
# Patch coverage analysis out of [tool.pytest.ini_options]:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/^--cov\b/d' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-openapi-schema-validator usr/lib/python3*/site-packages/openapi_schema_validator* usr/lib64/python3*/site-packages/openapi_schema_validator* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/openapi_schema_validator* usr/lib64/python3*/site-packages/openapi_schema_validator* usr/bin/*

%check

%if %{with tests}
%pytest
%endif
%files
%files -n python3-openapi-schema-validator -f %{oreon_filedir}/python3-openapi-schema-validator.list

%changelog

%autochangelog
