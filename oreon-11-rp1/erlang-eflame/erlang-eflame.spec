%global source0_hash afc3ebfcec3e822663a530b092e0c808840d4abd1b40e92498535128882fb80c
%global realname eflame
%global git_commit a08518142126f5fc541a3a3c4a04c27f24448bae
%global git_date 20150721
Name:		erlang-%{realname}
Version:	0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Flame Graph profiler for Erlang
License:	MIT
URL:		https://github.com/slfritchie/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/slfritchie/%{realname}/archive/%{git_commit}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
BuildRequires:  perl-generators
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
install -D -p -m 0755 flamegraph.pl %{buildroot}%{erlang_appdir}/bin/flamegraph.pl
install -D -p -m 0755 flamegraph.riak-color.pl %{buildroot}%{erlang_appdir}/bin/flamegraph.riak-color.pl
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
