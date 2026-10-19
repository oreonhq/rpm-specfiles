%global source0_hash e37241b3a062cf355685fef2d3cda00df3b8dd3746183663f0c7feef3a3fdad5
%global realname bbmustache
Name:		erlang-%{realname}
Version:	1.12.2
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Binary pattern match-based Mustache template engine for Erlang
License:	MIT
URL:		https://github.com/soranoba/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/soranoba/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{realname}-%{version}
# FIXME this test requires escriptized bbmustache which we do not ship (yet?)
#rm -rf ct/bbmustache_escript_SUITE.erl ct/bbmustache_escript_SUITE_data/
# FIXME we cannot pass Common_Tests suite because of the missing deps. At least
# we can pass eunit ones.
rm -rf ct/*

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
