%global source0_hash a3d0159bcf996f3c73ac20d6168d2aaedcd6877df8f7ae6a1994010ad8492784
Summary:        Pure Lua timerwheel implementation
Name:           lua-timerwheel
License:        MIT
Version:        1.0.2
Release:        1%{?dist}
URL:            https://github.com/Tieske/timerwheel.lua
Source0:        https://github.com/Tieske/timerwheel.lua/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch
Requires:       lua-coxpcall
# oreon:deps
BuildRequires:  lua-coxpcall
BuildRequires:  lua-devel
BuildRequires:  lua-socket
# /oreon:deps
%description
Efficient timer for timeout related timers: fast insertion, deletion, 
and execution (all as O(1) implemented), but with lesser precision.
This module will not provide the timer/runloop itself. Use your own 
runloop and call wheel:step to check and execute timers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir timerwheel.lua-%{version}
%oreon_prep
%build

%install
mkdir -p %{buildroot}%{lua_pkgdir}/timerwheel
cp -p src/timerwheel/init.lua %{buildroot}%{lua_pkgdir}/timerwheel/init.lua
%oreon_autofiles main

%check

LUA_PATH="%{buildroot}%{lua_pkgdir}/?.lua;%{buildroot}%{lua_pkgdir}/?/init.lua;;
" \
lua -e ' 
   local tw = require"timerwheel"
   local set_time, now
   do
     local _time
     _time = 0
     set_time = function(t)
       _time = t
     end
     now = function()
       return _time
     end
   end
   local wheel = tw.new()
   local wheel = tw.new {
     precision = 0.5,
     ringsize = 10,
     now = function() end,
     err_handler = function() end,
   }'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
