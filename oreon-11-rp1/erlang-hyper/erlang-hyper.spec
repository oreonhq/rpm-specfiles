%global source0_hash 61220617c764fd238e447106d362afed914f988c927223057cc3710c5ce43c45

%global realname hyper
%global git_commit 4b1abc4284fc784f6def4f4928f715b0d33136f9
%global git_date 20161011

Name:		erlang-%{realname}
Version:	0
Release:	%autorelease -p -s %{git_date}git%{sub %git_commit 0 7}
Summary:	An implementation of the HyperLogLog algorithm in Erlang
License:	MIT
URL:		https://github.com/GameAnalytics/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{git_commit}/%{realname}-%{version}.tar.gz
# Fedora-specific
Patch1:		erlang-hyper-0001-remove-need-for-bisect-lib-hyper_bisect-as-it.patch
# Sent upstream - https://github.com/GameAnalytics/hyper/pull/23
Patch2:		erlang-hyper-0002-Module-random-is-deprecated.patch
# Sent upstream - https://github.com/GameAnalytics/hyper/pull/21
Patch3:		erlang-hyper-0003-Remove-unused-functions.patch
# Sent upstream - https://github.com/GameAnalytics/hyper/pull/22
Patch4:		erlang-hyper-0004-Exclude-eunit-from-production-builds.patch
Patch5:		erlang-hyper-0005-Remove-test-failing-in-Erlang-20.patch
Patch6:		erlang-hyper-0006-Fix-for-Rebar3-layout.patch
BuildRequires:	erlang-basho_stats
BuildRequires:	erlang-proper
BuildRequires:	erlang-rebar3
BuildRequires:	erlang-stdlib2
BuildRequires:	gcc

%description
An implementation of the HyperLogLog algorithm in Erlang. Using HyperLogLog you
can estimate the cardinality of very large data sets using constant memory. The
relative error is 1.04 * sqrt(2^P). When creating a new HyperLogLog filter, you
provide the precision P, allowing you to trade memory for accuracy. The union
of two filters is lossless.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{git_commit}

%build
%{erlang3_compile}

# FIXME we don't have a port compiler plugin for rebar3 yet
gcc c_src/hyper_carray.c $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/hyper_carray.o
gcc c_src/hyper_carray.o $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -o priv/hyper_carray.so

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
