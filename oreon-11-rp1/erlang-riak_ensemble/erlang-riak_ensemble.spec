%global source0_hash 640664589b29bbb2a72179f6da04a4bfc7d75955bfca470637b25acdcf25dd34

%global realname riak_ensemble

Name:		erlang-%{realname}
Version:	3.0.10
Release:	%autorelease
Summary:	Multi-Paxos framework in Erlang
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/riak_kv-%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-riak_ensemble-0001-Disable-rebar3-plugins-for-now.patch
BuildRequires:	erlang-eleveldb
BuildRequires:	erlang-lager
BuildRequires:	erlang-rebar3
BuildRequires:	gcc
# Remove when https://bugzilla.redhat.com/show_bug.cgi?id=1770256 is resolved
#ExcludeArch: s390x
# There is a problem with tests passing and I don't know how to debug it (and I
# doubt a lot of people care about this arch in particular anyway).
ExcludeArch: ppc64le

%description
A consensus library that supports creating multiple consensus groups
(ensembles). Each ensemble is a separate Multi-Paxos instance with its own
leader, set of members, and state.

Each ensemble also supports an extended API that provides consistent key/value
operations. Conceptually, this is identical to treating each key as a separate
Paxos entity. However, this isn't accomplished by having each key maintain its
own Paxos group. Instead, an ensemble emulates per-key consensus through a
combination of per-key and per-ensemble state.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-riak_kv-%{version}

%build
%{erlang3_compile}

# FIXME we don't have a port compiler plugin for rebar3 yet
mkdir -p priv
gcc $CFLAGS -c -I%{_libdir}/erlang/usr/include c_src/riak_ensemble_clock.c -o c_src/riak_ensemble_clock.o
gcc $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei c_src/riak_ensemble_clock.o -o priv/riak_ensemble.so

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc doc/ README.md
%{erlang_appdir}/

%changelog
%autochangelog
