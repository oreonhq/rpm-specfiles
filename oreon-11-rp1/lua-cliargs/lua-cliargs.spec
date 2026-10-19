%global source0_hash 971d6f1440a55bdf9db581d4b2bcbf472a301d76f696a0d0ed9423957c7d176e
%global forgeurl https://github.com/amireh/lua_cliargs
%global tag v3.0-2
Name:      lua-cliargs
Version:   3.0.2
Release:        1%{?dist}
Summary:        A command-line argument parser
License:   MIT
URL:       %{forgeurl}
%forgemeta
Source0:        %{forgeurl}/archive/%{tag}/lua_cliargs-3.0-2.tar.gz
BuildArch:     noarch
# oreon:deps
BuildRequires:  lua-devel
# /oreon:deps
%description
This module adds support for accepting CLI arguments easily using multiple
notations and argument types.

cliargs allows you to define required, optional, and flag arguments.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build

%install
install -dD %{buildroot}%{lua_pkgdir}
cp -av src/. %{buildroot}%{lua_pkgdir}
%oreon_autofiles main

%check

LUA_PATH="%{buildroot}%{lua_pkgdir}/?.lua" \
lua examples/00_general.lua --version
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
