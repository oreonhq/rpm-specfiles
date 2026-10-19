%global source1_hash 33a8a65f4659341c09148adffc2657aa9901e2c0d14cba6e63abaaaf124e76d1
%global source0_hash 39742dd5db94f13886810cf69fc9b3db89bba3180c060384136115c9da431196
%global forgeurl https://github.com/leafo/loadkit
%global tag v%{version}
Name:      lua-loadkit
Version:   1.1.0
Release:        1%{?dist}
Summary:        Loadkit allows you to load arbitrary files within the Lua package path
License:   MIT
URL:       %{forgeurl}
%forgemeta
Source0:        %{forgeurl}/archive/%{tag}/loadkit-%{version}.tar.gz
Source1:   https://github.com/leafo/loadkit/raw/95b13a36442f59b41ab52df96d52233c4a725dfd/LICENSE
BuildArch:     noarch
# oreon:deps
BuildRequires:  lua-devel
# /oreon:deps
%description
Loadkit lets you register new file extension handlers that can be opened
with require, or you can just search for files of any extension using the
current search path.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

cp %{SOURCE1} .

%build

%install
install -dD %{buildroot}%{lua_pkgdir}
install -p -m 644 loadkit.lua %{buildroot}%{lua_pkgdir}
%oreon_autofiles main

%check

LUA_PATH=%{buildroot}%{lua_pkgdir}/loadkit.lua \
lua -e 'local loadkit = require "loadkit"; assert(not loadkit.is_registered("test"))'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
