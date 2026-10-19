%global source0_hash 8ff94f390ea9d98c734699373ca3b0ce500d651b2ab1cb8d7d2336fc5b79cded
%global luaminver 5.2
Name:           lua-term
Version:        0.08
Release:        1%{?dist}
Summary:        Terminal functions for Lua
License:        MIT
URL:            https://github.com/hoelzro/%{name}
Source0:        https://github.com/hoelzro/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       lua(abi) = %{lua_version}
Requires:       lua >= %{lua_version}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  lua-devel
# /oreon:deps
%description
Lua module for manipulating a terminal.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Lua is no longer installed by default. Grab Lua version for use in
# determining install locations.
%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}
# for compiled modules
%global lualibdir %{_libdir}/lua/%{luaver}
# for arch-independent modules
%global luapkgdir %{_datadir}/lua/%{luaver}

%setup -q

%build

%{__cc} %{optflags} -fPIC -c core.c -o core.o
%{__cc} %{__global_ldflags} -shared -o core.so core.o
chmod 755 core.so
%install
mkdir -p %{buildroot}%{luapkgdir}
cp -rp term  %{buildroot}%{luapkgdir}/
mkdir -p %{buildroot}%{lualibdir}/term
cp -p core.so %{buildroot}%{lualibdir}/term/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
