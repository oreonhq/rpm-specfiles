%global source0_hash 110b06572c6208fdeaa60c32cd549e6798f0a719d51bef97608c2aaa61151c11

%global srcname stun

%global fast_tls_ver 1.1.21
%global p1_utils_ver 1.0.26

Name:      erlang-%{srcname}
Version:   1.2.14
Release:   %autorelease
BuildArch: noarch

License: Apache-2.0
Summary: STUN and TURN library for Erlang / Elixir
URL:     https://github.com/processone/%{srcname}
VCS:     git:%{url}.git
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

Provides:  erlang-p1_stun = %{version}-%{release}
Obsoletes: erlang-p1_stun < 1.0.1

BuildRequires: erlang-edoc
BuildRequires: erlang-rebar3
BuildRequires: erlang-fast_tls >= %{fast_tls_ver}
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}

Requires: erlang-fast_tls >= %{fast_tls_ver}
Requires: erlang-p1_utils >= %{p1_utils_ver}

%description
STUN and TURN library for Erlang / Elixir. Both STUN (Session Traversal
Utilities for NAT) and TURN standards are used as techniques to establish media
connection between peers for VoIP (for example using SIP or Jingle) and WebRTC.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n stun-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
