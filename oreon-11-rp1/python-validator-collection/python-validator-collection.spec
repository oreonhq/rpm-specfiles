%global source0_hash ad807325d8ce2b83c630573670f953c582dc35192e25613f39dbfae5fc387534
Name:           python-validator-collection
Version:        1.5.0
Release:        1%{?dist}
Summary:        Collection of 60+ Python functions for validating data
License:        MIT
URL:            https://github.com/insightindustry/validator-collection
Source0:        https://github.com/insightindustry/validator-collection/archive/v.%{version}/validator-collection-v.%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-validator-collection = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-validator-collection
Summary:        Collection of 60+ Python functions for validating data
%description -n python3-validator-collection

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n validator-collection-v.%{version}

# Drop unnecessary linter dependency
sed -i '/codecov/d' requirements.txt setup.py tox.ini

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-validator-collection usr/lib/python3*/site-packages/validator_collection* usr/lib64/python3*/site-packages/validator_collection* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/validator_collection* usr/lib64/python3*/site-packages/validator_collection* usr/bin/*

%check

%pytest -v \
  --deselect='tests/test_checkers.py::test_is_readable[/var/data/xx1.txt-True-False]' \
  --deselect='tests/test_validators.py::test_readable[/var/data/xx1.txt-True-False]' \
  --deselect='tests/test_validators.py::test_writeable[/var/data/xx1.txt-True-False]' \
  --deselect='tests/test_validators.py::test_executable[/var/data/xx1.txt-True-False]' \
  %{nil}
%files
%files -n python3-validator-collection -f %{oreon_filedir}/python3-validator-collection.list

%changelog

%autochangelog
