%global source0_hash f9e9d124c00fbbe93a3ab644f4234ea66dacde9c1b2eb9bb9fdf06d44144bf2e
%global srcname yconf
%global fast_yaml_ver 1.0.39
Name:       erlang-%{srcname}
Version:    1.0.23
Release:        1%{?dist}
BuildArch:  noarch
License:    Apache-2.0
Summary:        YAML configuration processor
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:        https://github.com/processone/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Requires: erlang-fast_yaml >= %{fast_yaml_ver}
# oreon:deps
BuildRequires:  erlang-fast_yaml
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

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
