%global source0_hash 666482b6ed1d4ca4317db2345c46dc0fc54a39c8cfd14e34f1a83595864b0ae4

Name:           lua-sql
Version:        2.5.0
Release:        15%{?dist}
Summary:        Database connectivity for the Lua programming language

License:        MIT
URL:            https://keplerproject.github.io/luasql/
Source0:        https://github.com/keplerproject/luasql/archive/%{version}.tar.gz#/luasql-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  lua-devel >= 5.1
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel >= 3.0
BuildRequires:  mariadb-connector-c-devel openssl-devel
BuildRequires:  libpq-devel
BuildRequires: make

Requires:       lua-sql-mysql%{?_isa} = %{version}-%{release}
Requires:       lua-sql-postgresql%{?_isa} = %{version}-%{release}
Requires:       lua-sql-sqlite%{?_isa} = %{version}-%{release}

%description
LuaSQL is a simple interface from Lua to a DBMS. This package of LuaSQL
supports MySQL, SQLite and PostgreSQL databases. You can execute arbitrary SQL
statements and it allows for retrieving results in a row-by-row cursor fashion.

%package doc
Summary:        Documentation for LuaSQL
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
LuaSQL is a simple interface from Lua to a DBMS. This package contains the
documentation for LuaSQL.

%package sqlite
Summary:        SQLite database connectivity for the Lua programming language

%description sqlite
LuaSQL is a simple interface from Lua to a DBMS. This package provides access
to SQLite databases.

%package mysql
Summary:        MySQL database connectivity for the Lua programming language

%description mysql
LuaSQL is a simple interface from Lua to a DBMS. This package provides access
to MySQL databases.

%package postgresql
Summary:        PostgreSQL database connectivity for the Lua programming language

%description postgresql
LuaSQL is a simple interface from Lua to a DBMS. This package provides access
to PostgreSQL databases.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n luasql-%{version} -p1

%build
make %{?_smp_mflags} sqlite3 PREFIX=%{_prefix} DRIVER_INCS_sqlite3="`pkg-config --cflags sqlite3`" DRIVER_LIBS_sqlite3="`pkg-config --libs sqlite3`" DEFS="%{optflags} -fPIC -std=c99 -DLUA_COMPAT_APIINTCASTS"
make %{?_smp_mflags} postgres PREFIX=%{_prefix} DRIVER_INCS_postgres="" DRIVER_LIBS_postgres="-lpq" DEFS="%{optflags} -fPIC -std=c99 -DLUA_COMPAT_APIINTCASTS" WARN=
make %{?_smp_mflags} mysql PREFIX=%{_prefix} DRIVER_INCS_mysql="`mysql_config --include`" DRIVER_LIBS_mysql="`mysql_config --libs`" DEFS="%{optflags} -fPIC -std=c99 -DLUA_COMPAT_APIINTCASTS"

%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix} LUA_LIBDIR=$RPM_BUILD_ROOT%{lua_libdir} LUA_DIR=$RPM_BUILD_ROOT%{lua_pkgdir} T=sqlite3
make install PREFIX=$RPM_BUILD_ROOT%{_prefix} LUA_LIBDIR=$RPM_BUILD_ROOT%{lua_libdir} LUA_DIR=$RPM_BUILD_ROOT%{lua_pkgdir} T=postgres
make install PREFIX=$RPM_BUILD_ROOT%{_prefix} LUA_LIBDIR=$RPM_BUILD_ROOT%{lua_libdir} LUA_DIR=$RPM_BUILD_ROOT%{lua_pkgdir} T=mysql

%files
%license doc/us/license.html doc/us/doc.css doc/us/luasql.png
%doc README

%files doc
%doc doc/us/*

%files mysql
%dir %{lua_libdir}/luasql
%{lua_libdir}/luasql/mysql.so

%files postgresql
%dir %{lua_libdir}/luasql
%{lua_libdir}/luasql/postgres.so

%files sqlite
%dir %{lua_libdir}/luasql
%{lua_libdir}/luasql/sqlite3.so

%changelog
%autochangelog
