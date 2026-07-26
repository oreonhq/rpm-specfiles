%global source0_hash 07aa5f00da8521b24301c704026e5e2cf049e1c3cf29fbec87bc1fe5729b6acb

%global realname exometer_core

Name:		erlang-%{realname}
Version:	2.0.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Easy and efficient instrumentation of Erlang code
License:	MPL-2.0
URL:		https://github.com/feuerlabs/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-exometer_core-0001-Metric-names-might-be-tuples-they-have-to-be-escaped.patch
Patch:		erlang-exometer_core-0002-Add-test-case-for-erisata-fix_name_tuples.patch
Patch:		erlang-exometer_core-0003-exometer_report-Fix-static-subscriber-spec-with-Extr.patch
Patch:		erlang-exometer_core-0004-FIXME-disable-plugins-for-Rebar3.patch
BuildRequires:	erlang-edown
BuildRequires:	erlang-hut
BuildRequires:	erlang-meck
BuildRequires:	erlang-parse_trans
BuildRequires:	erlang-rebar3
BuildRequires:	erlang-setup

%description
The Exometer Core package allows for easy and efficient instrumentation of
Erlang code, allowing crucial data on system performance to be exported to a
wide variety of monitoring systems.

Exometer Core comes with a set of predefined monitor components, and can be
expanded with custom components to handle new types of Metrics, as well as
integration with additional external systems such as databases, load balancers,
etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}
# FIXME don't generate docs for now
rm -f doc/overview.edoc

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc doc/ README.md
%{erlang_appdir}/

%changelog
%autochangelog
