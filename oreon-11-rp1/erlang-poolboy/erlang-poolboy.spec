%global source0_hash ee4684c0de73782ddb7682aa257bf9e1bfaec6276d92ac53ab044a0983e111e3
%global realname poolboy
Name:		erlang-%{realname}
Version:	1.5.2
Release:        1%{?dist}
BuildArch:	noarch
Summary:        A hunky Erlang worker pool factory
License:	Unlicense OR ISC
URL:		https://github.com/devinus/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/devinus/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{realname}-%{version}
# FIXME plugins are currently broken
sed -i -e '/rebar3_eqc/d' rebar.config

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
