%global source0_hash none

Name:           python-sqlalchemy
Version:        2.0.54
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Database Abstraction Library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://docs.sqlalchemy.org
Source:         %{pypi_source sqlalchemy}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sqlalchemy' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-sqlalchemy
Summary:        %{summary}

%description -n python3-sqlalchemy %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-sqlalchemy aiomysql,aioodbc,aiosqlite,asyncio,asyncmy,mariadb-connector,mssql,mssql-pymssql,mssql-pyodbc,mypy,mysql,mysql-connector,oracle,oracle-oracledb,postgresql,postgresql-asyncpg,postgresql-pg8000,postgresql-psycopg,postgresql-psycopg2binary,postgresql-psycopg2cffi,postgresql-psycopgbinary,pymysql,sqlcipher


%prep
%autosetup -p1 -n sqlalchemy-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x aiomysql,aioodbc,aiosqlite,asyncio,asyncmy,mariadb-connector,mssql,mssql-pymssql,mssql-pyodbc,mypy,mysql,mysql-connector,oracle,oracle-oracledb,postgresql,postgresql-asyncpg,postgresql-pg8000,postgresql-psycopg,postgresql-psycopg2binary,postgresql-psycopg2cffi,postgresql-psycopgbinary,pymysql,sqlcipher


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-sqlalchemy -f %{pyproject_files}

%changelog
%autochangelog
