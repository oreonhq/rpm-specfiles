%global source1_hash de5c7593a32a0a0e58890307b5f53a887eb0f0cfe1a8c44a6785d132de3e48b3
%global source0_hash 236159461ecc61d4cc7d3738a7adcf3680ba6f61ea6e1f8e18f2c9b5e3a90244
Summary:        Binding to libunbound for Lua
Name:           lua-unbound
Version:        1.1.0
Release:        1%{?dist}
License:        MIT
URL:            https://www.zash.se/luaunbound.html
Source0:        https://code.zash.se/dl/luaunbound/luaunbound-%{version}.tar.gz
Source1:        https://code.zash.se/dl/luaunbound/luaunbound-%{version}.tar.gz.asc
Source2:        gpgkey-3E52119EF853C59678DBBF6BADED9A77B67AD329.gpg
Requires:       lua(abi) = %{lua_version}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  lua
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  unbound-devel
# /oreon:deps
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
chmod 755 %{buildroot}%{lua_libdir}/lunbound.so
%oreon_autofiles main

%check

lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   local lunbound = require("lunbound");
   print("Hello from "..lunbound._LIBVER.."!");'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
