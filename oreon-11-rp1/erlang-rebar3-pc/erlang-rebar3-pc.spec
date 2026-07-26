%global source0_hash 46204ca415ff0755aac14f05deb357306c1d17c3aa4fb0ab7219abf08f98057e

%global realname pc

Name:		erlang-rebar3-%{realname}
Version:	1.15.0
Release:	%autorelease
Summary:	A port compiler for Rebar3
License:	MIT
URL:		https://github.com/blt/port_compiler
VCS:		git:%{url}.git
Source0:	%{url}/archive/v%{version}/port_compiler-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	erlang-rebar3
# Required for port compiling but cannot be picked up automatically yet
Requires:	erlang-erl_interface

%description
This plugin is intended to replicate the Rebar2 support for compiling native
code. It is not a drop-in replacement in terms of command-line interface but
the exact configuration interface in projects' rebar.configs have been
preserved.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n port_compiler-%{version}

%build
%{erlang3_compile}

%check
%{erlang3_test}

%install
%{erlang3_install}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
