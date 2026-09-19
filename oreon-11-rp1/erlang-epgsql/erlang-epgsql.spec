%global source0_hash 7ead06a5f88491dc0447b6e57e4776f66530b3e13d624fb2036f26aa5fdb5620

%global realname epgsql

Summary:	Erlang PostgreSQL client library
Name:		erlang-%{realname}
Version:	4.8.0
Release:	%autorelease
BuildArch:	noarch
License:	BSD-3-Clause
URL:		https://github.com/%{realname}/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar3

%description
Library that gives possibility to Erlang programs to connect PostgreSQL
databases by plain TCP and execute simple SQL statements.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
# TODO Requires PostgreSQL connection
#%%{erlang3_test}

%files
%license LICENSE
%doc CHANGES README.md TODO
%{erlang_appdir}/

%changelog
%autochangelog
