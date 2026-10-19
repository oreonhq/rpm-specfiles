%global source0_hash e02c9bc16eec43a2bc08f9c7407f9dd5c6a2e3d1a57bca7f7c8929060aa5fc40
%global srcname provider_asn1
Name: erlang-%{srcname}
Version: 0.4.1
Release:        1%{?dist}
BuildArch: noarch
License: MIT
Summary:        Compile ASN.1 with Rebar3
URL: https://github.com/knusbaum/provider_asn1
VCS: git:%{url}.git
Source0:        https://github.com/knusbaum/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
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
