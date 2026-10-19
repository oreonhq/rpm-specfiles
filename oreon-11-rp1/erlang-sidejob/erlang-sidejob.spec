%global source0_hash 54e72fbe24e7221361751e025cc7ea0846f8dc382d98ff2ae6cda55f3b2666f8
%global realname sidejob
Name:		erlang-%{realname}
Version:	2.1.0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        An Erlang library that implements a parallel, capacity-limited request pool
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/basho/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-sidejob-0001-Don-t-compile-with-export_all.patch
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
An Erlang library that implements a parallel, capacity-limited request pool. In
sidejob, these pools are called resources. A resource is managed by multiple
gen_server like processes which can be sent calls and casts using sidejob:call
or sidejob:cast respectively.

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
