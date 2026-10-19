%global source0_hash 21d9f8cb4a3095a98d547e50b84e13fea11c9296302080d1a31f8322be76e217
%global realname providers
Name:     erlang-%{realname}
Version:  1.9.0
Release:        1%{?dist}
Summary:        An Erlang providers library
License:  Apache-2.0
URL:      https://github.com/tsloughter/%{realname}
VCS:      git:%{url}.git
Source0:        https://github.com/tsloughter/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildArch:  noarch
# oreon:deps
BuildRequires:  erlang-erlware_commons
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
