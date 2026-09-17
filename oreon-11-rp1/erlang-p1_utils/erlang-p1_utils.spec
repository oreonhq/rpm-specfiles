%global source0_hash 3525dac8bcee70ff2fdc89dde9d47e9346fdeff87193e42e743657abb52e0146

%global srcname p1_utils

Name:       erlang-%{srcname}
Version:    1.0.28
Release:    %autorelease
BuildArch:  noarch
License:    Apache-2.0
Summary:    Erlang utility modules from ProcessOne
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: erlang-rebar3

%description
p1_utils is an application containing ProcessOne modules and tools that are
leveraged in other development projects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%{erlang3_compile}

%check
%{erlang3_test}

%install
%{erlang3_install}

%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
