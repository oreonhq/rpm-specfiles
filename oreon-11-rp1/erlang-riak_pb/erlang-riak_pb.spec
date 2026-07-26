%global source0_hash 4582a9a91bdede236f87cb9c2f35cf9836067aae1b7bd3ed3b60490e89c9cfac

%global realname riak_pb
%global upstream basho

Name:		erlang-%{realname}
Version:	3.0.10
Release:	%autorelease
BuildArch:	noarch
Summary:	Riak Protocol Buffers Messages
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-riak_pb-0001-FIXME-remove-eqc-we-do-not-use-it.patch
Patch:		erlang-riak_pb-0002-Include-gpb.hrl-ad-include_lib.patch
BuildRequires:	erlang-gpb
BuildRequires:	erlang-hamcrest
BuildRequires:	erlang-rebar3
BuildRequires:	erlang-rebar3-gpb
BuildRequires:	erlang-rebar3-riak_pb_msgcodegen

%description
The message definitions for the Protocol Buffers-based interface to Riak and
various Erlang-specific utility modules for the message types.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
