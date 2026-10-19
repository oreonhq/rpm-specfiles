%global source0_hash 4dbfdecaf42995bc2b2ab628b429e6cebe042cf28fb28134c0243e38f4ff83b5
%global realname riak_core
Name:		erlang-%{realname}
Version:	3.0.16
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Distributed systems infrastructure used by Riak
License:	Apache-2.0 and ErlPL-1.1 and MIT and MPL-1.1
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/basho/%{realname}/archive/riak_kv-%{version}/%{realname}-%{version}.tar.gz
Patch1:	erlang-riak_core-0001-Don-t-use-pbkdf2-as-application.patch
Patch2:	erlang-riak_core-0002-Revert-Copy-in-mochiglobal-as-riak_core_mochiglobal.patch
Patch3:	erlang-riak_core-0003-Be-more-greedy-while-loading-schemas.patch
Patch4:	erlang-riak_core-0004-Load-cuttlefish-schemas-from-noarch-dir-as-well.patch
Patch5:	erlang-riak_core-0005-Disable-eqc-rebar3-plugin.patch
Patch6: erlang-riak_core-0006-Don-t-threat-warnings-as-errors.patch
Patch7:	erlang-riak_core-0007-Use-poolboy-API-for-stopping-poolboy.patch
Patch8:	erlang-riak_core-0008-Ignore-completely-reply-value.patch
Patch9:	erlang-riak_core-0009-Fix-test-with-self-signed-certificates.patch
# oreon:deps
BuildRequires:  erlang-basho_stats
BuildRequires:  erlang-clique
BuildRequires:  erlang-cluster_info
BuildRequires:  erlang-eleveldb
BuildRequires:  erlang-exometer_core
BuildRequires:  erlang-folsom
BuildRequires:  erlang-hut
BuildRequires:  erlang-lager
BuildRequires:  erlang-meck
BuildRequires:  erlang-mochiweb
BuildRequires:  erlang-poolboy
BuildRequires:  erlang-rebar3
BuildRequires:  erlang-riak_ensemble
BuildRequires:  erlang-riak_sysmon
BuildRequires:  openssl
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-riak_kv-%{version}
# Exometer removed Folsom support
rm -f src/riak_core_exo_monitor.erl

%build

%{erlang3_compile}
%install
%{erlang3_install}
install -D -p -m 644 priv/riak_core.schema %{buildroot}%{erlang_appdir}/priv/riak_core.schema
%oreon_autofiles main

%check

openssl req -x509 -newkey rsa:4096 -keyout ./test/site1-key.pem -out ./test/site1-cert.pem -sha256 -days 365 -subj "/CN=site1.example.com" -nodes
openssl req -x509 -newkey rsa:4096 -keyout ./test/site2-key.pem -out ./test/site2-cert.pem -sha256 -days 365 -subj "/CN=site1.example.com" -nodes
%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
