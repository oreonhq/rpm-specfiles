%global source0_hash aa70cc5fefbcb140e734a582e3d029a1e5d9b469c593ff0d43c5d3842a18ca0f
%global srcname p1_acme
%global base64url_ver 1.0.1
%global idna_ver 6.0.0
%global jiffy_ver 1.1.1
%global jose_ver 1.11.10
%global yconf_ver 1.0.22
Name:       erlang-%{srcname}
Version:    1.0.31
Release:        1%{?dist}
BuildArch:  noarch
License:    Apache-2.0
Summary:        ACME client library for Erlang
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:        https://github.com/processone/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Requires: erlang-base64url >= %{base64url_ver}
Requires: erlang-idna >= %{idna_ver}
Requires: erlang-jiffy >= %{jiffy_ver}
Requires: erlang-jose >= %{jose_ver}
Requires: erlang-yconf >= %{yconf_ver}
# oreon:deps
BuildRequires:  erlang-base64url
BuildRequires:  erlang-idna
BuildRequires:  erlang-jiffy
BuildRequires:  erlang-jose
BuildRequires:  erlang-rebar3
BuildRequires:  erlang-yconf
# /oreon:deps
%description
%{summary}.

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
