%global source0_hash 86d17aea5080a90671d965cffeb9b104c19e0e1ea55c08687c0924c4512b52b1

%global forgeurl https://github.com/mascarenhas/cosmo
%global tag v%{version}

Name:      lua-cosmo
Version:   16.06.04
Release:   9%{?dist}
Summary:   Safe templates for Lua
License:   MIT
URL:       %{forgeurl}

%forgemeta
Source:    %{forgesource}

BuildArch:     noarch
Requires:      lua-lpeg
BuildRequires: lua-devel
BuildRequires: make

#Tests
BuildRequires: lua-lpeg

%description
Cosmo is a "safe templates" engine. It allows you to fill nested templates,
providing many of the advantages of Turing-complete template engines,
without without the downside of allowing arbitrary code in the templates.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
# Nothing to do here

%install
%make_install LUA_DIR=%{lua_pkgdir}

%check
LUA_PATH="%{buildroot}%{lua_pkgdir}/?.lua;%{buildroot}%{lua_pkgdir}/?/init.lua;;" \
lua tests/test_cosmo.lua

%files
%license doc/cosmo.md
%doc README
%doc samples
%doc doc/*
%{lua_pkgdir}/cosmo.lua
%{lua_pkgdir}/cosmo/

%changelog
%autochangelog
