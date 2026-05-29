%global source0_hash bb1a37d679522089f6dc3751669e3dbe51bd56922f959ef3ce2706939b775217

%bcond tests 1

%global srcname	psycopg2
%global sum	A PostgreSQL database adapter for Python
%global desc	Psycopg is the most popular PostgreSQL adapter for the Python \
programming language. At its core it fully implements the Python DB \
API 2.0 specifications. Several extensions allow access to many of the \
features offered by PostgreSQL.


Summary:	%{sum}
Name:		python-%{srcname}
Version:	2.9.10
Release:	5%{?dist}
# The exceptions allow linking to OpenSSL and PostgreSQL's libpq
License:	LGPL-3.0-or-later WITH openvpn-openssl-exception
Url:		https://www.psycopg.org/

Source:        https://github.com/psycopg/psycopg2/archive/2.9.10/psycopg2-2.9.10.tar.gz

BuildRequires:	python3-devel

BuildRequires:	gcc
BuildRequires:	libpq-devel
BuildRequires:	python-sphinx

# For testsuite
%if %{with tests}
BuildRequires:	postgresql-test-rpm-macros
%endif

# Remove test 'test_from_tables' for s390 architecture
# from ./tests/test_types_extras.py
Patch0: test_types_extras-2.9.3-test_from_tables.patch

%description
%{desc}


%package -n python3-psycopg2
Summary: %{sum} 3

%description  -n python3-psycopg2
%{desc}


%package -n python3-%{srcname}-tests
Summary: A testsuite for %sum 3
Requires: python3-%srcname = %version-%release

%description -n python3-%{srcname}-tests
%desc
This sub-package delivers set of tests for the adapter.


%package doc
Summary:	Documentation for psycopg python PostgreSQL database adapter
%py_provides python3-%{srcname}-doc

%description doc
Documentation and example files for the psycopg python PostgreSQL
database adapter.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n psycopg2-%{version}

# The patch is applied only for s390 architecture as 
# on other architectures the test works
%ifarch s390x s390
%patch -P0 -p0
%endif


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# Fix for wrong-file-end-of-line-encoding problem; upstream also must fix this.
for i in `find doc -iname "*.html"`; do sed -i 's/\r//' $i; done
for i in `find doc -iname "*.css"`; do sed -i 's/\r//' $i; done

# Get rid of a "hidden" file that rpmlint complains about
rm -f doc/html/.buildinfo

# We can not build docs now:
# https://www.postgresql.org/message-id/2741387.dvL6Cb0VMB@nb.usersys.redhat.com
# as the bug was sorted, we can build the documentation again

# Remove design formatting package
sed -i '/better_theme_path/d' doc/src/conf.py
sed -i "/html_theme = 'better'/d" doc/src/conf.py

make html -C doc/src


%check
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

# Upstream removed tests from the package so we need to add them manually
cp -r tests/ %{buildroot}%{python3_sitearch}/%{srcname}/tests/
%py3_shebang_fix %{buildroot}%{python3_sitearch}/%{srcname}/tests/


%files -n python3-psycopg2 -f %{pyproject_files}
%doc AUTHORS NEWS README.rst


%files -n python3-%{srcname}-tests
%{python3_sitearch}/psycopg2/tests


%files doc
%license LICENSE
%doc doc/src/_build/html


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.9.10-5
- Prepare for Oreon 11 (RP1)
