%global source0_hash 53a4ba7528d6147afc1f38276f9fc74bb2740061235b2ae850be6e3954b00d79

%global realname riak_dt

Name:		erlang-%{realname}
Version:	3.0.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Convergent replicated data types in Erlang
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/riak_kv-%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-riak_dt-0001-A-couple-of-failing-tests-which-look-to-be-caused-by.patch
Patch:		erlang-riak_dt-0001-FIXME-disable-plugins.patch
BuildRequires:	erlang-rebar3

%description
A set of state based CRDTs implemented in Erlang.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-riak_kv-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
# Some tests requires a proprietary library - QuickCheck
%{erlang3_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
