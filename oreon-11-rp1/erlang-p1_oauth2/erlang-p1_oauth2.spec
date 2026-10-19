%global source0_hash 6437184239ea3053584834771776062c4e055e897dc6ca94dd8f960f393d891c
%global srcname p1_oauth2
Name:       erlang-%{srcname}
Version:    0.6.14
Release:        1%{?dist}
BuildArch:  noarch
License:    MIT
Summary:        An Oauth2 implementation for Erlang
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:        https://github.com/processone/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-meck
BuildRequires:  erlang-proper
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
This library is designed to simplify the implementation of the server side of
OAuth2. It is a fork of erlang-oauth2 by processone, and is needed by ejabberd.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build

%{erlang3_compile}
%check

%{erlang3_test}
%install
%{erlang3_install}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
