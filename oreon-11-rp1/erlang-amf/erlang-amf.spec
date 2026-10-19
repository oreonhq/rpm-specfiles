%global source0_hash b32e18e2072e4a7fc0d5cc4cfe881782bbbc3c74325a09f3f342ec6e1aea2dc8
%global realname amf
%global git_commit 8fea004e61c746c16271476c190a9c01e398a2d5
%global git_date 20110224
Name:		erlang-%{realname}
Version:	0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Erlang Action Message Format Library
License:	BSD-2-Clause
URL:		https://github.com/abuibrahim/erlang-%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/abuibrahim/%{name}/archive/%{git_commit}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n erlang-%{realname}-%{git_commit}

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
