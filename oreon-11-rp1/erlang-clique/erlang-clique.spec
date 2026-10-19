%global source0_hash 0b3c2b7a3bf5167681ed628a2f7196522886f6f4f4b2a4b367eceb0111af395c
%global realname clique
Name:		erlang-%{realname}
Version:	0.3.12
Release:        1%{?dist}
BuildArch:	noarch
Summary:        CLI Framework for Erlang
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/basho/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-clique-0001-Don-t-hide-dependency-on-mochiweb.patch
# oreon:deps
BuildRequires:  erlang-cuttlefish
BuildRequires:  erlang-mochiweb
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
Clique is an opinionated framework for building command line interfaces in
Erlang. It provides users with an interface that gives them enough power to
build complex CLIs, but enough constraint to make them appear consistent.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

%build

%{erlang3_compile}
%install
%{erlang3_install}
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
