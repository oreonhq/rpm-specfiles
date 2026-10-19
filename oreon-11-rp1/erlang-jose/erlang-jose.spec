%global source0_hash 60bb21984d212470f57d17a41a6fbd0b57298a03779580ebf437bcd3dd119edb
%global srcname jose
Name:      erlang-%{srcname}
Version:   1.11.12
Release:        1%{?dist}
BuildArch: noarch
License:   MIT
Summary:        JSON Object Signing and Encryption (JOSE) for Erlang and Elixir
URL:       https://github.com/potatosalad/%{name}
VCS:       git:%{url}.git
Source0:        https://github.com/potatosalad/%{name}/archive/%{version}/%{srcname}-%{version}.tar.gz
Recommends: erlang-jiffy
Recommends: erlang-jsx
# oreon:deps
BuildRequires:  erlang-base64url
BuildRequires:  erlang-proper
BuildRequires:  erlang-rebar3
BuildRequires:  erlang-triq
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%{erlang3_compile}
%install
%{erlang3_install}
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
