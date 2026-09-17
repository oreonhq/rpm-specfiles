%global source0_hash 0e3486bbe75d49abcd036eadda54fc218b26e8447310081fb85cca3114c4cf5d

%global realname bear

Name:		erlang-%{realname}
Version:	1.1
Release:	%autorelease
BuildArch:	noarch
Summary:	A set of statistics functions for erlang
License:	Apache-2.0
URL:		https://github.com/folsom-project/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar3

%description
A set of statistics functions for Erlang. Currently bear is focused on use
inside the Folsom Erlang metrics library but all of these functions are generic
and useful in other situations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

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
