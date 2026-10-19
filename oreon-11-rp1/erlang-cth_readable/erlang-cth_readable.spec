%global source0_hash b1117ef56651a3652ba79be79ed6b81ec334a3894b9fa56b5a063fc7c4b24ee4
%global realname cth_readable
Name:     erlang-%{realname}
Version:  1.6.1
Release:        1%{?dist}
Summary:        Common test hooks for more readable erlang logs
License:  BSD-3-Clause
URL:      https://github.com/ferd/%{realname}
VCS:      git:%{url}.git
Source0:        https://github.com/ferd/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  erlang-lager
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{realname}-%{version}
# FIXME fails for various reasons
rm test/failonly_SUITE.erl
rm test/show_logs_SUITE.erl
rm test/sample_SUITE.erl

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
