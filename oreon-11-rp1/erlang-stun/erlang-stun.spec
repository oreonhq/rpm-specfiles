%global source0_hash 22bf5bcc9c3c8ce281348acef9f6aa66f07f614d0310a905cb98defbf585de81
%global srcname stun
%global fast_tls_ver 1.1.21
%global p1_utils_ver 1.0.26
Name:      erlang-%{srcname}
Version:   1.2.23
Release:        1%{?dist}
BuildArch: noarch
License: Apache-2.0
Summary:        STUN and TURN library for Erlang / Elixir
URL:     https://github.com/processone/%{srcname}
VCS:     git:%{url}.git
Source0:        https://github.com/processone/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Provides:  erlang-p1_stun = %{version}-%{release}
Obsoletes: erlang-p1_stun < 1.0.1
Requires: erlang-fast_tls >= %{fast_tls_ver}
Requires: erlang-p1_utils >= %{p1_utils_ver}
# oreon:deps
BuildRequires:  erlang-edoc
BuildRequires:  erlang-fast_tls
BuildRequires:  erlang-p1_utils
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
STUN and TURN library for Erlang / Elixir. Both STUN (Session Traversal
Utilities for NAT) and TURN standards are used as techniques to establish media
connection between peers for VoIP (for example using SIP or Jingle) and WebRTC.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir stun-%{version}
%oreon_prep
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
