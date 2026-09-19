%global source0_hash d11990029946cf29ee33cdb563900ba8e105207c507b08887896e88e429d8429

%{!?lua_compat_version: %global lua_compat_version 5.1}
%{!?lua_compat_libdir: %global lua_compat_libdir %{_libdir}/lua/%{lua_compat_version}}
%{!?lua_compat_pkgdir: %global lua_compat_pkgdir %{_datadir}/lua/%{lua_compat_version}}
%{!?lua_compat_builddir: %global lua_compat_builddir %{_builddir}/compat-lua-%{name}-%{version}-%{release}}

Summary:        Database interface library for Lua
Name:           lua-dbi
Version:        0.7.5
Release:        2%{?dist}
License:        MIT
URL:            https://github.com/mwild1/luadbi
Source0:        https://github.com/mwild1/luadbi/archive/v%{version}/luadbi-%{version}.tar.gz
Requires:       lua(abi) = %{lua_version}
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  lua >= %{lua_version}
BuildRequires:  lua-devel >= %{lua_version}
BuildRequires:  sqlite-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  libpq-devel

%description
LuaDBI is a database interface library for Lua. It is designed to provide a
RDBMS agnostic API for handling database operations. LuaDBI also provides
support for prepared statement handles, placeholders and bind parameters for
all database operations.

Currently LuaDBI supports DB2, Oracle, MySQL, PostgreSQL and SQLite databases
with native database drivers.

%if 0%{?fedora}
%package -n lua%{lua_compat_version}-dbi
Summary:        Database interface library for Lua %{lua_compat_version}
Obsoletes:      lua-dbi-compat < 0.7.2
Provides:       lua-dbi-compat = %{version}-%{release}
Provides:       lua-dbi-compat%{?_isa} = %{version}-%{release}
Requires:       lua(abi) = %{lua_compat_version}
BuildRequires:  compat-lua >= %{lua_compat_version}
BuildRequires:  compat-lua-devel >= %{lua_compat_version}

%description -n lua%{lua_compat_version}-dbi
LuaDBI is a database interface library for Lua %{lua_compat_version}. It is designed to provide
a RDBMS agnostic API for handling database operations. LuaDBI also provides
support for prepared statement handles, placeholders and bind parameters for
all database operations.

Currently LuaDBI supports DB2, Oracle, MySQL, PostgreSQL and SQLite databases
with native database drivers.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n luadbi-%{version} -p1

%if 0%{?fedora}
rm -rf %{lua_compat_builddir}
cp -a . %{lua_compat_builddir}
%endif

%build
%make_build mysql psql sqlite3 \
  CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" \
  LUA_V=%{lua_version} LUA_INC="-I%{_includedir}" \
  MYSQL_LDFLAGS="-L%{_libdir}/mysql -lmysqlclient"

%if 0%{?fedora}
pushd %{lua_compat_builddir}
%make_build mysql psql sqlite3 \
  CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" \
  LUA_V=%{lua_compat_version} LUA_INC="-I%{_includedir}/lua-%{lua_compat_version}" \
  MYSQL_LDFLAGS="-L%{_libdir}/mysql -lmysqlclient"
popd
%endif

%install
make install_lua install_mysql install_psql install_sqlite3 INSTALL='install -p' \
  CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" \
  LUA_V=%{lua_version} LUA_INC="-I%{_includedir}" \
  LUA_CDIR=$RPM_BUILD_ROOT%{lua_libdir} LUA_LDIR=$RPM_BUILD_ROOT%{lua_pkgdir} \
  MYSQL_LDFLAGS="-L%{_libdir}/mysql -lmysqlclient"

%if 0%{?fedora}
pushd %{lua_compat_builddir}
make install_lua install_mysql install_psql install_sqlite3 INSTALL='install -p' \
  CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" \
  LUA_V=%{lua_compat_version} LUA_INC="-I%{_includedir}/lua-%{lua_compat_version}" \
  LUA_CDIR=$RPM_BUILD_ROOT%{lua_compat_libdir} LUA_LDIR=$RPM_BUILD_ROOT%{lua_compat_pkgdir} \
  MYSQL_LDFLAGS="-L%{_libdir}/mysql -lmysqlclient"
popd
%endif

%check
lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   package.path="%{buildroot}%{lua_pkgdir}/?.lua;"..package.path;
   local DBI = require("DBI"); print("Hello from "..DBI._VERSION.."!");'

%if 0%{?fedora}
lua-%{lua_compat_version} -e \
  'package.cpath="%{buildroot}%{lua_compat_libdir}/?.so;"..package.cpath;
   package.path="%{buildroot}%{lua_compat_pkgdir}/?.lua;"..package.path;
   local DBI = require("DBI"); print("Hello from "..DBI._VERSION.."!");'
%endif

%files
%license COPYING
%doc README.md
%{lua_libdir}/dbd/
%{lua_pkgdir}/DBI.lua

%if 0%{?fedora}
%files -n lua%{lua_compat_version}-dbi
%license COPYING
%doc README.md
%{lua_compat_libdir}/dbd/
%{lua_compat_pkgdir}/DBI.lua
%endif

%changelog
%autochangelog
