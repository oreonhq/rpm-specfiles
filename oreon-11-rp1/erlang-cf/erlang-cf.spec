%global source0_hash 0631beea75c7d8a62ab5972ef0289f51cf33b46f297d99c29188f8ec7264151c
%global realname cf
Name:     erlang-%{realname}
Version:  0.3.1
Release:        1%{?dist}
BuildArch:noarch
Summary:        Terminal color helper
License:  BSD-3-Clause
URL:      https://github.com/project-fifo/%{realname}
VCS:      git:%{url}.git
Source0:        https://github.com/project-fifo/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
# oreon:deps
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
