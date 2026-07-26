%global source0_hash 6389b30e4dfc903c289019138bcc71653bdf156d4951af41f9a02c84907ecaf8

%global realname fuse

Name:		erlang-%{realname}
Version:	2.5.0
Release:	%autorelease
BuildArch:	noarch
Summary:	A Circuit Breaker for Erlang
License:	MIT
URL:		https://github.com/jlouis/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-fuse-0001-Disable-support-for-Prometheus-in-Fedora.patch
BuildRequires:	erlang-exometer_core
BuildRequires:	erlang-folsom
# FIXME include into fedora oneday - see patch no. 1
#BuildRequires:	erlang-prometheus
BuildRequires:	erlang-rebar3

%description
This application implements a so-called circuit-breaker for Erlang.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}
rm -rf ./rebar.config
rm -rf ./test/fuse_SUITE.erl

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
# Requires a proprietary eqc library
%{erlang3_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
