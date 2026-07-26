%global source0_hash 32667b79066fabc12d4f17f16a8fd7361b5f4435208b3ba32c226e52212a8c30

%global pypi_name mongomock

Name:           python-%{pypi_name}
Version:        4.3.0
Release:        2%{?dist}
Summary:        Module for testing MongoDB-dependent code

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/mongomock/mongomock
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Mongomock is a small library to help testing Python code that interacts
with MongoDB via Pymongo.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description -n python3-%{pypi_name}
Mongomock is a small library to help testing Python code that interacts
with MongoDB via Pymongo.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mongomock

%check
%pytest -v tests -k "not BulkOperationsWithPymongoTest and not CollectionComparisonTest \
  and not MongoClientCollectionTest and not MongoClientSortSkipLimitTest \
  and not test__insert_do_not_modify_input"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
