%global source0_hash 55ba9f032bb4eb0e2e93dc66a368549bcf1a915bdd9f9a467eb778c3133c6373

%global forgeurl https://github.com/hoelzro/lua-repl
%global tag %{version}

Name:      lua-luarepl
Version:   0.10
Release:   9%{?dist}
Summary:   REPL.lua - a reusable Lua REPL written in Lua
License:   MIT
URL:       %{forgeurl}

%forgemeta
Source:    %{forgesource}

BuildArch:     noarch
BuildRequires: lua-devel

# https://github.com/hoelzro/lua-repl#recommended-packages
Recommends:    lua-linenoise
# Enable filename_completion plugin
Suggests:      lua-filesystem

%description
REPL.lua has two uses:

  - An alternative to the standalone interpreter included with Lua, one that
    supports things like plugins, tab completion, and automatic insertion of
    `return` in front of expressions.

  - A REPL library you may embed in your application, to provide all of the
    niceties of the standalone interpreter included with Lua and then some.

Many software projects have made the choice to embed Lua in their projects to
allow their users some extra flexibility.  Some of these projects would also
like to provide a Lua REPL in their programs for debugging or rapid development.
Most Lua programmers are familiar with the standalone Lua interpreter as a
Lua REPL; however, it is bound to the command line. Until now, Lua programmers
would have to implement their own REPL from scratch if they wanted to include
one in their programs. This project aims to provide a REPL implemented in pure
Lua that almost any project can make use of.

This library also includes an example application (rep.lua), which serves as an
alternative to the standalone interpreter included with Lua. If the
lua-linenoise library is installed, it uses linenoise for history and
tab completion; otherwise, it tries to use rlwrap for basic line editing.
If you would like the arrow keys to work as expected rather than printing things
like `^[[A`, please install the lua-linenoise library or the rlwrap program.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
# Nothing to do here

%install
install -dD %{buildroot}%{lua_pkgdir}
cp -av repl/ %{buildroot}%{lua_pkgdir}

install -dD %{buildroot}%{_bindir}
install -p -m 755 rep.lua %{buildroot}%{_bindir}/rep.lua

%check
# Missing dependency on lua-testmore, only smoke test for now

LUA_PATH="%{buildroot}%{lua_pkgdir}/?.lua;%{buildroot}%{lua_pkgdir}/?/init.lua" \
lua -e 'local repl = require "repl.console"
print(repl.VERSION)'

%files
%license COPYING
%doc README.md
%doc Changes
%{_bindir}/rep.lua
%{lua_pkgdir}/repl/

%changelog
%autochangelog
