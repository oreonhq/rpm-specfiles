%global source0_hash e5f587804cced3d1842ce650ced101dd96894381241aa1f1c1cdfd3490b49bd2

%if %{defined rhel} || %{defined flatpak}
# CentOS/RHEL missing mysql-connector-python3
%bcond mysql_tests 0
%else
%ifarch %{ix86}
# mysql-connector-python3 isn't built for i686
# https://src.fedoraproject.org/rpms/mysql-connector-python/c/fc4b2fbfd138116c918f8ac74d6570dd27a41eb8?branch=rawhide
%bcond mysql_tests 0
%else
%bcond mysql_tests 1
%endif
%endif

%bcond postgres_tests 1

Name:           python-peewee
Version:        3.19.0
Release:        %autorelease
Summary:        A little orm

# main license is MIT
# playhouse/_pysqlite is Zlib
License:        MIT AND Zlib
URL:            https://github.com/coleifer/peewee
# PyPI tarball doesn't have tests
Source:         %{url}/archive/%{version}/peewee-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  sqlite-devel

# documentation
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

# tests
BuildRequires:  python3-apsw
%if %{with mysql_tests}
BuildRequires:  mysql-connector-python3
%endif
%if %{with postgres_tests}
BuildRequires:  python3-psycopg2
BuildRequires:  python3-psycopg3
BuildRequires:  postgresql-test-rpm-macros
BuildRequires:  postgresql-contrib
%endif

%global _description %{expand:
Peewee is a simple and small ORM. It has few (but expressive) concepts, making
it easy to learn and intuitive to use.}

%description %_description

%package -n python3-peewee
Summary:        %{summary}

%description -n python3-peewee %_description

%package docs
Summary:        Documentation for %{name}
Conflicts:      python3-peewee < 3.15.1-3

%description docs
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n peewee-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# Test suite requires an in-place build of the compiled extensions.
# https://github.com/coleifer/peewee/blob/3.15.2/.github/workflows/tests.yaml#L49
%{set_build_flags}
%{python3} %{py_setup} %{?py_setup_args} build_ext --inplace

# Build the documentation
sphinx-build docs html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l peewee playhouse pwiz

%check
%if %{with postgres_tests}
export PGTESTS_LOCALE="C.UTF-8"
%postgresql_tests_run
createdb peewee_test
psql -c "CREATE EXTENSION hstore" peewee_test
%endif
%{py3_test_envvars} %{python3} runtests.py

%files -n python3-peewee -f %{pyproject_files}
%doc README.rst CHANGELOG.md
%{_bindir}/pwiz

%files docs
%doc html

%changelog
%autochangelog
