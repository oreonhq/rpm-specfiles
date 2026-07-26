%global source0_hash 917e794c03ecef6b553f960739444f7e92ea62f35c33aeaa787655f4d5e10580

%global srcname	PyGreSQL
%global uversion 6.1.0

%{!?runselftest:%global runselftest 1}

Name:		%{srcname}
Version:	6.1.0
Release:	6%{?dist}
Summary:	Python client library for PostgreSQL

URL:		http://www.pygresql.org/
License:	PostgreSQL

Source0:	https://github.com/PyGreSQL/%{name}/archive/%{uversion}/%{name}-%{uversion}.tar.gz#/%{name}-%{uversion}.tar.gz

# Patch to remove overly strict version constraints on pip and virtualenv
# These constraints break builds on Fedora Rawhide where newer versions are used
Patch0:		tox.patch

BuildRequires:	gcc
BuildRequires:	libpq-devel
BuildRequires:	python3-devel
BuildRequires:  pyproject-rpm-macros

# For testsuite
%if 0%{?runselftest:1}
BuildRequires:	postgresql-test-rpm-macros
%endif

%global _description\
PostgreSQL is an advanced Object-Relational database management system.\
The PyGreSQL package provides a module for developers to use when writing\
Python code for accessing a PostgreSQL database.

%description %_description

%package -n python3-pygresql
Summary:	%summary
%{?python_provide:%python_provide python3-pygresql}
# Remove before F30
Provides: python3-PyGreSQL = %{uversion}-%{release}
Provides: python3-PyGreSQL%{?_isa} = %{uversion}-%{release}
Obsoletes: python3-PyGreSQL < %{uversion}-%{release}

%description -n python3-pygresql

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{uversion} -p1

%generate_buildrequires
%pyproject_buildrequires -t

# PyGreSQL releases have execute bits on all files
find -type f -exec chmod 644 {} +

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-pygresql
%license docs/copyright.rst
%license %{python3_sitearch}/pygresql-*.dist-info/licenses/LICENSE.txt
%doc docs/*.rst
%{python3_sitearch}/pg/*.so
%{python3_sitearch}/pg/*.py
%{python3_sitearch}/pg/__pycache__/*.py{c,o}
%{python3_sitearch}/pg/py.typed
%{python3_sitearch}/pg/_pg.pyi
%{python3_sitearch}/pgdb/*.py
%{python3_sitearch}/pgdb/__pycache__/*.py{c,o}
%{python3_sitearch}/pgdb/py.typed
%{python3_sitearch}/pygresql-*.dist-info/WHEEL
%{python3_sitearch}/pygresql-*.dist-info/INSTALLER
%{python3_sitearch}/pygresql-*.dist-info/METADATA
%{python3_sitearch}/pygresql-*.dist-info/top_level.txt

%check
%if %runselftest == 0
exit 0
%endif

%postgresql_tests_run

cat > LOCAL_PyGreSQL.py <<EOF
dbname = '${PGTESTS_DATABASES##*:}'
# Per https://mail.vex.net/mailman/private.cgi/pygresql/2017-July/003446.html
# advice to leave 'dbhost' empty.
dbhost = ''
dbport = $PGPORT
EOF

%tox

%changelog
%autochangelog
