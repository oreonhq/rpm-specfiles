%global source0_hash f0f188e9a4424851d9263ab69302b6b2ffc5c6efb67a25fffc52187a29c94024
Name:           fennel
Version:        1.6.1
Release:        1%{?dist}
Summary:        A Lisp that compiles to Lua
License:        MIT
URL:            https://fennel-lang.org/
Source0:        https://git.sr.ht/~technomancy/fennel/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
Provides:       lua-fennel = %{version}-%{release}
Recommends:     lua-readline
# oreon:deps
BuildRequires:  lua-devel
BuildRequires:  make
# /oreon:deps
%description
Fennel is a Lisp that compiles to Lua. It aims to be easy to use, expressive,
and has almost zero overhead compared to handwritten Lua.

* *Full Lua compatibility* - You can use any function or library from Lua.
* *Zero overhead* - Compiled code should be just as or more efficient than
   hand-written Lua.
* *Compile-time macros* - Ship compiled code with no runtime dependency on
   Fennel.
* *Embeddable* - Fennel is a one-file library as well as an executable. Embed it
   in other programs to support runtime extensibility and interactive
   development.

At https://fennel-lang.org there's a live in-browser repl you can use without
installing anything.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build
%install
%make_install \
  LUA_VERSION=%{lua_version} \
  PREFIX=%{_prefix}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
