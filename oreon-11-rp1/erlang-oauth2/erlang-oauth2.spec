%global source0_hash 344e3036292d18c8f0bd37d3c193833acee47367b7e633df21a38db10f99bef6

%global srcname oauth2

Name:       erlang-%{srcname}
Version:    0.9.5
Release:    %autorelease
BuildArch:  noarch
License:    MIT
Summary:    An Oauth2 implementation for Erlang
URL:        https://github.com/kivra/%{srcname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: erlang-meck
BuildRequires: erlang-proper
BuildRequires: erlang-rebar3

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

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
