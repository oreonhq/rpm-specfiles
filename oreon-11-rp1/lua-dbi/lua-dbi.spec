%global source0_hash d11990029946cf29ee33cdb563900ba8e105207c507b08887896e88e429d8429
%{!?lua_compat_version: %global lua_compat_version 5.1}
%{!?lua_compat_libdir: %global lua_compat_libdir %{_libdir}/lua/%{lua_compat_version}}
%{!?lua_compat_pkgdir: %global lua_compat_pkgdir %{_datadir}/lua/%{lua_compat_version}}
%{!?lua_compat_builddir: %global lua_compat_builddir %{_builddir}/compat-lua-%{name}-%{version}-%{release}}
Summary:        Database interface library for Lua
Name:           lua-dbi
Version:        0.7.5
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/mwild1/luadbi
Source0:        https://github.com/mwild1/luadbi/archive/v%{version}/luadbi-%{version}.tar.gz
Requires:       lua(abi) = %{lua_version}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libpq-devel
BuildRequires:  lua
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  sqlite-devel
# /oreon:deps
%description
LuaDBI is a database interface library for Lua. It is designed to provide a
RDBMS agnostic API for handling database operations. LuaDBI also provides
support for prepared statement handles, placeholders and bind parameters for
all database operations.

Currently LuaDBI supports DB2, Oracle, MySQL, PostgreSQL and SQLite databases
with native database drivers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir luadbi-%{version}
%oreon_prep
%build

%make_build mysql psql sqlite3 \
  CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" \
  LUA_V=%{lua_version} LUA_INC="-I%{_includedir}" \
  MYSQL_LDFLAGS="-L%{_libdir}/mysql -lmysqlclient"
%install
make install_lua install_mysql install_psql install_sqlite3 INSTALL='install -p' \
  CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" \
  LUA_V=%{lua_version} LUA_INC="-I%{_includedir}" \
  LUA_CDIR=$RPM_BUILD_ROOT%{lua_libdir} LUA_LDIR=$RPM_BUILD_ROOT%{lua_pkgdir} \
  MYSQL_LDFLAGS="-L%{_libdir}/mysql -lmysqlclient"
%oreon_autofiles main

%check

lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   package.path="%{buildroot}%{lua_pkgdir}/?.lua;"..package.path;
   local DBI = require("DBI"); print("Hello from "..DBI._VERSION.."!");'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
