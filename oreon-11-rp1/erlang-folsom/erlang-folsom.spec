%global source0_hash b223fb23810bd864f6fba89176af1e03e52e1650a9a604d1834a703091ba3d83
%global realname folsom
Name:		erlang-%{realname}
Version:	1.1.1
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Erlang-based metrics system
License:	Apache-2.0
URL:		https://github.com/folsom-project/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/%{realname}-project/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-bear
BuildRequires:  erlang-meck
BuildRequires:  erlang-mochiweb
BuildRequires:  erlang-proper
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
Folsom is an Erlang based metrics system inspired by Coda Hale's metrics.
The metrics API's purpose is to collect realtime metrics from your Erlang
applications and publish them via Erlang APIs and output plugins. Folsom is not
a persistent store. There are 6 types of metrics: counters, gauges, histograms
and timers, histories, meter_readers and meters. Metrics can be created, read
and updated via the folsom_metrics module.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{realname}-%{version}
rm -f test/mochijson2.erl
rm -f test/mochinum.erl

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
