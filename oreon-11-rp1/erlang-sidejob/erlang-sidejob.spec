%global source0_hash 33192940b10e2c11d756761354784aabfac17b17dfe6261150db3ff41a0925c0

%global realname sidejob

Name:		erlang-%{realname}
Version:	2.0.2
Release:	%autorelease
BuildArch:	noarch
Summary:	An Erlang library that implements a parallel, capacity-limited request pool
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-sidejob-0001-Don-t-compile-with-export_all.patch
BuildRequires:	erlang-rebar3

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

%check
# Requires a proprietary test-site, QuickCheck
# FIXME port to erlang-proper ?
%{erlang3_test}

%files
%{erlang_appdir}/

%changelog
%autochangelog
