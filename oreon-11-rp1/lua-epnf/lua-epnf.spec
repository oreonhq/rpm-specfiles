%global source0_hash 57c0ad1917e45c5677bfed0f6122da2baff98117aba05a5e987a0238600f85f9

%global forgeurl https://github.com/siffiejoe/lua-luaepnf
%global tag v%{version}

Name:      lua-epnf
Version:   0.3
Release:   9%{?dist}
Summary:   Extended PEG Notation Format (easy grammars for LPeg)
License:   MIT
URL:       %{forgeurl}

%forgemeta
Source:    %{forgesource}

BuildArch:     noarch
Requires:      lua-lpeg
BuildRequires: lua-devel

#Tests
BuildRequires: lua-lpeg

%description
This Lua module provides sugar for writing grammars/parsers using
the LPeg library. It simplifies error reporting and AST building.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
# Nothing to do here

%install
install -dD %{buildroot}%{lua_pkgdir}
install -p -m 644 src/epnf.lua %{buildroot}%{lua_pkgdir}/epnf.lua

%check
cd tests
for test in *.lua; do
  lua $test
done

%files
%license README.md
%doc doc/readme.txt
%{lua_pkgdir}/epnf.lua

%changelog
%autochangelog
