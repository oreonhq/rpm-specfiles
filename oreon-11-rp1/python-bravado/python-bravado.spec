%global source0_hash 9660bd867068d45cd62eafe5dd8f74c1a856483ebeaa059ada2ee6711b37403a
Name:           python-bravado
Version:        12.0.1
Release:        1%{?dist}
Summary:        Library for accessing Swagger-enabled API's
License:        BSD-3-Clause
URL:            https://github.com/Yelp/bravado
Source0:        https://github.com/Yelp/bravado/archive/v%{version}/bravado-%{version}.tar.gz
Patch:          0001-Use-standard-library-mock-when-possible.patch
Patch:          0002-Drop-monotonic-dependency.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-bravado = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-bravado
Summary:        Library for accessing Swagger-enabled API's
%description -n python3-bravado

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir bravado-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-bravado usr/lib/python3*/site-packages/bravado* usr/lib64/python3*/site-packages/bravado* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/bravado* usr/lib64/python3*/site-packages/bravado* usr/bin/*

%check

%pytest -v \
    --ignore tests/fido_client \
    --ignore tests/integration/fido_client_test.py \
    tests
%files
%files -n python3-bravado -f %{oreon_filedir}/python3-bravado.list

%changelog

%autochangelog
