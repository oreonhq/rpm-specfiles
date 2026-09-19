%global source0_hash cb8c4f09d55d422bf19359e66b67678b2978dd67c713ae68373899ecf2bf8f8c

# fallback for EPEL
%{!?lua_version: %global lua_version %{lua: print(string.sub(_VERSION, 5))}}
%{!?lua_libdir: %global lua_libdir %{_libdir}/lua/%{lua_version}}
Name:           lua-ldap
Version:        1.4.0
Release:        3%{?dist}
Summary:        LDAP client library for Lua, using OpenLDAP
License:        MIT
URL:            https://lualdap.github.io/lualdap/
Source0:        https://github.com/lualdap/lualdap/archive/v%{version}/lualdap-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  lua-devel >= %{lua_version}
BuildRequires:  openldap-devel
BuildRequires:  lua >= %{lua_version}
%if 0%{?rhel} && 0%{?rhel} < 9
Requires:       lua(abi) = %{lua_version}
%endif
%if 0%{?rhel} == 7
BuildRequires:  lua-rpm-macros
%endif

%description
LuaLDAP is a simple interface from Lua to an LDAP client. It enables a Lua 
program to:
* Connect to an LDAP server;
* Execute any operation (search, add, compare, delete, modify and rename);
* Retrieve entries and references of the search result.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n lualdap-%{version}
sed -i -e 's/-DLUA_USE_C89//' -e 's/-std=c89//' Makefile

%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags} -fPIC" LUA_LIBDIR=%{_libdir} LUA_INCDIR=%{_includedir}

%check
lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   local lualdap = require("lualdap"); print("Hello from "..lualdap._VERSION.."!");'

%install
%make_install INST_LIBDIR=%{lua_libdir}

%files
%doc README.md docs/[cmn]*.md
%license docs/license.md
%{lua_libdir}/lualdap.so*

%changelog
%autochangelog
