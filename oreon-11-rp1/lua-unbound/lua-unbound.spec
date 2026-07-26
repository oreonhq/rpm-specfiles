%global source0_hash 6de45aa64c21cf0ecbccb734b7c1eda8873a6135bbe142fbf353f772a90750d3

Summary:        Binding to libunbound for Lua
Name:           lua-unbound
Version:        1.0.0
Release:        12%{?dist}
License:        MIT
URL:            https://www.zash.se/luaunbound.html
Source0:        https://code.zash.se/dl/luaunbound/luaunbound-%{version}.tar.gz
Source1:        https://code.zash.se/dl/luaunbound/luaunbound-%{version}.tar.gz.asc
Source2:        gpgkey-3E52119EF853C59678DBBF6BADED9A77B67AD329.gpg
Requires:       lua(abi) = %{lua_version}
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  lua >= %{lua_version}
BuildRequires:  lua-devel >= %{lua_version}
BuildRequires:  unbound-devel

%description
Lua bindings for the Unbound APIs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q -n luaunbound-%{version}

%build
%make_build \
  LUA_VERSION=%{lua_version} \
  MYCFLAGS="$RPM_OPT_FLAGS" \
  MYLDFLAGS="$RPM_LD_FLAGS" \
  LD=%{__cc}

%install
%make_install LUA_LIBDIR=%{lua_libdir}

# Correct strange upstream file permission
chmod 755 %{buildroot}%{lua_libdir}/lunbound.so

%check
lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   local lunbound = require("lunbound");
   print("Hello from "..lunbound._LIBVER.."!");'

%files
%license LICENSE
%doc README.markdown
%{lua_libdir}/lunbound.so

%changelog
%autochangelog
