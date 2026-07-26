%global source0_hash 3dd0e1df31993c1945e4b9332583bfe79b6fb2638ff975cc0a43559d34f2a04c

%global realname ranch

Name:		erlang-%{realname}
Version:	2.2.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Socket acceptor pool for TCP protocols
License:	ISC
URL:		https://github.com/ninenines/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-ranch-0001-Fix-testing-with-rebar.patch
Patch:		erlang-ranch-0002-Don-t-care-about-return-value.patch
BuildRequires:	erlang-ct_helper
BuildRequires:	erlang-rebar3

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}
# FIXME we don't have stampede yet
rm -f test/stampede_SUITE.erl
# FIXME this test is very fragile and cannot be run with Rebar3 directly
rm -f test/upgrade_SUITE.erl

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.asciidoc doc/ examples/
%{erlang_appdir}/

%changelog
%autochangelog
