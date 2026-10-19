%global source0_hash 93ded46baacac564e8d8a8123ff3d14fbc0c92d76f13a624ad81056bcf82a7fa
%global srcname oauth2
Name:       erlang-%{srcname}
Version:    1.0.7
Release:        1%{?dist}
BuildArch:  noarch
License:    MIT
Summary:        An Oauth2 implementation for Erlang
URL:        https://github.com/kivra/%{srcname}
VCS:        git:%{url}.git
Source0:        https://github.com/kivra/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-meck
BuildRequires:  erlang-proper
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
This library is designed to simplify the implementation of the server side of
OAuth2.

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
