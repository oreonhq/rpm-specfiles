%global source0_hash 7a8cfc47111e16aff4ff49e92ff3760c1100b117cb4da03cde95593a80ccd69b

%global realname lucene_parser
%global git_commit 7818ac9e7a4f1af60e8b9d84a6ad27552d530f4b

Name:		erlang-%{realname}
Version:	1
Release:	%autorelease
BuildArch:	noarch
Summary:	A library for Lucene-like query syntax parsing
License:	Apache-2.0
URL:		https://github.com/basho/riak_search
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{git_commit}/%{realname}-%{version}.tar.gz
Patch1:		erlang-lucene_parser-0001-Move-tests-to-the-canonical-directory.patch
BuildRequires:	erlang-rebar3

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p3 -n riak_search-%{git_commit}/apps/%{realname}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%doc README.txt
%{erlang_appdir}/

%changelog
%autochangelog
