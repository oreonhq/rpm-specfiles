%global source0_hash f461cd92ad43b2a0185c6663abe3e0679c41cf0fdbc365a8814963849c5a5194

%global realname hex_core

Name:     erlang-%{realname}
Version:  0.15.0
Release:  %autorelease
Summary:  Reference implementation of Hex specifications
License:  Apache-2.0
URL:      https://github.com/hexpm/%{realname}
VCS:      git:%{url}.git
Source0:  %{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch:    erlang-hex_core-0001-Disable-non-deterministic-tarball-checksum-tests.patch
BuildArch:     noarch
BuildRequires: erlang-proper
BuildRequires: erlang-rebar3
BuildRequires: erlang-rebar3-gpb

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

%build
{%erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.md examples/
%{erlang_appdir}/

%changelog
%autochangelog
