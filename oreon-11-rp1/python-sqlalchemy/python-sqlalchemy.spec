%global source0_hash fcf3cbb33bb23bad75d2150157c21804618745731e9931ab27e61879a9f6123b
Name:           python-sqlalchemy
Version:        2.1.1
Release:        1%{?dist}
Summary:        Database Abstraction Library
License:        MIT
URL:            https://docs.sqlalchemy.org
Source0:        https://files.pythonhosted.org/packages/source/s/sqlalchemy/sqlalchemy-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.3
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-sqlalchemy = %{version}-%{release}
# /oreon:deps
%package -n       python3-sqlalchemy+asyncio
Summary:        Metapackage for python3-sqlalchemy asyncio extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Requires:       python3dist(greenlet) >= 1
Provides:       python3dist(sqlalchemy[asyncio]) = %{version}-%{release}

%description -n python3-sqlalchemy+asyncio
Metapackage for python3-sqlalchemy asyncio extras.

%package -n       python3-sqlalchemy+mypy
Summary:        Metapackage for python3-sqlalchemy mypy extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Requires:       python3dist(mypy) >= 2.3
Requires:       python3dist(types-greenlet) >= 2
Provides:       python3dist(sqlalchemy[mypy]) = %{version}-%{release}

%description -n python3-sqlalchemy+mypy
Metapackage for python3-sqlalchemy mypy extras.

%package -n       python3-sqlalchemy+mssql
Summary:        Metapackage for python3-sqlalchemy mssql extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Provides:       python3dist(sqlalchemy[mssql]) = %{version}-%{release}

%description -n python3-sqlalchemy+mssql
Metapackage for python3-sqlalchemy mssql extras.

%package -n       python3-sqlalchemy+mssql-pymssql
Summary:        Metapackage for python3-sqlalchemy mssql-pymssql extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Provides:       python3dist(sqlalchemy[mssql-pymssql]) = %{version}-%{release}

%description -n python3-sqlalchemy+mssql-pymssql
Metapackage for python3-sqlalchemy mssql-pymssql extras.

%package -n       python3-sqlalchemy+mssql-pyodbc
Summary:        Metapackage for python3-sqlalchemy mssql-pyodbc extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Provides:       python3dist(sqlalchemy[mssql-pyodbc]) = %{version}-%{release}

%description -n python3-sqlalchemy+mssql-pyodbc
Metapackage for python3-sqlalchemy mssql-pyodbc extras.

%package -n       python3-sqlalchemy+mssql-python
Summary:        Metapackage for python3-sqlalchemy mssql-python extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Requires:       python3dist(mssql-python) >= 1.9.0
Provides:       python3dist(sqlalchemy[mssql-python]) = %{version}-%{release}

%description -n python3-sqlalchemy+mssql-python
Metapackage for python3-sqlalchemy mssql-python extras.

%package -n       python3-sqlalchemy+mysql
Summary:        Metapackage for python3-sqlalchemy mysql extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Requires:       python3dist(mysqlclient) >= 1.4.0
Provides:       python3dist(sqlalchemy[mysql]) = %{version}-%{release}

%description -n python3-sqlalchemy+mysql
Metapackage for python3-sqlalchemy mysql extras.

%package -n       python3-sqlalchemy+mysql-connector
Summary:        Metapackage for python3-sqlalchemy mysql-connector extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Provides:       python3dist(sqlalchemy[mysql-connector]) = %{version}-%{release}

%description -n python3-sqlalchemy+mysql-connector
Metapackage for python3-sqlalchemy mysql-connector extras.

%package -n       python3-sqlalchemy+mariadb-connector
Summary:        Metapackage for python3-sqlalchemy mariadb-connector extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Requires:       python3dist(mariadb) >= 1.0.1
Provides:       python3dist(sqlalchemy[mariadb-connector]) = %{version}-%{release}

%description -n python3-sqlalchemy+mariadb-connector
Metapackage for python3-sqlalchemy mariadb-connector extras.

%package -n       python3-sqlalchemy+oracle
Summary:        Metapackage for python3-sqlalchemy oracle extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Requires:       python3dist(oracledb) >= 2.0.1
Provides:       python3dist(sqlalchemy[oracle]) = %{version}-%{release}

%description -n python3-sqlalchemy+oracle
Metapackage for python3-sqlalchemy oracle extras.

%package -n       python3-sqlalchemy+oracle-cxoracle
Summary:        Metapackage for python3-sqlalchemy oracle-cxoracle extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Requires:       python3dist(cx-oracle) >= 8
Provides:       python3dist(sqlalchemy[oracle-cxoracle]) = %{version}-%{release}

%description -n python3-sqlalchemy+oracle-cxoracle
Metapackage for python3-sqlalchemy oracle-cxoracle extras.

%package -n       python3-sqlalchemy+oracle-oracledb
Summary:        Metapackage for python3-sqlalchemy oracle-oracledb extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Requires:       python3dist(oracledb) >= 2.0.1
Provides:       python3dist(sqlalchemy[oracle-oracledb]) = %{version}-%{release}

%description -n python3-sqlalchemy+oracle-oracledb
Metapackage for python3-sqlalchemy oracle-oracledb extras.

%package -n       python3-sqlalchemy+postgresql
Summary:        Metapackage for python3-sqlalchemy postgresql extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Requires:       python3dist(psycopg) >= 3.0.7
Provides:       python3dist(sqlalchemy[postgresql]) = %{version}-%{release}

%description -n python3-sqlalchemy+postgresql
Metapackage for python3-sqlalchemy postgresql extras.

