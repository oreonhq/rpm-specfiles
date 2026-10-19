%global source0_hash 71de5b42d933b6ba05e39ea6e3ab8aab51d59774a04f7aac98ac4e495771c20d
%global realname cuttlefish
Name:		erlang-%{realname}
Version:	2.1.1
Release:        1%{?dist}
BuildArch:	noarch
Summary:        A library for dealing with sysctl-like configuration syntax
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/basho/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Source1:	%{realname}.escript
Patch1:		erlang-cuttlefish-0001-Disable-escript-generation.patch
Patch2:		erlang-cuttlefish-0002-No-rebar_mustache-available.patch
Patch3:		erlang-cuttlefish-0003-Add-recent-otp-versions-to-rebar.config.patch
Patch4:		erlang-cuttlefish-0004-erlang-get_stacktrace-0-deprecated.patch
# oreon:deps
BuildRequires:  erlang-bbmustache
BuildRequires:  erlang-getopt
BuildRequires:  erlang-lager
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
Cuttlefish is a library for Erlang applications that wish to walk the fine line
between Erlang app.configs and a sysctl-like syntax. The name is a pun on the
pronunciation of 'sysctl' and jokes are better explained.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}
# Temporarily remove rebar plugin until we start packaging rebar plugins
rm -f src/cuttlefish_rebar_plugin.erl

%build

%{erlang3_compile}
%install
%{erlang3_install}
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/%{realname}
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
