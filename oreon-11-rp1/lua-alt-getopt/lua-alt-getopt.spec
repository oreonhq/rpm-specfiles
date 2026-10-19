%global source0_hash 5cce2fa9342c096303e16bba6144c592294db0103c72ae4936159c4f2df33170
Name:           lua-alt-getopt
Version:        0.8.0
Release:        1%{?dist}
Summary:        Argument processing module for Lua
License:        MIT
URL:            https://github.com/cheusov/lua-alt-getopt
Source0:        https://github.com/cheusov/lua-alt-getopt/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       lua(abi) = %{lua_version}
# oreon:deps
BuildRequires:  lua-devel
# /oreon:deps
%description
alt-getopt is a module for Lua programming language for processing
application's arguments the same way BSD/GNU getopt_long(3) functions
do. The main goal is compatibility with SUS "Utility Syntax
Guidelines" guidelines 3-13.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
mkdir -p %{buildroot}%{lua_pkgdir}
cp -p alt_getopt.lua %{buildroot}%{lua_pkgdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
