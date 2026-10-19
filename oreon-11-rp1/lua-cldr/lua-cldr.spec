%global source0_hash bf38132c274a35b500787668fd561302374c6687333ff8be0c6751ad35151399
%global forgeurl https://github.com/alerque/cldr-lua
%global tag v%{version}
Name:      lua-cldr
Version:   0.3.0
Release:        1%{?dist}
Summary:        Lua interface to Unicode CLDR data
License:   MIT AND ICU
URL:       %{forgeurl}
%forgemeta
Source0:        %{forgeurl}/archive/%{tag}/cldr-lua-%{version}.tar.gz
BuildArch:     noarch
Requires:      lua-penlight
# oreon:deps
BuildRequires:  lua-devel
BuildRequires:  lua-penlight
# /oreon:deps
%description
Unicode CLDR (Common Locale Data Repository) data and Lua interface.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build

%install
install -dD %{buildroot}%{lua_pkgdir}
cp -av cldr/ %{buildroot}%{lua_pkgdir}
%oreon_autofiles main

%check

LUA_PATH="%{buildroot}%{lua_pkgdir}/?.lua;%{buildroot}%{lua_pkgdir}/?/init.lua;;" \
lua -e 'local CLDR = require("cldr")
print(#CLDR.locales)
assert(#CLDR.locales > 100)'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
