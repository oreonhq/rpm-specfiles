%global source0_hash a3d0159bcf996f3c73ac20d6168d2aaedcd6877df8f7ae6a1994010ad8492784

Summary:        Pure Lua timerwheel implementation 
Name:           lua-timerwheel
License:        MIT

Version:        1.0.2
Release:        12%{?dist}

URL:            https://github.com/Tieske/timerwheel.lua
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch
Requires:       lua-coxpcall
BuildRequires:  lua-devel
BuildRequires:  lua-coxpcall
#Needed for tests
BuildRequires:  lua-socket
#BuildRequires:  lua-busted

%description
Efficient timer for timeout related timers: fast insertion, deletion, 
and execution (all as O(1) implemented), but with lesser precision.
This module will not provide the timer/runloop itself. Use your own 
runloop and call wheel:step to check and execute timers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n timerwheel.lua-%{version} 

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{lua_pkgdir}/timerwheel
cp -p src/timerwheel/init.lua %{buildroot}%{lua_pkgdir}/timerwheel/init.lua
 

%check
#Uses lua-busted which is not available yet.
#Smoke test
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

%files
%license LICENSE
%doc README.md
%doc docs/ldoc.css
%doc docs/index.html  
%doc docs/topics/readme.md.html
%dir %{lua_pkgdir}/timerwheel
%{lua_pkgdir}/timerwheel/init.lua

%changelog
%autochangelog
