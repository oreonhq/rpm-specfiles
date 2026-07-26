%global source0_hash 4da69014f10b4f88672b791c961e7b9dd1ce410d60897679a57b3694b26fae7d

%global srcname yconf
%global fast_yaml_ver 1.0.39

Name:       erlang-%{srcname}
Version:    1.0.22
Release:    %autorelease
BuildArch:  noarch
License:    Apache-2.0
Summary:    YAML configuration processor
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: erlang-fast_yaml >= %{fast_yaml_ver}
BuildRequires: erlang-rebar3
Requires: erlang-fast_yaml >= %{fast_yaml_ver}

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
