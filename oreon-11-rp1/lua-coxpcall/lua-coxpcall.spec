%global source0_hash 6044f70fcc01f50cae3a191cba13c252dcf9e6f169502e3d9c4a151934c46be0

%global         gittag %(v=%{version}; echo ${v//./_})
%global         forgeurl https://github.com/keplerproject/coxpcall
Summary:        Coroutine safe xpcall and pcall versions for Lua
Name:           lua-coxpcall
License:        MIT

Version:        1.17.0
Release:        11%{?dist}

URL:            http://keplerproject.github.io/coxpcall/ 
Source0:        %{forgeurl}/archive/v%{gittag}/coxpcall-v%{gittag}.tar.gz

BuildArch:      noarch
BuildRequires:  lua-devel

%description
Coxpcall encapsulates the protected calls with a coroutine based loop,
so errors can be handled without the usual pcall/xpcall issues with 
coroutines for Lua 5.1.

Using Coxpcall usually consists in simply loading the module and then 
replacing Lua pcall and xpcall by copcall and coxpcall.

Coxpcall is free software and uses the same license as Lua 5.1.

Lua 5.2 was extended with the Coxpcall functionality and hence it 
is no longer required. The 5.2+ compatibility by coxpcall means 
that it maintains backward compatibility while using the built-in 
Lua implementation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n coxpcall-%{gittag} 

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{lua_pkgdir}/
cp -p src/coxpcall.lua %{buildroot}%{lua_pkgdir}/

%check
lua tests/test.lua

%files
%doc README.md
%doc doc/coxpcall.png
%doc doc/doc.css
%doc doc/index.html  
%license doc/license.html
%{lua_pkgdir}/coxpcall.lua

%changelog
%autochangelog
