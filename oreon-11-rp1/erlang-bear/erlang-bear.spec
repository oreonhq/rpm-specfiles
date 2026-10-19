%global source0_hash 776acb43274a2d66531c10721c76789be051d8db81be3d5a7dd18d0941d8a68e
%global realname bear
Name:		erlang-%{realname}
Version:	1.1.1
Release:        1%{?dist}
BuildArch:	noarch
Summary:        A set of statistics functions for erlang
License:	Apache-2.0
URL:		https://github.com/folsom-project/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/folsom-project/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
A set of statistics functions for Erlang. Currently bear is focused on use
inside the Folsom Erlang metrics library but all of these functions are generic
and useful in other situations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

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
