%global source0_hash 1a3bd8e2229bbaada9b27d23cc3ac4cdf19418a3fc83dd7f4f176588d7520088
%global srcname readline
%bcond_with tests
Name:           lua-%{srcname}
Version:        3.3
Release:        1%{?dist}
Summary:        Lua interface to the readline and history libraries
License:        MIT
URL:            http://peterbillam.fastmail.com.user.fm/comp/lua/%{srcname}.html
Source0:        http://peterbillam.fastmail.com.user.fm/comp/lua/%{srcname}-%{version}.tar.gz
%if %{with tests}
%endif
Requires:       lua-posix
%if 0%{?el7}
%endif
%if 0%{?fedora} < 33 && 0%{?rhel} < 9 && 0%{?oreon} < 11
Requires:       lua(abi) = %{lua_version}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  lua-devel
BuildRequires:  lua-posix
BuildRequires:  readline-devel
# /oreon:deps
%description
This Lua module offers a simple calling interface to the GNU Readline/History
Library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build

%{__cc} %{optflags} %{?__global_ldflags} -fPIC \
  $(pkgconf --cflags --libs lua) $(pkgconf --cflags --libs readline) \
  -c C-%{srcname}.c
%{__cc} %{?__global_ldflags} -shared -o C-%{srcname}.so C-%{srcname}.o
%install
mkdir -p %{buildroot}%{lua_libdir}
mkdir -p %{buildroot}%{lua_pkgdir}
cp -p C-%{srcname}.so %{buildroot}%{lua_libdir}/
cp -p %{srcname}.lua %{buildroot}%{lua_pkgdir}/
%oreon_autofiles main

%check

lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   package.path="%{buildroot}%{lua_pkgdir}/?.lua;"..package.path;
   local RL = require("readline"); print("Hello from "..RL.Version.."!");'
%if %{with tests}
lua test/test_rl.lua
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
