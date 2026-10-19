%global source0_hash cc1cdb4047edd056a10dcdeec853dbaf5088e2202941d579e4592584d733f09c
%global forgeurl https://github.com/hoelzro/lua-linenoise
%global tag %{version}
%forgemeta
Name:      lua-linenoise
Version:   0.9
Release:        1%{?dist}
Summary:        A binding for the linenoise command line library
License:   MIT AND BSD-2-Clause
URL:       %{forgeurl}
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
Provides: bundled(linenoise)
Provides: bundled(linenoise-utf8)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  lua-devel
# /oreon:deps
%description
Linenoise (https://github.com/antirez/linenoise) is a delightfully simple
command line library. This Lua module is simply a binding for it.

The main Linenoise upstream has stagnated a bit, so this binding tracks
https://github.com/yhirose/linenoise/tree/utf8-support, which includes things
like UTF-8 support and ANSI terminal escape sequence detection.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build

%{__cc} %{optflags} %{?__global_ldflags} -fPIC -c -o linenoise.o linenoise.c
%{__cc} %{optflags} %{?__global_ldflags} -fPIC -c -o encodings/utf8.o encodings/utf8.c
%{__cc} %{optflags} %{?__global_ldflags} -fPIC -c -o linenoiselib.o linenoiselib.c
%{__cc} %{?__global_ldflags} -shared -o linenoise.so linenoise.o encodings/utf8.o linenoiselib.o
%install
install -dD %{buildroot}%{lua_libdir}
install -p -m 755 linenoise.so %{buildroot}%{lua_libdir}/
%oreon_autofiles main

%check

LUA_CPATH=%{buildroot}%{lua_libdir}/linenoise.so \
lua -e 'local L = require "linenoise"; L.enableutf8();'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
