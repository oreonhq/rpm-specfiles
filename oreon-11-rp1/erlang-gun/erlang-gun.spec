%global source0_hash 795a1ad8574ff5ca4943b822f1f0bfe97bfb279ffea4c83def1380ed43689f82
%global realname gun
Name:		erlang-%{realname}
Version:	2.6.0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Erlang HTTP client with support for HTTP/1.1, HTTP/2, Websocket and more
License:	ISC
URL:		https://github.com/ninenines/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/ninenines/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-gun-0001-Fix-testing-with-rebar.patch
# oreon:deps
BuildRequires:  erlang-cowlib
BuildRequires:  erlang-ct_helper
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

%build

%{erlang3_compile}
%install
%{erlang3_install}
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
