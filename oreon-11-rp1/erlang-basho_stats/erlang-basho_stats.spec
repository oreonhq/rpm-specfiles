%global source0_hash 99994644eeff8be3f232450252ad8bc0ecddb474cf1c736ed6af51645250f6df

%global realname basho_stats

Name:		erlang-%{realname}
Version:	1.1.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Basic Erlang statistics library
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-basho_stats-0001-We-still-do-not-use-eqc-for-checking.patch
BuildRequires:	erlang-rebar3

%description
%{summary}.

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
%{erlang_appdir}/

%changelog
%autochangelog
