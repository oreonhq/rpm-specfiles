%global source0_hash e01ed713311cab131c92154b61a326ec8bf17aaed2a84a58e0b270a8efca2d50

%global forgeurl https://github.com/luarocks/argparse
%global tag %{version}
%global extractdir argparse-412e6aca393e365f92c0315dfe50181b193f1ace
%global archivename lua-argparse-%{version}

Name:           lua-argparse
Version:        0.7.1
Release:        7%{?dist}
Summary:        Feature-rich command line parser for Lua

License:        MIT
URL:            %{forgeurl}

%forgemeta
Source0:        %{forgesource}

BuildArch:      noarch
BuildRequires:  lua-devel

%description
Argparse is a feature-rich command line parser for Lua inspired by argparse
for Python.

Argparse supports positional arguments, options, flags, optional arguments,
subcommands and more. Argparse automatically generates usage, help and error
messages.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
Requires:       python3-sphinx_rtd_theme

%description    doc
This package contains documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
sphinx-build-3 -b html docsrc doc

%install
install -m 644 -D -p src/argparse.lua %{buildroot}%{lua_pkgdir}/argparse.lua

%check
# Smoke test for now
LUA_PATH="%{buildroot}%{lua_pkgdir}/?.lua;%{buildroot}%{lua_pkgdir}/?/init.lua" \
lua -e 'local argparse = require "argparse"
local parser = argparse()
assert(#parser == 0)'

%files
%license LICENSE
%doc README.md
%doc CHANGELOG.md
%{lua_pkgdir}/argparse.lua

%files doc
%license LICENSE
%doc doc/*

%changelog
%autochangelog
