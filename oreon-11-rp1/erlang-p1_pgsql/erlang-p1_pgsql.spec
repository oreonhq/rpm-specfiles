%global source0_hash ccf733fce009f19d636df490937e612571a9099099caefb8cb90d5a5df15bdd8
%global srcname p1_pgsql
Name:       erlang-%{srcname}
Version:    1.1.41
Release:        1%{?dist}
BuildArch:  noarch
License:    ErlPL-1.1
Summary:        Pure Erlang PostgreSQL driver
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:        https://github.com/processone/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Provides:   erlang-pgsql = %{version}-%{release}
Obsoletes:  erlang-pgsql < 0-16
# oreon:deps
BuildRequires:  erlang-rebar3
BuildRequires:  erlang-stringprep
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

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
