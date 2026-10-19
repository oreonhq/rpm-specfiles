%global source0_hash fac1f9943b5488640afce3771ffe84769acc295096c29c1c92fbee5f8ba68880
%global realname hex_core
Name:     erlang-%{realname}
Version:  0.19.0
Release:        1%{?dist}
Summary:        Reference implementation of Hex specifications
License:  Apache-2.0
URL:      https://github.com/hexpm/%{realname}
VCS:      git:%{url}.git
Source0:        https://github.com/hexpm/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch:    erlang-hex_core-0001-Disable-non-deterministic-tarball-checksum-tests.patch
BuildArch:     noarch
# oreon:deps
BuildRequires:  erlang-proper
BuildRequires:  erlang-rebar3
BuildRequires:  erlang-rebar3-gpb
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

%build

{%erlang3_compile}
%install
%{erlang3_install}
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
