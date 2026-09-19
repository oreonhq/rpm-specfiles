%global source0_hash 971d6f1440a55bdf9db581d4b2bcbf472a301d76f696a0d0ed9423957c7d176e

%global forgeurl https://github.com/amireh/lua_cliargs
%global tag v3.0-2

Name:      lua-cliargs
Version:   3.0.2
Release:   9%{?dist}
Summary:   A command-line argument parser
License:   MIT
URL:       %{forgeurl}

%forgemeta
Source:    %{forgesource}

BuildArch:     noarch
BuildRequires: lua-devel

%description
This module adds support for accepting CLI arguments easily using multiple
notations and argument types.

cliargs allows you to define required, optional, and flag arguments.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
# Nothing to do here

%install
install -dD %{buildroot}%{lua_pkgdir}
cp -av src/. %{buildroot}%{lua_pkgdir}

%check
LUA_PATH="%{buildroot}%{lua_pkgdir}/?.lua" \
lua examples/00_general.lua --version

%files
%license LICENSE
%doc README.md
%doc UPGRADE.md
%{lua_pkgdir}/cliargs.lua
%{lua_pkgdir}/cliargs/

%changelog
%autochangelog
