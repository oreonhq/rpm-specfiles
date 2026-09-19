%global source0_hash c38b8c9e51a8c3404b66ab32e49cfb8859fc65c0154585c4a53029b40bba73d0

%global srcname p1_mysql

Name:       erlang-%{srcname}
Version:    1.0.28
Release:    %autorelease
BuildArch:  noarch
Summary:    Pure Erlang MySQL driver, used by ejabberd
License:    BSD-3-Clause
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: erlang-rebar3

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
%license COPYING
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
