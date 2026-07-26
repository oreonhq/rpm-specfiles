%global source0_hash 6bea74d70897bba5f5110ad73e6c2dd9081ad7cc1ece4d80fde4735afa7cbcf2

%global realname ssl_verify_fun

Name:     erlang-%{realname}
Version:  1.1.7
Release:  %autorelease
Summary:  Collection of ssl verification functions for Erlang
License:  MIT
URL:      https://github.com/deadtrickster/%{realname}.erl
VCS:      git:%{url}.git
Source0:  %{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  erlang-rebar3

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}.erl-%{version}

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
