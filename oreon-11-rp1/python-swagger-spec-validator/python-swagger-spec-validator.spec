%global source0_hash 4ac92170d30554bfa71330f89bad74f9b3ef4cc1f594bebb8e8901b3d999c7bf

Name:           python-swagger-spec-validator
Version:        3.0.4
Release:        %autorelease
Summary:        Validation of Swagger specifications

License:        Apache-2.0
URL:            https://github.com/Yelp/swagger_spec_validator
Source:         %{url}/archive/v%{version}/swagger-spec-validator-%{version}.tar.gz

# https://github.com/Yelp/swagger_spec_validator/pull/176
Patch:          0001-Use-importlib.resources-if-possible.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Swagger Spec Validator is a Python library that validates Swagger Specs against
the Swagger 1.2 or Swagger 2.0 specification. The validator aims to check for
full compliance with the Specification.}

%description %{_description}

%package     -n python3-swagger-spec-validator
Summary:        %{summary}

%description -n python3-swagger-spec-validator %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n swagger_spec_validator-%{version} -p 1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files swagger_spec_validator

%check
%pytest -v tests

%files -n python3-swagger-spec-validator -f %{pyproject_files}
%doc README.md CHANGELOG.rst

%changelog
%autochangelog
