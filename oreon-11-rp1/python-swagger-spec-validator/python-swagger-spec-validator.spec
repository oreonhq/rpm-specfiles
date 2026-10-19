%global source0_hash 4ac92170d30554bfa71330f89bad74f9b3ef4cc1f594bebb8e8901b3d999c7bf
Name:           python-swagger-spec-validator
Version:        3.0.4
Release:        1%{?dist}
Summary:        Validation of Swagger specifications
License:        Apache-2.0
URL:            https://github.com/Yelp/swagger_spec_validator
Source0:        https://github.com/Yelp/swagger_spec_validator/archive/v%{version}/swagger-spec-validator-%{version}.tar.gz
Patch:          0001-Use-importlib.resources-if-possible.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-swagger-spec-validator = %{version}-%{release}
# /oreon:deps
%description

%package     -n python3-swagger-spec-validator
Summary:        Validation of Swagger specifications
%description -n python3-swagger-spec-validator

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir swagger_spec_validator-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-swagger-spec-validator usr/lib/python3*/site-packages/swagger_spec_validator* usr/lib64/python3*/site-packages/swagger_spec_validator* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/swagger_spec_validator* usr/lib64/python3*/site-packages/swagger_spec_validator* usr/bin/*

%check

%pytest -v tests
%files
%files -n python3-swagger-spec-validator -f %{oreon_filedir}/python3-swagger-spec-validator.list

%changelog

%autochangelog
