%global source0_hash 903abe7ea67465fd1733f89bb0e7986072e1935148ff521f6e3d70656bcee992

%global realname mustache

Name:		erlang-%{realname}
Version:	0.1.1
Release:	%autorelease
BuildArch:	noarch
Summary:	Mustache template engine for Erlang
License:	MIT
URL:		https://github.com/mojombo/%{realname}.erl
VCS:		git:%{url}.git
Source0:	%{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-mustache-0001-Migrate-to-a-new-Meck.patch
BuildRequires:	erlang-meck
BuildRequires:	erlang-rebar3

%description
An Erlang port of Mustache for Ruby. Mustache is a framework-agnostic template
system that enforces separation of view logic from the template file. Indeed, it
is not even possible to embed logic in the template. This allows templates to be
reused across language boundaries and for other language independent uses.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}.erl-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc examples/ README.md
%{erlang_appdir}/

%changelog
%autochangelog
