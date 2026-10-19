%global source0_hash c5f8340a6beb66744c5669e651b29048bbd845d79fa1caf413d1348aef30d6ae
%global realname riak_api
Name:		erlang-%{realname}
Version:	3.0.16
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Riak Client APIs
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/basho/%{realname}/archive/riak_kv-%{version}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-meck
BuildRequires:  erlang-mochiweb
BuildRequires:  erlang-rebar3
BuildRequires:  erlang-riak_core
BuildRequires:  erlang-riak_pb
BuildRequires:  erlang-webmachine
# /oreon:deps
%description
This OTP application encapsulates services for presenting Riak's public-facing
interfaces. Currently this means a generic interface for exposing Protocol
Buffers-based services; HTTP services via Webmachine will be moved here at a
later time.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-riak_kv-%{version}

%build

%{erlang3_compile}
%install
%{erlang3_install}
install -D -p -m 644 priv/riak_api.schema %{buildroot}%{erlang_appdir}/priv/riak_api.schema
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
