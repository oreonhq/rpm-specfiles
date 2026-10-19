%global source0_hash 1674bb19d4cdec74b15354fe0125f524ddf00b2fcbdd8d6d68f954e4d9c1d9f0
%global realname rebar3_gpb_plugin
Name:		erlang-rebar3-gpb
Version:	3.0.1
Release:        1%{?dist}
Summary:        A protobuf compiler for Rebar3
License:	MIT
URL:		https://github.com/lrascao/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/lrascao/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  erlang-gpb
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
A Rebar3 plugin for automatically compiling .proto files using the gpb protobuf
compiler.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

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
