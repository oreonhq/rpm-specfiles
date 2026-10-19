%global source0_hash f2f6019289d9f97d1c33e91a5433ace63a6a5f84735ce65f6dd2b1a5aa0f4847
%global realname gen_leader
%global git_commit d9689e6e80cd8a437bc207d37cb53290ecd64b35
Name:		erlang-%{realname}
Version:	1.0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        A leader election behavior modeled after gen_server
License:	ErlPL-1.1
URL:		https://github.com/garret-smith/%{realname}_revival
VCS:		git:%{url}.git
Source0:        https://github.com/garret-smith/%{realname}_revival/archive/%{git_commit}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
This application implements a leader election behavior modeled after gen_server.
This behavior intends to make it reasonably straightforward to implement a fully
distributed server with master-slave semantics.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}_revival-%{git_commit}

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
