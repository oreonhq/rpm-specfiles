%global source0_hash 26ac116722a241bf59daf5315ce0ffe751c1babea9a146ffc0a389f1af3facca

Summary:        Lua integration with libev
Name:           lua-ev
License:        MIT

Version:        1.5
Release:        11%{?dist}

URL:            https://github.com/brimworks/lua-ev
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libev-devel
BuildRequires:  lua-devel

%description
Event loop programming with Lua.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} 

%build
%cmake -DINSTALL_CMOD=%{lua_libdir}
%cmake_build

%install
%cmake_install 
ln -s README README.copy

%check
#packaged tests do not work directly
#Use example program as a smoke test
LUA_CPATH=%{buildroot}%{lua_libdir}/?.so \
lua example.lua
LUA_CPATH=%{buildroot}%{lua_libdir}/?.so \
lua -e 'ev = require "ev"; print(ev.version())'

%files
%license README
%doc example.lua
%doc README.copy
%{lua_libdir}/ev.so

%changelog
%autochangelog
