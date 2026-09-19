%global source0_hash 60bb21984d212470f57d17a41a6fbd0b57298a03779580ebf437bcd3dd119edb

%global srcname jose

Name:      erlang-%{srcname}
Version:   1.11.12
Release:   %autorelease
BuildArch: noarch
License:   MIT
Summary:   JSON Object Signing and Encryption (JOSE) for Erlang and Elixir
URL:       https://github.com/potatosalad/%{name}
VCS:       git:%{url}.git
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: erlang-base64url
BuildRequires: erlang-proper
BuildRequires: erlang-rebar3
BuildRequires: erlang-triq
Recommends: erlang-jiffy
Recommends: erlang-jsx

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
# FIXME Not enough dependencies
#%%{erlang3_test}

%files
%license LICENSE.md
%doc ALGORITHMS.md
%doc CHANGELOG.md
%doc examples
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
