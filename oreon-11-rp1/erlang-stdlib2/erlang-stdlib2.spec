%global source0_hash 082f0004e07dced74fc48bf92376aca99558456ee3a4063d941564fddc47e66b
%global realname stdlib2
Name:		erlang-%{realname}
Version:	1.4.7
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Erlang stdlib extensions
License:	BSD-2-Clause AND Apache-2.0
URL:		https://github.com/kivra/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/kivra/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-folsom
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

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
