%global source0_hash 18357c83b82bc941dbe8b64e85763e5820649913a2a2200a690f546af3b3234f
%global realname cowlib
Name:		erlang-%{realname}
Version:	2.20.0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Support library for manipulating Web protocols
License:	Apache-2.0
URL:		https://github.com/ninenines/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/ninenines/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-proper
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
%{summary}.

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