%package -n       python3-sqlalchemy+postgresql-pg8000
Summary:        Metapackage for python3-sqlalchemy postgresql-pg8000 extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Requires:       python3dist(pg8000) >= 1.29.3
Provides:       python3dist(sqlalchemy[postgresql-pg8000]) = %{version}-%{release}

%description -n python3-sqlalchemy+postgresql-pg8000
Metapackage for python3-sqlalchemy postgresql-pg8000 extras.

%package -n       python3-sqlalchemy+postgresql-asyncpg
Summary:        Metapackage for python3-sqlalchemy postgresql-asyncpg extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Provides:       python3dist(sqlalchemy[postgresql-asyncpg]) = %{version}-%{release}

%description -n python3-sqlalchemy+postgresql-asyncpg
Metapackage for python3-sqlalchemy postgresql-asyncpg extras.

%package -n       python3-sqlalchemy+postgresql-psycopg2binary
Summary:        Metapackage for python3-sqlalchemy postgresql-psycopg2binary extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Provides:       python3dist(sqlalchemy[postgresql-psycopg2binary]) = %{version}-%{release}

%description -n python3-sqlalchemy+postgresql-psycopg2binary
Metapackage for python3-sqlalchemy postgresql-psycopg2binary extras.

%package -n       python3-sqlalchemy+postgresql-psycopg2cffi
Summary:        Metapackage for python3-sqlalchemy postgresql-psycopg2cffi extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Provides:       python3dist(sqlalchemy[postgresql-psycopg2cffi]) = %{version}-%{release}

%description -n python3-sqlalchemy+postgresql-psycopg2cffi
Metapackage for python3-sqlalchemy postgresql-psycopg2cffi extras.

%package -n       python3-sqlalchemy+postgresql-psycopg
Summary:        Metapackage for python3-sqlalchemy postgresql-psycopg extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Requires:       python3dist(psycopg) >= 3.0.7
Provides:       python3dist(sqlalchemy[postgresql-psycopg]) = %{version}-%{release}

%description -n python3-sqlalchemy+postgresql-psycopg
Metapackage for python3-sqlalchemy postgresql-psycopg extras.

%package -n       python3-sqlalchemy+postgresql-psycopgbinary
Summary:        Metapackage for python3-sqlalchemy postgresql-psycopgbinary extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Requires:       python3dist(psycopg[binary]) >= 3.0.7
Provides:       python3dist(sqlalchemy[postgresql-psycopgbinary]) = %{version}-%{release}

%description -n python3-sqlalchemy+postgresql-psycopgbinary
Metapackage for python3-sqlalchemy postgresql-psycopgbinary extras.

%package -n       python3-sqlalchemy+pymysql
Summary:        Metapackage for python3-sqlalchemy pymysql extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Provides:       python3dist(sqlalchemy[pymysql]) = %{version}-%{release}

%description -n python3-sqlalchemy+pymysql
Metapackage for python3-sqlalchemy pymysql extras.

%package -n       python3-sqlalchemy+cymysql
Summary:        Metapackage for python3-sqlalchemy cymysql extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Provides:       python3dist(sqlalchemy[cymysql]) = %{version}-%{release}

%description -n python3-sqlalchemy+cymysql
Metapackage for python3-sqlalchemy cymysql extras.

%package -n       python3-sqlalchemy+aiomysql
Summary:        Metapackage for python3-sqlalchemy aiomysql extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Provides:       python3dist(sqlalchemy[aiomysql]) = %{version}-%{release}

%description -n python3-sqlalchemy+aiomysql
Metapackage for python3-sqlalchemy aiomysql extras.

%package -n       python3-sqlalchemy+aioodbc
Summary:        Metapackage for python3-sqlalchemy aioodbc extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Provides:       python3dist(sqlalchemy[aioodbc]) = %{version}-%{release}

%description -n python3-sqlalchemy+aioodbc
Metapackage for python3-sqlalchemy aioodbc extras.

%package -n       python3-sqlalchemy+asyncmy
Summary:        Metapackage for python3-sqlalchemy asyncmy extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Requires:       python3dist(asyncmy) >= 0.2.12
Provides:       python3dist(sqlalchemy[asyncmy]) = %{version}-%{release}

%description -n python3-sqlalchemy+asyncmy
Metapackage for python3-sqlalchemy asyncmy extras.

%package -n       python3-sqlalchemy+aiosqlite
Summary:        Metapackage for python3-sqlalchemy aiosqlite extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Provides:       python3dist(sqlalchemy[aiosqlite]) = %{version}-%{release}

%description -n python3-sqlalchemy+aiosqlite
Metapackage for python3-sqlalchemy aiosqlite extras.

%package -n       python3-sqlalchemy+sqlcipher
Summary:        Metapackage for python3-sqlalchemy sqlcipher extras
Requires:       python3-sqlalchemy = %{version}-%{release}
Provides:       python3dist(sqlalchemy[sqlcipher]) = %{version}-%{release}

%description -n python3-sqlalchemy+sqlcipher
Metapackage for python3-sqlalchemy sqlcipher extras.

%description

%package -n     python3-sqlalchemy
Summary:        Database Abstraction Library
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 4.6.0
# /oreon:reqs
%description -n python3-sqlalchemy

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sqlalchemy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sqlalchemy usr/lib/python3*/site-packages/sqlalchemy* usr/lib64/python3*/site-packages/sqlalchemy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sqlalchemy* usr/lib64/python3*/site-packages/sqlalchemy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sqlalchemy -f %{oreon_filedir}/python3-sqlalchemy.list

%changelog

%autochangelog
