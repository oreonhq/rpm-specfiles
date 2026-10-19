%global source0_hash be22dcf4daeeec7cbc9b9b5ae65da8e257e981d8b719b7f100b27422a45a68f9
%global srcname p1_utils
Name:       erlang-%{srcname}
Version:    1.0.29
Release:        1%{?dist}
BuildArch:  noarch
License:    Apache-2.0
Summary:        Erlang utility modules from ProcessOne
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:        https://github.com/processone/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
p1_utils is an application containing ProcessOne modules and tools that are
leveraged in other development projects.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build

%{erlang3_compile}
%check

%{erlang3_test}
%install
%{erlang3_install}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
