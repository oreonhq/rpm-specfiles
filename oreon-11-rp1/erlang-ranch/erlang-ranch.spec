%global source0_hash de86577d38fb176f1771e42d4b2edbe16754989db500b8d184e6386daede7192
%global realname ranch
Name:		erlang-%{realname}
Version:	2.3.0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Socket acceptor pool for TCP protocols
License:	ISC
URL:		https://github.com/ninenines/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/ninenines/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-ranch-0001-Fix-testing-with-rebar.patch
Patch:		erlang-ranch-0002-Don-t-care-about-return-value.patch
# oreon:deps
BuildRequires:  erlang-ct_helper
BuildRequires:  erlang-rebar3
# /oreon:deps
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
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
