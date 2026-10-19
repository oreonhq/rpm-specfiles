%global source0_hash 46204ca415ff0755aac14f05deb357306c1d17c3aa4fb0ab7219abf08f98057e
%global realname pc
Name:		erlang-rebar3-%{realname}
Version:	1.15.0
Release:        1%{?dist}
Summary:        A port compiler for Rebar3
License:	MIT
URL:		https://github.com/blt/port_compiler
VCS:		git:%{url}.git
Source0:        https://github.com/blt/port_compiler/archive/v%{version}/port_compiler-%{version}.tar.gz
BuildArch:	noarch
Requires:	erlang-erl_interface
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
This plugin is intended to replicate the Rebar2 support for compiling native
code. It is not a drop-in replacement in terms of command-line interface but
the exact configuration interface in projects' rebar.configs have been
preserved.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir port_compiler-%{version}
%oreon_prep
%build

%{erlang3_compile}
%check

%{erlang3_test}
%install
%{erlang3_install}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
