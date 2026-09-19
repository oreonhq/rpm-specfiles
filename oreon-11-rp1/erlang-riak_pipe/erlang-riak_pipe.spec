%global source0_hash 24ba8914ff8d368e82da34c8d7c8d0a68ca6c056a2f77775ecae8bd4f7737452

%global realname riak_pipe

Name:		erlang-%{realname}
Version:	3.0.16
Release:	%autorelease
BuildArch:	noarch
Summary:	Riak Pipelines
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/riak_kv-%{version}/%{realname}-%{version}.tar.gz
Patch1:         erlang-riak_pipe-0001-Disable-eqc-rebar3-plugin.patch
BuildRequires:	erlang-cluster_info
BuildRequires:	erlang-exometer_core
BuildRequires:	erlang-lager
BuildRequires:	erlang-rebar3
BuildRequires:	erlang-riak_core

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-riak_kv-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}
install -p -m 644 priv/app.slave0.config %{buildroot}%{erlang_appdir}/priv

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.org
%{erlang_appdir}/

%changelog
%autochangelog
