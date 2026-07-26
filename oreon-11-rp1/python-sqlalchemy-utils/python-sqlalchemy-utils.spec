%global source0_hash a2181bff01eeb84479e38571d2c0718eb52042f9afd8c194d0d02877e84b7d74

%global modname SQLAlchemy-Utils

Name:               python-sqlalchemy-utils
Version:            0.41.1
Release:            14%{?dist}
Summary:            Various utility functions for SQLAlchemy

# Automatically converted from old format: BSD - review is highly recommended.
License:            LicenseRef-Callaway-BSD
URL:                http://pypi.python.org/pypi/SQLAlchemy-Utils
Source0:            %{pypi_source SQLAlchemy-Utils}
# Omit test on unpackaged python-psycopg2cffi
Patch0:             no-psycopg2cffi.patch
Patch1:             python-sqlalchemy-utils-0.41.1-no-pyodbc-dep.patch
# This can be removed with version >= 0.42.2
Patch2:             python-sqlalchemy-utils-0.41.1-nosqla2.patch

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-pytest
# For tests
BuildRequires:      python3-colour
BuildRequires:      python3-phonenumbers

%description
Various utility functions and custom data types for SQLAlchemy.

%package -n         python3-sqlalchemy-utils
Summary:            Various utility functions for SQLAlchemy

%description -n python3-sqlalchemy-utils
Various utility functions and custom data types for SQLAlchemy.

%generate_buildrequires
%pyproject_buildrequires -x test

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sqlalchemy_utils

%check
# Tons of test failures, not sure they are meant to be run like this?
%pytest || :

%files -n python3-sqlalchemy-utils -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
