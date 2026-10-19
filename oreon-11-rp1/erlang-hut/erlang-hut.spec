%global source0_hash 09e376c232bd702089e842ccb7d4d1db8544fd2a3ad44efad7dec055db14017c
%global realname hut
Name:		erlang-%{realname}
Version:	1.4.0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        A helper library for making Erlang libraries logging framework agnostic
License:	MIT
URL:		https://github.com/tolbrino/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/tolbrino/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
A a minimal library for Erlang libraries and small applications to stay
agnostic to the logging framework in use. Its purpose is to allow the
developers of umbrella applications to use their logging framework of choice
and ensure that dependency stick to that choice as well.

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
