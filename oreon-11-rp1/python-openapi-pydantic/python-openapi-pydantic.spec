%global source0_hash 9a74bb7759592d2e5d9999b6e20fd67487dc135391f75fb1d78e5501b674cad7
Name:           python-openapi-pydantic
Version:        0.5.1
Release:        1%{?dist}
Summary:        Pydantic OpenAPI schema implementation
License:        MIT
URL:            https://github.com/mike-oakley/openapi-pydantic
Source0:        https://github.com/mike-oakley/openapi-pydantic/archive/v%{version}/openapi-pydantic-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-openapi-pydantic = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-openapi-pydantic
Summary:        Pydantic OpenAPI schema implementation
%description -n python3-openapi-pydantic

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-openapi-pydantic usr/lib/python3*/site-packages/openapi_pydantic* usr/lib64/python3*/site-packages/openapi_pydantic* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/openapi_pydantic* usr/lib64/python3*/site-packages/openapi_pydantic* usr/bin/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-openapi-pydantic -f %{oreon_filedir}/python3-openapi-pydantic.list

%changelog

%autochangelog
