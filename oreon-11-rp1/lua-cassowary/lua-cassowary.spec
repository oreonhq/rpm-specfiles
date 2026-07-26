%global source0_hash 20fe7309f59004ce59e6c65d69ed9993de907267fd0314fc224f40e017d59798

%global forgeurl https://github.com/sile-typesetter/cassowary.lua
%global tag v%{version}

Name:      lua-cassowary
Version:   2.3.2
Release:   9%{?dist}
Summary:   The cassowary constraint solver
License:   Apache-2.0
URL:       %{forgeurl}

%forgemeta
Source:    %{forgesource}

BuildArch:     noarch
Requires:      lua-penlight
BuildRequires: lua-devel

# Tests
BuildRequires: lua-penlight

%description
This is a Lua port of the Cassowary constraint solving toolkit.
It allows you to use Lua to solve algebraic equations and inequalities
and find the values of unknown variables which satisfy those inequalities.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
# Nothing to do here

%install
install -dD %{buildroot}%{lua_pkgdir}
cp -av cassowary/ %{buildroot}%{lua_pkgdir}

%check
# Smoke test for now, missing dependency busted for test suite
LUA_PATH="%{buildroot}%{lua_pkgdir}/?.lua;%{buildroot}%{lua_pkgdir}/?/init.lua;;" \
lua -e '
cassowary = require("cassowary")
local solver = cassowary.SimplexSolver();
local x = cassowary.Variable({ name = "x" });
local y = cassowary.Variable({ name = "y" });
solver:addConstraint(cassowary.Inequality(x, "<=", y))
solver:addConstraint(cassowary.Equation(y, cassowary.plus(x, 3)))
solver:addConstraint(cassowary.Equation(x, 10, cassowary.Strength.weak))
solver:addConstraint(cassowary.Equation(y, 10, cassowary.Strength.weak))
print("x = "..x.value)
print("y = "..y.value)
assert(x.value == 7 or x.value == 10)
assert(y.value == 10 or y.value == 13)'

%files
%license LICENSE
%doc README.md
%{lua_pkgdir}/cassowary/

%changelog
%autochangelog
