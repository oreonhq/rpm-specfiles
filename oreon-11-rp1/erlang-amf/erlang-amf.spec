%global source0_hash b32e18e2072e4a7fc0d5cc4cfe881782bbbc3c74325a09f3f342ec6e1aea2dc8

%global realname amf
%global git_commit 8fea004e61c746c16271476c190a9c01e398a2d5
%global git_date 20110224

Name:		erlang-%{realname}
Version:	0
Release:	%autorelease -p -s %{git_date}git%{sub %git_commit 0 7}
BuildArch:	noarch
Summary:	Erlang Action Message Format Library
License:	BSD-2-Clause
URL:		https://github.com/abuibrahim/erlang-%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{git_commit}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar3

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n erlang-%{realname}-%{git_commit}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc README doc
%{erlang_appdir}/

%changelog
%autochangelog
