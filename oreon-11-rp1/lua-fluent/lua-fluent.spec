%global source0_hash 2458b80c8dad59c86de459bb7b4deef285d196b54ab449e73a8b8814f9822633

%global forgeurl https://github.com/alerque/fluent-lua
%global tag v%{version}

Name:      lua-fluent
Version:   0.2.0
Release:   8%{?dist}
Summary:   Lua implementation of Project Fluent
License:   MIT
URL:       %{forgeurl}

%forgemeta
Source:    %{forgesource}

BuildArch:     noarch
BuildRequires: lua-devel
Requires:      lua-cldr
Requires:      lua-epnf
Requires:      lua-penlight

# Tests
BuildRequires: lua-cldr
BuildRequires: lua-epnf
BuildRequires: lua-penlight

%description
A Lua implementation of Project Fluent, a localization paradigm designed to
unleash the entire expressive power of natural language translations.
Fluent is a family of localization specifications, implementations and good
practices developed by Mozilla who extracted parts of their 'l20n' solution
(used in Firefox and other apps) into a re-usable specification.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
# Nothing to do here

%install
install -dD %{buildroot}%{lua_pkgdir}
cp -av fluent/ %{buildroot}%{lua_pkgdir}

%check
# Smoke test for now, missing dependency busted for test suite
LUA_PATH="%{buildroot}%{lua_pkgdir}/?.lua;%{buildroot}%{lua_pkgdir}/?/init.lua;;" \
lua -e '
local FluentBundle = require("fluent")
local bundle = FluentBundle()

bundle:add_messages([[
hello = Hello { $name }!
foo = bar
    .attr = baz
]])

print(bundle:format("foo"))
print(bundle:format("foo.attr"))
print(bundle:format("hello", { name = "World" }))
'

%files
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%{lua_pkgdir}/fluent/

%changelog
%autochangelog
