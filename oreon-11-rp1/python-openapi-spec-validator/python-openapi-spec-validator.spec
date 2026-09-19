%global source0_hash cc029309b5c5dbc7859df0372d55e9d1ff43e96d678b9ba087f7c56fc586f734

%global srcname openapi-spec-validator
%global modname openapi_spec_validator

Name:           python-%{srcname}
Version:        0.7.2
Release:        %autorelease
Summary:        Python library for OpenAPI specs validation

License:        Apache-2.0
URL:            https://github.com/python-openapi/%{srcname}
Source:         %{pypi_source %{modname}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
OpenAPI Spec Validator is a Python library that validates OpenAPI Specs against
the OpenAPI 2.0 (aka Swagger), OpenAPI 3.0 and OpenAPI 3.1 specification. The
validator aims to check for full compliance with the Specification.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{modname}-%{version}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/^--cov[-=]/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pytest -m 'not network'

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/%{srcname}

%changelog
%autochangelog
