%global source0_hash 197c4e6751ad7cde934633b6b53929964c0bfae756e86864f9c198346cb25fcf

%global realname lager

Name:       erlang-%{realname}
Version:    3.9.2
Release:    %autorelease
BuildArch:  noarch
Summary:    A logging framework for Erlang/OTP
License:    Apache-2.0
URL:        http://github.com/erlang-lager/%{realname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch3:		erlang-lager-0003-Allow-trace-filter-to-silence-log-output.patch
Patch4:		erlang-lager-0004-Add-test-and-some-documentation.patch
Patch5:		erlang-lager-0005-Separate-line-and-col-metadata-on-OTP-24.patch
Patch6:		erlang-lager-0006-Since-Erlang-24-stacktraces-include-BIF-and-NIF-func.patch
Patch7:		erlang-lager-0007-Workaround-for-Erlang-25.patch
Patch8:		erlang-lager-0008-Workaround-for-slow-builders-increase-timeout.patch
Patch9:		erlang-lager-0009-It-s-the-other-way-around-on-a-modern-Erlang.patch
BuildRequires:  erlang-goldrush >= 0.1.9
BuildRequires:  erlang-rebar3

%description
Lager (as in the beer) is a logging framework for Erlang. Its purpose is to
provide a more traditional way to perform logging in an erlang application that
plays nicely with traditional UNIX logging tools like logrotate and syslog.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
# Sometimes the tests fail on Rawhide:
# https://github.com/erlang-lager/lager/issues/463
%{erlang3_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
