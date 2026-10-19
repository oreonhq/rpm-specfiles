%global source0_hash fbe180274790b8d7436d57690a4c8600b24cb5878738aa19ad157f08f76eeb34
%global srcname cache_tab
%global p1_utils_ver 1.0.28
Name: erlang-%{srcname}
Version: 1.0.34
Release:        1%{?dist}
License: Apache-2.0
Summary:        Erlang cache table application
URL: https://github.com/processone/%{srcname}
VCS: git:%{url}.git
Source0:        https://github.com/processone/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Requires: erlang-p1_utils >= %{p1_utils_ver}
# oreon:deps
BuildRequires:  erlang-p1_utils
BuildRequires:  erlang-rebar3
BuildRequires:  erlang-rebar3-pc
BuildRequires:  gcc
# /oreon:deps
%description
This application is intended to proxy back-end operations for Key-Value insert,
lookup and delete and maintain a cache of those Key-Values in-memory, to save
back-end operations. Operations are intended to be atomic between back-end and
cache tables. The lifetime of the cache object and the max size of the cache
can be defined as table parameters to limit the size of the in-memory tables.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build

%{erlang3_compile}
%install
%{erlang3_install}
install -p -D -m 755 priv/lib/* --target-directory=%{buildroot}%{erlang_appdir}/priv/lib/
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
