%global source0_hash 1d62a7fa119f49f13e1cfae040404ee0f5d07b4fe348932ecdc2c2fd38108ff0

%global srcname cache_tab
%global p1_utils_ver 1.0.28

Name: erlang-%{srcname}
Version: 1.0.33
Release: %autorelease
License: Apache-2.0
Summary: Erlang cache table application
URL: https://github.com/processone/%{srcname}
VCS: git:%{url}.git
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: erlang-rebar3
BuildRequires: erlang-rebar3-pc
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
Requires: erlang-p1_utils >= %{p1_utils_ver}

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

%check
%{erlang3_test}

%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
