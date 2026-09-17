%global source0_hash cb3b4b966aac971d95871d027ea72422eef53587a32fa043d2ab61592ffa01cd

%global srcname p1_pgsql

Name:       erlang-%{srcname}
Version:    1.1.40
Release:    %autorelease
BuildArch:  noarch
License:    ErlPL-1.1
Summary:    Pure Erlang PostgreSQL driver
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Provides:   erlang-pgsql = %{version}-%{release}
Obsoletes:  erlang-pgsql < 0-16
BuildRequires: erlang-rebar3
BuildRequires: erlang-stringprep

%description
%{summary}.

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
%license EPLICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
