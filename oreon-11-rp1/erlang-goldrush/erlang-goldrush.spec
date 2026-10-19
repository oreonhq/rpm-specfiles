%global source0_hash 45eb313413226933fcb8d723d087e82563dbd80897b236c45ac3a7016a7d192f
%global realname goldrush
Name:		erlang-%{realname}
Version:	0.2.0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Small, fast event processing and monitoring for Erlang/OTP applications
License:	MIT
URL:		https://github.com/DeadZen/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/DeadZen/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
A small Erlang app that provides fast event stream processing.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{realname}-%{version}

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
