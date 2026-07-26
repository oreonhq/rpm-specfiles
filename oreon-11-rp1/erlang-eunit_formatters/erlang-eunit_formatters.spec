%global source0_hash a4edaac77c94158a98af50a8557d0698deb3cd9f0f549212f4a58644a201fe41

%global realname eunit_formatters

Name:     erlang-%{realname}
Version:  0.6.0
Release:  %autorelease
BuildArch:noarch
Summary:  Better output format for eunit test suites
License:  Apache-2.0
URL:      https://github.com/seancribbs/%{realname}
VCS:      git:%{url}.git
Source0:  %{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildRequires: erlang-rebar3

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{realname}-%{version}

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
