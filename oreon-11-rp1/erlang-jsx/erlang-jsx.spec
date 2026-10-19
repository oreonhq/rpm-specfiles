%global source0_hash dbcd1a117e4e297fbbd9e7441d300185e7192a9ed881082f949d132c798acf78
%global realname jsx
Name:		erlang-%{realname}
Version:	3.1.0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        A streaming, evented json parsing toolkit
License:	MIT
URL:		https://github.com/talentdeficit/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/talentdeficit/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-jsx-0001-Adapt-to-OTP-24.patch
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
An Erlang application for consuming, producing and manipulating json. inspired
by yajl.

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
