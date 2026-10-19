%global source0_hash 5ff68e589aa2cbade6fce076408eec56eaa6c912bfdc6b408c40aaed04ae0654
%global realname gettext
%global git_commit 2bcba56069721afc7d8c58f84ce701958ec7a761
%global git_date 20170123
Name:		erlang-%{realname}
Version:	2.1.0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Erlang internationalization library
License:	MIT
URL:		https://github.com/etnt/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/etnt/%{realname}/archive/%{git_commit}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{git_commit}

%build

%{erlang3_compile}
%install
%{erlang3_install}
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
