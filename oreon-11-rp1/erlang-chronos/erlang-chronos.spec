%global source0_hash 4b21ecd28129011badccf0347030ab5db7d99dd97bbac44841b2e6ccacde8465
%global realname chronos
Name:		erlang-%{realname}
Version:	1.0.1
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Timer utility for Erlang tests
License:	MIT
URL:		https://github.com/lehoff/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/lehoff/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

%build

%{erlang3_compile}
%install
%{erlang3_install}
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
