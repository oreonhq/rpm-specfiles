%global source0_hash 98fcf86d47694c81ccf9012e310f86d443ddf516e90b267ea33eb7ff1b0747c4
%bcond tests 0
%global pkgname moonscript
Name:           lua-%{pkgname}
Version:        0.7.0
Release:        1%{?dist}
Summary:        A little language that compiles to Lua
License:        MIT
URL:            http://moonscript.org/
Source0:        https://github.com/leafo/%{pkgname}/archive/v%{version}.tar.gz#/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       /usr/bin/lua
Requires:       lua-argparse >= 0.7
Requires:       lua-filesystem >= 1.5
Requires:       lua-lpeg >= 0.12
Recommends:     lua-inotify
# oreon:deps
BuildRequires:  lua-argparse
BuildRequires:  lua-devel
BuildRequires:  lua-filesystem
BuildRequires:  lua-lpeg
BuildRequires:  make
# /oreon:deps
%description
MoonScript is a dynamic scripting language that compiles into Lua. It
gives you the power of Lua combined with a rich set of features.

MoonScript can either be compiled into Lua and run at a later time, or
it can be dynamically compiled and run using the moonloader. It’s as
simple as require "moonscript" in order to have Lua understand how to
load and run any MoonScript file.

Because it compiles right into Lua code, it is completely compatible
with alternative Lua implementations like LuaJIT, and it is also
compatible with all existing Lua code and libraries.

The command line tools also let you run MoonScript directly from the
command line, like any first-class scripting language.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkgname}-%{version}
chmod +x bin/moonc

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -p bin/moon{,c,-tags} $RPM_BUILD_ROOT%{_bindir}/
mkdir -p $RPM_BUILD_ROOT%{lua_pkgdir}
cp -pr moon moonscript $RPM_BUILD_ROOT%{lua_pkgdir}/
%oreon_autofiles main

%check

%if %{with tests}
make test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
