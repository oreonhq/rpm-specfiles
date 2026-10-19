%global source0_hash ecb6b24812a769248a1a6be092d15fa999406a9581774b8f0f2ab76a6304bf89
%global realname xmlrpc
%global git_commit f3f696c3c0988282fea182b61cdafdaa6a56d169
Name:		erlang-%{realname}
Version:	1.14
Release:        1%{?dist}
BuildArch:	noarch
Summary:        HTTP 1.1 compliant XML-RPC library for Erlang
License:	BSD-2-Clause
URL:		https://github.com/etnt/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/etnt/%{realname}/archive/%{git_commit}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
BuildRequires:  erlang-xmerl
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{git_commit}
rm -f ./rebar ./rebar.config

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
