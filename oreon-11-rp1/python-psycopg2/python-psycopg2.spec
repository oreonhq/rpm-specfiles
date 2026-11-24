# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b6a96fda7de54772266e7073af93e7528e6a6626c59b94ac4bd214a7d40cb495
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond tests 0

%global srcname	psycopg2
%global sum	A PostgreSQL database adapter for Python
%global desc	Psycopg is the most popular PostgreSQL adapter for the Python \
programming language. At its core it fully implements the Python DB \
API 2.0 specifications. Several extensions allow access to many of the \
features offered by PostgreSQL.

Summary:	%{sum}
Name:		python-%{srcname}
Version:	2.9.12
Release:	1%{?dist}
License:	LGPL-3.0-or-later WITH openvpn-openssl-exception
Url:		https://www.psycopg.org/

Source0:        https://github.com/psycopg/psycopg2/archive/%{version}/psycopg2-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:	python3-devel

BuildRequires:	libpq-devel
BuildRequires:	python3-sphinx

%if %{with tests}
BuildRequires:	postgresql-test-rpm-macros
%endif

Patch: test_types_extras-2.9.3-test_from_tables.patch

%description
%{desc}

%package -n python3-psycopg2
Summary:	%{sum}

%description  -n python3-psycopg2
%{desc}

%package -n python3-%{srcname}-tests
Summary: A test suite for %{sum} 3
Requires: python3-%{srcname}%{?_isa} = %{version}-%{release}

%description -n python3-%{srcname}-tests
%{desc}
This package contains the test suite for psycopg2.

%package doc
Summary:	Documentation for psycopg python PostgreSQL database adapter
BuildArch:	noarch

%description doc
Documentation and example files for the psycopg python PostgreSQL
database adapter.

%prep
%oreon_sha256
%autosetup -N -n psycopg2-%{version}

%ifarch s390x s390
%patch -P 0 -p0
%endif

find tests -type f -name "*.py" -exec sed -i -e '/^#!\//d' {} +

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

sed -i '/better_theme_path/d' doc/src/conf.py
sed -i "/html_theme = 'better'/d" doc/src/conf.py

make html -C doc/src

find doc/src/_build/html -iname "*.html" -exec sed -i 's/\r//' {} +
find doc/src/_build/html -iname "*.css" -exec sed -i 's/\r//' {} +

rm -f doc/src/_build/html/.buildinfo

%check
%pyproject_check_import

%if %{with tests}
export PGTESTS_LOCALE=C.UTF-8
%postgresql_tests_run

export PSYCOPG2_TESTDB=${PGTESTS_DATABASES##*:}
export PSYCOPG2_TESTDB_HOST=$PGHOST
export PSYCOPG2_TESTDB_PORT=$PGPORT

cmd="import tests; tests.unittest.main(defaultTest='tests.test_suite')"

%py3_test_envvars %python3 -c "$cmd" --verbose
%endif

%install
%pyproject_install
%pyproject_save_files -l psycopg2

cp -r tests/ %{buildroot}%{python3_sitearch}/%{srcname}/tests/
%py3_shebang_fix %{buildroot}%{python3_sitearch}/%{srcname}/tests/

%files -n python3-psycopg2 -f %{pyproject_files}
%doc AUTHORS NEWS README.rst

%files -n python3-%{srcname}-tests
%license LICENSE
%doc README.rst
%{python3_sitearch}/psycopg2/tests

%files doc
%license LICENSE
%doc doc/src/_build/html

%changelog
%autochangelog
