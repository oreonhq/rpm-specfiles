%global source0_hash 9a74bb7759592d2e5d9999b6e20fd67487dc135391f75fb1d78e5501b674cad7

Name:           python-openapi-pydantic
Version:        0.5.1
Release:        %autorelease
Summary:        Pydantic OpenAPI schema implementation

License:        MIT
URL:            https://github.com/mike-oakley/openapi-pydantic
Source:         %{url}/archive/v%{version}/openapi-pydantic-%{version}.tar.gz

BuildSystem:    pyproject
# No LICENSE in metadata.
BuildOption(install):  -L openapi_pydantic

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-openapi-spec-validator

%global _description %{expand:
Pydantic OpenAPI schema implementation.}

%description %_description

%package -n     python3-openapi-pydantic
Summary:        %{summary}

%description -n python3-openapi-pydantic %_description

%files -n python3-openapi-pydantic -f %{pyproject_files}
%license LICENSE

%check -a
%pyproject_check_import
%pytest

%changelog
%autochangelog
